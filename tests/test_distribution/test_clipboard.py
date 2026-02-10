"""Tests for clipboard and browser helpers."""

from unittest.mock import patch

from src.distribution.clipboard import (
    PLATFORM_URLS,
    clipboard_publish,
    copy_to_clipboard,
    open_url,
)
from src.distribution.state import Platform


class TestCopyToClipboard:
    def test_success(self):
        with patch("src.distribution.clipboard.subprocess.run") as mock_run:
            assert copy_to_clipboard("hello") is True
            mock_run.assert_called_once_with(["pbcopy"], input=b"hello", check=True)

    def test_failure(self):
        with patch("src.distribution.clipboard.subprocess.run", side_effect=FileNotFoundError):
            assert copy_to_clipboard("hello") is False


class TestOpenUrl:
    def test_success(self):
        with patch("src.distribution.clipboard.subprocess.run") as mock_run:
            assert open_url("https://x.com") is True
            mock_run.assert_called_once_with(["open", "https://x.com"], check=True)

    def test_failure(self):
        with patch("src.distribution.clipboard.subprocess.run", side_effect=FileNotFoundError):
            assert open_url("https://x.com") is False


class TestClipboardPublish:
    def test_full_publish(self):
        with patch("src.distribution.clipboard.copy_to_clipboard", return_value=True) as mock_clip:
            with patch("src.distribution.clipboard.open_url", return_value=True) as mock_open:
                clip, browser = clipboard_publish(Platform.X, "thread content")
                assert clip is True
                assert browser is True
                mock_clip.assert_called_once_with("thread content")
                mock_open.assert_called_once_with("https://x.com/compose/post")

    def test_clipboard_fails(self):
        with patch("src.distribution.clipboard.copy_to_clipboard", return_value=False):
            with patch("src.distribution.clipboard.open_url", return_value=True):
                clip, browser = clipboard_publish(Platform.LINKEDIN, "post")
                assert clip is False
                assert browser is True


class TestPlatformUrls:
    def test_all_platforms_have_urls(self):
        for platform in Platform:
            assert platform in PLATFORM_URLS, f"Missing URL for {platform}"
