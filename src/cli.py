import click
from rich.console import Console

from src.config import load_pipeline_config

console = Console()


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """Writing Improver: Multi-agent content pipeline with Kolmogorov complexity enforcement."""


@cli.command()
@click.argument("topic")
@click.option("--tier", type=click.IntRange(1, 3), default=1, help="Pipeline tier (1=quick, 2=deep, 3=maximum)")
@click.option("--resume-from", type=str, default=None, help="Resume from a specific phase")
def run(topic: str, tier: int, resume_from: str | None):
    """Run the full content pipeline on a topic."""
    config = load_pipeline_config()
    console.print(f"[bold]Pipeline:[/bold] Tier {tier} for '{topic}'")
    console.print(f"[dim]Phases: {len(config.get('phases', []))}[/dim]")
    if resume_from:
        console.print(f"[dim]Resuming from: {resume_from}[/dim]")
    console.print("[yellow]Pipeline not yet implemented. See PR 11.[/yellow]")


@cli.command()
@click.argument("file", type=click.Path(exists=True))
def scan(file: str):
    """Run quality scanners on a draft."""
    console.print(f"[bold]Scanning:[/bold] {file}")
    console.print("[yellow]Quality scanners not yet implemented. See PR 2-3.[/yellow]")


@cli.command(name="quality-check")
@click.argument("file", type=click.Path(exists=True))
def quality_check(file: str):
    """Run full quality gate check on a file."""
    console.print(f"[bold]Quality check:[/bold] {file}")
    console.print("[yellow]Quality gates not yet implemented. See PR 2-3.[/yellow]")


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


if __name__ == "__main__":
    cli()
