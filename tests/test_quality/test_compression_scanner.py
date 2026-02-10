"""Tests for the compression scanner quality gate."""

from src.quality.compression_scanner import scan_compression

# Dense, high-quality text (specific, minimal filler)
DENSE_TEXT = """
Circle's S-1 filing reveals $908M paid to Coinbase in 2024 — 54% of total revenue
directed to a single distribution partner. Tether meanwhile allocated $4B to AI
infrastructure across three subsidiaries. The GENIUS Act Section 4(a)(2) creates
a $10B asset threshold for stablecoin issuers.

JPMorgan's Kinexys processed $1.5T in notional volume by Q3 2025. BNY Mellon's
custody infrastructure handles 38% of global cross-border settlements. State Street
launched its digital asset division with a $200M allocation.

Power consumption per GPU rack doubled: NVIDIA B200 draws 1,200W per chip.
A single GB200 rack requires 140kW — at industrial rates of $0.04/kWh,
that's $49K annually per rack. The chip costs $30-40K. After 2 years,
power exceeds hardware as the dominant cost.
"""

# Bloated, low-density text (filler-heavy, generic)
BLOATED_TEXT = """
It's important to note that the stablecoin market has experienced significant growth.
Additionally, there are several key factors that we should consider when examining
this trend. Furthermore, the regulatory landscape continues to evolve in meaningful ways.

In other words, the future of digital payments is changing rapidly. It's clear that
traditional financial institutions are beginning to adapt. There's no doubt that
technology will continue to drive innovation in this space.

Moreover, as previously mentioned, the key takeaway is that companies need to position
themselves strategically. It goes without saying that the winners will be those who
can navigate the increasingly complex regulatory environment. Needless to say,
the stakes have never been higher.
"""


def test_dense_text_high_score():
    result = scan_compression(DENSE_TEXT)
    assert result.lexical_density >= 0.50, f"Expected >=0.50, got {result.lexical_density}"
    assert result.zero_info_transitions <= 3
    assert result.filler_phrases <= 3


def test_bloated_text_low_score():
    result = scan_compression(BLOATED_TEXT)
    assert result.zero_info_transitions > 3, (
        f"Expected >3 zero-info transitions, got {result.zero_info_transitions}"
    )
    assert result.filler_phrases > 3, (
        f"Expected >3 filler phrases, got {result.filler_phrases}"
    )


def test_specificity_ratio():
    result = scan_compression(DENSE_TEXT)
    assert result.specificity_ratio >= 2.0, (
        f"Expected >=2.0% specificity, got {result.specificity_ratio}"
    )


def test_bloated_specificity_low():
    result = scan_compression(BLOATED_TEXT)
    assert result.specificity_ratio < 2.0, (
        f"Expected <2.0% specificity for generic text, got {result.specificity_ratio}"
    )


def test_redundancy_detection():
    result = scan_compression(BLOATED_TEXT)
    assert result.redundancy_count >= 1, "Expected redundancy markers in bloated text"


def test_score_method():
    result = scan_compression(DENSE_TEXT)
    score = result.score()
    assert score >= 6.0, f"Expected >=6.0 for dense text, got {score}"


def test_bloated_score_low():
    result = scan_compression(BLOATED_TEXT)
    score = result.score()
    assert score <= 6.0, f"Expected <=6.0 for bloated text, got {score}"


def test_empty_text():
    result = scan_compression("")
    assert len(result.issues) >= 1


def test_issues_reported():
    result = scan_compression(BLOATED_TEXT)
    assert len(result.issues) >= 2, f"Expected >=2 issues, got {len(result.issues)}"
