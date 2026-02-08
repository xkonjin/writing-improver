"""SQLite-backed facts database with freshness tracking."""

import sqlite3
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

DB_PATH = Path("data/facts.db")


@dataclass
class Fact:
    id: int = 0
    claim: str = ""
    source_url: str = ""
    source_name: str = ""
    claim_date: str = ""
    added_at: str = ""
    last_verified: str = ""
    stale: bool = False
    category: str = ""  # financial, regulatory, market, technical


class FactsDB:
    def __init__(self, db_path: Path | None = None):
        self.db_path = db_path or DB_PATH
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS facts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    claim TEXT NOT NULL,
                    source_url TEXT DEFAULT '',
                    source_name TEXT DEFAULT '',
                    claim_date TEXT DEFAULT '',
                    added_at TEXT NOT NULL,
                    last_verified TEXT DEFAULT '',
                    stale INTEGER DEFAULT 0,
                    category TEXT DEFAULT ''
                )
            """)

    def add(
        self,
        claim: str,
        source_url: str = "",
        source_name: str = "",
        claim_date: str = "",
        category: str = "",
    ) -> Fact:
        now = datetime.now(UTC).isoformat()
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "INSERT INTO facts "
                "(claim, source_url, source_name, claim_date, added_at, last_verified, category) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (claim, source_url, source_name, claim_date, now, now, category),
            )
            return Fact(
                id=cursor.lastrowid or 0,
                claim=claim,
                source_url=source_url,
                source_name=source_name,
                claim_date=claim_date,
                added_at=now,
                last_verified=now,
                category=category,
            )

    def get(self, fact_id: int) -> Fact | None:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                "SELECT * FROM facts WHERE id = ?", (fact_id,)
            ).fetchone()
        if row is None:
            return None
        d = dict(row)
        d["stale"] = bool(d["stale"])
        return Fact(**d)

    def list_all(self, stale_only: bool = False) -> list[Fact]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            if stale_only:
                rows = conn.execute(
                    "SELECT * FROM facts WHERE stale = 1 ORDER BY id DESC"
                ).fetchall()
            else:
                rows = conn.execute(
                    "SELECT * FROM facts ORDER BY id DESC"
                ).fetchall()
        result = []
        for r in rows:
            d = dict(r)
            d["stale"] = bool(d["stale"])
            result.append(Fact(**d))
        return result

    def mark_stale(self, fact_id: int) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("UPDATE facts SET stale = 1 WHERE id = ?", (fact_id,))

    def mark_verified(self, fact_id: int) -> None:
        now = datetime.now(UTC).isoformat()
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "UPDATE facts SET stale = 0, last_verified = ? WHERE id = ?",
                (now, fact_id),
            )

    def check_freshness(self, max_age_months: int = 6) -> list[Fact]:
        """Return facts older than max_age_months since last verification."""
        all_facts = self.list_all()
        stale = []
        now = datetime.now(UTC)
        for fact in all_facts:
            if not fact.last_verified:
                stale.append(fact)
                continue
            verified = datetime.fromisoformat(fact.last_verified)
            if verified.tzinfo is None:
                verified = verified.replace(tzinfo=UTC)
            age_days = (now - verified).days
            if age_days > max_age_months * 30:
                self.mark_stale(fact.id)
                fact.stale = True
                stale.append(fact)
        return stale

    def delete(self, fact_id: int) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM facts WHERE id = ?", (fact_id,))

    def search(self, query: str) -> list[Fact]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            rows = conn.execute(
                "SELECT * FROM facts WHERE claim LIKE ? ORDER BY id DESC",
                (f"%{query}%",),
            ).fetchall()
        result = []
        for r in rows:
            d = dict(r)
            d["stale"] = bool(d["stale"])
            result.append(Fact(**d))
        return result
