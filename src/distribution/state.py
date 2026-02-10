"""Distribution state model with StrEnum types."""

from __future__ import annotations

import json
import os
import tempfile
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from enum import StrEnum
from pathlib import Path
from typing import Any


class Platform(StrEnum):
    SUBSTACK = "substack"
    SUBSTACK_NOTES = "substack_notes"
    X = "x"
    LINKEDIN = "linkedin"
    TELEGRAM = "telegram"


class PublishStatus(StrEnum):
    READY = "ready"
    SCHEDULED = "scheduled"
    PUBLISHED = "published"


@dataclass
class PlatformStatus:
    status: PublishStatus
    content: str
    scheduled_at: datetime | None = None
    published_at: datetime | None = None
    published_url: str | None = None
    validation_warnings: list[str] = field(default_factory=list)


@dataclass
class DistributionState:
    run_id: str
    article_path: str
    platforms: dict[Platform, PlatformStatus] = field(default_factory=dict)
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def to_dict(self) -> dict[str, Any]:
        """Serialize to JSON-compatible dict."""
        d: dict[str, Any] = {
            "run_id": self.run_id,
            "article_path": self.article_path,
            "created_at": self.created_at.isoformat(),
            "platforms": {},
        }
        for platform, status in self.platforms.items():
            d["platforms"][platform.value] = {
                "status": status.status.value,
                "content": status.content,
                "scheduled_at": status.scheduled_at.isoformat() if status.scheduled_at else None,
                "published_at": status.published_at.isoformat() if status.published_at else None,
                "published_url": status.published_url,
                "validation_warnings": status.validation_warnings,
            }
        return d

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> DistributionState:
        """Deserialize from JSON-compatible dict."""
        platforms: dict[Platform, PlatformStatus] = {}
        for platform_str, status_dict in d.get("platforms", {}).items():
            platform = Platform(platform_str)
            platforms[platform] = PlatformStatus(
                status=PublishStatus(status_dict["status"]),
                content=status_dict["content"],
                scheduled_at=datetime.fromisoformat(status_dict["scheduled_at"]) if status_dict.get("scheduled_at") else None,
                published_at=datetime.fromisoformat(status_dict["published_at"]) if status_dict.get("published_at") else None,
                published_url=status_dict.get("published_url"),
                validation_warnings=status_dict.get("validation_warnings", []),
            )
        return cls(
            run_id=d["run_id"],
            article_path=d["article_path"],
            platforms=platforms,
            created_at=datetime.fromisoformat(d["created_at"]),
        )

    def save(self, path: Path) -> None:
        """Atomic write to JSON file (tmp + os.replace)."""
        path.parent.mkdir(parents=True, exist_ok=True)
        data = json.dumps(self.to_dict(), indent=2)
        fd, tmp_path = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
        try:
            os.write(fd, data.encode())
            os.close(fd)
            os.replace(tmp_path, path)
        except Exception:
            os.close(fd) if not os.get_inheritable(fd) else None
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
            raise

    @classmethod
    def load(cls, path: Path) -> DistributionState:
        """Load from JSON file."""
        return cls.from_dict(json.loads(path.read_text()))
