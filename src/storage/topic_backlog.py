"""SQLite-backed topic backlog for content planning."""

import sqlite3
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

DB_PATH = Path("data/topics.db")


@dataclass
class Topic:
    id: int = 0
    title: str = ""
    angle: str = ""
    source: str = ""
    urgency: str = "normal"  # low, normal, high, breaking
    status: str = "backlog"  # backlog, researching, drafting, published, dropped
    created_at: str = ""
    notes: str = ""


class TopicBacklog:
    def __init__(self, db_path: Path | None = None):
        self.db_path = db_path or DB_PATH
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS topics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    angle TEXT DEFAULT '',
                    source TEXT DEFAULT '',
                    urgency TEXT DEFAULT 'normal',
                    status TEXT DEFAULT 'backlog',
                    created_at TEXT NOT NULL,
                    notes TEXT DEFAULT ''
                )
            """)

    def add(self, title: str, angle: str = "", source: str = "",
            urgency: str = "normal", notes: str = "") -> Topic:
        now = datetime.now(UTC).isoformat()
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "INSERT INTO topics (title, angle, source, urgency, created_at, notes) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (title, angle, source, urgency, now, notes),
            )
            return Topic(
                id=cursor.lastrowid or 0,
                title=title,
                angle=angle,
                source=source,
                urgency=urgency,
                status="backlog",
                created_at=now,
                notes=notes,
            )

    def list_all(self, status: str | None = None) -> list[Topic]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            if status:
                rows = conn.execute(
                    "SELECT * FROM topics WHERE status = ? ORDER BY id DESC", (status,)
                ).fetchall()
            else:
                rows = conn.execute(
                    "SELECT * FROM topics ORDER BY id DESC"
                ).fetchall()
        return [Topic(**dict(r)) for r in rows]

    def update_status(self, topic_id: int, status: str) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "UPDATE topics SET status = ? WHERE id = ?", (status, topic_id)
            )

    def get(self, topic_id: int) -> Topic | None:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                "SELECT * FROM topics WHERE id = ?", (topic_id,)
            ).fetchone()
        if row is None:
            return None
        return Topic(**dict(row))

    def delete(self, topic_id: int) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM topics WHERE id = ?", (topic_id,))
