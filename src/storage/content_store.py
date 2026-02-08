"""Version-controlled content storage with metadata."""

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

OUTPUT_DIR = Path("output")


class ContentStore:
    def __init__(self, base_dir: Path | None = None):
        self.base_dir = base_dir or OUTPUT_DIR

    def save_run(
        self,
        topic: str,
        tier: int,
        phases: dict[str, Any],
        article: str,
        scores: dict[str, Any],
        cost: float,
    ) -> Path:
        timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")
        slug = topic.lower().replace(" ", "-")[:40]
        run_dir = self.base_dir / f"{timestamp}_{slug}"
        run_dir.mkdir(parents=True, exist_ok=True)

        # Save article
        (run_dir / "article.md").write_text(article)

        # Save metadata
        meta = {
            "topic": topic,
            "tier": tier,
            "timestamp": timestamp,
            "scores": scores,
            "cost_usd": cost,
            "phases_completed": list(phases.keys()),
        }
        (run_dir / "metadata.json").write_text(json.dumps(meta, indent=2))

        # Save each phase output
        phases_dir = run_dir / "phases"
        phases_dir.mkdir(exist_ok=True)
        for name, content in phases.items():
            (phases_dir / f"{name}.md").write_text(str(content))

        return run_dir

    def list_runs(self) -> list[dict[str, Any]]:
        if not self.base_dir.exists():
            return []
        runs = []
        for run_dir in sorted(self.base_dir.iterdir(), reverse=True):
            meta_path = run_dir / "metadata.json"
            if meta_path.exists():
                runs.append(json.loads(meta_path.read_text()))
        return runs
