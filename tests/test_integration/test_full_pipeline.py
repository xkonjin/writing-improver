"""Integration tests: full pipeline with mocked LLM calls."""

from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.orchestrator import PipelineOrchestrator

MOCK_RESEARCH = """## Money Flow
Circle paid Coinbase $908 million in 2024. That's roughly 55% of Circle's distribution costs.
Tether's market cap hit $120 billion. But Tether spends almost nothing on distribution.
The economics are completely different depending on whether you're an issuer or a distributor.

## Regulatory
The GENIUS Act passed the Senate Banking Committee. It sets reserve requirements for stablecoins
over $10 billion. BNY Mellon is already custodying for Circle. The compliance infrastructure
is being built by traditional finance, not crypto companies.

## Practitioner
I talked to three people building on stablecoins. And they all said the same thing: the
distribution layer is where the money goes. Not issuance. Not compliance. Distribution.
"""

MOCK_INSIGHT = """## Anomalies
The $908M Circle-Coinbase payment is anomalous. No other issuer pays anywhere near this.
Tether pays almost nothing for distribution but has 3x the market cap.

## Mechanism
Value capture in stablecoins follows distribution, not issuance. The company that owns
the user relationship extracts the most value. This is the Visa model, not the Fed model."""

MOCK_OUTLINE = """Start with the $908M number — it's the hook.
Then pivot: why would Circle pay Coinbase more than half its distribution costs?
Direction change: Tether doesn't pay anything. Why?
Spend the most time on the distribution layer.
Quick prediction: the GENIUS Act will accelerate this."""

MOCK_ARTICLE = """Circle paid Coinbase $908 million in 2024. I spent the week trying to figure
out why. And the answer isn't what I expected.

The stablecoin stack has five layers. But only one of them matters for making money. It's not
issuance — that's a commodity. It's not compliance — that's a cost center. It's distribution.

Tether has $120 billion in market cap and spends almost nothing on distribution. Circle has
$45 billion and spends more than half its revenue getting Coinbase to carry USDC. The difference?
Tether got there first. Circle is buying its way in.

But here's where it gets interesting. The GENIUS Act just passed the Senate Banking Committee.
And it sets reserve requirements that basically lock out anyone without a banking relationship.
BNY Mellon is already custodying for Circle. So the compliance layer is being built by TradFi.

Which means the only layer left to compete on is distribution. And distribution is a
network effects game. Whoever owns the user wins.

I was wrong about one thing. I thought the orchestration layer — the Visa equivalent — would
be the value capture point. But it's not. The orchestration layer is a commodity too.
The only defensible position is the user relationship."""


@pytest.fixture
def mock_all_agents():
    """Mock all agent classes used by the orchestrator."""
    patches = {}

    # Research
    research_result = MagicMock()
    research_result.tracks = [
        MagicMock(name="money_flow", content=MOCK_RESEARCH),
    ]
    research_result.usage = MagicMock(
        input_tokens=2000, output_tokens=5000, calls=5
    )

    # Insight
    insight_result = MagicMock()
    insight_result.anomalies = "Anomaly: $908M payment"
    insight_result.cross_references = "Cross ref data"
    insight_result.mechanism = "Distribution captures value"
    insight_result.predictions = "GENIUS Act accelerates consolidation"
    insight_result.validation = "Passes Kolmogorov test"
    insight_result.usage = MagicMock(
        input_tokens=3000, output_tokens=6000, calls=5
    )

    # Disorder
    disorder_result = MagicMock()
    disorder_result.outline = MOCK_OUTLINE
    disorder_result.usage = MagicMock(
        input_tokens=1000, output_tokens=2000, calls=1
    )

    # Writer
    writer_result = MagicMock()
    writer_result.draft = MOCK_ARTICLE
    writer_result.usage = MagicMock(
        input_tokens=2000, output_tokens=4000, calls=1
    )

    # Publisher
    publish_result = MagicMock()
    publish_result.newsletter = "Newsletter version"
    publish_result.linkedin = "LinkedIn version"
    publish_result.x_thread = "X thread version"
    publish_result.usage = MagicMock(
        input_tokens=1000, output_tokens=2000, calls=3
    )

    # Socratic engine
    socratic_result = MagicMock()
    socratic_result.falsification = MagicMock(
        survival_score=0.8, raw_output="Thesis survives"
    )
    socratic_result.inversion = MagicMock(raw_output="Inversion findings")
    socratic_result.bisociation = MagicMock(raw_output="Cross-domain findings")
    socratic_result.passed = True
    socratic_result.usage = MagicMock(
        input_tokens=2000, output_tokens=3000, calls=3
    )

    # Image gen
    image_result = MagicMock()
    image_result.image_path = "/tmp/test_header.jpg"
    image_result.content_type = "REGULATORY"
    image_result.style = "Art Deco institutional"
    image_result.prompt_used = "Art Deco test prompt"
    image_result.usage = MagicMock(
        input_tokens=500, output_tokens=200, calls=2
    )

    with (
        patch("src.orchestrator.ResearchAgent") as mock_research,
        patch("src.orchestrator.InsightPipeline") as mock_insight,
        patch("src.orchestrator.SocraticEngine") as mock_socratic,
        patch("src.orchestrator.DisorderAgent") as mock_disorder,
        patch("src.orchestrator.WriterAgent") as mock_writer,
        patch("src.orchestrator.PublisherAgent") as mock_publisher,
        patch("src.orchestrator.ImageGenAgent") as mock_image,
    ):
        mock_research.return_value.run_all_tracks = AsyncMock(
            return_value=research_result
        )
        mock_insight.return_value.run = AsyncMock(return_value=insight_result)
        mock_socratic.return_value.stress_test = AsyncMock(
            return_value=socratic_result
        )
        mock_disorder.return_value.disorder = AsyncMock(
            return_value=disorder_result
        )
        mock_writer.return_value.write_and_revise = AsyncMock(
            return_value=writer_result
        )
        mock_writer.return_value.revise = AsyncMock(return_value=MOCK_ARTICLE)
        mock_writer.return_value.agent = MagicMock()
        mock_writer.return_value.agent.usage = MagicMock(
            input_tokens=0, output_tokens=0, calls=0
        )
        mock_publisher.return_value.format_all = AsyncMock(
            return_value=publish_result
        )
        mock_image.return_value.run = AsyncMock(return_value=image_result)

        patches["research"] = mock_research
        patches["insight"] = mock_insight
        patches["socratic"] = mock_socratic
        patches["disorder"] = mock_disorder
        patches["writer"] = mock_writer
        patches["publisher"] = mock_publisher
        patches["image"] = mock_image
        yield patches


