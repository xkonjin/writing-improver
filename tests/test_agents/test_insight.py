from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.agents.insight import (
    AnomalyAgent,
    CrossReferenceAgent,
    InsightPipeline,
    InsightResult,
    MechanismAgent,
    PredictionAgent,
    ValidationAgent,
)


def _mock_agent():
    mock = MagicMock()
    mock.call = AsyncMock(return_value="Mock response with data.")
    mock.usage = MagicMock(input_tokens=100, output_tokens=200, calls=1)
    return mock


@pytest.mark.asyncio
async def test_anomaly_agent():
    with patch("src.agents.insight.BaseAgent", return_value=_mock_agent()):
        agent = AnomalyAgent()
        result = await agent.detect("Research text here")
        assert result == "Mock response with data."


@pytest.mark.asyncio
async def test_cross_reference_agent():
    with patch("src.agents.insight.BaseAgent", return_value=_mock_agent()):
        agent = CrossReferenceAgent()
        result = await agent.find_connections("research", "anomalies")
        assert len(result) > 0


@pytest.mark.asyncio
async def test_mechanism_agent():
    with patch("src.agents.insight.BaseAgent", return_value=_mock_agent()):
        agent = MechanismAgent()
        result = await agent.articulate("cross_refs", "anomalies")
        assert len(result) > 0


@pytest.mark.asyncio
async def test_prediction_agent():
    with patch("src.agents.insight.BaseAgent", return_value=_mock_agent()):
        agent = PredictionAgent()
        result = await agent.predict("mechanism text")
        assert len(result) > 0


@pytest.mark.asyncio
async def test_validation_agent():
    with patch("src.agents.insight.BaseAgent", return_value=_mock_agent()):
        agent = ValidationAgent()
        result = await agent.validate("insight text")
        assert len(result) > 0


@pytest.mark.asyncio
async def test_insight_pipeline():
    with patch("src.agents.insight.BaseAgent", return_value=_mock_agent()):
        pipeline = InsightPipeline()
        result = await pipeline.run("Full research text here")
        assert isinstance(result, InsightResult)
        assert len(result.anomalies) > 0
        assert len(result.mechanism) > 0
        assert len(result.predictions) > 0
        assert result.usage.calls > 0


def test_insight_result_defaults():
    result = InsightResult()
    assert result.anomalies == ""
    assert result.mechanism == ""
    assert result.usage.calls == 0
