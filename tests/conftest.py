from pathlib import Path

import pytest

CONTENT_DIR = Path(__file__).parent.parent / "content"
CONFIG_DIR = Path(__file__).parent.parent / "config"


@pytest.fixture
def article_02() -> str:
    return (CONTENT_DIR / "02-insight-ai-capex-stablecoins.md").read_text()


@pytest.fixture
def article_03() -> str:
    return (CONTENT_DIR / "03-insight-what-ai-actually-means.md").read_text()


@pytest.fixture
def article_04() -> str:
    return (CONTENT_DIR / "04-insight-compression-substitution.md").read_text()


@pytest.fixture
def pipeline_config() -> dict:
    import yaml
    return yaml.safe_load((CONFIG_DIR / "pipeline.yaml").read_text())


@pytest.fixture
def quality_thresholds() -> dict:
    import yaml
    return yaml.safe_load((CONFIG_DIR / "quality_thresholds.yaml").read_text())
