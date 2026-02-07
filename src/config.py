from pathlib import Path
from typing import Any

import yaml

CONFIG_DIR = Path(__file__).parent.parent / "config"


def _load_yaml(name: str) -> dict[str, Any]:
    path = CONFIG_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    with open(path) as f:
        result: dict[str, Any] = yaml.safe_load(f)
        return result


def load_pipeline_config() -> dict[str, Any]:
    return _load_yaml("pipeline.yaml")


def load_quality_thresholds() -> dict[str, Any]:
    return _load_yaml("quality_thresholds.yaml")
