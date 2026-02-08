from dataclasses import dataclass, field

from src.agents.base import AgentUsage, BaseAgent
from src.prompts.disorder import DISORDER_SYSTEM


@dataclass
class DisorderResult:
    outline: str = ""
    discovery_sequence: str = ""
    direction_changes: list[str] = field(default_factory=list)
    usage: AgentUsage = field(default_factory=AgentUsage)


class DisorderAgent:
    def __init__(self, model: str = "claude-opus-4-6"):
        self.agent = BaseAgent(model=model)

    async def disorder(self, research: str, insight: str) -> DisorderResult:
        user_prompt = (
            f"ORGANIZED RESEARCH (break this):\n{research[:10000]}\n\n"
            f"VALIDATED INSIGHT:\n{insight[:4000]}\n\n"
            "Now BREAK the organization. Output a messy, discovery-order outline."
        )

        outline = await self.agent.call(DISORDER_SYSTEM, user_prompt, max_tokens=4096)

        return DisorderResult(
            outline=outline,
            usage=self.agent.usage,
        )
