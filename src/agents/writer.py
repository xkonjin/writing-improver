from dataclasses import dataclass, field

from src.agents.base import AgentUsage, BaseAgent
from src.prompts.writing import REVISION_SYSTEM, WRITER_SYSTEM


@dataclass
class WriterResult:
    draft: str = ""
    revision_count: int = 0
    usage: AgentUsage = field(default_factory=AgentUsage)


class WriterAgent:
    def __init__(self, model: str = "claude-opus-4-6"):
        self.agent = BaseAgent(model=model)

    async def write_draft(self, outline: str, research_summary: str) -> str:
        user_prompt = (
            f"MESSY OUTLINE (follow this order exactly):\n{outline}\n\n"
            f"RESEARCH NOTES:\n{research_summary[:8000]}\n\n"
            "Write the article following the outline's discovery order. "
            "Follow ALL 12 rules. Write 1500-2500 words."
        )
        return await self.agent.call(WRITER_SYSTEM, user_prompt, max_tokens=8192)

    async def revise(self, draft: str, scan_results: str) -> str:
        user_prompt = (
            f"CURRENT DRAFT:\n{draft}\n\n"
            f"SCAN RESULTS (fix these issues):\n{scan_results}\n\n"
            "Revise the draft to fix the flagged issues while preserving "
            "discovery-order structure and voice."
        )
        return await self.agent.call(REVISION_SYSTEM, user_prompt, max_tokens=8192)

    async def write_and_revise(
        self,
        outline: str,
        research_summary: str,
        scan_fn: object = None,
        max_revisions: int = 3,
    ) -> WriterResult:
        result = WriterResult()
        result.draft = await self.write_draft(outline, research_summary)
        result.usage = self.agent.usage
        return result
