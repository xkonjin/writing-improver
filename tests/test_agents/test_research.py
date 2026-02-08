from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.agents.research import ResearchAgent, ResearchResult, ResearchTrack
from src.prompts.research_track import TRACK_PROMPTS


def test_track_prompts_exist():
    assert len(TRACK_PROMPTS) == 5
    assert "money_flow" in TRACK_PROMPTS
    assert "power_structure" in TRACK_PROMPTS
    assert "regulatory" in TRACK_PROMPTS
    assert "comparative" in TRACK_PROMPTS
    assert "practitioner" in TRACK_PROMPTS


def test_track_prompts_include_base():
    for name, prompt in TRACK_PROMPTS.items():
        assert "RULES:" in prompt, f"{name} missing rules"
        assert "15 data points" in prompt, f"{name} missing data point requirement"


def test_research_track_word_count():
    track = ResearchTrack(name="test", content="word " * 100)
    assert track.word_count == 100


def test_research_result_total_words():
    result = ResearchResult(
        topic="test",
        tracks=[
            ResearchTrack(name="a", content="word " * 50),
            ResearchTrack(name="b", content="word " * 75),
        ],
    )
    assert result.total_words == 125


@pytest.mark.asyncio
async def test_research_single_track():
    mock_response = "Fact 1: Circle paid $908M. " * 50

    with patch("src.agents.research.BaseAgent") as mock_agent:
        instance = mock_agent.return_value
        instance.call = AsyncMock(return_value=mock_response)
        instance.usage = MagicMock(input_tokens=500, output_tokens=1000, calls=1)

        agent = ResearchAgent()
        track = await agent.research_track("money_flow", "Stablecoin Economics")

        assert track.name == "money_flow"
        assert track.word_count > 100
        instance.call.assert_called_once()


@pytest.mark.asyncio
async def test_research_all_tracks():
    mock_response = "Research data here with facts and figures. " * 100

    with patch("src.agents.research.BaseAgent") as mock_agent:
        instance = mock_agent.return_value
        instance.call = AsyncMock(return_value=mock_response)
        instance.usage = MagicMock(input_tokens=500, output_tokens=1000, calls=1)

        agent = ResearchAgent()
        result = await agent.run_all_tracks("Stablecoin Economics")

        assert len(result.tracks) == 5
        assert result.topic == "Stablecoin Economics"
        assert result.total_words > 0


@pytest.mark.asyncio
async def test_research_custom_tracks():
    mock_response = "Custom track research. " * 50

    with patch("src.agents.research.BaseAgent") as mock_agent:
        instance = mock_agent.return_value
        instance.call = AsyncMock(return_value=mock_response)
        instance.usage = MagicMock(input_tokens=500, output_tokens=1000, calls=1)

        agent = ResearchAgent()
        result = await agent.run_all_tracks(
            "Test Topic", track_names=["money_flow", "regulatory"]
        )

        assert len(result.tracks) == 2
