from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.agents.publisher import PublisherAgent, PublisherResult
from src.prompts.platform_format import (
    LINKEDIN_SYSTEM,
    NEWSLETTER_SYSTEM,
    X_THREAD_SYSTEM,
)


def test_newsletter_prompt():
    assert "title" in NEWSLETTER_SYSTEM.lower()
    assert "Matt Levine" in NEWSLETTER_SYSTEM
    assert "TITLE_A" in NEWSLETTER_SYSTEM


def test_linkedin_prompt():
    assert "1300 characters" in LINKEDIN_SYSTEM
    assert "No hashtags" in LINKEDIN_SYSTEM
    assert "No emoji" in LINKEDIN_SYSTEM


def test_x_thread_prompt():
    assert "280 characters" in X_THREAD_SYSTEM
    assert "5-8 tweets" in X_THREAD_SYSTEM
    assert "[LINK]" in X_THREAD_SYSTEM


def _mock_agent():
    mock = MagicMock()
    mock.call = AsyncMock(return_value="Formatted output.")
    mock.usage = MagicMock(input_tokens=200, output_tokens=500, calls=1)
    return mock


@pytest.mark.asyncio
async def test_format_newsletter():
    with patch("src.agents.publisher.BaseAgent", return_value=_mock_agent()):
        agent = PublisherAgent()
        result = await agent.format_newsletter("Article text here")
        assert len(result) > 0


@pytest.mark.asyncio
async def test_format_linkedin():
    with patch("src.agents.publisher.BaseAgent", return_value=_mock_agent()):
        agent = PublisherAgent()
        result = await agent.format_linkedin("Article text here")
        assert len(result) > 0


@pytest.mark.asyncio
async def test_format_x_thread():
    with patch("src.agents.publisher.BaseAgent", return_value=_mock_agent()):
        agent = PublisherAgent()
        result = await agent.format_x_thread("Article text here")
        assert len(result) > 0


@pytest.mark.asyncio
async def test_format_all():
    with patch("src.agents.publisher.BaseAgent", return_value=_mock_agent()):
        agent = PublisherAgent()
        result = await agent.format_all("Article text here")
        assert isinstance(result, PublisherResult)
        assert len(result.newsletter) > 0
        assert len(result.linkedin) > 0
        assert len(result.x_thread) > 0


def test_publisher_result_defaults():
    result = PublisherResult()
    assert result.newsletter == ""
    assert result.linkedin == ""
    assert result.x_thread == ""
