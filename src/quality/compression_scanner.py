"""Compression scanner — measures information density and Kolmogorov compression quality.

Metrics:
1. Lexical density (content words / total words)
2. Zero-information transitions (filler transitions that add no conceptual weight)
3. Redundancy markers (phrases that signal repetition)
4. Specificity ratio (specific entities+numbers vs. generic descriptors)
"""

import re
from dataclasses import dataclass, field

import nltk

try:
    nltk.data.find("taggers/averaged_perceptron_tagger_eng")
except LookupError:
    nltk.download("averaged_perceptron_tagger_eng", quiet=True)

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab", quiet=True)


@dataclass
class CompressionResult:
    lexical_density: float = 0.0
    zero_info_transitions: int = 0
    redundancy_count: int = 0
    specificity_ratio: float = 0.0
    filler_phrases: int = 0
    overall_score: float = 0.0
    issues: list[str] = field(default_factory=list)

    def score(self, thresholds: dict | None = None) -> float:
        """Score 0-10 based on compression quality."""
        t = thresholds or {}
        checks = [
            self.lexical_density >= t.get("lexical_density_min", 0.50),
            self.zero_info_transitions <= t.get("zero_info_transitions_max", 3),
            self.redundancy_count <= t.get("redundancy_max", 2),
            self.specificity_ratio >= t.get("specificity_ratio_min", 0.02),
            self.filler_phrases <= t.get("filler_phrases_max", 3),
        ]
        passed = sum(checks)
        self.overall_score = round(passed / len(checks) * 10, 1)
        return self.overall_score


# Transitions that carry zero information
ZERO_INFO_TRANSITIONS = re.compile(
    r"\b(?:Also|Additionally|In addition|Furthermore|Moreover|"
    r"As mentioned (?:earlier|above|before|previously)|"
    r"It is (?:worth|important to) not(?:e|ing)|"
    r"It should be noted|As we can see|"
    r"Having said that|That being said|With that in mind|"
    r"Moving on|Let's (?:now |)(?:look at|turn to|consider|examine)|"
    r"As previously (?:mentioned|discussed|noted))\b",
    re.IGNORECASE,
)

# Phrases that signal repetition / redundancy
REDUNDANCY_MARKERS = re.compile(
    r"\b(?:In other words|To put it (?:another way|simply|differently)|"
    r"What this means is|Simply put|That is to say|"
    r"To reiterate|As I (?:said|mentioned)|"
    r"Again|Once again|To repeat)\b",
    re.IGNORECASE,
)

# Filler phrases that add no information
FILLER_PHRASES = re.compile(
    r"\b(?:It's (?:clear|obvious|evident|apparent|undeniable|no secret) that|"
    r"The (?:fact|reality|truth) (?:is|remains) that|"
    r"It goes without saying|Needless to say|"
    r"At the end of the day|When all is said and done|"
    r"There's no (?:doubt|denying|question) that|"
    r"It's (?:important|crucial|essential|vital) to (?:note|understand|remember)|"
    r"The question (?:is|remains)|"
    r"(?:Very|Quite|Rather|Extremely|Incredibly|Absolutely) (?=\w))\b",
    re.IGNORECASE,
)

# Specific entities: numbers, dates, company names, regulatory references
SPECIFICITY_MARKERS = re.compile(
    r"(?:\$[\d,.]+[BMKbmk]?|[\d,.]+%|"
    r"\bQ[1-4]\s*(?:\'|20)\d{2}\b|\bFY\s*20\d{2}\b|"
    r"\bSection\s+\d+(?:\([a-z]\))?|"
    r"\b(?:19|20)\d{2}\b|"
    r"\b[A-Z][a-z]+(?:'s)?\s+(?:S-1|10-K|10-Q|8-K|IPO|filing)\b)",
)

# POS tags that count as "content words"
CONTENT_POS_TAGS = {
    "NN", "NNS", "NNP", "NNPS",  # nouns
    "VB", "VBD", "VBG", "VBN", "VBP", "VBZ",  # verbs
    "JJ", "JJR", "JJS",  # adjectives
    "RB", "RBR", "RBS",  # adverbs (some are filler, but count for density)
}


def scan_compression(text: str) -> CompressionResult:
    """Analyze text for information density and compression quality."""
    result = CompressionResult()

    # Strip markdown headers for analysis
    clean = re.sub(r"^#{1,6}\s+.*$", "", text, flags=re.MULTILINE)
    clean = clean.strip()
    words = clean.split()
    word_count = len(words)

    if word_count < 50:
        result.issues.append("Text too short for compression analysis")
        return result

    # 1. Lexical density via POS tagging
    tokens = nltk.word_tokenize(clean)
    tagged = nltk.pos_tag(tokens)
    content_count = sum(1 for _, tag in tagged if tag in CONTENT_POS_TAGS)
    result.lexical_density = round(content_count / len(tagged), 3) if tagged else 0

    if result.lexical_density < 0.50:
        result.issues.append(
            f"Low lexical density ({result.lexical_density:.2f}, need >=0.50). "
            "Too many function words relative to content words."
        )

    # 2. Zero-information transitions
    result.zero_info_transitions = len(ZERO_INFO_TRANSITIONS.findall(text))
    if result.zero_info_transitions > 3:
        result.issues.append(
            f"Found {result.zero_info_transitions} zero-information transitions "
            "(Also, Furthermore, Moving on, etc.)"
        )

    # 3. Redundancy markers
    result.redundancy_count = len(REDUNDANCY_MARKERS.findall(text))
    if result.redundancy_count > 2:
        result.issues.append(
            f"Found {result.redundancy_count} redundancy markers "
            "(In other words, To put it simply, etc.)"
        )

    # 4. Specificity ratio (specific markers per 1k words)
    specificity_count = len(SPECIFICITY_MARKERS.findall(text))
    result.specificity_ratio = round(specificity_count / word_count * 100, 2)

    if result.specificity_ratio < 2.0:
        result.issues.append(
            f"Low specificity ({result.specificity_ratio:.1f}%, need >=2.0%). "
            "Add specific numbers, dates, entity names, regulatory references."
        )

    # 5. Filler phrases
    result.filler_phrases = len(FILLER_PHRASES.findall(text))
    if result.filler_phrases > 3:
        result.issues.append(
            f"Found {result.filler_phrases} filler phrases "
            "(It's clear that, There's no doubt, etc.)"
        )

    return result
