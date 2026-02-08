from pathlib import Path

import pytest

from src.storage.facts_db import Fact, FactsDB


@pytest.fixture
def db(tmp_path: Path) -> FactsDB:
    return FactsDB(db_path=tmp_path / "test_facts.db")


def test_add_fact(db: FactsDB):
    fact = db.add(
        "Circle paid Coinbase $908M in 2024",
        source_url="https://example.com",
        claim_date="2024-01-15",
        category="financial",
    )
    assert fact.id > 0
    assert fact.claim == "Circle paid Coinbase $908M in 2024"
    assert fact.category == "financial"


def test_get_fact(db: FactsDB):
    fact = db.add("Test claim", source_name="Bloomberg")
    result = db.get(fact.id)
    assert result is not None
    assert result.source_name == "Bloomberg"


def test_get_nonexistent(db: FactsDB):
    assert db.get(999) is None


def test_list_all(db: FactsDB):
    db.add("Fact A")
    db.add("Fact B")
    facts = db.list_all()
    assert len(facts) == 2


def test_mark_stale(db: FactsDB):
    fact = db.add("Old data")
    db.mark_stale(fact.id)
    result = db.get(fact.id)
    assert result is not None
    assert result.stale is True


def test_mark_verified(db: FactsDB):
    fact = db.add("Verified data")
    db.mark_stale(fact.id)
    db.mark_verified(fact.id)
    result = db.get(fact.id)
    assert result is not None
    assert result.stale is False


def test_list_stale_only(db: FactsDB):
    db.add("Fresh fact")
    stale = db.add("Stale fact")
    db.mark_stale(stale.id)
    stale_facts = db.list_all(stale_only=True)
    assert len(stale_facts) == 1
    assert stale_facts[0].claim == "Stale fact"


def test_delete(db: FactsDB):
    fact = db.add("Delete me")
    db.delete(fact.id)
    assert db.get(fact.id) is None


def test_search(db: FactsDB):
    db.add("Circle paid $908M")
    db.add("Tether market cap $120B")
    results = db.search("Circle")
    assert len(results) == 1
    assert "Circle" in results[0].claim


def test_fact_defaults():
    f = Fact()
    assert f.stale is False
    assert f.category == ""


def test_check_freshness(db: FactsDB):
    # All freshly added facts should not be stale
    db.add("Recent fact")
    stale = db.check_freshness(max_age_months=6)
    assert len(stale) == 0
