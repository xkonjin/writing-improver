from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.agents.debate import DebateAgent, DebateResult


def _mock_agent():
    mock = MagicMock()
    mock.call = AsyncMock(return_value="Hypothesis response.")
    mock.usage = MagicMock(input_tokens=100, output_tokens=200, calls=1)
    return mock


@pytest.mark.asyncio
async def test_debate_generates_hypotheses():
    with patch("src.agents.debate.BaseAgent", return_value=_mock_agent()):
        agent = DebateAgent()
        result = await agent.run("research", "anomalies")
        assert isinstance(result, DebateResult)
        assert len(result.hypotheses) == 3


@pytest.mark.asyncio
async def test_debate_has_challenge():
    with patch("src.agents.debate.BaseAgent", return_value=_mock_agent()):
        agent = DebateAgent()
        result = await agent.run("research", "anomalies")
        assert len(result.challenge) > 0


@pytest.mark.asyncio
async def test_debate_has_winner():
    with patch("src.agents.debate.BaseAgent", return_value=_mock_agent()):
        agent = DebateAgent()
        result = await agent.run("research", "anomalies")
        assert len(result.winner) > 0


def test_debate_result_defaults():
    result = DebateResult()
    assert result.hypotheses == []
    assert result.challenge == ""
