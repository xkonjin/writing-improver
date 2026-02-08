import json
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.orchestrator import PipelineOrchestrator, PipelineState, QualityGateResult
from src.storage.content_store import ContentStore


def test_pipeline_state_defaults():
    state = PipelineState()
    assert state.topic == ""
    assert state.tier == 1
    assert state.phase_outputs == {}


def test_quality_gate_result_defaults():
    gate = QualityGateResult()
    assert gate.passed is True
    assert gate.failures == []


def test_should_skip_tier1():
    orch = PipelineOrchestrator(tier=1)
    assert orch._should_skip("debate") is True
    assert orch._should_skip("forced_impasse") is True
    assert orch._should_skip("bisociate") is True
    assert orch._should_skip("saturate") is False


def test_should_skip_tier3():
    orch = PipelineOrchestrator(tier=3)
    assert orch._should_skip("debate") is False
    assert orch._should_skip("forced_impasse") is False


def test_quality_scan_real_article(article_02):
    orch = PipelineOrchestrator(tier=1)
    gate = orch.run_quality_scan(article_02)
    assert "structural" in gate.scores
    assert "vocabulary" in gate.scores
    assert "burstiness" in gate.scores


def test_content_store_save_and_list(tmp_path: Path):
    store = ContentStore(base_dir=tmp_path / "output")
    run_dir = store.save_run(
        topic="Test Topic",
        tier=1,
        phases={"research": "research output", "draft": "draft output"},
        article="# Test Article\n\nContent here.",
        scores={"structural": 7.5, "vocabulary": 8.0},
        cost=5.50,
    )
    assert run_dir.exists()
    assert (run_dir / "article.md").exists()
    assert (run_dir / "metadata.json").exists()
    assert (run_dir / "phases" / "research.md").exists()

    meta = json.loads((run_dir / "metadata.json").read_text())
    assert meta["topic"] == "Test Topic"
    assert meta["cost_usd"] == 5.50

    runs = store.list_runs()
    assert len(runs) == 1
    assert runs[0]["topic"] == "Test Topic"


def test_content_store_empty(tmp_path: Path):
    store = ContentStore(base_dir=tmp_path / "nonexistent")
    assert store.list_runs() == []


@pytest.mark.asyncio
async def test_run_research():
    mock_result = MagicMock()
    mock_result.tracks = [
        MagicMock(name="money_flow", content="Money data..."),
        MagicMock(name="regulatory", content="Reg data..."),
    ]
    mock_result.usage = MagicMock(input_tokens=500, output_tokens=2000, calls=2)

    with patch("src.orchestrator.ResearchAgent") as mock_ra:
        mock_ra.return_value.run_all_tracks = AsyncMock(return_value=mock_result)
        orch = PipelineOrchestrator(tier=1)
        result = await orch.run_research("stablecoins")
        assert len(result) > 0
        assert "saturate" in orch.state.completed_phases


@pytest.mark.asyncio
async def test_run_insight():
    mock_result = MagicMock()
    mock_result.anomalies = "Anomaly 1"
    mock_result.cross_references = "Cross ref"
    mock_result.mechanism = "Mechanism"
    mock_result.predictions = "Predictions"
    mock_result.validation = "Validation"
    mock_result.usage = MagicMock(input_tokens=1000, output_tokens=3000, calls=5)

    with patch("src.orchestrator.InsightPipeline") as mock_ip:
        mock_ip.return_value.run = AsyncMock(return_value=mock_result)
        orch = PipelineOrchestrator(tier=1)
        result = await orch.run_insight("research text")
        assert "Anomalies" in result
        assert "anomalies" in orch.state.completed_phases


@pytest.mark.asyncio
async def test_run_debate_skipped_tier1():
    orch = PipelineOrchestrator(tier=1)
    result = await orch.run_debate("research", "anomalies")
    assert result == ""


@pytest.mark.asyncio
async def test_run_debate_tier3():
    mock_result = MagicMock()
    mock_result.synthesis = "Winning hypothesis"
    mock_result.usage = MagicMock(input_tokens=500, output_tokens=1000, calls=5)

    with patch("src.orchestrator.DebateAgent") as mock_da:
        mock_da.return_value.run = AsyncMock(return_value=mock_result)
        orch = PipelineOrchestrator(tier=3)
        result = await orch.run_debate("research", "anomalies")
        assert result == "Winning hypothesis"
        assert "debate" in orch.state.completed_phases
