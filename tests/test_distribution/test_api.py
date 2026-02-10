"""Tests for distribution API."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.agents.publisher import PublisherResult
from src.distribution.api import DistributionAPI
from src.distribution.state import Platform, PublishStatus


def _mock_publisher_result():
    return PublisherResult(
        newsletter="TITLE_A: Test\nPREVIEW: A perfectly good test subject for newsletters\nBODY:\nArticle body.",
        linkedin="Short hook\n\nLinkedIn body.\n\n#stablecoins #fintech #crypto",
        x_thread="\n\n".join([f"{i}/ Tweet number {i} about stablecoins." for i in range(1, 7)]),
        substack_notes="Short hook under 280.\n\nKey insight here.\n\n[LINK]",
        telegram="<b>Hook</b> with specific data.\n\nFull analysis: [LINK]",
    )


@pytest.mark.asyncio
async def test_distribute_creates_state(tmp_path):
    article = tmp_path / "article.md"
    article.write_text("# Test Article\n\nSome content about stablecoins.")

    mock_publisher = MagicMock()
    mock_publisher.format_all = AsyncMock(return_value=_mock_publisher_result())

    with patch("src.distribution.api.PublisherAgent", return_value=mock_publisher):
        with patch("src.distribution.api.DIST_DIR", tmp_path / "dist"):
            api = DistributionAPI()
            state = await api.distribute(str(article))

    assert state.run_id.startswith("dist_")
    assert len(state.platforms) == 5
    for platform in Platform:
        assert platform in state.platforms
        assert state.platforms[platform].status == PublishStatus.READY
        assert len(state.platforms[platform].content) > 0


@pytest.mark.asyncio
async def test_distribute_persists_to_disk(tmp_path):
    article = tmp_path / "article.md"
    article.write_text("# Test\n\nContent.")

    mock_publisher = MagicMock()
    mock_publisher.format_all = AsyncMock(return_value=_mock_publisher_result())

    dist_dir = tmp_path / "dist"
    with patch("src.distribution.api.PublisherAgent", return_value=mock_publisher):
        with patch("src.distribution.api.DIST_DIR", dist_dir):
            api = DistributionAPI()
            state = await api.distribute(str(article))

    # State file should exist
    state_file = dist_dir / state.run_id / "state.json"
    assert state_file.exists()


@pytest.mark.asyncio
async def test_get_status(tmp_path):
    article = tmp_path / "article.md"
    article.write_text("# Test\n\nContent.")

    mock_publisher = MagicMock()
    mock_publisher.format_all = AsyncMock(return_value=_mock_publisher_result())

    dist_dir = tmp_path / "dist"
    with patch("src.distribution.api.PublisherAgent", return_value=mock_publisher):
        with patch("src.distribution.api.DIST_DIR", dist_dir):
            api = DistributionAPI()
            state = await api.distribute(str(article))
            loaded = api.get_status(state.run_id)

    assert loaded.run_id == state.run_id
    assert len(loaded.platforms) == 5


@pytest.mark.asyncio
async def test_edit_content(tmp_path):
    article = tmp_path / "article.md"
    article.write_text("# Test\n\nContent.")

    mock_publisher = MagicMock()
    mock_publisher.format_all = AsyncMock(return_value=_mock_publisher_result())

    dist_dir = tmp_path / "dist"
    with patch("src.distribution.api.PublisherAgent", return_value=mock_publisher):
        with patch("src.distribution.api.DIST_DIR", dist_dir):
            api = DistributionAPI()
            state = await api.distribute(str(article))

            # Edit LinkedIn content
            new_content = "New hook line\n\nNew body text.\n\n#stablecoins"
            warnings = api.edit_content(state.run_id, Platform.LINKEDIN, new_content)

            # Reload and check
            updated = api.get_status(state.run_id)
            assert updated.platforms[Platform.LINKEDIN].content == new_content


@pytest.mark.asyncio
async def test_list_distributions(tmp_path):
    article = tmp_path / "article.md"
    article.write_text("# Test\n\nContent.")

    mock_publisher = MagicMock()
    mock_publisher.format_all = AsyncMock(return_value=_mock_publisher_result())

    dist_dir = tmp_path / "dist"
    with patch("src.distribution.api.PublisherAgent", return_value=mock_publisher):
        with patch("src.distribution.api.DIST_DIR", dist_dir):
            api = DistributionAPI()
            await api.distribute(str(article))
            await api.distribute(str(article))

            distributions = api.list_distributions()
            assert len(distributions) == 2
