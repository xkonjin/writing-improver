from unittest.mock import AsyncMock, patch

import pytest

from src.quality.ai_tell_detector import AITellResult, detect_ai_tells_llm, detect_ai_tells_regex


def test_signposting_detection():
    text = "In this article, we'll explore the dynamics. Let's dive into the data. As we'll see, the trend is clear."
    result = detect_ai_tells_regex(text)
    assert result.signposting_count >= 2, f"Signposting count={result.signposting_count}"


def test_no_signposting_in_human_text():
    text = "The number that caught my eye was $908 million. That's what Circle paid Coinbase in 2024. I spent the week trying to figure out why."
    result = detect_ai_tells_regex(text)
    assert result.signposting_count == 0


def test_summarizing_conclusion():
    text = "Some content here. " * 50 + "In conclusion, we've seen that the data clearly shows a trend toward consolidation."
    result = detect_ai_tells_regex(text)
    assert result.summarizing_conclusion is True


def test_no_summarizing_conclusion():
    text = "Some content here. " * 50 + "I still don't know if this holds. But the data is moving that direction."
    result = detect_ai_tells_regex(text)
    assert result.summarizing_conclusion is False


def test_performative_introspection():
    text = "I've been thinking about this for weeks. I find myself wondering if the market has it wrong."
    result = detect_ai_tells_regex(text)
    assert result.performative_introspection_count >= 1


def test_parallelism_detection():
    text = """**Layer 1: Settlement** — This handles the base chain.

**Layer 2: Issuance** — This manages the minting process.

**Layer 3: Distribution** — This covers how tokens reach users."""
    result = detect_ai_tells_regex(text)
    assert result.parallelism_detected is True


def test_no_parallelism():
    text = """The first thing I noticed was the settlement layer. It's where everything starts.

I spent the week looking at distribution economics. The numbers are stark.

Then there's the regulatory angle — and this is where it gets interesting."""
    result = detect_ai_tells_regex(text)
    assert result.parallelism_detected is False


def test_score_clean_text():
    result = AITellResult(
        signposting_count=0,
        parallelism_detected=False,
        summarizing_conclusion=False,
        performative_introspection_count=0,
    )
    assert result.score() == 10.0


def test_score_ai_text():
    result = AITellResult(
        signposting_count=3,
        parallelism_detected=True,
        summarizing_conclusion=True,
        performative_introspection_count=2,
    )
    assert result.score() < 3.0


def test_article_02_low_ai_tells(article_02):
    result = detect_ai_tells_regex(article_02)
    assert result.score() >= 6.0, f"Article 02 AI tell score={result.score()}"


def test_article_04_has_tells(article_04):
    result = detect_ai_tells_regex(article_04)
    # Article 04 should have more AI tells than 02
    assert isinstance(result.issues, list)


@pytest.mark.asyncio
async def test_llm_detection_mock():
    mock_response = '{"signposting": {"count": 2, "examples": ["In this section"]}, "parallelism": {"detected": false, "examples": []}, "summarizing_conclusion": false, "performative_introspection": {"count": 0, "examples": []}, "data_density_issues": []}'

    with patch("src.quality.ai_tell_detector.BaseAgent") as MockAgent:
        instance = MockAgent.return_value
        instance.call = AsyncMock(return_value=mock_response)
        result = await detect_ai_tells_llm("Test text here.")
        assert result.signposting_count >= 2
