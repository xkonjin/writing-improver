"""Compression-Maximized Swarm Pipeline.

Core features:
1) Socratic first-principles discovery (observation -> why -> mechanism)
2) Multi-agent specialist swarm with shared context
3) Collision detection (contradictions + syntheses)
4) Real-time quality guidance during generation
5) Adaptive, topic-specific thresholds learned from successful outputs
"""

from __future__ import annotations

import asyncio
import json
import math
import random
import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from src.agents.openrouter_swarm import OpenRouterSwarm, SwarmResult
from src.compression.kolmogorov_maximizer import KolmogorovInsight, KolmogorovMaximizer
from src.config import load_quality_thresholds
from src.quality.adaptive_thresholds import AdaptiveThresholds
from src.quality.guidance import QualityGuidanceEngine, QualitySnapshot


@dataclass
class RoleSpec:
    name: str
    focus: str
    kind: str
    model_tier: str


@dataclass
class SwarmConfig:
    socratic_depth: int = 4
    observation_count: int = 6
    max_insights_per_agent: int = 6
    target_words: int = 1400
    chunk_words: int = 350
    writer_model_tier: str = "premium"
    socratic_model_tier: str = "premium"
    observation_model_tier: str = "fast"
    enable_llm_collision: bool = True
    enable_llm_compression: bool = True
    guidance_actions: int = 6
    min_quality_score: float = 7.0
    specialist_roles: list[RoleSpec] = field(
        default_factory=lambda: [
            RoleSpec(
                name="Mechanism Engineer",
                focus="Extract causal chains with thresholds and numbers.",
                kind="mechanism",
                model_tier="premium",
            ),
            RoleSpec(
                name="Threshold Hunter",
                focus="Find tipping points, critical masses, and exact percentages.",
                kind="mechanism",
                model_tier="fast",
            ),
            RoleSpec(
                name="Inversion Spotter",
                focus="Identify opposite correlations and counterintuitive reversals.",
                kind="inversion",
                model_tier="specialized",
            ),
            RoleSpec(
                name="Incentive Mapper",
                focus="Who benefits, who loses, and what incentives drive the outcome.",
                kind="mechanism",
                model_tier="fast",
            ),
            RoleSpec(
                name="Historical Rhymer",
                focus="Find concrete historical parallels with dates and outcomes.",
                kind="prediction",
                model_tier="fast",
            ),
            RoleSpec(
                name="Prediction Engine",
                focus="Produce falsifiable predictions with time bounds and quantities.",
                kind="prediction",
                model_tier="premium",
            ),
        ]
    )


@dataclass
class Observation:
    text: str
    evidence: str = ""
    uncertainty: str = ""


@dataclass
class SocraticTurn:
    question: str
    answer: str
    mechanism: str
    assumption_broken: str
    next_question: str
    depth: int


@dataclass
class SocraticChain:
    observation: Observation
    turns: list[SocraticTurn] = field(default_factory=list)


@dataclass
class Insight:
    agent: str
    kind: str
    text: str
    evidence: str = ""
    entities: list[str] = field(default_factory=list)
    direction: str = "flat"


@dataclass
class Collision:
    kind: str
    insight_a: Insight
    insight_b: Insight
    shared_entities: list[str]
    rationale: str


@dataclass
class CollisionReport:
    contradictions: list[Collision] = field(default_factory=list)
    syntheses: list[Collision] = field(default_factory=list)
    llm_notes: str = ""


@dataclass
class CompressionBrief:
    principles: list[str] = field(default_factory=list)
    predictions: list[str] = field(default_factory=list)
    kolmogorov_insights: list[KolmogorovInsight] = field(default_factory=list)
    collision_notes: list[str] = field(default_factory=list)


@dataclass
class SwarmRun:
    topic: str
    observations: list[Observation]
    socratic_chains: list[SocraticChain]
    insights: list[Insight]
    collisions: CollisionReport
    compression_brief: CompressionBrief
    draft: str
    guidance_log: list[QualitySnapshot]
    final_snapshot: QualitySnapshot
    thresholds_used: dict[str, Any]
    tokens_used: int
    started_at: str
    finished_at: str


