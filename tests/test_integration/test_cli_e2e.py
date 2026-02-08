"""E2E tests: CLI commands work against real article files."""

from pathlib import Path

from click.testing import CliRunner

from src.cli import cli


def test_scan_article_02():
    path = Path("content/02-insight-ai-capex-stablecoins.md")
    if not path.exists():
        return
    runner = CliRunner()
    result = runner.invoke(cli, ["scan", str(path)])
    assert result.exit_code == 0
    assert "Quality Scan" in result.output
    assert "Structural Score" in result.output
    assert "Burstiness" in result.output


def test_scan_article_03():
    path = Path("content/03-insight-what-ai-actually-means.md")
    if not path.exists():
        return
    runner = CliRunner()
    result = runner.invoke(cli, ["scan", str(path)])
    assert result.exit_code == 0
    assert "PASS" in result.output or "FAIL" in result.output


def test_scan_article_04():
    path = Path("content/04-insight-compression-substitution.md")
    if not path.exists():
        return
    runner = CliRunner()
    result = runner.invoke(cli, ["scan", str(path)])
    assert result.exit_code == 0


def test_quality_check_article_02():
    path = Path("content/02-insight-ai-capex-stablecoins.md")
    if not path.exists():
        return
    runner = CliRunner()
    result = runner.invoke(cli, ["quality-check", str(path)])
    assert result.exit_code == 0
    assert "PASSED" in result.output or "FAILED" in result.output


def test_list_runs():
    runner = CliRunner()
    result = runner.invoke(cli, ["list-runs"])
    assert result.exit_code == 0


def test_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "multi-agent content pipeline" in result.output


def test_version():
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.output


def test_scan_subcommands():
    runner = CliRunner()
    result = runner.invoke(cli, ["topics", "--help"])
    assert result.exit_code == 0
    assert "scan" in result.output
    assert "backlog" in result.output
    assert "add" in result.output


def test_facts_subcommands():
    runner = CliRunner()
    result = runner.invoke(cli, ["facts", "--help"])
    assert result.exit_code == 0
    assert "check" in result.output
    assert "add" in result.output
