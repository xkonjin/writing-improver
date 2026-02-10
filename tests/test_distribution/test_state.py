"""Tests for distribution state model."""

import json
from datetime import UTC, datetime

from src.distribution.state import (
    DistributionState,
    Platform,
    PlatformStatus,
    PublishStatus,
)


def _make_state() -> DistributionState:
    return DistributionState(
        run_id="dist_20260209_abc123",
        article_path="content/06-thesis.md",
        platforms={
            Platform.X: PlatformStatus(
                status=PublishStatus.READY,
                content="1/ Thread tweet one.\n\n2/ Tweet two.",
                validation_warnings=["Thread has 2 tweets, minimum is 5"],
            ),
            Platform.LINKEDIN: PlatformStatus(
                status=PublishStatus.SCHEDULED,
                content="LinkedIn post here.",
                scheduled_at=datetime(2026, 2, 12, 10, 0, tzinfo=UTC),
            ),
        },
    )


class TestPlatformEnum:
    def test_all_platforms(self):
        assert len(Platform) == 5
        assert Platform.SUBSTACK == "substack"
        assert Platform.X == "x"

    def test_str_enum(self):
        assert str(Platform.TELEGRAM) == "telegram"
        assert Platform("linkedin") == Platform.LINKEDIN


class TestPublishStatus:
    def test_all_statuses(self):
        assert len(PublishStatus) == 3
        assert PublishStatus.READY == "ready"
        assert PublishStatus.PUBLISHED == "published"


class TestDistributionState:
    def test_to_dict_roundtrip(self):
        state = _make_state()
        d = state.to_dict()
        restored = DistributionState.from_dict(d)

        assert restored.run_id == state.run_id
        assert restored.article_path == state.article_path
        assert len(restored.platforms) == 2
        assert restored.platforms[Platform.X].status == PublishStatus.READY
        assert restored.platforms[Platform.LINKEDIN].status == PublishStatus.SCHEDULED
        assert restored.platforms[Platform.LINKEDIN].scheduled_at is not None

    def test_json_serializable(self):
        state = _make_state()
        d = state.to_dict()
        json_str = json.dumps(d, indent=2)
        parsed = json.loads(json_str)
        restored = DistributionState.from_dict(parsed)
        assert restored.run_id == "dist_20260209_abc123"

    def test_save_and_load(self, tmp_path):
        state = _make_state()
        path = tmp_path / "test_state.json"
        state.save(path)

        loaded = DistributionState.load(path)
        assert loaded.run_id == state.run_id
        assert loaded.platforms[Platform.X].content == "1/ Thread tweet one.\n\n2/ Tweet two."
        assert loaded.platforms[Platform.X].validation_warnings == ["Thread has 2 tweets, minimum is 5"]

    def test_save_atomic(self, tmp_path):
        """Save should create parent directories and write atomically."""
        state = _make_state()
        path = tmp_path / "nested" / "dir" / "state.json"
        state.save(path)
        assert path.exists()

    def test_validation_warnings_preserved(self):
        state = _make_state()
        d = state.to_dict()
        restored = DistributionState.from_dict(d)
        assert len(restored.platforms[Platform.X].validation_warnings) == 1

    def test_none_dates_serialized(self):
        state = _make_state()
        d = state.to_dict()
        assert d["platforms"]["x"]["scheduled_at"] is None
        assert d["platforms"]["x"]["published_at"] is None

    def test_defaults(self):
        state = DistributionState(run_id="test", article_path="test.md")
        assert len(state.platforms) == 0
        assert state.created_at is not None
