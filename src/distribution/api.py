"""Distribution API — Python interface for all distribution operations."""

from __future__ import annotations

import hashlib
import uuid
from datetime import UTC, datetime
from pathlib import Path

from src.agents.publisher import PublisherAgent
from src.distribution.state import (
    DistributionState,
    Platform,
    PlatformStatus,
    PublishStatus,
)
from src.distribution.validator import validate_all

DIST_DIR = Path("output") / "distributions"


def _generate_run_id(article_path: str) -> str:
    """Generate a unique run ID from article path + timestamp + random suffix."""
    ts = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")
    h = uuid.uuid4().hex[:6]
    return f"dist_{ts}_{h}"


def _state_path(run_id: str) -> Path:
    return DIST_DIR / run_id / "state.json"


class DistributionAPI:
    def __init__(self, model: str = "claude-sonnet-4-5-20250929"):
        self.model = model

    async def distribute(self, article_path: str) -> DistributionState:
        """Format article for all platforms, validate, and save state.

        Auto-marks platforms as READY if validation passes.
        """
        article = Path(article_path).read_text()
        run_id = _generate_run_id(article_path)

        # Format for all 5 platforms
        publisher = PublisherAgent(model=self.model)
        result = await publisher.format_all(article)

        # Validate all outputs
        warnings = validate_all(
            newsletter=result.newsletter,
            linkedin=result.linkedin,
            x_thread=result.x_thread,
            substack_notes=result.substack_notes,
            telegram=result.telegram,
        )

        # Build platform statuses
        platform_content = {
            Platform.SUBSTACK: result.newsletter,
            Platform.SUBSTACK_NOTES: result.substack_notes,
            Platform.X: result.x_thread,
            Platform.LINKEDIN: result.linkedin,
            Platform.TELEGRAM: result.telegram,
        }

        platforms: dict[Platform, PlatformStatus] = {}
        for platform, content in platform_content.items():
            platform_key = platform.value
            platform_warnings = warnings.get(platform_key, [])
            # Add guardrail warnings to each platform
            guardrail_warnings = warnings.get("guardrails", [])

            platforms[platform] = PlatformStatus(
                status=PublishStatus.READY,
                content=content,
                validation_warnings=platform_warnings + guardrail_warnings,
            )

        state = DistributionState(
            run_id=run_id,
            article_path=article_path,
            platforms=platforms,
        )

        state.save(_state_path(run_id))
        return state

    def get_status(self, run_id: str) -> DistributionState:
        """Load distribution state by run ID."""
        return DistributionState.load(_state_path(run_id))

    def edit_content(self, run_id: str, platform: Platform, content: str) -> list[str]:
        """Update content for a platform and revalidate. Returns new warnings."""
        state = self.get_status(run_id)

        if platform not in state.platforms:
            raise ValueError(f"Platform {platform} not found in distribution {run_id}")

        # Revalidate the edited content
        validate_fn_map = {
            Platform.X: "x_thread",
            Platform.LINKEDIN: "linkedin",
            Platform.SUBSTACK: "newsletter",
            Platform.SUBSTACK_NOTES: "substack_notes",
            Platform.TELEGRAM: "telegram",
        }
        key = validate_fn_map[platform]
        warnings = validate_all(**{key: content})
        platform_warnings = warnings.get(key, [])

        state.platforms[platform].content = content
        state.platforms[platform].validation_warnings = platform_warnings
        state.platforms[platform].status = PublishStatus.READY

        state.save(_state_path(run_id))
        return platform_warnings

    def list_distributions(self) -> list[DistributionState]:
        """List all distribution states."""
        if not DIST_DIR.exists():
            return []
        states = []
        for run_dir in sorted(DIST_DIR.iterdir(), reverse=True):
            state_file = run_dir / "state.json"
            if state_file.exists():
                states.append(DistributionState.load(state_file))
        return states
