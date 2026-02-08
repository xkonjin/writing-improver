from unittest.mock import AsyncMock, patch

import pytest

from src.quality.data_verifier import VerificationResult, extract_claims_regex, verify_claims


def test_extract_dollar_claims():
    text = "Circle paid Coinbase $908 million in 2024. The total market cap hit $2.1 trillion."
    claims = extract_claims_regex(text)
    assert len(claims) >= 2


def test_extract_percentage_claims():
    text = "Revenue grew 15.3% year-over-year. The market share dropped to 42%."
    claims = extract_claims_regex(text)
    assert len(claims) >= 2


def test_extract_year_claims():
    text = "In 2024, the regulatory landscape shifted. Since 2020, stablecoin volume has grown 10x."
    claims = extract_claims_regex(text)
    assert len(claims) >= 2


def test_extract_claims_from_article(article_02):
    claims = extract_claims_regex(article_02)
    assert len(claims) >= 5, f"Article 02 claims found: {len(claims)}"


def test_deduplication():
    text = "In 2024, revenue was $500 million. In 2024, revenue was $500 million."
    claims = extract_claims_regex(text)
    assert len(claims) == 1


def test_verification_result_passes():
    result = VerificationResult(claims_checked=10, claims_verified=9, claims_stale=0)
    assert result.passes_gate() is True
    assert result.verification_rate == 0.9


def test_verification_result_fails_stale():
    result = VerificationResult(claims_checked=10, claims_verified=8, claims_stale=1)
    assert result.passes_gate() is False


def test_verification_result_fails_rate():
    result = VerificationResult(claims_checked=10, claims_verified=5, claims_stale=0, claims_unverified=5)
    assert result.passes_gate() is False


def test_empty_text():
    claims = extract_claims_regex("")
    assert len(claims) == 0


@pytest.mark.asyncio
async def test_verify_claims_mock():
    mock_response = (
        '{"claims": [{"claim": "test", "verifiable": true, "has_date": true, '
        '"potentially_stale": false, "has_source": true}]}'
    )

    with patch("src.quality.data_verifier.BaseAgent") as mock_agent:
        instance = mock_agent.return_value
        instance.call = AsyncMock(return_value=mock_response)
        result = await verify_claims("Circle paid $908 million in 2024.")
        assert result.claims_checked >= 1
