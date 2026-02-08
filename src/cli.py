import asyncio
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

from src.config import load_pipeline_config, load_quality_thresholds
from src.orchestrator import PipelineOrchestrator
from src.quality.burstiness import compute_burstiness
from src.quality.structural_scanner import scan_structural
from src.quality.vocabulary_scanner import scan_vocabulary
from src.storage.content_store import ContentStore

console = Console()


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """Writing Improver: multi-agent content pipeline."""


@cli.command()
@click.argument("topic")
@click.option(
    "--tier",
    type=click.IntRange(1, 3),
    default=1,
    help="Pipeline tier (1=quick, 2=deep, 3=maximum)",
)
def run(topic: str, tier: int):
    """Run the full content pipeline on a topic."""
    config = load_pipeline_config()
    tier_info = config["tiers"][tier]
    console.print(f"[bold]Pipeline:[/bold] {tier_info['name']} (Tier {tier})")
    console.print(f"[dim]Estimated cost: {tier_info['cost_estimate']}[/dim]")
    console.print(f"[bold]Topic:[/bold] {topic}")

    orch = PipelineOrchestrator(tier=tier)
    state = asyncio.run(orch.run_full(topic))

    # Print results
    cost = state.usage.estimated_cost("claude-opus-4-6")
    console.print("\n[green bold]Pipeline complete![/green bold]")
    console.print(f"Phases: {len(state.completed_phases)}")
    console.print(f"API calls: {state.usage.calls}")
    console.print(f"Cost: ${cost:.2f}")

    if state.scores:
        table = Table(title="Quality Scores")
        table.add_column("Metric")
        table.add_column("Score", justify="right")
        for k, v in state.scores.items():
            table.add_row(k, f"{v:.1f}")
        console.print(table)


@cli.command()
@click.argument("file", type=click.Path(exists=True))
def scan(file: str):
    """Run quality scanners on a draft."""
    text = Path(file).read_text()
    thresholds = load_quality_thresholds()
    st = thresholds.get("structural", {})
    anti = thresholds.get("anti_ai", {})
    voice = thresholds.get("voice", {})

    structural = scan_structural(text)
    vocab = scan_vocabulary(text)
    burstiness = compute_burstiness(text)

    s_score = structural.score(st)
    v_score = vocab.score(thresholds)

    table = Table(title=f"Quality Scan: {file}")
    table.add_column("Metric")
    table.add_column("Value", justify="right")
    table.add_column("Status")

    # Structural metrics
    table.add_row("Structural Score", f"{s_score:.1f}/10", _status(s_score >= 7))
    table.add_row(
        "Sentence Length CV",
        f"{structural.sentence_length_cv:.2f}",
        _status(structural.sentence_length_cv >= st.get("sentence_length_cv", {}).get("min", 0.35)),
    )
    table.add_row(
        "Paragraph Word Std",
        f"{structural.paragraph_word_std:.1f}",
        _status(structural.paragraph_word_std >= st.get("paragraph_word_std", {}).get("min", 20)),
    )
    table.add_row(
        "Single-Sentence Paras",
        str(structural.single_sentence_paragraphs),
        _status(structural.single_sentence_paragraphs >= st.get("single_sentence_paragraphs", {}).get("min", 3)),
    )
    table.add_row(
        "Formal Transitions/1k",
        f"{structural.formal_transitions_per_1k:.1f}",
        _status(structural.formal_transitions_per_1k <= st.get("formal_transitions_per_1k", {}).get("max", 2.5)),
    )
    table.add_row(
        "Section Ratio",
        f"{structural.section_ratio:.1f}",
        _status(
            st.get("section_ratio", {}).get("min", 2.0)
            <= structural.section_ratio
            <= st.get("section_ratio", {}).get("max", 12.0)
        ),
    )

    # Vocabulary metrics
    table.add_row("Vocabulary Score", f"{v_score:.1f}/10", _status(v_score >= 7))
    table.add_row(
        "Banned Words",
        str(vocab.banned_word_count),
        _status(vocab.banned_word_count <= anti.get("banned_words", {}).get("max", 2)),
    )
    table.add_row(
        "Conjunction Starts",
        str(vocab.conjunction_starts),
        _status(vocab.conjunction_starts >= voice.get("conjunction_starts", {}).get("min", 5)),
    )
    table.add_row(
        "Fragments",
        str(vocab.fragment_count),
        _status(vocab.fragment_count >= voice.get("fragments", {}).get("min", 1)),
    )

    # Burstiness
    table.add_row(
        "Burstiness",
        f"{burstiness:.2f}",
        _status(burstiness >= anti.get("burstiness_score", {}).get("min", 0.3)),
    )

    console.print(table)

    if structural.issues:
        console.print("\n[bold]Issues:[/bold]")
        for issue in structural.issues:
            console.print(f"  - {issue}")


@cli.command(name="quality-check")
@click.argument("file", type=click.Path(exists=True))
def quality_check(file: str):
    """Run full quality gate check (pass/fail)."""
    text = Path(file).read_text()
    orch = PipelineOrchestrator(tier=1)
    gate = orch.run_quality_scan(text)

    if gate.passed:
        console.print("[green bold]PASSED[/green bold] all quality gates")
    else:
        console.print("[red bold]FAILED[/red bold] quality gates:")
        for f in gate.failures:
            console.print(f"  [red]- {f}[/red]")

    if gate.scores:
        for k, v in gate.scores.items():
            console.print(f"  {k}: {v:.1f}")


@cli.command(name="list-runs")
def list_runs():
    """List previous pipeline runs."""
    store = ContentStore()
    runs = store.list_runs()
    if not runs:
        console.print("[dim]No runs found.[/dim]")
        return

    table = Table(title="Pipeline Runs")
    table.add_column("Timestamp")
    table.add_column("Topic")
    table.add_column("Tier")
    table.add_column("Cost")
    for r in runs:
        table.add_row(
            r.get("timestamp", "?"),
            r.get("topic", "?"),
            str(r.get("tier", "?")),
            f"${r.get('cost_usd', 0):.2f}",
        )
    console.print(table)


@cli.group()
def topics():
    """Topic selection and backlog management."""


@topics.command(name="scan")
def topics_scan():
    """Run intelligence scan for new topics."""
    console.print("[yellow]Topic scanning not yet implemented. See PR 13.[/yellow]")


@topics.command(name="backlog")
def topics_backlog():
    """View topic backlog."""
    console.print("[yellow]Topic backlog not yet implemented. See PR 13.[/yellow]")


@topics.command(name="add")
@click.argument("topic")
def topics_add(topic: str):
    """Add a topic to the backlog."""
    console.print(f"[bold]Adding:[/bold] {topic}")
    console.print("[yellow]Topic backlog not yet implemented. See PR 13.[/yellow]")


@cli.group()
def facts():
    """Facts database management."""


@facts.command(name="check")
def facts_check():
    """Run freshness audit on facts database."""
    console.print("[yellow]Facts database not yet implemented. See PR 14.[/yellow]")


@facts.command(name="add")
@click.argument("claim")
@click.option("--source", required=True, help="Source URL")
@click.option("--date", required=True, help="Date of claim (YYYY-MM-DD)")
def facts_add(claim: str, source: str, date: str):
    """Add a fact to the database."""
    console.print(f"[bold]Adding fact:[/bold] {claim}")
    console.print("[yellow]Facts database not yet implemented. See PR 14.[/yellow]")


def _status(passed: bool) -> str:
    return "[green]PASS[/green]" if passed else "[red]FAIL[/red]"


if __name__ == "__main__":
    cli()
