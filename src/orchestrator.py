"""Full pipeline orchestrator with state management and quality gates."""

from dataclasses import dataclass, field
from typing import Any

from src.agents.base import AgentUsage
from src.agents.debate import DebateAgent
from src.agents.disorder import DisorderAgent
from src.agents.insight import InsightPipeline
from src.agents.publisher import PublisherAgent
from src.agents.research import ResearchAgent
from src.agents.writer import WriterAgent
from src.config import load_pipeline_config, load_quality_thresholds
from src.quality.burstiness import compute_burstiness
from src.quality.structural_scanner import scan_structural
from src.quality.vocabulary_scanner import scan_vocabulary
from src.storage.content_store import ContentStore


@dataclass
class PipelineState:
    topic: str = ""
    tier: int = 1
    phase_outputs: dict[str, Any] = field(default_factory=dict)
    scores: dict[str, Any] = field(default_factory=dict)
    usage: AgentUsage = field(default_factory=AgentUsage)
    current_phase: str = ""
    completed_phases: list[str] = field(default_factory=list)


@dataclass
class QualityGateResult:
    passed: bool = True
    failures: list[str] = field(default_factory=list)
    scores: dict[str, float] = field(default_factory=dict)


class PipelineOrchestrator:
    def __init__(self, tier: int = 1) -> None:
        self.tier = tier
        self.config = load_pipeline_config()
        self.thresholds = load_quality_thresholds()
        self.state = PipelineState(tier=tier)
        self.store = ContentStore()

    def _should_skip(self, phase_name: str) -> bool:
        tier_config = self.config["tiers"].get(self.tier, {})
        skip = tier_config.get("skip_phases", [])
        return phase_name in skip

    def _add_usage(self, usage: AgentUsage) -> None:
        self.state.usage.input_tokens += usage.input_tokens
        self.state.usage.output_tokens += usage.output_tokens
        self.state.usage.calls += usage.calls

    async def run_research(self, topic: str) -> str:
        self.state.current_phase = "saturate"
        agent = ResearchAgent()
        result = await agent.run_all_tracks(topic)
        combined = "\n\n".join(
            f"## {t.name}\n{t.content}" for t in result.tracks
        )
        self.state.phase_outputs["research"] = combined
        self._add_usage(result.usage)
        self.state.completed_phases.append("saturate")
        return combined

    async def run_insight(self, research: str) -> str:
        self.state.current_phase = "insight"
        pipeline = InsightPipeline()
        result = await pipeline.run(research)
        insight = (
            f"## Anomalies\n{result.anomalies}\n\n"
            f"## Cross-References\n{result.cross_references}\n\n"
            f"## Mechanism\n{result.mechanism}\n\n"
            f"## Predictions\n{result.predictions}\n\n"
            f"## Validation\n{result.validation}"
        )
        self.state.phase_outputs["insight"] = insight
        self._add_usage(result.usage)
        self.state.completed_phases.extend(
            ["anomalies", "cross_reference", "mechanism", "predict", "validate"]
        )
        return insight

    async def run_debate(self, research: str, anomalies: str) -> str:
        if self._should_skip("debate"):
            return ""
        self.state.current_phase = "debate"
        agent = DebateAgent()
        result = await agent.run(research, anomalies)
        self.state.phase_outputs["debate"] = result.synthesis
        self._add_usage(result.usage)
        self.state.completed_phases.append("debate")
        return result.synthesis

    async def run_disorder(self, research: str, insight: str) -> str:
        self.state.current_phase = "disorder"
        agent = DisorderAgent()
        result = await agent.disorder(research, insight)
        self.state.phase_outputs["disorder"] = result.outline
        self._add_usage(result.usage)
        self.state.completed_phases.append("disorder")
        return result.outline

    async def run_write(self, outline: str, research: str) -> str:
        self.state.current_phase = "write"
        agent = WriterAgent()
        result = await agent.write_and_revise(outline, research)
        self.state.phase_outputs["draft"] = result.draft
        self._add_usage(result.usage)
        self.state.completed_phases.append("write")
        return result.draft

    def run_quality_scan(self, article: str) -> QualityGateResult:
        self.state.current_phase = "quality_scan"
        gate = QualityGateResult()

        structural = scan_structural(article)
        vocab = scan_vocabulary(article)
        burstiness = compute_burstiness(article)

        gate.scores["structural"] = structural.score(
            self.thresholds.get("structural", {})
        )
        gate.scores["vocabulary"] = vocab.score(self.thresholds)
        gate.scores["burstiness"] = burstiness

        # Check structural thresholds
        st = self.thresholds.get("structural", {})
        if "sentence_length_cv" in st:
            if structural.sentence_length_cv < st["sentence_length_cv"].get("min", 0):
                gate.failures.append(
                    f"sentence_length_cv={structural.sentence_length_cv:.2f} "
                    f"< {st['sentence_length_cv']['min']}"
                )

        # Check anti-AI thresholds
        anti = self.thresholds.get("anti_ai", {})
        if "banned_words" in anti:
            if vocab.banned_word_count > anti["banned_words"].get("max", 0):
                gate.failures.append(
                    f"banned_words={vocab.banned_word_count} "
                    f"> {anti['banned_words']['max']}"
                )
        if "burstiness_score" in anti:
            if burstiness < anti["burstiness_score"].get("min", 0):
                gate.failures.append(
                    f"burstiness={burstiness:.2f} "
                    f"< {anti['burstiness_score']['min']}"
                )

        # Check voice thresholds
        voice = self.thresholds.get("voice", {})
        if "conjunction_starts" in voice:
            if vocab.conjunction_starts < voice["conjunction_starts"].get("min", 0):
                gate.failures.append(
                    f"conjunction_starts={vocab.conjunction_starts} "
                    f"< {voice['conjunction_starts']['min']}"
                )
        if "fragments" in voice:
            if vocab.fragment_count < voice["fragments"].get("min", 0):
                gate.failures.append(
                    f"fragments={vocab.fragment_count} "
                    f"< {voice['fragments']['min']}"
                )

        gate.passed = len(gate.failures) == 0
        self.state.scores = gate.scores
        self.state.completed_phases.append("quality_scan")
        return gate

    async def run_revision(
        self, article: str, failures: list[str], max_iterations: int = 3
    ) -> str:
        self.state.current_phase = "revision"
        agent = WriterAgent()
        current = article
        for i in range(max_iterations):
            scan_text = "\n".join(f"- {f}" for f in failures)
            current = await agent.revise(current, scan_text)
            self._add_usage(agent.agent.usage)

            gate = self.run_quality_scan(current)
            if gate.passed:
                break
            failures = gate.failures

        self.state.phase_outputs["revision"] = current
        self.state.completed_phases.append("revision")
        return current

    async def run_publish(self, article: str) -> dict[str, str]:
        self.state.current_phase = "platform_format"
        agent = PublisherAgent()
        result = await agent.format_all(article)
        output = {
            "newsletter": result.newsletter,
            "linkedin": result.linkedin,
            "x_thread": result.x_thread,
        }
        self.state.phase_outputs["publish"] = output
        self._add_usage(result.usage)
        self.state.completed_phases.append("platform_format")
        return output

    async def run_full(self, topic: str) -> PipelineState:
        self.state.topic = topic

        # Phase 1: Research
        research = await self.run_research(topic)

        # Phase 2: Insight generation
        insight = await self.run_insight(research)

        # Phase 3: Debate (tier 3 only)
        await self.run_debate(research, insight)

        # Phase 4: DISORDER
        outline = await self.run_disorder(research, insight)

        # Phase 5: Write
        article = await self.run_write(outline, research)

        # Phase 6: Quality scan
        gate = self.run_quality_scan(article)

        # Phase 7: Revision if needed
        if not gate.passed:
            article = await self.run_revision(article, gate.failures)

        # Phase 8: Platform formatting
        await self.run_publish(article)

        # Save outputs
        cost = self.state.usage.estimated_cost("claude-opus-4-6")
        self.store.save_run(
            topic=topic,
            tier=self.tier,
            phases=self.state.phase_outputs,
            article=article,
            scores=self.state.scores,
            cost=cost,
        )

        return self.state
