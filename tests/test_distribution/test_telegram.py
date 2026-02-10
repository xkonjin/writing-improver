"""Tests for Telegram publisher."""

from unittest.mock import AsyncMock, patch

import httpx
import pytest

from src.distribution.telegram import TelegramPublisher


@pytest.fixture
def publisher():
    return TelegramPublisher(bot_token="test-token", channel_id="@testchannel")


class TestTelegramPublisher:
    def test_validate_missing_token(self):
        pub = TelegramPublisher(bot_token="", channel_id="@ch")
        with pytest.raises(RuntimeError, match="TELEGRAM_BOT_TOKEN"):
            pub._validate()

    def test_validate_missing_channel(self):
        pub = TelegramPublisher(bot_token="tok", channel_id="")
        with pytest.raises(RuntimeError, match="TELEGRAM_CHANNEL_ID"):
            pub._validate()

    def test_validate_success(self, publisher):
        publisher._validate()  # Should not raise

    @pytest.mark.asyncio
    async def test_send_message(self, publisher):
        mock_resp = AsyncMock()
        mock_resp.raise_for_status = lambda: None
        mock_resp.json = lambda: {"ok": True, "result": {"message_id": 1}}

        mock_client = AsyncMock()
        mock_client.post.return_value = mock_resp
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)

        with patch("src.distribution.telegram.httpx.AsyncClient", return_value=mock_client):
            result = await publisher.send_message("Hello <b>world</b>")

        assert result["ok"] is True
        mock_client.post.assert_called_once()
        call_kwargs = mock_client.post.call_args
        assert call_kwargs[1]["data"]["parse_mode"] == "HTML"
        assert call_kwargs[1]["data"]["chat_id"] == "@testchannel"

    @pytest.mark.asyncio
    async def test_send_photo(self, publisher, tmp_path):
        img_file = tmp_path / "test.png"
        img_file.write_bytes(b"\x89PNG\r\n\x1a\n" + b"\x00" * 100)

        mock_resp = AsyncMock()
        mock_resp.raise_for_status = lambda: None
        mock_resp.json = lambda: {"ok": True, "result": {"message_id": 2}}

        mock_client = AsyncMock()
        mock_client.post.return_value = mock_resp
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)

        with patch("src.distribution.telegram.httpx.AsyncClient", return_value=mock_client):
            result = await publisher.send_photo("Caption here", img_file)

        assert result["ok"] is True
        call_kwargs = mock_client.post.call_args
        assert call_kwargs[1]["data"]["caption"] == "Caption here"
        assert "photo" in call_kwargs[1]["files"]

    @pytest.mark.asyncio
    async def test_send_photo_with_link(self, publisher, tmp_path):
        img_file = tmp_path / "test.png"
        img_file.write_bytes(b"\x89PNG\r\n\x1a\n" + b"\x00" * 100)

        mock_resp = AsyncMock()
        mock_resp.raise_for_status = lambda: None
        mock_resp.json.return_value = {"ok": True}

        mock_client = AsyncMock()
        mock_client.post.return_value = mock_resp
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)

        with patch("src.distribution.telegram.httpx.AsyncClient", return_value=mock_client):
            await publisher.send_photo(
                "Caption", img_file, link_url="https://example.com", link_text="Read more"
            )

        call_kwargs = mock_client.post.call_args
        assert "reply_markup" in call_kwargs[1]["data"]

    @pytest.mark.asyncio
    async def test_send_message_truncates(self, publisher):
        mock_resp = AsyncMock()
        mock_resp.raise_for_status = lambda: None
        mock_resp.json.return_value = {"ok": True}

        mock_client = AsyncMock()
        mock_client.post.return_value = mock_resp
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)

        long_text = "x" * 5000
        with patch("src.distribution.telegram.httpx.AsyncClient", return_value=mock_client):
            await publisher.send_message(long_text)

        call_kwargs = mock_client.post.call_args
        assert len(call_kwargs[1]["data"]["text"]) == 4096

    @pytest.mark.asyncio
    async def test_send_photo_truncates_caption(self, publisher, tmp_path):
        img_file = tmp_path / "test.png"
        img_file.write_bytes(b"\x89PNG\r\n\x1a\n" + b"\x00" * 100)

        mock_resp = AsyncMock()
        mock_resp.raise_for_status = lambda: None
        mock_resp.json.return_value = {"ok": True}

        mock_client = AsyncMock()
        mock_client.post.return_value = mock_resp
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)

        long_caption = "y" * 2000
        with patch("src.distribution.telegram.httpx.AsyncClient", return_value=mock_client):
            await publisher.send_photo(long_caption, img_file)

        call_kwargs = mock_client.post.call_args
        assert len(call_kwargs[1]["data"]["caption"]) == 1024
