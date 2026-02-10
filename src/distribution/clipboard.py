"""Clipboard and browser helpers for manual publishing."""

from __future__ import annotations

import subprocess

from src.distribution.state import Platform

PLATFORM_URLS: dict[Platform, str] = {
    Platform.SUBSTACK: "https://substack.com/home",
    Platform.SUBSTACK_NOTES: "https://substack.com/notes",
    Platform.X: "https://x.com/compose/post",
    Platform.LINKEDIN: "https://www.linkedin.com/feed/",
    Platform.TELEGRAM: "https://web.telegram.org/",
}


def copy_to_clipboard(content: str) -> bool:
    """Copy text to macOS clipboard via pbcopy. Returns True on success."""
    try:
        subprocess.run(["pbcopy"], input=content.encode(), check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False


def open_url(url: str) -> bool:
    """Open URL in default browser via macOS open. Returns True on success."""
    try:
        subprocess.run(["open", url], check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False


def clipboard_publish(platform: Platform, content: str) -> tuple[bool, bool]:
    """Copy content to clipboard and open platform URL.

    Returns:
        Tuple of (clipboard_success, browser_success).
    """
    clip = copy_to_clipboard(content)
    url = PLATFORM_URLS.get(platform, "")
    browser = open_url(url) if url else False
    return clip, browser
