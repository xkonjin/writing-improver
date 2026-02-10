"""Image generation agent using Gemini via OpenRouter or Google AI SDK."""

import base64
import os
from dataclasses import dataclass, field
from pathlib import Path

import httpx

from src.agents.base import AgentUsage, BaseAgent
from src.prompts.image_gen import CLASSIFY_CONTENT_SYSTEM, IMAGE_PROMPT_SYSTEM, STYLE_MAP

OPENROUTER_MODELS = [
    "google/gemini-2.5-flash-image",
    "google/gemini-3-pro-image-preview",
]

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


@dataclass
class ImageGenResult:
    image_path: str = ""
    content_type: str = ""
    style: str = ""
    prompt_used: str = ""
    model_used: str = ""
    usage: AgentUsage = field(default_factory=AgentUsage)


class ImageGenAgent:
    def __init__(self, model: str | None = None) -> None:
        self.classifier = BaseAgent(model="claude-haiku-4-5-20251001")
        self.prompter = BaseAgent(model="claude-haiku-4-5-20251001")
        self.usage = AgentUsage()
        self.forced_model = model

    async def classify_content(self, article: str) -> str:
        """Classify article into one of 7 content types."""
        raw = await self.classifier.call(
            CLASSIFY_CONTENT_SYSTEM,
            f"Classify this article:\n\n{article[:2000]}",
            max_tokens=20,
        )
        self._add_usage(self.classifier)
        label = raw.strip().upper().replace(" ", "_")
        if label not in STYLE_MAP:
            label = "TECHNICAL"
        return label

    async def generate_prompt(self, title: str, article: str, content_type: str) -> str:
        """Generate an image prompt based on content type and style mapping."""
        style = STYLE_MAP[content_type]
        user_msg = (
            f"Title: {title}\n"
            f"Summary: {article[:1000]}\n"
            f"Content type: {content_type}\n"
            f"Art style: {style['primary']}\n"
            f"Style directive: {style['prompt']}\n"
            f"Palette: {style['palette']}"
        )
        prompt = await self.prompter.call(
            IMAGE_PROMPT_SYSTEM, user_msg, max_tokens=300
        )
        self._add_usage(self.prompter)
        return prompt.strip()

    def _try_openrouter(self, model: str, prompt: str, output_path: Path) -> str | None:
        """Generate image via OpenRouter API. Returns saved path or None."""
        api_key = os.environ.get("OPENROUTER_API_KEY", "")
        if not api_key:
            return None
        try:
            resp = httpx.post(
                OPENROUTER_URL,
                headers={"Authorization": f"Bearer {api_key}"},
                json={
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                },
                timeout=120,
            )
            resp.raise_for_status()
            data = resp.json()
            images = data.get("choices", [{}])[0].get("message", {}).get("images", [])
            for img in images:
                url = img.get("image_url", {}).get("url", "")
                if url.startswith("data:image/"):
                    # Strip "data:image/png;base64," prefix
                    b64 = url.split(",", 1)[1]
                    output_path.write_bytes(base64.b64decode(b64))
                    return str(output_path)
        except Exception:
            pass
        return None

    def _try_google_sdk(self, model: str, prompt: str, aspect_ratio: str, output_path: Path) -> str | None:
        """Fallback: generate via Google AI SDK directly."""
        api_key = os.environ.get("GEMINI_API_KEY", "")
        if not api_key:
            return None
        try:
            from google import genai
            from google.genai import types
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model=model,
                contents=[prompt],
                config=types.GenerateContentConfig(
                    response_modalities=["TEXT", "IMAGE"],
                    image_config=types.ImageConfig(
                        aspect_ratio=aspect_ratio,
                        image_size="2K",
                    ),
                ),
            )
            for part in response.parts:
                if part.inline_data:
                    part.as_image().save(str(output_path))
                    return str(output_path)
        except Exception:
            pass
        return None

    async def generate_image(
        self,
        prompt: str,
        output_dir: Path,
        filename: str = "header.png",
        aspect_ratio: str = "16:9",
    ) -> tuple[str, str]:
        """Generate image, trying OpenRouter first, then Google SDK. Returns (path, model_used)."""
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / filename

        # If a specific model is forced
        if self.forced_model:
            or_model = self.forced_model
            if not or_model.startswith("google/"):
                or_model = f"google/{or_model}"
            result = self._try_openrouter(or_model, prompt, output_path)
            if result:
                return result, or_model
            # Try Google SDK with bare model name
            bare = self.forced_model.removeprefix("google/")
            result = self._try_google_sdk(bare, prompt, aspect_ratio, output_path)
            if result:
                return result, bare
            raise RuntimeError(f"Image generation failed with model {self.forced_model}")

        # Try OpenRouter models (preferred — works without billing)
        for model in OPENROUTER_MODELS:
            result = self._try_openrouter(model, prompt, output_path)
            if result:
                return result, model

        # Fallback to Google SDK
        for model in ["gemini-3-pro-image-preview", "gemini-2.5-flash-image"]:
            result = self._try_google_sdk(model, prompt, aspect_ratio, output_path)
            if result:
                return result, model

        raise RuntimeError(
            "All image generation models failed. Set OPENROUTER_API_KEY or "
            "GEMINI_API_KEY with billing enabled."
        )

    async def run(
        self,
        title: str,
        article: str,
        output_dir: Path,
    ) -> ImageGenResult:
        """Full pipeline: classify → prompt → generate."""
        content_type = await self.classify_content(article)
        style = STYLE_MAP[content_type]
        prompt = await self.generate_prompt(title, article, content_type)

        image_path, model_used = await self.generate_image(prompt, output_dir)

        return ImageGenResult(
            image_path=image_path,
            content_type=content_type,
            style=style["primary"],
            prompt_used=prompt,
            model_used=model_used,
            usage=self.usage,
        )

    def _add_usage(self, agent: BaseAgent) -> None:
        self.usage.input_tokens += agent.usage.input_tokens
        self.usage.output_tokens += agent.usage.output_tokens
        self.usage.calls += agent.usage.calls
