import statistics

import nltk

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab", quiet=True)


def _get_sentence_lengths(text: str) -> list[int]:
    sentences = [s.strip() for s in nltk.sent_tokenize(text) if s.strip()]
    return [len(s.split()) for s in sentences]


def compute_burstiness(text: str, window_size: int = 5) -> float:
    """Compute burstiness score from sentence length variation.

    High burstiness (>0.6) = human-like clustering of short/long sentences.
    Low burstiness (<0.4) = AI-like uniform sentence lengths.

    Uses coefficient of variation of sentence lengths, combined with
    adjacent-difference analysis to capture clustering patterns.
    """
    lengths = _get_sentence_lengths(text)

    if len(lengths) < 3:
        return 0.0

    mean = statistics.mean(lengths)
    if mean == 0:
        return 0.0

    # Base: coefficient of variation of sentence lengths
    cv = statistics.stdev(lengths) / mean

    # Adjacent difference analysis: how much do consecutive sentences vary?
    diffs = [abs(lengths[i] - lengths[i - 1]) for i in range(1, len(lengths))]
    if diffs:
        avg_diff = statistics.mean(diffs)
        diff_ratio = avg_diff / mean if mean > 0 else 0
    else:
        diff_ratio = 0

    # Combine: CV captures overall variation, diff_ratio captures local clustering
    # Weight CV more heavily since it's a better overall indicator
    raw = 0.6 * cv + 0.4 * diff_ratio

    # Normalize to 0-1 range
    score = min(raw / 1.5, 1.0)
    return round(score, 3)
