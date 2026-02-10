"""Telegram Bot API publisher using raw httpx."""

from __future__ import annotations

import os
from pathlib import Path

import httpx

TELEGRAM_API = "https://api.telegram.org"


class TelegramPublisher:
    def __init__(
        self,
        bot_token: str | None = None,
        channel_id: str | None = None,
    ):
        self.bot_token = bot_token or os.environ.get("TELEGRAM_BOT_TOKEN", "")
        self.channel_id = channel_id or os.environ.get("TELEGRAM_CHANNEL_ID", "")

    def _validate(self) -> None:
        if not self.bot_token:
            raise RuntimeError("TELEGRAM_BOT_TOKEN not set")
        if not self.channel_id:
            raise RuntimeError("TELEGRAM_CHANNEL_ID not set")

    async def send_photo(
        self,
        caption: str,
        image_path: Path | str,
        *,
        link_url: str | None = None,
        link_text: str = "Read full analysis",
    ) -> dict:
        """Send photo with caption to Telegram channel.

        Args:
            caption: HTML-formatted caption (max 1024 chars).
            image_path: Path to image file.
            link_url: Optional URL for inline keyboard button.
            link_text: Label for inline keyboard button.

        Returns:
            Telegram API response dict.
        """
        self._validate()
        url = f"{TELEGRAM_API}/bot{self.bot_token}/sendPhoto"

        data = {
            "chat_id": self.channel_id,
            "caption": caption[:1024],
            "parse_mode": "HTML",
        }

        # Add inline keyboard with link button if URL provided
        if link_url:
            import json

            data["reply_markup"] = json.dumps({
                "inline_keyboard": [[{"text": link_text, "url": link_url}]]
            })

        image = Path(image_path)
        async with httpx.AsyncClient(timeout=30) as client:
            with open(image, "rb") as f:
                resp = await client.post(url, data=data, files={"photo": f})

        resp.raise_for_status()
        return resp.json()

    async def send_message(self, text: str) -> dict:
        """Send text message to Telegram channel (no photo).

        Args:
            text: HTML-formatted message (max 4096 chars).

        Returns:
            Telegram API response dict.
        """
        self._validate()
        url = f"{TELEGRAM_API}/bot{self.bot_token}/sendMessage"

        data = {
            "chat_id": self.channel_id,
            "text": text[:4096],
            "parse_mode": "HTML",
        }

        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(url, data=data)

        resp.raise_for_status()
        return resp.json()
