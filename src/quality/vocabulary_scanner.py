import re
from dataclasses import dataclass, field

BANNED_WORDS = [
    "delve", "tapestry", "landscape", "paradigm", "synergy", "leverage",
    "holistic", "robust", "seamless", "cutting-edge", "game-changer",
    "groundbreaking", "revolutionary", "transformative", "unprecedented",
    "navigate", "unpack", "unlock", "harness", "foster", "empower",
    "spearhead", "underscored", "realm", "multifaceted", "intricate",
    "nuanced", "pivotal", "crucial", "vital", "essential",
    "in today's world", "it's important to note", "it's worth noting",
    "at the end of the day", "the bottom line is", "moving forward",
    "let's dive in", "without further ado",
]

BANNED_PATTERNS = [
    re.compile(r"(?:It's not (?:just )?(?:about )?[\w\s]+[;,] it's (?:about )?[\w\s]+[.])", re.IGNORECASE),
    re.compile(r"(?:This isn't (?:just )?[\w\s]+[;,] (?:it's|this is) [\w\s]+[.])", re.IGNORECASE),
]

NOT_X_ITS_Y = re.compile(
    r"(?:(?:It'?s|This isn'?t) not (?:just )?(?:about )?[\w\s,]+[.;—]\s*(?:it'?s|this is))",
    re.IGNORECASE,
)

FRAGMENT_PATTERN = re.compile(r"^[A-Z][^.!?]{3,40}[.]$", re.MULTILINE)

CONJUNCTION_START = re.compile(r"(?:^|(?<=[.!?]\s))(?:And|But|So|Or|Yet|Still)\b", re.MULTILINE)

CONTRACTION = re.compile(
    r"\b(?:\w+'(?:t|s|re|ve|ll|d|m))\b",
    re.IGNORECASE,
)

EM_DASH = re.compile(r"—|--")


@dataclass
class VocabScanResult:
    banned_word_count: int = 0
    banned_words_found: list[str] = field(default_factory=list)
    banned_pattern_count: int = 0
    not_x_its_y_count: int = 0
    fragment_count: int = 0
    conjunction_starts: int = 0
    contractions_per_200w: float = 0.0
    em_dashes_per_1k: float = 0.0
    issues: list[str] = field(default_factory=list)

    def score(self, thresholds: dict) -> float:  # type: ignore[type-arg]
        """Score 0-10 based on anti-AI and voice checks."""
        anti_ai = thresholds.get("anti_ai", {})
        voice = thresholds.get("voice", {})
        checks = [
            self.banned_word_count <= anti_ai.get("banned_words", {}).get("max", 0),
            self.not_x_its_y_count <= anti_ai.get("not_x_its_y", {}).get("max", 1),
            self.fragment_count >= voice.get("fragments", {}).get("min", 3),
            self.conjunction_starts >= voice.get("conjunction_starts", {}).get("min", 5),
            self.contractions_per_200w >= voice.get("contractions_per_200w", {}).get("min", 1),
        ]
        passed = sum(checks)
        return float(round(passed / len(checks) * 10, 1))


def scan_vocabulary(text: str) -> VocabScanResult:
    result = VocabScanResult()
    text_lower = text.lower()
    total_words = len(text.split())

    if total_words == 0:
        return result

    # Banned words
    for word in BANNED_WORDS:
        if word.lower() in text_lower:
            result.banned_word_count += 1
            result.banned_words_found.append(word)

    # Banned patterns
    for pattern in BANNED_PATTERNS:
        result.banned_pattern_count += len(pattern.findall(text))

    # Not X, it's Y
    result.not_x_its_y_count = len(NOT_X_ITS_Y.findall(text))

    # Fragments (short declarative sentences as standalone paragraphs)
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    result.fragment_count = sum(
        1 for p in paragraphs
        if len(p.split()) <= 8 and not p.startswith("#") and p.endswith((".", "?", "!"))
    )

    # Conjunction starts
    result.conjunction_starts = len(CONJUNCTION_START.findall(text))

    # Contractions per 200 words
    contraction_count = len(CONTRACTION.findall(text))
    result.contractions_per_200w = round(contraction_count / total_words * 200, 2)

    # Em dashes per 1k words
    em_dash_count = len(EM_DASH.findall(text))
    result.em_dashes_per_1k = round(em_dash_count / total_words * 1000, 2)

    # Issues
    if result.banned_word_count > 0:
        result.issues.append(f"Banned words found: {', '.join(result.banned_words_found)}")
    if result.not_x_its_y_count > 1:
        result.issues.append(f"Too many 'Not X, it's Y' patterns ({result.not_x_its_y_count}, max 1)")
    if result.conjunction_starts < 5:
        result.issues.append(f"Too few conjunction starts ({result.conjunction_starts}, need >=5)")
    if result.contractions_per_200w < 1:
        result.issues.append(f"Too few contractions ({result.contractions_per_200w}/200w, need >=1)")

    return result
