"""Tests for the image generation agent."""

import base64
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.agents.image_gen import ImageGenAgent
from src.prompts.image_gen import STYLE_MAP


@pytest.fixture
def mock_classifier():
    with patch("src.agents.base.BaseAgent.call", new_callable=AsyncMock) as mock:
        yield mock


def _make_openrouter_response(image_bytes: bytes = b"fakepng") -> dict:
    b64 = base64.b64encode(image_bytes).decode()
    return {
        "choices": [{
            "message": {
                "role": "assistant",
                "content": "",
                "images": [{
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{b64}"},
                }],
            }
        }]
    }


@pytest.mark.asyncio
async def test_classify_bullish(mock_classifier):
    mock_classifier.return_value = "BULLISH"
    agent = ImageGenAgent()
    result = await agent.classify_content("Growth is coming. Revenue up 300%.")
    assert result == "BULLISH"


@pytest.mark.asyncio
async def test_classify_unknown_falls_back_to_technical(mock_classifier):
    mock_classifier.return_value = "NONSENSE_TYPE"
    agent = ImageGenAgent()
    result = await agent.classify_content("Some article text")
    assert result == "TECHNICAL"


@pytest.mark.asyncio
async def test_classify_strips_whitespace(mock_classifier):
    mock_classifier.return_value = "  REGULATORY\n"
    agent = ImageGenAgent()
    result = await agent.classify_content("The GENIUS Act passed")
    assert result == "REGULATORY"


@pytest.mark.asyncio
async def test_generate_prompt_uses_style(mock_classifier):
    mock_classifier.return_value = "Art Deco stablecoin regulation prompt, no text, no words"
    agent = ImageGenAgent()
    prompt = await agent.generate_prompt(
        "Stablecoin Regulation", "Article about regulation", "REGULATORY"
    )
    assert "Art Deco" in prompt


@pytest.mark.asyncio
async def test_generate_image_via_openrouter(tmp_path):
    """OpenRouter path is preferred when OPENROUTER_API_KEY is set."""
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = _make_openrouter_response(b"fake-image-data")
    mock_resp.raise_for_status = MagicMock()

    with (
        patch("src.agents.image_gen.httpx.post", return_value=mock_resp),
        patch.dict("os.environ", {"OPENROUTER_API_KEY": "test-or-key"}, clear=True),
    ):
        agent = ImageGenAgent()
        path, model = await agent.generate_image("test prompt", tmp_path)

    assert path == str(tmp_path / "header.png")
    assert model == "google/gemini-2.5-flash-image"
    assert (tmp_path / "header.png").read_bytes() == base64.b64decode(
        base64.b64encode(b"fake-image-data")
    )


@pytest.mark.asyncio
async def test_generate_image_falls_back_to_google_sdk(tmp_path):
    """When OpenRouter is not available, falls back to Google SDK."""
    mock_image = MagicMock()
    mock_part = MagicMock()
    mock_part.inline_data = True
    mock_part.as_image.return_value = mock_image

    mock_response = MagicMock()
    mock_response.parts = [mock_part]

    with (
        patch("src.agents.image_gen.httpx.post", side_effect=Exception("no openrouter")),
        patch.dict("os.environ", {"OPENROUTER_API_KEY": "key", "GEMINI_API_KEY": "test-key"}, clear=True),
    ):
        with patch("src.agents.image_gen.ImageGenAgent._try_google_sdk") as mock_sdk:
            mock_sdk.return_value = str(tmp_path / "header.png")
            agent = ImageGenAgent()
            path, model = await agent.generate_image("test prompt", tmp_path)

    assert "header.png" in path
    assert model == "gemini-3-pro-image-preview"


@pytest.mark.asyncio
async def test_generate_image_raises_when_all_fail(tmp_path):
    """When all backends fail, raises RuntimeError."""
    with (
        patch("src.agents.image_gen.httpx.post", side_effect=Exception("fail")),
        patch.dict("os.environ", {"OPENROUTER_API_KEY": "k", "GEMINI_API_KEY": "k"}, clear=True),
    ):
        agent = ImageGenAgent()
        with pytest.raises(RuntimeError, match="All image generation models failed"):
            await agent.generate_image("test", tmp_path)


@pytest.mark.asyncio
async def test_generate_image_raises_without_any_api_key(tmp_path):
    """No keys set at all → RuntimeError."""
    with patch.dict("os.environ", {}, clear=True):
        agent = ImageGenAgent()
        with pytest.raises(RuntimeError, match="All image generation models failed"):
            await agent.generate_image("test", tmp_path)


@pytest.mark.asyncio
async def test_generate_image_forced_model(tmp_path):
    """Forced model routes through OpenRouter with google/ prefix."""
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = _make_openrouter_response()
    mock_resp.raise_for_status = MagicMock()

    with (
        patch("src.agents.image_gen.httpx.post", return_value=mock_resp),
        patch.dict("os.environ", {"OPENROUTER_API_KEY": "key"}, clear=True),
    ):
        agent = ImageGenAgent(model="gemini-2.5-flash-image")
        path, model = await agent.generate_image("test", tmp_path)

    assert model == "google/gemini-2.5-flash-image"


def test_all_content_types_have_styles():
    expected = {"BULLISH", "BEARISH", "REGULATORY", "CONTRARIAN", "PARADOX", "TECHNICAL", "PARADIGM_SHIFT"}
    assert set(STYLE_MAP.keys()) == expected


def test_style_map_has_required_keys():
    for content_type, style in STYLE_MAP.items():
        assert "primary" in style, f"{content_type} missing 'primary'"
        assert "prompt" in style, f"{content_type} missing 'prompt'"
        assert "palette" in style, f"{content_type} missing 'palette'"


@pytest.mark.asyncio
async def test_full_run(mock_classifier, tmp_path):
    mock_classifier.side_effect = [
        "BEARISH",  # classify call
        "Nihei megastructure prompt, no text",  # prompter call
    ]

    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = _make_openrouter_response()
    mock_resp.raise_for_status = MagicMock()

    with (
        patch("src.agents.image_gen.httpx.post", return_value=mock_resp),
        patch.dict("os.environ", {"OPENROUTER_API_KEY": "key"}, clear=True),
    ):
        agent = ImageGenAgent()
        result = await agent.run("Market Crash", "The market is crashing", tmp_path)

    assert result.content_type == "BEARISH"
    assert result.style == "Isometric diorama — decay"
    assert result.image_path == str(tmp_path / "header.png")
    assert result.model_used == "google/gemini-2.5-flash-image"
