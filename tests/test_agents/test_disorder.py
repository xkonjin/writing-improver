from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.agents.disorder import DisorderAgent, DisorderResult
from src.prompts.disorder import DISORDER_SYSTEM


def test_disorder_prompt_content():
    assert "BREAK the organization" in DISORDER_SYSTEM
    assert "DISCOVERY SEQUENCE" in DISORDER_SYSTEM
    assert "DIRECTION CHANGES" in DISORDER_SYSTEM
    assert "ASYMMETRIC ATTENTION" in DISORDER_SYSTEM
    assert "MESSY OUTLINE" in DISORDER_SYSTEM
    assert "OPEN LOOPS" in DISORDER_SYSTEM


def test_disorder_prompt_anti_patterns():
    assert "NOT:" in DISORDER_SYSTEM
    assert "Introduction: topic" in DISORDER_SYSTEM
    assert "most surprising data point" in DISORDER_SYSTEM


@pytest.mark.asyncio
async def test_disorder_agent():
    mock = MagicMock()
    mock.call = AsyncMock(return_value="- Start with the $908M number\n- Pivot when...")
    mock.usage = MagicMock(input_tokens=500, output_tokens=1000, calls=1)

    with patch("src.agents.disorder.BaseAgent", return_value=mock):
        agent = DisorderAgent()
        result = await agent.disorder("research text", "insight text")
        assert isinstance(result, DisorderResult)
        assert len(result.outline) > 0
        mock.call.assert_called_once()


def test_disorder_result_defaults():
    result = DisorderResult()
    assert result.outline == ""
    assert result.direction_changes == []
