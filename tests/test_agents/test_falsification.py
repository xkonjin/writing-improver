"""Tests for the falsification, inversion, and bisociation agents."""

from unittest.mock import AsyncMock, patch

import pytest

from src.agents.falsification import (
    BisociationAgent,
    FalsificationAgent,
    InversionAgent,
    SocraticEngine,
)


@pytest.fixture
def mock_call():
    """Mock the BaseAgent.call method."""
    with patch("src.agents.base.BaseAgent.call", new_callable=AsyncMock) as mock:
        yield mock


@pytest.mark.asyncio
async def test_falsification_agent_parses_score(mock_call):
    mock_call.return_value = (
        "## ROUND 1\nAttack 1: Reserve data is stale\n\n"
        "## ROUND 3\n"
        "SURVIVAL_SCORE: 0.7\n"
        "WEAKNESSES_FOUND: Reserve data from 2024\n"
        "STRONGEST_ATTACK: Regulatory timeline uncertain\n"
        "SURVIVED_BECAUSE: Core mechanism holds regardless of timeline\n"
        "REFINED_THESIS: Same thesis with narrowed timeline"
    )
    agent = FalsificationAgent()
    result = await agent.stress_test("mechanism", "predictions", "research")
    assert result.survival_score == 0.7
    assert "Reserve data" in result.raw_output


@pytest.mark.asyncio
async def test_falsification_default_score(mock_call):
    mock_call.return_value = "No clear score in output"
    agent = FalsificationAgent()
    result = await agent.stress_test("mechanism", "predictions", "research")
    assert result.survival_score == 0.5  # default


@pytest.mark.asyncio
async def test_inversion_agent(mock_call):
    mock_call.return_value = (
        "CLAIM: Stablecoins capture value via reserves\n"
        "FORWARD: Yield on reserves creates margin\n"
        "INVERTED: How would I destroy stablecoin value?\n"
        "DIVERGENCE: Inverted reveals user trust is the real value\n"
        "PREDICTION: User confidence metrics predict market share better than yield"
    )
    agent = InversionAgent()
    result = await agent.invert("mechanism", "predictions")
    assert "DIVERGENCE" in result.raw_output


@pytest.mark.asyncio
async def test_bisociation_agent(mock_call):
    mock_call.return_value = (
        "FOREIGN_DOMAIN_1: Mutualistic symbiosis\n"
        "PARALLEL: One organism provides resource, other captures value\n"
        "BREAK_POINT: Biology has natural selection; crypto has regulation\n"
        "NOVEL_PREDICTION: Monopolization triggers ecosystem collapse\n"
        "BISOCIATION_TEST: PASS"
    )
    agent = BisociationAgent()
    result = await agent.cross_domain("mechanism", "anomalies")
    assert "FOREIGN_DOMAIN" in result.raw_output


@pytest.mark.asyncio
async def test_socratic_engine_runs_parallel(mock_call):
    mock_call.return_value = (
        "SURVIVAL_SCORE: 0.8\n"
        "WEAKNESSES_FOUND: Minor timeline uncertainty\n"
        "DIVERGENCE: Inversion reveals hidden assumption\n"
        "FOREIGN_DOMAIN_1: Thermodynamics"
    )
    engine = SocraticEngine()
    result = await engine.stress_test("mechanism", "predictions", "anomalies", "research")
    assert result.passed  # 0.8 >= 0.6
    assert result.falsification.survival_score == 0.8
    assert mock_call.call_count == 3  # parallel: falsification + inversion + bisociation


@pytest.mark.asyncio
async def test_socratic_engine_fails_below_threshold(mock_call):
    mock_call.return_value = "SURVIVAL_SCORE: 0.3\nThesis is dead."
    engine = SocraticEngine()
    result = await engine.stress_test("mechanism", "predictions", "anomalies", "research")
    assert not result.passed  # 0.3 < 0.6
