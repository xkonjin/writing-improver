from click.testing import CliRunner

from src.cli import cli
from src.config import load_pipeline_config, load_quality_thresholds


def test_cli_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Writing Improver" in result.output


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.output


def test_cli_scan_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["scan", "--help"])
    assert result.exit_code == 0


def test_cli_run_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["run", "--help"])
    assert result.exit_code == 0
    assert "--tier" in result.output


def test_cli_topics_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["topics", "--help"])
    assert result.exit_code == 0


def test_cli_facts_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["facts", "--help"])
    assert result.exit_code == 0


def test_cli_quality_check_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["quality-check", "--help"])
    assert result.exit_code == 0


def test_pipeline_config_loads(pipeline_config):
    assert "phases" in pipeline_config
    assert "tiers" in pipeline_config
    assert len(pipeline_config["phases"]) > 0


def test_pipeline_config_phase_structure(pipeline_config):
    for phase in pipeline_config["phases"]:
        assert "name" in phase
        assert "model" in phase
        assert "description" in phase


def test_pipeline_config_tiers(pipeline_config):
    tiers = pipeline_config["tiers"]
    assert 1 in tiers
    assert 2 in tiers
    assert 3 in tiers


def test_quality_thresholds_loads(quality_thresholds):
    assert "structural" in quality_thresholds
    assert "anti_ai" in quality_thresholds
    assert "voice" in quality_thresholds
    assert "data_integrity" in quality_thresholds


def test_quality_thresholds_structural(quality_thresholds):
    structural = quality_thresholds["structural"]
    assert "sentence_length_cv" in structural
    assert structural["sentence_length_cv"]["min"] == 0.35
    assert "paragraph_word_std" in structural
    assert "section_ratio" in structural


def test_quality_thresholds_anti_ai(quality_thresholds):
    anti_ai = quality_thresholds["anti_ai"]
    assert anti_ai["banned_words"]["max"] == 0
    assert anti_ai["burstiness_score"]["min"] == 0.5


def test_article_fixtures_load(article_02, article_03, article_04):
    assert len(article_02) > 1000
    assert len(article_03) > 1000
    assert len(article_04) > 1000