class CompressionMaxSwarm:
    """Unified swarm pipeline with Socratic discovery + compression guidance."""

    def __init__(
        self,
        swarm: OpenRouterSwarm,
        config: SwarmConfig | None = None,
        thresholds: dict[str, Any] | None = None,
        adaptive: AdaptiveThresholds | None = None,
    ) -> None:
        self.swarm = swarm
        self.config = config or SwarmConfig()
        self.base_thresholds = thresholds or load_quality_thresholds()
        self.adaptive = adaptive or AdaptiveThresholds()
        self.guidance_engine = QualityGuidanceEngine()
        self.compressor = KolmogorovMaximizer()

    async def run(self, topic: str) -> SwarmRun:
        started = datetime.utcnow().isoformat()

        observations = await self._collect_observations(topic)
        socratic_chains = await self._socratic_discovery(topic, observations)
        insights, tokens_used = await self._specialist_swarm(topic, observations, socratic_chains)
        collisions = await self._detect_collisions(topic, insights)
        compression_brief = await self._build_compression_brief(topic, observations, socratic_chains, insights, collisions)

        thresholds = self.adaptive.thresholds_for_topic(self.base_thresholds, topic)
        draft, guidance_log, writer_tokens = await self._write_with_guidance(
            topic, observations, socratic_chains, insights, collisions, compression_brief, thresholds
        )
        tokens_used += writer_tokens

        final_snapshot = self.guidance_engine.analyze(draft, thresholds)
        passed = self._passes(final_snapshot)
        self.adaptive.record(topic, final_snapshot.to_metrics(), passed=passed)

        finished = datetime.utcnow().isoformat()

        return SwarmRun(
            topic=topic,
            observations=observations,
            socratic_chains=socratic_chains,
            insights=insights,
            collisions=collisions,
            compression_brief=compression_brief,
            draft=draft,
            guidance_log=guidance_log,
            final_snapshot=final_snapshot,
            thresholds_used=thresholds,
            tokens_used=tokens_used,
            started_at=started,
            finished_at=finished,
        )

    async def _collect_observations(self, topic: str) -> list[Observation]:
        model = random.choice(self.swarm.MODELS[self.config.observation_model_tier])
        system = "You are a field researcher. Output only JSON."
        user = (
            f"Topic: {topic}\n\n"
            f"Provide {self.config.observation_count} to {self.config.observation_count + 2} concrete observations.\n"
            "Rules:\n"
            "- Each observation must include a specific number, date, or named entity\n"
            "- No interpretation or narrative\n"
            "- Output JSON: {\"observations\":[{\"text\":\"...\",\"evidence\":\"...\",\"uncertainty\":\"low|medium|high\"}]}"
        )
        result = await self.swarm.call_model(model, system, user, temperature=0.6, max_tokens=900)
        if result.error:
            return []
        data = self._safe_json(result.content)
        observations = []
        for item in data.get("observations", []):
            if not isinstance(item, dict):
                continue
            observations.append(
                Observation(
                    text=str(item.get("text", "")).strip(),
                    evidence=str(item.get("evidence", "")).strip(),
                    uncertainty=str(item.get("uncertainty", "")).strip(),
                )
            )
        if observations:
            return observations
        return self._fallback_observations(result.content)

    async def _socratic_discovery(
        self, topic: str, observations: list[Observation]
    ) -> list[SocraticChain]:
        tasks = [self._socratic_chain(topic, obs) for obs in observations]
        return await asyncio.gather(*tasks) if tasks else []

    async def _socratic_chain(self, topic: str, observation: Observation) -> SocraticChain:
        chain = SocraticChain(observation=observation)
        current_question = f"Why does this observation hold: {observation.text}?"

        for depth in range(self.config.socratic_depth):
            model = random.choice(self.swarm.MODELS[self.config.socratic_model_tier])
            system = "You are a Socratic mechanism interrogator. Output only JSON."
            user = (
                f"Topic: {topic}\nObservation: {observation.text}\n"
                f"Question: {current_question}\n\n"
                "Return JSON with keys: answer, mechanism, assumption_broken, next_question."
            )
            result = await self.swarm.call_model(model, system, user, temperature=0.5, max_tokens=700)
            if result.error:
                break
            data = self._safe_json(result.content)
            answer = str(data.get("answer", "")).strip()
            mechanism = str(data.get("mechanism", "")).strip()
            assumption = str(data.get("assumption_broken", "")).strip()
            next_q = str(data.get("next_question", "")).strip()
            if not answer:
                break
            chain.turns.append(
                SocraticTurn(
                    question=current_question,
                    answer=answer,
                    mechanism=mechanism or answer,
                    assumption_broken=assumption or "unstated assumption",
                    next_question=next_q or current_question,
                    depth=depth,
                )
            )
            if not next_q or next_q == current_question:
                break
            current_question = next_q

        return chain

    async def _specialist_swarm(
        self,
        topic: str,
        observations: list[Observation],
        socratic_chains: list[SocraticChain],
    ) -> tuple[list[Insight], int]:
        tasks = []
        for role in self.config.specialist_roles:
            tasks.append(self._run_specialist(role, topic, observations, socratic_chains))
        results = await asyncio.gather(*tasks) if tasks else []

        insights: list[Insight] = []
        tokens_used = 0
        for role, result in results:
            tokens_used += result.tokens_used
            if result.error or not result.content:
                continue
            insights.extend(self._parse_insights(role, result.content))
        return insights, tokens_used

    async def _run_specialist(
        self,
        role: RoleSpec,
        topic: str,
        observations: list[Observation],
        socratic_chains: list[SocraticChain],
    ) -> tuple[RoleSpec, SwarmResult]:
        model = random.choice(self.swarm.MODELS[role.model_tier])
        system = f"You are {role.name}. Output only JSON."
        observation_block = "\n".join(f"- {o.text} ({o.evidence})" for o in observations[:8])
        socratic_block = "\n".join(
            f"- {c.observation.text} -> {c.turns[-1].mechanism}"
            for c in socratic_chains
            if c.turns
        )
        user = (
            f"Topic: {topic}\n\n"
            f"Observations:\n{observation_block}\n\n"
            f"Socratic mechanisms:\n{socratic_block}\n\n"
            f"Task: {role.focus}\n"
            f"Return JSON: {{\"insights\":[{{\"kind\":\"{role.kind}\",\"text\":\"...\","
            "\"evidence\":\"numbers/dates\", \"direction\":\"up|down|flat\"}}]}}\n"
            f"Limit to {self.config.max_insights_per_agent} insights. No narrative."
        )
        result = await self.swarm.call_model(model, system, user, temperature=0.7, max_tokens=1200)
        return role, result

    async def _detect_collisions(self, topic: str, insights: list[Insight]) -> CollisionReport:
        report = CollisionReport()
        report.contradictions = self._heuristic_contradictions(insights)
        report.syntheses = self._heuristic_syntheses(insights)

        if not self.config.enable_llm_collision or not insights:
            return report

        model = random.choice(self.swarm.MODELS["fast"])
        system = "You are a collision detector. Output concise bullet points."
        insight_block = "\n".join(f"- ({i.kind}) {i.text}" for i in insights[:20])
        user = (
            f"Topic: {topic}\n\nInsights:\n{insight_block}\n\n"
            "Find contradictions and syntheses. Output two sections:\n"
            "Contradictions:\n- ...\nSyntheses:\n- ..."
        )
        result = await self.swarm.call_model(model, system, user, temperature=0.4, max_tokens=700)
        if not result.error:
            report.llm_notes = result.content.strip()
        return report

    async def _build_compression_brief(
        self,
        topic: str,
        observations: list[Observation],
        socratic_chains: list[SocraticChain],
        insights: list[Insight],
        collisions: CollisionReport,
    ) -> CompressionBrief:
        candidates = [i.text for i in insights if i.text]
        candidates.extend([o.text for o in observations])
        candidates = candidates[:24]

        kolmogorov_insights: list[KolmogorovInsight] = []
        for chunk in self._chunk_list(candidates, 8):
            if len(chunk) < 3:
                continue
            kolmogorov_insights.append(self.compressor.compress_observations(chunk))

        principles = [k.core_statement for k in kolmogorov_insights]
        predictions = [k.falsifiable_prediction for k in kolmogorov_insights]
        collision_notes = self._collision_notes(collisions)

        if self.config.enable_llm_compression and candidates:
            model = random.choice(self.swarm.MODELS["premium"])
            system = "You are a compression maximizer. Output concise bullet points."
            socratic_block = "\n".join(
                f"- {c.observation.text}: {c.turns[-1].mechanism}" for c in socratic_chains if c.turns
            )
            user = (
                f"Topic: {topic}\n\n"
                f"Observations:\n{chr(10).join(candidates[:12])}\n\n"
                f"Socratic mechanisms:\n{socratic_block}\n\n"
                f"Collisions:\n{chr(10).join(collision_notes)}\n\n"
                "Produce:\n"
                "1) 3-5 compression-maximized principles (one sentence each)\n"
                "2) 3 falsifiable predictions with time bounds\n"
                "Output in plain text with bullet points."
            )
            result = await self.swarm.call_model(model, system, user, temperature=0.5, max_tokens=900)
            if not result.error:
                principles, predictions = self._parse_principles_predictions(result.content)

        return CompressionBrief(
            principles=principles[:5],
            predictions=predictions[:4],
            kolmogorov_insights=kolmogorov_insights,
            collision_notes=collision_notes,
        )

    async def _write_with_guidance(
        self,
        topic: str,
        observations: list[Observation],
        socratic_chains: list[SocraticChain],
        insights: list[Insight],
        collisions: CollisionReport,
        brief: CompressionBrief,
        thresholds: dict[str, Any],
    ) -> tuple[str, list[QualitySnapshot], int]:
        model = random.choice(self.swarm.MODELS[self.config.writer_model_tier])
        chunks = max(1, math.ceil(self.config.target_words / self.config.chunk_words))

        observation_block = "\n".join(f"- {o.text} ({o.evidence})" for o in observations[:8])
        socratic_block = "\n".join(
            f"- {c.observation.text} -> {c.turns[-1].mechanism}" for c in socratic_chains if c.turns
        )
        collision_block = "\n".join(self._collision_notes(collisions))
        principle_block = "\n".join(f"- {p}" for p in brief.principles)
        prediction_block = "\n".join(f"- {p}" for p in brief.predictions)

        guidance_log: list[QualitySnapshot] = []
        draft_parts: list[str] = []
        tokens_used = 0
        guidance = (
            "Start with the most surprising number. Build from concrete observations to general rules. "
            "No signposting. No uniform sections. Ventilated prose. Iceberg structure."
        )

        for index in range(chunks):
            tail = self._tail_text(" ".join(draft_parts), 200)
            system = "Write dense, mechanism-first analysis. No em-dashes."
            user = (
                f"Topic: {topic}\n\n"
                f"Observations:\n{observation_block}\n\n"
                f"Socratic mechanisms:\n{socratic_block}\n\n"
                f"Collision map:\n{collision_block}\n\n"
                f"Compression principles:\n{principle_block}\n\n"
                f"Predictions:\n{prediction_block}\n\n"
                f"Guidance:\n{guidance}\n\n"
                f"Existing tail (avoid repeating):\n{tail}\n\n"
                f"Write the next ~{self.config.chunk_words} words. "
                "No headings, no bullets, no summary ending. "
                "Embed margin-note style asides in brackets sparingly."
            )
            result = await self.swarm.call_model(model, system, user, temperature=0.7, max_tokens=1400)
            tokens_used += result.tokens_used
            if result.error:
                break
            draft_parts.append(result.content.strip())
            partial = "\n\n".join(draft_parts)
            snapshot = self.guidance_engine.analyze(partial, thresholds)
            guidance_log.append(snapshot)
            guidance = self.guidance_engine.build_guidance(
                snapshot, thresholds, max_actions=self.config.guidance_actions
            )

        return "\n\n".join(draft_parts).strip(), guidance_log, tokens_used

    def _passes(self, snapshot: QualitySnapshot) -> bool:
        scores = snapshot.scores
        if not scores:
            return False
        required = [scores.get("compression", 0), scores.get("vocabulary", 0), scores.get("structural", 0)]
        return min(required) >= self.config.min_quality_score

    def _parse_insights(self, role: RoleSpec, text: str) -> list[Insight]:
        data = self._safe_json(text)
        insights: list[Insight] = []
        for item in data.get("insights", []):
            if not isinstance(item, dict):
                continue
            content = str(item.get("text", "")).strip()
            if not content:
                continue
            kind = str(item.get("kind", role.kind)).strip() or role.kind
            evidence = str(item.get("evidence", "")).strip()
            direction = str(item.get("direction", "")).strip() or self._direction_from_text(content)
            entities = self._extract_entities(content)
            insights.append(
                Insight(
                    agent=role.name,
                    kind=kind,
                    text=content,
                    evidence=evidence,
                    direction=direction,
                    entities=entities,
                )
            )
        if insights:
            return insights
        return self._fallback_insights(role, text)

    def _heuristic_contradictions(self, insights: list[Insight]) -> list[Collision]:
        contradictions: list[Collision] = []
        for i, a in enumerate(insights):
            for b in insights[i + 1 :]:
                shared = list(set(a.entities) & set(b.entities))
                if not shared:
                    continue
                if a.direction != "flat" and b.direction != "flat" and a.direction != b.direction:
                    contradictions.append(
                        Collision(
                            kind="contradiction",
                            insight_a=a,
                            insight_b=b,
                            shared_entities=shared,
                            rationale="Opposite directional claims for shared entities.",
                        )
                    )
        return contradictions

    def _heuristic_syntheses(self, insights: list[Insight]) -> list[Collision]:
        syntheses: list[Collision] = []
        for i, a in enumerate(insights):
            for b in insights[i + 1 :]:
                shared = list(set(a.entities) & set(b.entities))
                if not shared:
                    continue
                if a.kind != b.kind and a.direction == b.direction:
                    syntheses.append(
                        Collision(
                            kind="synthesis",
                            insight_a=a,
                            insight_b=b,
                            shared_entities=shared,
                            rationale="Same entities with different lenses; combine for deeper mechanism.",
                        )
                    )
        return syntheses

    def _collision_notes(self, collisions: CollisionReport) -> list[str]:
        notes = []
        for c in collisions.contradictions[:5]:
            notes.append(f"Contradiction: {c.insight_a.text} <> {c.insight_b.text}")
        for c in collisions.syntheses[:5]:
            notes.append(f"Synthesis: {c.insight_a.text} + {c.insight_b.text}")
        if collisions.llm_notes:
            notes.append(collisions.llm_notes)
        return notes

    def _direction_from_text(self, text: str) -> str:
        up = re.search(r"\b(increase|rise|grow|expand|accelerat|higher)\b", text, re.IGNORECASE)
        down = re.search(r"\b(decrease|fall|decline|shrink|slower|lower)\b", text, re.IGNORECASE)
        if up and down:
            return "mixed"
        if up:
            return "up"
        if down:
            return "down"
        return "flat"

    def _extract_entities(self, text: str) -> list[str]:
        entities = re.findall(r"\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b", text)
        acronyms = re.findall(r"\b[A-Z]{2,}\b", text)
        return list(dict.fromkeys(entities + acronyms))[:6]

    def _parse_principles_predictions(self, text: str) -> tuple[list[str], list[str]]:
        principles: list[str] = []
        predictions: list[str] = []
        current = None
        for line in text.splitlines():
            clean = line.strip("-• ").strip()
            if not clean:
                continue
            if clean.lower().startswith("predictions"):
                current = "predictions"
                continue
            if clean.lower().startswith("principles"):
                current = "principles"
                continue
            if current == "predictions":
                predictions.append(clean)
            else:
                principles.append(clean)
        if not predictions and principles:
            predictions = [p for p in principles if "by" in p.lower() or "within" in p.lower()]
        return principles, predictions

    def _chunk_list(self, items: list[str], size: int) -> list[list[str]]:
        return [items[i : i + size] for i in range(0, len(items), size)]

    def _tail_text(self, text: str, max_words: int) -> str:
        words = text.split()
        return " ".join(words[-max_words:]) if words else ""

    def _safe_json(self, text: str) -> dict[str, Any]:
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            match = re.search(r"\{.*\}", text, re.DOTALL)
            if match:
                try:
                    return json.loads(match.group(0))
                except json.JSONDecodeError:
                    return {}
        return {}

    def _fallback_observations(self, text: str) -> list[Observation]:
        observations = []
        for line in text.splitlines():
            clean = line.strip("-• ").strip()
            if len(clean) < 8:
                continue
            observations.append(Observation(text=clean))
        return observations[: self.config.observation_count]

    def _fallback_insights(self, role: RoleSpec, text: str) -> list[Insight]:
        insights = []
        for line in text.splitlines():
            clean = line.strip("-• ").strip()
            if len(clean) < 8:
                continue
            insights.append(
                Insight(
                    agent=role.name,
                    kind=role.kind,
                    text=clean,
                    entities=self._extract_entities(clean),
                    direction=self._direction_from_text(clean),
                )
            )
        return insights[: self.config.max_insights_per_agent]
