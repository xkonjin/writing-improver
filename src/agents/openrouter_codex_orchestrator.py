"""Codex-style autonomous orchestration built on OpenRouterSwarm."""

from __future__ import annotations

import asyncio
import random
from dataclasses import dataclass, field

from src.agents.openrouter_swarm import OpenRouterSwarm, SwarmResult
from src.quality.compression_scanner import scan_compression
from src.quality.settlers_validator import (
    SettlersQualityResult,
    SettlersThresholds,
    validate_settlers_quality,
)
from src.quality.surprise_detector import detect_surprise
from src.quality.vocabulary_scanner import scan_vocabulary


@dataclass
class DraftEvaluation:
    draft: str
    settlers: SettlersQualityResult
    compression_score: float
    surprise_score: float
    banned_words: int
    em_dashes_per_1k: float
    failures: list[str] = field(default_factory=list)
    score: float = 0.0


@dataclass
class OrchestrationResult:
    topic: str
    research: list[SwarmResult]
    artifacts: dict[str, str]
    draft: str
    evaluation: DraftEvaluation
    attempts: int
    revisions: list[str] = field(default_factory=list)


class OpenRouterCodexOrchestrator:
    """Parallel agents with self-correction and Settlers-quality validation."""

    def __init__(
        self,
        swarm: OpenRouterSwarm,
        thresholds: SettlersThresholds | None = None,
        max_rounds: int = 3,
        draft_candidates: int = 3,
    ) -> None:
        self.swarm = swarm
        self.thresholds = thresholds or SettlersThresholds()
        self.max_rounds = max_rounds
        self.draft_candidates = draft_candidates

    async def run(self, topic: str, research_agents: int = 7) -> OrchestrationResult:
        research = await self.swarm.research_swarm(topic, num_agents=research_agents)
        research_text = self._merge_research(research, limit=14000)

        artifacts = await self._build_artifacts(topic, research_text)
        drafts = await self._draft_candidates(topic, research_text, artifacts)

        evaluations = [self._evaluate(d) for d in drafts if d.strip()]
        best = self._pick_best(evaluations) if evaluations else self._empty_evaluation()

        revisions = []
        attempts = 1
        while attempts <= self.max_rounds and not self._passes(best):
            revised = await self._self_correct(best.draft, best, artifacts)
            revisions.extend(revised)
            if revised:
                revised_evals = [self._evaluate(d) for d in revised if d.strip()]
                best = self._pick_best([best, *revised_evals])
            attempts += 1

        return OrchestrationResult(
            topic=topic,
            research=research,
            artifacts=artifacts,
            draft=best.draft,
            evaluation=best,
            attempts=attempts,
            revisions=revisions,
        )

    async def _build_artifacts(self, topic: str, research_text: str) -> dict[str, str]:
        tasks = [
            self._mechanism_brief(topic, research_text),
            self._inversion_brief(topic, research_text),
            self._prediction_brief(topic, research_text),
            self._personal_layer_brief(topic, research_text),
        ]
        results = await asyncio.gather(*tasks)
        return {
            "mechanisms": results[0],
            "inversions": results[1],
            "predictions": results[2],
            "personal_layer": results[3],
        }

    async def _mechanism_brief(self, topic: str, research_text: str) -> str:
        model = random.choice(self.swarm.MODELS["premium"])
        system = "You are a mechanism engineer. Return only mechanisms with thresholds."
        user = (
            f"Topic: {topic}\n\nResearch:\n{research_text}\n\n"
            "Produce 12 mechanisms. Each mechanism must include:\n"
            "- A numeric threshold (>=, <=, %, or explicit number)\n"
            "- A causal verb (causes, triggers, forces, flips)\n"
            "No em-dashes. No transitions. No narrative language.\n"
            "Format as short lines, one per mechanism."
        )
        result = await self.swarm.call_model(model, system, user, temperature=0.7, max_tokens=1200)
        return result.content.strip() if not result.error else ""

    async def _inversion_brief(self, topic: str, research_text: str) -> str:
        model = random.choice(self.swarm.MODELS["fast"])
        system = "You are an inversion spotter. Return only inversions with numbers."
        user = (
            f"Topic: {topic}\n\nResearch:\n{research_text}\n\n"
            "Find 6 inversions with specific numbers. Each line must show a reversal or opposite correlation.\n"
            "No em-dashes. No transitions. No narrative language."
        )
        result = await self.swarm.call_model(model, system, user, temperature=0.7, max_tokens=900)
        return result.content.strip() if not result.error else ""

    async def _prediction_brief(self, topic: str, research_text: str) -> str:
        model = random.choice(self.swarm.MODELS["specialized"])
        system = "You are a falsifiable prediction engine."
        user = (
            f"Topic: {topic}\n\nResearch:\n{research_text}\n\n"
            "Produce 6 predictions. Each must include:\n"
            "- A time boundary (year, quarter, or within N months)\n"
            "- A measurable quantity (number or percentage)\n"
            "No em-dashes. No transitions. No narrative language."
        )
        result = await self.swarm.call_model(model, system, user, temperature=0.6, max_tokens=900)
        return result.content.strip() if not result.error else ""

    async def _personal_layer_brief(self, topic: str, research_text: str) -> str:
        model = random.choice(self.swarm.MODELS["premium"])
        system = "You are a voice authenticator. Return short personal layer lines."
        user = (
            f"Topic: {topic}\n\nResearch:\n{research_text}\n\n"
            "Write 4-6 short sentences that include:\n"
            "- A confession or admission (I remember, I got, I was wrong)\n"
            "- Inclusion language (we/us/our)\n"
            "- A concrete memory detail or insider reference\n"
            "No em-dashes. No transitions. No narrative framing."
        )
        result = await self.swarm.call_model(model, system, user, temperature=0.8, max_tokens=700)
        return result.content.strip() if not result.error else ""

    async def _draft_candidates(self, topic: str, research_text: str, artifacts: dict[str, str]) -> list[str]:
        models = [
            random.choice(self.swarm.MODELS["premium"]),
            random.choice(self.swarm.MODELS["premium"]),
            random.choice(self.swarm.MODELS["specialized"]),
        ]
        models = models[: self.draft_candidates]

        tasks = []
        artifact_block = self._artifact_block(artifacts)
        for model in models:
            system = (
                "Write dense analysis without transitions or narrative framing. "
                "No em-dashes. No scene-setting. No summary ending."
            )
            user = (
                f"Topic: {topic}\n\n"
                f"Research:\n{research_text}\n\n"
                f"Mechanisms:\n{artifacts.get('mechanisms','')}\n\n"
                f"Inversions:\n{artifacts.get('inversions','')}\n\n"
                f"Predictions:\n{artifacts.get('predictions','')}\n\n"
                f"Personal layer:\n{artifacts.get('personal_layer','')}\n\n"
                "Write 1200-1700 words.\n"
                "Hard constraints:\n"
                "- Include at least 7 sentences with numeric thresholds and causal verbs.\n"
                "- Include at least 2 inversion sentences with numbers.\n"
                "- Include at least 3 falsifiable predictions with time bounds and quantities.\n"
                "- Include the personal layer inside the article (no separate section).\n"
                "- No em-dashes. No transitions. No narrative language.\n"
                "- No bullet lists, no headings, no summaries.\n"
                "Return only the article text."
            )
            tasks.append(self.swarm.call_model(model, system, user, temperature=0.75, max_tokens=2400))

        results = await asyncio.gather(*tasks)
        return [r.content for r in results if not r.error and r.content]

    async def _self_correct(
        self,
        draft: str,
        evaluation: DraftEvaluation,
        artifacts: dict[str, str],
    ) -> list[str]:
        tasks = []

        missing_mechanisms = self.thresholds.min_mechanisms - evaluation.settlers.mechanism_count
        if missing_mechanisms > 0:
            tasks.append(self._revision_task(
                draft,
                "Mechanism Enforcer",
                "Add missing mechanisms with numeric thresholds and causal verbs. "
                f"Add at least {missing_mechanisms} new mechanism sentences.",
                artifact_block,
            ))

        missing_inversions = self.thresholds.min_inversions - evaluation.settlers.inversion_count
        if missing_inversions > 0:
            tasks.append(self._revision_task(
                draft,
                "Inversion Injector",
                "Add inversion sentences with specific numbers. "
                f"Add at least {missing_inversions} inversions.",
                artifact_block,
            ))

        missing_predictions = self.thresholds.min_predictions - evaluation.settlers.prediction_count
        if missing_predictions > 0:
            tasks.append(self._revision_task(
                draft,
                "Prediction Injector",
                "Add falsifiable predictions with time bounds and measurable quantities. "
                f"Add at least {missing_predictions} predictions.",
                artifact_block,
            ))

        if (
            not evaluation.settlers.confession_found
            or evaluation.settlers.inclusion_pronouns < self.thresholds.min_inclusion_pronouns
        ):
            tasks.append(self._revision_task(
                draft,
                "Personal Layer Injector",
                "Add a short personal layer with confession/admission and we/us/our language. "
                "Keep it embedded, not a separate section.",
                artifact_block,
            ))

        if (
            evaluation.settlers.em_dash_count > 0
            or evaluation.settlers.transition_count > 0
            or evaluation.settlers.narrative_markers > 0
            or evaluation.banned_words > 0
            or evaluation.em_dashes_per_1k > 0
        ):
            tasks.append(self._revision_task(
                draft,
                "AI Tell Scrubber",
                "Remove em-dashes, transitions, narrative markers, and banned AI phrasing. "
                "Do not add new transitions or narrative framing.",
                artifact_block,
            ))

        if evaluation.surprise_score < 0.6:
            tasks.append(self._revision_task(
                draft,
                "Surprise Amplifier",
                "Increase surprise via specific inversions, counterintuitive mechanisms, and named entities.",
                artifact_block,
            ))

        if len(evaluation.failures) >= 2:
            tasks.append(self._revision_task(
                draft,
                "Comprehensive Repair",
                "Fix all detected failures: " + "; ".join(evaluation.failures),
                artifact_block,
            ))

        if not tasks:
            return []

        results = await asyncio.gather(*tasks)
        return [r for r in results if r.strip()]

    async def _revision_task(
        self,
        draft: str,
        role: str,
        instruction: str,
        artifact_block: str,
    ) -> str:
        model = random.choice(self.swarm.MODELS["fast"])
        system = f"You are a {role}. Fix only the listed issues without changing structure."
        user = (
            f"Issues to fix:\n{instruction}\n\n"
            f"{artifact_block}\n\n"
            "Rules:\n"
            "- No em-dashes. No transitions. No narrative language.\n"
            "- No bullet lists or headings.\n"
            "- Keep length within 10%.\n"
            "Rewrite the full article with fixes applied.\n\n"
            f"Article:\n{draft}"
        )
        result = await self.swarm.call_model(model, system, user, temperature=0.6, max_tokens=2400)
        return result.content.strip() if not result.error else ""

    def _evaluate(self, draft: str) -> DraftEvaluation:
        settlers = validate_settlers_quality(draft, self.thresholds)
        compression = scan_compression(draft)
        surprise = detect_surprise(draft)
        vocab = scan_vocabulary(draft)

        failures = list(settlers.failures)
        if surprise.overall < 0.6:
            failures.append(f"surprise_overall={surprise.overall:.2f} < 0.60")
        if compression.overall_score < 7.0:
            failures.append(f"compression_score={compression.overall_score:.1f} < 7.0")
        if vocab.banned_word_count > 0:
            failures.append(f"banned_words={vocab.banned_word_count}")

        score = 0.0
        score += min(settlers.mechanism_count, self.thresholds.min_mechanisms) / self.thresholds.min_mechanisms
        score += min(settlers.inversion_count, self.thresholds.min_inversions) / self.thresholds.min_inversions
        score += min(settlers.prediction_count, self.thresholds.min_predictions) / self.thresholds.min_predictions
        score += 1.0 if (settlers.confession_found or settlers.admission_found) else 0.0
        score += min(surprise.overall, 1.0)
        score += min(compression.overall_score / 10.0, 1.0)
        score -= len(failures) * 0.15

        return DraftEvaluation(
            draft=draft,
            settlers=settlers,
            compression_score=compression.overall_score,
            surprise_score=surprise.overall,
            banned_words=vocab.banned_word_count,
            em_dashes_per_1k=vocab.em_dashes_per_1k,
            failures=failures,
            score=round(score, 3),
        )

    def _pick_best(self, evaluations: list[DraftEvaluation]) -> DraftEvaluation:
        return sorted(
            evaluations,
            key=lambda e: (len(e.failures), -e.score),
        )[0]

    def _passes(self, evaluation: DraftEvaluation) -> bool:
        return len(evaluation.failures) == 0

    def _merge_research(self, research: list[SwarmResult], limit: int = 12000) -> str:
        combined = "\n\n---\n\n".join(
            f"[{r.agent_name} via {r.model}]\n{r.content}" for r in research if not r.error
        )
        return combined[:limit]

    def _artifact_block(self, artifacts: dict[str, str]) -> str:
        return (
            "Reference artifacts (use as raw material, do not paste verbatim unless needed):\n"
            f"Mechanisms:\n{artifacts.get('mechanisms','')}\n\n"
            f"Inversions:\n{artifacts.get('inversions','')}\n\n"
            f"Predictions:\n{artifacts.get('predictions','')}\n\n"
            f"Personal layer:\n{artifacts.get('personal_layer','')}"
        )

    def _empty_evaluation(self) -> DraftEvaluation:
        empty = validate_settlers_quality("", self.thresholds)
        return DraftEvaluation(
            draft="",
            settlers=empty,
            compression_score=0.0,
            surprise_score=0.0,
            banned_words=0,
            em_dashes_per_1k=0.0,
            failures=["no_draft_generated"],
            score=0.0,
        )
