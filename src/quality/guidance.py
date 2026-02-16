"""Real-time quality guidance for compression-maximized writing.

Provides:
1) QualitySnapshot: metrics + scores for a draft or partial draft
2) QualityGuidanceEngine: converts metrics into actionable guidance

Designed to be used during generation (chunk-by-chunk), not just after.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from src.quality.burstiness import compute_burstiness
from src.quality.compression_scanner import scan_compression
from src.quality.structural_scanner import scan_structural
from src.quality.surprise_detector import detect_surprise
from src.quality.vocabulary_scanner import scan_vocabulary


@dataclass
class QualitySnapshot:
    """Metrics and scores for a draft or partial draft."""

    metrics: dict[str, float] = field(default_factory=dict)
    scores: dict[str, float] = field(default_factory=dict)
    issues: list[str] = field(default_factory=list)

    def to_metrics(self) -> dict[str, float]:
        return dict(self.metrics)


class QualityGuidanceEngine:
    """Compute metrics and produce actionable guidance for the next chunk."""

    def analyze(self, text: str, thresholds: dict[str, Any]) -> QualitySnapshot:
        structural = scan_structural(text)
        vocab = scan_vocabulary(text)
        surprise = detect_surprise(text)
        compression = scan_compression(text)
        burstiness = compute_burstiness(text)

        scores = {
            "structural": structural.score(thresholds.get("structural", {})),
            "vocabulary": vocab.score(thresholds),
            "surprise": round(surprise.overall, 2),
            "compression": compression.score(thresholds.get("compression", {})),
            "burstiness": round(burstiness, 3),
        }

        metrics = {
            "structural.sentence_length_cv": structural.sentence_length_cv,
            "structural.paragraph_word_std": structural.paragraph_word_std,
            "structural.single_sentence_paragraphs": float(structural.single_sentence_paragraphs),
            "structural.formal_transitions_per_1k": structural.formal_transitions_per_1k,
            "structural.self_refs_per_1k": structural.self_refs_per_1k,
            "structural.section_ratio": structural.section_ratio,
            "structural.solution_pct": structural.solution_pct,
            "vocab.banned_words": float(vocab.banned_word_count),
            "vocab.conjunction_starts": float(vocab.conjunction_starts),
            "vocab.fragments": float(vocab.fragment_count),
            "vocab.contractions_per_200w": vocab.contractions_per_200w,
            "compression.lexical_density": compression.lexical_density,
            "compression.zero_info_transitions": float(compression.zero_info_transitions),
            "compression.redundancy_count": float(compression.redundancy_count),
            "compression.specificity_ratio": compression.specificity_ratio,
            "compression.filler_phrases": float(compression.filler_phrases),
            "surprise.overall": surprise.overall,
            "surprise.levine_score": surprise.levine_score,
            "surprise.first_principles_score": surprise.first_principles_score,
            "surprise.bidirectional_score": surprise.bidirectional_score,
            "surprise.falsification_score": surprise.falsification_score,
            "burstiness.score": burstiness,
        }

        issues = []
        issues.extend(self._threshold_issues(metrics, thresholds))
        issues.extend(structural.issues)
        issues.extend(vocab.issues)
        issues.extend(compression.issues)
        issues.extend(surprise.issues)

        return QualitySnapshot(metrics=metrics, scores=scores, issues=list(dict.fromkeys(issues)))

    def build_guidance(
        self,
        snapshot: QualitySnapshot,
        thresholds: dict[str, Any],
        max_actions: int = 6,
    ) -> str:
        """Translate metrics into concise, high-impact instructions."""

        actions: list[str] = []
        compression_t = thresholds.get("compression", {})
        structural_t = thresholds.get("structural", {})
        anti_ai = thresholds.get("anti_ai", {})
        voice_t = thresholds.get("voice", {})
        surprise_t = thresholds.get("surprise", {})

        metrics = snapshot.metrics

        # Compression guidance
        if metrics.get("compression.lexical_density", 0) < compression_t.get("lexical_density_min", 0.5):
            actions.append(
                f"Increase lexical density to >= {compression_t.get('lexical_density_min', 0.5):.2f} "
                "by removing scaffolding and compressing clauses."
            )
        if metrics.get("compression.zero_info_transitions", 0) > compression_t.get("zero_info_transitions_max", 3):
            actions.append("Remove zero-info transitions (Also, Furthermore, Moving on).")
        if metrics.get("compression.redundancy_count", 0) > compression_t.get("redundancy_max", 2):
            actions.append("Cut redundancy markers (In other words, To put it simply).")
        if metrics.get("compression.specificity_ratio", 0) < compression_t.get("specificity_ratio_min", 2.0):
            actions.append(
                f"Raise specificity ratio to >= {compression_t.get('specificity_ratio_min', 2.0):.1f}% "
                "by adding more numbers, dates, and proper nouns."
            )
        if metrics.get("compression.filler_phrases", 0) > compression_t.get("filler_phrases_max", 3):
            actions.append("Remove filler phrases (It's clear that, There's no doubt).")

        # Structural guidance
        if metrics.get("structural.sentence_length_cv", 0) < structural_t.get("sentence_length_cv", {}).get("min", 0):
            actions.append("Increase sentence length variance with sharp short lines and longer mechanics.")
        if metrics.get("structural.single_sentence_paragraphs", 0) < structural_t.get(
            "single_sentence_paragraphs", {}
        ).get("min", 0):
            actions.append("Add a few single-sentence paragraphs for ventilation.")
        if metrics.get("structural.formal_transitions_per_1k", 0) > structural_t.get(
            "formal_transitions_per_1k", {}
        ).get("max", 0):
            actions.append("Remove formal transition phrases and jump straight to mechanisms.")

        # Anti-AI / voice guidance
        if metrics.get("vocab.banned_words", 0) > anti_ai.get("banned_words", {}).get("max", 0):
            actions.append("Replace banned buzzwords; use concrete verbs and numbers.")
        if metrics.get("vocab.conjunction_starts", 0) < voice_t.get("conjunction_starts", {}).get("min", 0):
            actions.append("Start more sentences with And/But/So to vary rhythm.")
        if metrics.get("vocab.fragments", 0) < voice_t.get("fragments", {}).get("min", 0):
            actions.append("Add short fragments as stand-alone paragraphs.")

        # Surprise guidance
        if metrics.get("surprise.overall", 0) < surprise_t.get("overall", {}).get("min", 0.5):
            actions.append(
                "Add theory-reality gaps with specific numbers and a falsifiable prediction."
            )

        # Keep the list short and actionable
        unique = list(dict.fromkeys(actions))
        return "\n".join(f"- {action}" for action in unique[:max_actions])

    def _threshold_issues(self, metrics: dict[str, float], thresholds: dict[str, Any]) -> list[str]:
        issues: list[str] = []

        compression_t = thresholds.get("compression", {})
        if metrics.get("compression.lexical_density", 1) < compression_t.get("lexical_density_min", 0.5):
            issues.append("Compression: lexical density below target.")
        if metrics.get("compression.zero_info_transitions", 0) > compression_t.get("zero_info_transitions_max", 3):
            issues.append("Compression: too many zero-info transitions.")
        if metrics.get("compression.redundancy_count", 0) > compression_t.get("redundancy_max", 2):
            issues.append("Compression: redundancy markers above target.")
        if metrics.get("compression.specificity_ratio", 100) < compression_t.get("specificity_ratio_min", 2.0):
            issues.append("Compression: specificity ratio below target.")
        if metrics.get("compression.filler_phrases", 0) > compression_t.get("filler_phrases_max", 3):
            issues.append("Compression: filler phrases above target.")

        structural_t = thresholds.get("structural", {})
        if metrics.get("structural.sentence_length_cv", 1) < structural_t.get("sentence_length_cv", {}).get("min", 0):
            issues.append("Structural: sentence length variance too low.")
        if metrics.get("structural.paragraph_word_std", 1) < structural_t.get("paragraph_word_std", {}).get("min", 0):
            issues.append("Structural: paragraph length variance too low.")
        if metrics.get("structural.single_sentence_paragraphs", 0) < structural_t.get(
            "single_sentence_paragraphs", {}
        ).get("min", 0):
            issues.append("Structural: not enough single-sentence paragraphs.")
        if metrics.get("structural.formal_transitions_per_1k", 0) > structural_t.get(
            "formal_transitions_per_1k", {}
        ).get("max", 999):
            issues.append("Structural: too many formal transitions.")

        anti_ai = thresholds.get("anti_ai", {})
        if metrics.get("vocab.banned_words", 0) > anti_ai.get("banned_words", {}).get("max", 0):
            issues.append("Vocabulary: banned words present.")

        voice_t = thresholds.get("voice", {})
        if metrics.get("vocab.conjunction_starts", 0) < voice_t.get("conjunction_starts", {}).get("min", 0):
            issues.append("Voice: too few conjunction starts.")
        if metrics.get("vocab.fragments", 0) < voice_t.get("fragments", {}).get("min", 0):
            issues.append("Voice: not enough fragments.")

        surprise_t = thresholds.get("surprise", {})
        if metrics.get("surprise.overall", 1) < surprise_t.get("overall", {}).get("min", 0):
            issues.append("Surprise: overall surprise below target.")

        return issues
