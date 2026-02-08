"""Platform-specific formatting agents."""

from dataclasses import dataclass, field

from src.agents.base import AgentUsage, BaseAgent
from src.prompts.platform_format import (
    LINKEDIN_SYSTEM,
    NEWSLETTER_SYSTEM,
    X_THREAD_SYSTEM,
)


@dataclass
class PublisherResult:
    newsletter: str = ""
    linkedin: str = ""
    x_thread: str = ""
    usage: AgentUsage = field(default_factory=AgentUsage)


class PublisherAgent:
    def __init__(self, model: str = "claude-sonnet-4-5-20250929"):
        self.model = model
        self.usage = AgentUsage()

    async def format_newsletter(self, article: str) -> str:
        agent = BaseAgent(model=self.model)
        result = await agent.call(
            NEWSLETTER_SYSTEM,
            f"Format this article for newsletter:\n\n{article}",
            max_tokens=8192,
        )
        self._add_usage(agent)
        return result

    async def format_linkedin(self, article: str) -> str:
        agent = BaseAgent(model=self.model)
        result = await agent.call(
            LINKEDIN_SYSTEM,
            f"Convert to LinkedIn post:\n\n{article}",
            max_tokens=1024,
        )
        self._add_usage(agent)
        return result

    async def format_x_thread(self, article: str) -> str:
        agent = BaseAgent(model=self.model)
        result = await agent.call(
            X_THREAD_SYSTEM,
            f"Convert to X thread:\n\n{article}",
            max_tokens=2048,
        )
        self._add_usage(agent)
        return result

    async def format_all(self, article: str) -> PublisherResult:
        import asyncio

        newsletter, linkedin, x_thread = await asyncio.gather(
            self.format_newsletter(article),
            self.format_linkedin(article),
            self.format_x_thread(article),
        )
        return PublisherResult(
            newsletter=newsletter,
            linkedin=linkedin,
            x_thread=x_thread,
            usage=self.usage,
        )

    def _add_usage(self, agent: BaseAgent) -> None:
        self.usage.input_tokens += agent.usage.input_tokens
        self.usage.output_tokens += agent.usage.output_tokens
        self.usage.calls += agent.usage.calls
