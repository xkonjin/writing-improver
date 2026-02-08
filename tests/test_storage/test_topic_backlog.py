from pathlib import Path

import pytest

from src.storage.topic_backlog import Topic, TopicBacklog


@pytest.fixture
def backlog(tmp_path: Path) -> TopicBacklog:
    return TopicBacklog(db_path=tmp_path / "test_topics.db")


def test_add_topic(backlog: TopicBacklog):
    topic = backlog.add("Stablecoin Distribution Economics", angle="value capture")
    assert topic.id > 0
    assert topic.title == "Stablecoin Distribution Economics"
    assert topic.status == "backlog"


def test_list_all(backlog: TopicBacklog):
    backlog.add("Topic A")
    backlog.add("Topic B")
    topics = backlog.list_all()
    assert len(topics) == 2


def test_list_by_status(backlog: TopicBacklog):
    backlog.add("Topic A")
    t = backlog.add("Topic B")
    backlog.update_status(t.id, "researching")
    backlog_topics = backlog.list_all(status="backlog")
    assert len(backlog_topics) == 1
    assert backlog_topics[0].title == "Topic A"


def test_update_status(backlog: TopicBacklog):
    topic = backlog.add("Test Topic")
    backlog.update_status(topic.id, "drafting")
    updated = backlog.get(topic.id)
    assert updated is not None
    assert updated.status == "drafting"


def test_get_topic(backlog: TopicBacklog):
    topic = backlog.add("Get Me", source="twitter")
    result = backlog.get(topic.id)
    assert result is not None
    assert result.source == "twitter"


def test_get_nonexistent(backlog: TopicBacklog):
    assert backlog.get(999) is None


def test_delete(backlog: TopicBacklog):
    topic = backlog.add("Delete Me")
    backlog.delete(topic.id)
    assert backlog.get(topic.id) is None


def test_topic_defaults():
    t = Topic()
    assert t.urgency == "normal"
    assert t.status == "backlog"
