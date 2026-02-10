"""End-to-end integration tests for distribution system."""

from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.agents.publisher import PublisherResult
from src.distribution.api import DistributionAPI
from src.distribution.state import Platform, PublishStatus


def _mock_publisher_result():
    newsletter = (
        "TITLE_A: Test Article Title\n"
        "PREVIEW: A perfectly good test subject line for email readers\n"
        "BODY:\nFull newsletter body content here."
    )
    linkedin = (
        "Short hook for LinkedIn engagement\n\n"
        "LinkedIn body with real analysis.\n\n"
        "#stablecoins #fintech #crypto"
    )
    x_thread = "\n\n".join(
        [f"{i}/ Tweet number {i} about stablecoin regulation." for i in range(1, 7)]
    )
    return PublisherResult(
        newsletter=newsletter,
        linkedin=linkedin,
        x_thread=x_thread,
        substack_notes="Short hook under 280 chars.\n\nKey insight.\n\n[LINK]",
        telegram="<b>Stablecoin regulation</b> changed the game.\n\nFull analysis: [LINK]",
    )


@pytest.mark.asyncio
async def test_full_distribute_edit_schedule_flow(tmp_path):
    """End-to-end: distribute → edit → schedule → verify."""
    article = tmp_path / "article.md"
    article.write_text("# Stablecoin Thesis\n\nRegulatory analysis of GENIUS Act implications.")

    mock_publisher = MagicMock()
    mock_publisher.format_all = AsyncMock(return_value=_mock_publisher_result())

    dist_dir = tmp_path / "dist"
    config_path = tmp_path / "dist_config.yaml"
    config_path.write_text(
        "schedule:\n"
        "  x:\n"
        "    day_offset: 0\n"
        "    time: '12:00'\n"
        "  linkedin:\n"
        "    day_offset: 1\n"
        "    time: '08:00'\n"
        "  telegram:\n"
        "    day_offset: 0\n"
        "    time: '10:00'\n"
    )

    with patch("src.distribution.api.PublisherAgent", return_value=mock_publisher):
        with patch("src.distribution.api.DIST_DIR", dist_dir):
            with patch("src.distribution.api.DIST_CONFIG", config_path):
                api = DistributionAPI()

                # Step 1: Distribute
                state = await api.distribute(str(article))
                assert len(state.platforms) == 5
                for p in Platform:
                    assert state.platforms[p].status == PublishStatus.READY

                # Step 2: Edit one platform
                new_x = "\n\n".join([f"{i}/ Updated tweet {i} about GENIUS Act." for i in range(1, 7)])
                api.edit_content(state.run_id, Platform.X, new_x)
                updated = api.get_status(state.run_id)
                assert updated.platforms[Platform.X].content == new_x

                # Step 3: Schedule
                base_date = datetime(2026, 2, 15, 9, 0, tzinfo=UTC)
                scheduled = api.schedule(state.run_id, publish_date=base_date)

                # X should be same day at 12:00
                assert scheduled.platforms[Platform.X].scheduled_at.hour == 12
                assert scheduled.platforms[Platform.X].scheduled_at.day == 15
                assert scheduled.platforms[Platform.X].status == PublishStatus.SCHEDULED

                # LinkedIn should be next day at 08:00
                assert scheduled.platforms[Platform.LINKEDIN].scheduled_at.hour == 8
                assert scheduled.platforms[Platform.LINKEDIN].scheduled_at.day == 16

                # Step 4: Verify persistence
                reloaded = api.get_status(state.run_id)
                assert reloaded.platforms[Platform.X].status == PublishStatus.SCHEDULED
                assert reloaded.platforms[Platform.LINKEDIN].scheduled_at is not None


@pytest.mark.asyncio
async def test_distribute_then_list(tmp_path):
    """Multiple distributions appear in list."""
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
            await api.distribute(str(article))

            distributions = api.list_distributions()
            assert len(distributions) == 3
            # Each has a unique run_id
            run_ids = {d.run_id for d in distributions}
            assert len(run_ids) == 3