@pytest.mark.asyncio
async def test_full_pipeline_tier1(mock_all_agents, tmp_path: Path):
    orch = PipelineOrchestrator(tier=1)
    orch.store.base_dir = tmp_path / "output"

    state = await orch.run_full("Stablecoin Distribution Economics")

    assert state.topic == "Stablecoin Distribution Economics"
    assert "saturate" in state.completed_phases
    assert "anomalies" in state.completed_phases
    assert "disorder" in state.completed_phases
    assert "write" in state.completed_phases
    assert "platform_format" in state.completed_phases
    assert state.usage.calls > 0


@pytest.mark.asyncio
async def test_full_pipeline_saves_output(mock_all_agents, tmp_path: Path):
    orch = PipelineOrchestrator(tier=1)
    orch.store.base_dir = tmp_path / "output"

    await orch.run_full("Test Topic")

    runs = orch.store.list_runs()
    assert len(runs) == 1
    assert runs[0]["topic"] == "Test Topic"


@pytest.mark.asyncio
async def test_full_pipeline_has_quality_scores(mock_all_agents, tmp_path: Path):
    orch = PipelineOrchestrator(tier=1)
    orch.store.base_dir = tmp_path / "output"

    state = await orch.run_full("Test Topic")

    assert "structural" in state.scores
    assert "vocabulary" in state.scores
    assert "burstiness" in state.scores


@pytest.mark.asyncio
async def test_tier1_skips_debate(mock_all_agents, tmp_path: Path):
    orch = PipelineOrchestrator(tier=1)
    orch.store.base_dir = tmp_path / "output"

    state = await orch.run_full("Test Topic")

    assert "debate" not in state.completed_phases
    mock_all_agents["research"].return_value.run_all_tracks.assert_called_once()


@pytest.mark.asyncio
async def test_pipeline_publishes_all_formats(mock_all_agents, tmp_path: Path):
    orch = PipelineOrchestrator(tier=1)
    orch.store.base_dir = tmp_path / "output"

    state = await orch.run_full("Test Topic")

    publish = state.phase_outputs.get("publish", {})
    assert "newsletter" in publish
    assert "linkedin" in publish
    assert "x_thread" in publish


@pytest.mark.asyncio
async def test_pipeline_generates_image(mock_all_agents, tmp_path: Path):
    orch = PipelineOrchestrator(tier=1)
    orch.store.base_dir = tmp_path / "output"

    state = await orch.run_full("Test Topic")

    assert "image_gen" in state.completed_phases
    image = state.phase_outputs.get("image", {})
    assert image["content_type"] == "REGULATORY"
    assert image["style"] == "Art Deco institutional"
    assert image["path"] == "/tmp/test_header.jpg"
