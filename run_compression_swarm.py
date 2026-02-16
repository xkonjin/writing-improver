#!/usr/bin/env python3
"""Run the compression-maximized swarm pipeline."""

from __future__ import annotations

import asyncio
import json
from datetime import UTC, datetime
from pathlib import Path
import re
import sys

from src.agents.openrouter_swarm import OpenRouterSwarm
from src.pipeline.compression_swarm import CompressionMaxSwarm


def _slug(text: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return cleaned[:40] if cleaned else "topic"


async def _run(topic: str) -> None:
    swarm = OpenRouterSwarm()
    pipeline = CompressionMaxSwarm(swarm)
    result = await pipeline.run(topic)

    print("\n=== COMPRESSION SWARM RESULT ===\n")
    print(result.draft)

    # Persist output
    timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")
    run_dir = Path("output") / f"{timestamp}_{_slug(topic)}_compression_swarm"
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "article.md").write_text(result.draft)
    (run_dir / "observations.json").write_text(
        json.dumps([o.__dict__ for o in result.observations], indent=2)
    )
    (run_dir / "collisions.json").write_text(
        json.dumps(
            {
                "contradictions": [
                    {
                        "a": c.insight_a.text,
                        "b": c.insight_b.text,
                        "entities": c.shared_entities,
                        "rationale": c.rationale,
                    }
                    for c in result.collisions.contradictions
                ],
                "syntheses": [
                    {
                        "a": c.insight_a.text,
                        "b": c.insight_b.text,
                        "entities": c.shared_entities,
                        "rationale": c.rationale,
                    }
                    for c in result.collisions.syntheses
                ],
                "llm_notes": result.collisions.llm_notes,
            },
            indent=2,
        )
    )
    (run_dir / "metrics.json").write_text(
        json.dumps(
            {
                "scores": result.final_snapshot.scores,
                "issues": result.final_snapshot.issues,
                "metrics": result.final_snapshot.metrics,
                "tokens_used": result.tokens_used,
                "started_at": result.started_at,
                "finished_at": result.finished_at,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_compression_swarm.py \"Your topic\"")
        sys.exit(1)
    asyncio.run(_run(" ".join(sys.argv[1:])))
