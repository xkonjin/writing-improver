"""Integration tests: quality gate enforcement."""


from src.orchestrator import PipelineOrchestrator


def test_quality_gate_article_02(article_02):
    """Article 02 (good) should score reasonably on quality gates."""
    orch = PipelineOrchestrator(tier=1)
    gate = orch.run_quality_scan(article_02)
    assert gate.scores["structural"] >= 3.0
    assert gate.scores["burstiness"] >= 0.0


def test_quality_gate_poor_article():
    """A deliberately bad article should fail quality gates."""
    bad = (
        "Furthermore, it is important to note that the landscape is evolving. "
        "Moreover, we must consider the implications. "
        "Additionally, the data suggests a paradigm shift. "
        "In conclusion, we have seen that these factors clearly demonstrate "
        "the transformative nature of this revolutionary technology. "
    ) * 10

    orch = PipelineOrchestrator(tier=1)
    gate = orch.run_quality_scan(bad)
    # Bad articles should have more failures
    assert len(gate.failures) > 0 or gate.scores["structural"] < 5.0


def test_quality_gate_scores_are_numeric():
    text = "This is a test article. " * 100
    orch = PipelineOrchestrator(tier=1)
    gate = orch.run_quality_scan(text)
    for score in gate.scores.values():
        assert isinstance(score, float)
