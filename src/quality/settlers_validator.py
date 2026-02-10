"""Settlers-quality validator.

Targets the mechanisms + inversion + anti-AI constraints extracted from the
"The Settlers" analysis. This is a strict gate for OpenRouter swarm output.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import re

from src.quality.compression_scanner import ZERO_INFO_TRANSITIONS
from src.quality.structural_scanner import FORMAL_TRANSITIONS
from src.quality.vocabulary_scanner import EM_DASH


NUMBER_PATTERN = re.compile(
    r"(?:\$[\d,.]+[BMKbmk]?|[\d,.]+%|\b\d{1,3}(?:,\d{3})*(?:\.\d+)?\b)",
    re.IGNORECASE,
)

THRESHOLD_PATTERN = re.compile(
    r"\b(?:>=|<=|>|<|at least|at most|above|below|over|under|"
    r"cross(?:es|ed)|exceed(?:s|ed)|falls below|"
    r"threshold|tipping point|breakpoint|critical mass|"
    r"once .* hits|when .* hits|after .* hits)\b",
    re.IGNORECASE,
)

MECHANISM_VERB = re.compile(
    r"\b(?:caus(?:es|ed)|driv(?:es|en)|force(?:s|d)|trigger(?:s|ed)|"
    r"creates?|makes?|turns?|converts?|locks?|shifts?|push(?:es|ed)|"
    r"pull(?:s|ed)|reduces?|increases?|decreases?|accelerates?|slows?)\b",
    re.IGNORECASE,
)

CONDITIONAL_MARKER = re.compile(r"\b(?:if|when|once|until|after|before)\b", re.IGNORECASE)

INVERSION_PATTERN = re.compile(
    r"\b(?:inversion|inverse|opposite|flip(?:s|ped)?|revers(?:es|ed)|"
    r"backfires?|counterintuitive|instead of|rather than|the more .* the less|"
    r"the less .* the more|rises? while .* falls?)\b",
    re.IGNORECASE,
)

PREDICTION_VERB = re.compile(
    r"\b(?:will|won't|expect|predict|forecast|likely)\b",
    re.IGNORECASE,
)

TIMEFRAME_PATTERN = re.compile(
    r"\b(?:by|within|over the next|in the next|before|after)\s+\d+"
    r"(?:\s+(?:days|weeks|months|quarters|years))?\b|"
    r"\bQ[1-4]\s*20\d{2}\b|\b20\d{2}\b",
    re.IGNORECASE,
)

CONFESSION_PATTERN = re.compile(
    r"\bI (?:remember|got|kept|was|lost|made|held|sold|bought|"
    r"saw|spent|wrote|joined|worked|lived|used to|did|clicked|"
    r"paid|bagged|blew)\b",
    re.IGNORECASE,
)

ADMISSION_PATTERN = re.compile(
    r"\bI (?:was wrong|didn't|couldn't|can't|shouldn't|regret|admit)\b",
    re.IGNORECASE,
)

INCLUSION_PATTERN = re.compile(r"\b(?:we|us|our|ours)\b", re.IGNORECASE)

NARRATIVE_MARKERS = re.compile(
    r"\b(?:story|narrative|plot|chapter|journey|tale|arc|hero|villain)\b",
    re.IGNORECASE,
)

EXTRA_TRANSITIONS = re.compile(
    r"\b(?:however|therefore|thus|meanwhile|overall|in summary|in conclusion)\b",
    re.IGNORECASE,
)


def _sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


@dataclass
class SettlersThresholds:
    min_mechanisms: int = 7
    min_inversions: int = 2
    min_predictions: int = 2
    min_inclusion_pronouns: int = 2
    require_confession: bool = True


@dataclass
class SettlersQualityResult:
    mechanism_count: int = 0
    mechanism_sentences: list[str] = field(default_factory=list)
    inversion_count: int = 0
    prediction_count: int = 0
    confession_found: bool = False
    admission_found: bool = False
    inclusion_pronouns: int = 0
    transition_count: int = 0
    em_dash_count: int = 0
    narrative_markers: int = 0
    failures: list[str] = field(default_factory=list)
    passed: bool = False

    def finalize(self, thresholds: SettlersThresholds) -> None:
        if self.mechanism_count < thresholds.min_mechanisms:
            self.failures.append(
                f"mechanisms_with_thresholds={self.mechanism_count} < {thresholds.min_mechanisms}"
            )
        if self.inversion_count < thresholds.min_inversions:
            self.failures.append(
                f"inversions={self.inversion_count} < {thresholds.min_inversions}"
            )
        if self.prediction_count < thresholds.min_predictions:
            self.failures.append(
                f"predictions={self.prediction_count} < {thresholds.min_predictions}"
            )
        if thresholds.require_confession and not (self.confession_found or self.admission_found):
            self.failures.append("personal_layer_missing_confession_or_admission")
        if self.inclusion_pronouns < thresholds.min_inclusion_pronouns:
            self.failures.append(
                f"inclusion_pronouns={self.inclusion_pronouns} < {thresholds.min_inclusion_pronouns}"
            )
        if self.em_dash_count > 0:
            self.failures.append(f"em_dashes_found={self.em_dash_count}")
        if self.transition_count > 0:
            self.failures.append(f"transitions_found={self.transition_count}")
        if self.narrative_markers > 0:
            self.failures.append(f"narrative_markers_found={self.narrative_markers}")
        self.passed = len(self.failures) == 0


def validate_settlers_quality(
    text: str, thresholds: SettlersThresholds | None = None
) -> SettlersQualityResult:
    t = thresholds or SettlersThresholds()
    result = SettlersQualityResult()

    sentences = _sentences(text)
    for sentence in sentences:
        has_number = NUMBER_PATTERN.search(sentence) is not None
        has_threshold = THRESHOLD_PATTERN.search(sentence) is not None
        has_mechanism = MECHANISM_VERB.search(sentence) is not None
        has_conditional = CONDITIONAL_MARKER.search(sentence) is not None
        if has_number and has_threshold and (has_mechanism or has_conditional):
            result.mechanism_count += 1
            if len(result.mechanism_sentences) < 12:
                result.mechanism_sentences.append(sentence)

        if INVERSION_PATTERN.search(sentence):
            result.inversion_count += 1

        if (
            PREDICTION_VERB.search(sentence)
            and TIMEFRAME_PATTERN.search(sentence)
            and NUMBER_PATTERN.search(sentence)
        ):
            result.prediction_count += 1

    result.confession_found = CONFESSION_PATTERN.search(text) is not None
    result.admission_found = ADMISSION_PATTERN.search(text) is not None
    result.inclusion_pronouns = len(INCLUSION_PATTERN.findall(text))

    result.transition_count = (
        len(ZERO_INFO_TRANSITIONS.findall(text))
        + len(FORMAL_TRANSITIONS.findall(text))
        + len(EXTRA_TRANSITIONS.findall(text))
    )
    result.em_dash_count = len(EM_DASH.findall(text))
    result.narrative_markers = len(NARRATIVE_MARKERS.findall(text))

    result.finalize(t)
    return result
