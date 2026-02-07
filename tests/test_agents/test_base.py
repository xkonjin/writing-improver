from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.agents.base import AgentResult, AgentUsage, BaseAgent


def test_agent_usage_total():
    usage = AgentUsage(input_tokens=1000, output_tokens=500)
    assert usage.total_tokens == 1500


def test_agent_usage_cost_opus():
    usage = AgentUsage(input_tokens=1000, output_tokens=500)
    cost = usage.estimated_cost("claude-opus-4-6")
    # 1000 * 15 / 1M + 500 * 75 / 1M = 0.015 + 0.0375 = 0.0525
    assert abs(cost - 0.0525) < 0.001


def test_agent_usage_cost_sonnet():
    usage = AgentUsage(input_tokens=1000, output_tokens=500)
    cost = usage.estimated_cost("claude-sonnet-4-5-20250929")
    # 1000 * 3 / 1M + 500 * 15 / 1M = 0.003 + 0.0075 = 0.0105
    assert abs(cost - 0.0105) < 0.001


def test_agent_usage_cost_haiku():
    usage = AgentUsage(input_tokens=1000, output_tokens=500)
    cost = usage.estimated_cost("claude-haiku-4-5-20251001")
    # 1000 * 0.8 / 1M + 500 * 4 / 1M = 0.0008 + 0.002 = 0.0028
    assert abs(cost - 0.0028) < 0.001


def test_agent_result_structure():
    result = AgentResult(content="test", model="opus", phase="research")
    assert result.content == "test"
    assert result.model == "opus"
    assert result.phase == "research"


@pytest.mark.asyncio
async def test_base_agent_call():
    with patch("src.agents.base.anthropic.AsyncAnthropic") as MockClient:
        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="Hello from Claude")]
        mock_response.usage.input_tokens = 100
        mock_response.usage.output_tokens = 50

        instance = MockClient.return_value
        instance.messages.create = AsyncMock(return_value=mock_response)

        agent = BaseAgent(model="claude-haiku-4-5-20251001")
        result = await agent.call("Be helpful", "Hello")

        assert result == "Hello from Claude"
        assert agent.usage.input_tokens == 100
        assert agent.usage.output_tokens == 50
        assert agent.usage.calls == 1


@pytest.mark.asyncio
async def test_base_agent_tracks_cumulative_usage():
    with patch("src.agents.base.anthropic.AsyncAnthropic") as MockClient:
        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="response")]
        mock_response.usage.input_tokens = 100
        mock_response.usage.output_tokens = 50

        instance = MockClient.return_value
        instance.messages.create = AsyncMock(return_value=mock_response)

        agent = BaseAgent()
        await agent.call("system", "user1")
        await agent.call("system", "user2")

        assert agent.usage.input_tokens == 200
        assert agent.usage.output_tokens == 100
        assert agent.usage.calls == 2
