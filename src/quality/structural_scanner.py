import re
import statistics
from dataclasses import dataclass, field

import nltk

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab", quiet=True)


@dataclass
class StructuralScanResult:
    sentence_length_cv: float = 0.0
    paragraph_word_std: float = 0.0
    single_sentence_paragraphs: int = 0
    formal_transitions_per_1k: float = 0.0
    self_refs_per_1k: float = 0.0
    section_ratio: float = 0.0
    solution_pct: float = 0.0
    issues: list[str] = field(default_factory=list)

    def score(self, thresholds: dict) -> float:  # type: ignore[type-arg]
        """Score 0-10 based on how many thresholds pass."""
        checks = [
            self.sentence_length_cv >= thresholds.get("sentence_length_cv", {}).get("min", 0.35),
            self.paragraph_word_std >= thresholds.get("paragraph_word_std", {}).get("min", 35),
            self.single_sentence_paragraphs >= thresholds.get("single_sentence_paragraphs", {}).get("min", 3),
            self.formal_transitions_per_1k <= thresholds.get("formal_transitions_per_1k", {}).get("max", 2.5),
            self.self_refs_per_1k >= thresholds.get("self_refs_per_1k", {}).get("min", 4.0),
            self.self_refs_per_1k <= thresholds.get("self_refs_per_1k", {}).get("max", 6.0),
            self.section_ratio >= thresholds.get("section_ratio", {}).get("min", 2.0),
            self.section_ratio <= thresholds.get("section_ratio", {}).get("max", 5.0),
            self.solution_pct <= thresholds.get("solution_pct", {}).get("max", 7),
        ]
        passed = sum(checks)
        return float(round(passed / len(checks) * 10, 1))


FORMAL_TRANSITIONS = re.compile(
    r"\b(?:Furthermore|Moreover|Additionally|Consequently|Subsequently|In addition|As a result|In conclusion|"
    r"To summarize|It is worth noting|It is important to note|Notably|Significantly|"
    r"This demonstrates|This illustrates|This suggests)\b",
    re.IGNORECASE,
)

SELF_REFS = re.compile(r"\bI\b|\bI'm\b|\bI've\b|\bI'd\b|\bI'll\b|\bmy\b|\bme\b", re.MULTILINE)

SOLUTION_HEADERS = re.compile(
    r"^#{1,3}\s+(?:Solution|What to do|How to|Conclusion|Takeaway|Action|Next step|Summary)",
    re.IGNORECASE | re.MULTILINE,
)


def _get_sentences(text: str) -> list[str]:
    return [s.strip() for s in nltk.sent_tokenize(text) if s.strip()]


def _get_paragraphs(text: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip() and not p.strip().startswith("#")]


def _get_sections(text: str) -> list[str]:
    parts = re.split(r"^#{1,3}\s+", text, flags=re.MULTILINE)
    return [p.strip() for p in parts if p.strip() and len(p.strip().split()) > 10]


def _word_count(text: str) -> int:
    return len(text.split())


def scan_structural(text: str) -> StructuralScanResult:
    result = StructuralScanResult()
    sentences = _get_sentences(text)
    paragraphs = _get_paragraphs(text)
    sections = _get_sections(text)
    total_words = _word_count(text)

    if not sentences or total_words == 0:
        return result

    # Sentence length CV
    sent_lengths = [len(s.split()) for s in sentences]
    if len(sent_lengths) > 1:
        mean = statistics.mean(sent_lengths)
        std = statistics.stdev(sent_lengths)
        result.sentence_length_cv = round(std / mean, 3) if mean > 0 else 0
    else:
        result.sentence_length_cv = 0

    # Paragraph word std
    para_lengths = [len(p.split()) for p in paragraphs]
    if len(para_lengths) > 1:
        result.paragraph_word_std = round(statistics.stdev(para_lengths), 1)
    else:
        result.paragraph_word_std = 0

    # Single-sentence paragraphs
    result.single_sentence_paragraphs = sum(1 for p in paragraphs if len(_get_sentences(p)) == 1)

    # Formal transitions per 1k words
    transition_count = len(FORMAL_TRANSITIONS.findall(text))
    result.formal_transitions_per_1k = round(transition_count / total_words * 1000, 2)

    # Self-references per 1k words
    self_ref_count = len(SELF_REFS.findall(text))
    result.self_refs_per_1k = round(self_ref_count / total_words * 1000, 2)

    # Section ratio (max/min word count)
    if len(sections) >= 2:
        section_lengths = [_word_count(s) for s in sections]
        result.section_ratio = round(max(section_lengths) / min(section_lengths), 2) if min(section_lengths) > 0 else 0
    else:
        result.section_ratio = 1.0

    # Solution percentage
    solution_match = list(SOLUTION_HEADERS.finditer(text))
    if solution_match:
        last_solution = solution_match[-1]
        solution_text = text[last_solution.start():]
        # Find next header or end
        next_header = re.search(r"^#{1,3}\s+", solution_text[1:], re.MULTILINE)
        if next_header:
            solution_text = solution_text[:next_header.start() + 1]
        result.solution_pct = round(_word_count(solution_text) / total_words * 100, 1)
    else:
        result.solution_pct = 0.0

    # Build issues list
    if result.sentence_length_cv < 0.35:
        result.issues.append(f"Low sentence variation (CV={result.sentence_length_cv}, need >0.35)")
    if result.paragraph_word_std < 35:
        result.issues.append(f"Uniform paragraph lengths (std={result.paragraph_word_std}, need >35)")
    if result.single_sentence_paragraphs < 3:
        result.issues.append(f"Too few single-sentence paragraphs ({result.single_sentence_paragraphs}, need >=3)")
    if result.formal_transitions_per_1k > 2.5:
        result.issues.append(f"Too many formal transitions ({result.formal_transitions_per_1k}/1k, need <2.5)")
    if result.self_refs_per_1k < 4.0:
        result.issues.append(f"Too few self-references ({result.self_refs_per_1k}/1k, need 4.0-6.0)")
    if result.self_refs_per_1k > 6.0:
        result.issues.append(f"Too many self-references ({result.self_refs_per_1k}/1k, need 4.0-6.0)")

    return result
