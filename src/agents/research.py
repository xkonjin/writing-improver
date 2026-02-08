import asyncio
from dataclasses import dataclass, field

from src.agents.base import AgentUsage, BaseAgent
from src.prompts.research_track import TRACK_PROMPTS


@dataclass
class ResearchTrack:
    name: str
    content: str
    word_count: int = 0
    data_point_count: int = 0

    def __post_init__(self) -> None:
        self.word_count = len(self.content.split())


@dataclass
class ResearchResult:
    topic: str
    tracks: list[ResearchTrack] = field(default_factory=list)
    usage: AgentUsage = field(default_factory=AgentUsage)

    @property
    def total_words(self) -> int:
        return sum(t.word_count for t in self.tracks)


class ResearchAgent:
    def __init__(self, model: str = "claude-sonnet-4-5-20250929"):
        self.model = model
        self.usage = AgentUsage()

    async def research_track(self, track_name: str, topic: str) -> ResearchTrack:
        agent = BaseAgent(model=self.model)
        system = TRACK_PROMPTS.get(track_name, TRACK_PROMPTS["comparative"])
        user = f"Research topic: {topic}\n\nProvide comprehensive, fact-dense research for this track."

        content = await agent.call(system, user, max_tokens=8192)

        self.usage.input_tokens += agent.usage.input_tokens
        self.usage.output_tokens += agent.usage.output_tokens
        self.usage.calls += agent.usage.calls

        return ResearchTrack(name=track_name, content=content)

    async def run_all_tracks(
        self, topic: str, track_names: list[str] | None = None
    ) -> ResearchResult:
        if track_names is None:
            track_names = list(TRACK_PROMPTS.keys())

        tasks = [self.research_track(name, topic) for name in track_names]
        tracks = await asyncio.gather(*tasks)

        return ResearchResult(
            topic=topic,
            tracks=list(tracks),
            usage=self.usage,
        )
