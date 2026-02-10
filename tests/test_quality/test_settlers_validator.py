"""Tests for Settlers-quality validator."""

from src.quality.settlers_validator import validate_settlers_quality


GOOD_TEXT = """
I remember buying 3 BTC in 2017, and we kept our names on the same forum thread.
When adoption crosses 7%, public participation triggers backlash.
Once visibility exceeds 12%, status signaling forces rejection.
At least 40% of viewers under 45 causes a neutral response, but above 60% causes booing.
Churn above 18% forces revenue below $500M.
If resale volume falls under $2B, it forces liquidity below baseline and spreads double.
When wallet share passes 3%, support costs increase to 2x.
The more price volatility rises, the less trust forms; above 60% annualized it forces a reversal.
Instead of higher income raising holdings, $111K income pairs with only $597 held.
By 2027, stablecoin float will exceed $500B.
Within 18 months, 30% of exchanges will delist high-fee tokens.
"""

BAD_TEXT = """
This is a story about markets. Moreover, the narrative shows progress — but it's complicated.
"""


def test_good_text_passes():
    result = validate_settlers_quality(GOOD_TEXT)
    assert result.passed
    assert result.mechanism_count >= 7
    assert result.inversion_count >= 2
    assert result.prediction_count >= 2
    assert result.em_dash_count == 0
    assert result.transition_count == 0


def test_bad_text_fails():
    result = validate_settlers_quality(BAD_TEXT)
    assert not result.passed
    assert result.em_dash_count > 0
    assert result.transition_count > 0
    assert result.narrative_markers > 0
