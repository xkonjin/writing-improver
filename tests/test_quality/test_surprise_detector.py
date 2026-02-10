"""Tests for the surprise detector quality gate."""

from src.quality.surprise_detector import detect_surprise

# Sample text with high surprise (specific, non-obvious, direction changes)
HIGH_SURPRISE_TEXT = """
Circle paid Coinbase $908M in 2024 — that's 54% of revenue going to a single distribution
partner. I was wrong about this being a payments company. What actually happened is more
interesting: Circle built a holding company disguised as a stablecoin issuer.

But actually, the real surprise isn't Circle. Section 4(a)(2) of the GENIUS Act creates
a $10B threshold that turns out to favor banks, not crypto-native companies. JPMorgan's
Kinexys will issue retail stablecoins by Q2 2027 — not because they want to, but because
the regulatory structure makes it cheaper than not doing it.

Most of it fell apart when I looked at x402 data. Total AI-payment volume: $1.2M.
The thesis should have died there. Instead it pointed somewhere else entirely.
Tether's $4B allocation to AI infrastructure isn't a pivot — it's Berkshire Hathaway
with a stablecoin balance sheet.
"""

# Sample text with low surprise (generic, framework-heavy, no direction changes)
LOW_SURPRISE_TEXT = """
Network effects create winner-take-all dynamics in the stablecoin market. The moat
is deep and the flywheel is spinning. As platforms aggregate more users, the
switching costs increase and lock-in becomes permanent.

It's clear that disruption is coming to traditional finance. The key takeaway is
that commoditization of payments will create new platform plays. The bottom line:
aggregation theory suggests that the value chain will be restructured, and the
companies with the strongest network effects will dominate.

Time will tell how this plays out, but it's obvious that the future belongs to
those who can scale their platform advantage. The real question is whether
traditional players can adapt quickly enough.
"""


def test_high_surprise_passes():
    result = detect_surprise(HIGH_SURPRISE_TEXT)
    assert result.overall >= 0.6, f"Expected >=0.6, got {result.overall}"
    assert result.passed


def test_low_surprise_fails():
    result = detect_surprise(LOW_SURPRISE_TEXT)
    assert result.overall < 0.6, f"Expected <0.6, got {result.overall}"
    assert not result.passed


def test_levine_score_detects_gap():
    result = detect_surprise(HIGH_SURPRISE_TEXT)
    assert result.levine_score >= 0.7, f"Expected >=0.7, got {result.levine_score}"


def test_framework_dependency_detected():
    result = detect_surprise(LOW_SURPRISE_TEXT)
    assert result.first_principles_score < 0.5, (
        f"Expected <0.5 for framework-heavy text, got {result.first_principles_score}"
    )


def test_direction_changes_detected():
    result = detect_surprise(HIGH_SURPRISE_TEXT)
    assert result.bidirectional_score >= 0.6


def test_obvious_patterns_penalized():
    result = detect_surprise(LOW_SURPRISE_TEXT)
    assert len(result.issues) >= 1
    has_obvious = any("obvious" in i.lower() or "framework" in i.lower() for i in result.issues)
    assert has_obvious, f"Expected obvious/framework issue, got: {result.issues}"


def test_empty_text():
    result = detect_surprise("")
    assert result.overall == 0.0


def test_short_text():
    result = detect_surprise("This is too short.")
    assert len(result.issues) >= 1
