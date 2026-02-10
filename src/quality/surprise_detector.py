"""Surprise detector — automated non-obviousness scoring for insights.

Implements four tests:
1. Levine Test: Is there a specific gap between theory and reality?
2. First Principles Test: Is it surprising without domain jargon?
3. Bidirectional Test: Is the inverted claim NOT equally surprising?
4. Falsification Strength: Can the claim be disproved in <=2 logic steps?
"""

import re
from dataclasses import dataclass, field


@dataclass
class SurpriseResult:
    levine_score: float = 0.0  # 0-1: specificity of theory-reality gap
    first_principles_score: float = 0.0  # 0-1: surprising without jargon?
    bidirectional_score: float = 0.0  # 0-1: asymmetry of surprise
    falsification_score: float = 0.0  # 0-1: how concisely can it be disproved?
    overall: float = 0.0
    passed: bool = False
    issues: list[str] = field(default_factory=list)

    def compute_overall(self) -> float:
        scores = [
            self.levine_score,
            self.first_principles_score,
            self.bidirectional_score,
            self.falsification_score,
        ]
        self.overall = sum(scores) / len(scores) if scores else 0.0
        self.passed = self.overall >= 0.6
        return self.overall


# Patterns indicating template/framework application (low surprise)
FRAMEWORK_TEMPLATES = re.compile(
    r"\b(?:aggregation theory|network effects?|winner.?take.?all|moat|flywheel|"
    r"disruption|commoditiz|platform play|value chain|scale advantage|"
    r"first.?mover|switching cost|lock.?in)\b",
    re.IGNORECASE,
)

# Patterns indicating specific, surprising claims (high surprise)
SPECIFICITY_MARKERS = re.compile(
    r"(?:\$[\d,.]+[BMK]?|[\d,.]+%|\bQ[1-4]\s+20\d{2}\b|\bSection\s+\d+|"
    r"\b(?:19|20)\d{2}\b|\b[A-Z][a-z]+(?:'s)?\s+(?:S-1|10-K|10-Q|8-K|filing|Act)\b)",
    re.IGNORECASE,
)

# Patterns indicating the writer located a gap (Levine test)
GAP_INDICATORS = re.compile(
    r"\b(?:should(?:n't| not| have)|supposed to|expected|but (?:instead|actually|in practice)|"
    r"turns out|the surprise|what actually happened|in theory .{0,40} in practice|"
    r"the gap between|contrary to)\b",
    re.IGNORECASE,
)

# Patterns suggesting generic/obvious analysis
OBVIOUS_PATTERNS = re.compile(
    r"\b(?:it's clear that|obviously|as we all know|it goes without saying|"
    r"the real question is|the key takeaway|the bottom line|"
    r"time will tell|remains to be seen|only time)\b",
    re.IGNORECASE,
)


def detect_surprise(text: str) -> SurpriseResult:
    """Analyze text for genuine surprise/non-obviousness."""
    result = SurpriseResult()
    word_count = len(text.split())

    if word_count < 50:
        result.issues.append("Text too short for surprise detection")
        return result

    # Test 1: Levine Test — is there a specific theory-reality gap?
    gap_count = len(GAP_INDICATORS.findall(text))
    specificity_count = len(SPECIFICITY_MARKERS.findall(text))
    specificity_per_1k = specificity_count / word_count * 1000

    if gap_count >= 2 and specificity_per_1k >= 3.0:
        result.levine_score = 1.0
    elif gap_count >= 1 and specificity_per_1k >= 2.0:
        result.levine_score = 0.7
    elif gap_count >= 1 or specificity_per_1k >= 3.0:
        result.levine_score = 0.4
    else:
        result.levine_score = 0.2
        result.issues.append(
            f"Weak Levine score: {gap_count} gap indicators, "
            f"{specificity_per_1k:.1f} specificity markers/1k (need >=2.0)"
        )

    # Test 2: First Principles — surprising without jargon?
    framework_count = len(FRAMEWORK_TEMPLATES.findall(text))
    framework_per_1k = framework_count / word_count * 1000

    if framework_per_1k <= 1.0 and specificity_per_1k >= 3.0:
        result.first_principles_score = 1.0
    elif framework_per_1k <= 2.0:
        result.first_principles_score = 0.7
    elif framework_per_1k <= 3.0:
        result.first_principles_score = 0.4
    else:
        result.first_principles_score = 0.2
        result.issues.append(
            f"High framework dependency: {framework_per_1k:.1f} templates/1k "
            f"(insight may be framework application, not genuine surprise)"
        )

    # Test 3: Bidirectional — inverted claim should NOT be equally surprising
    # Heuristic: if text contains direction changes and self-corrections,
    # the author explored both directions (asymmetric surprise)
    direction_markers = len(re.findall(
        r"\b(?:but actually|I was wrong|turns out|most of it fell apart|"
        r"the real|what I missed|I should have)\b",
        text, re.IGNORECASE,
    ))
    if direction_markers >= 2:
        result.bidirectional_score = 1.0
    elif direction_markers >= 1:
        result.bidirectional_score = 0.6
    else:
        result.bidirectional_score = 0.3
        result.issues.append(
            "No direction changes detected — insight may be on obvious axis"
        )

    # Test 4: Falsification Strength — concise disproof = strong claim
    # Heuristic: claims with specific entities + timeframes are concisely falsifiable
    entity_predictions = len(re.findall(
        r"\b(?:will|by Q[1-4]|by 20\d{2}|within \d+|predic)\b",
        text, re.IGNORECASE,
    ))
    if entity_predictions >= 3 and specificity_per_1k >= 3.0:
        result.falsification_score = 1.0
    elif entity_predictions >= 2:
        result.falsification_score = 0.7
    elif entity_predictions >= 1:
        result.falsification_score = 0.4
    else:
        result.falsification_score = 0.2
        result.issues.append(
            "Low falsifiability — claims lack specific entities or timeframes"
        )

    # Check for obvious/generic patterns (penalty)
    obvious_count = len(OBVIOUS_PATTERNS.findall(text))
    if obvious_count >= 3:
        penalty = min(0.3, obvious_count * 0.1)
        result.levine_score = max(0, result.levine_score - penalty)
        result.first_principles_score = max(0, result.first_principles_score - penalty)
        result.issues.append(
            f"Found {obvious_count} obvious/generic phrases (penalty applied)"
        )

    result.compute_overall()
    return result
