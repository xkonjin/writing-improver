from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.agents.writer import WriterAgent, WriterResult
from src.prompts.writing import REVISION_SYSTEM, WRITER_SYSTEM


def test_writer_prompt_has_12_rules():
    assert "RULE 1" in WRITER_SYSTEM
    assert "RULE 12" in WRITER_SYSTEM
    for i in range(1, 13):
        assert f"RULE {i}" in WRITER_SYSTEM, f"Missing RULE {i}"


def test_writer_prompt_voice_model():
    assert "Austin Campbell" in WRITER_SYSTEM
    assert "patio11" in WRITER_SYSTEM
    assert "Matt Levine" in WRITER_SYSTEM


def test_writer_prompt_anti_patterns():
    assert "BANNED" in WRITER_SYSTEM
    assert "Do NOT reorganize" in WRITER_SYSTEM


def test_revision_prompt():
    assert "scan results" in REVISION_SYSTEM.lower()
    assert "do NOT" in REVISION_SYSTEM


@pytest.mark.asyncio
async def test_writer_draft():
    mock = MagicMock()
    mock.call = AsyncMock(return_value="# Draft Article\n\nContent here...")
    mock.usage = MagicMock(input_tokens=1000, output_tokens=3000, calls=1)

    with patch("src.agents.writer.BaseAgent", return_value=mock):
        writer = WriterAgent()
        draft = await writer.write_draft("outline", "research")
        assert len(draft) > 0
        mock.call.assert_called_once()


@pytest.mark.asyncio
async def test_writer_revise():
    mock = MagicMock()
    mock.call = AsyncMock(return_value="# Revised Article\n\nBetter content...")
    mock.usage = MagicMock(input_tokens=1000, output_tokens=3000, calls=1)

    with patch("src.agents.writer.BaseAgent", return_value=mock):
        writer = WriterAgent()
        revised = await writer.revise("draft text", "scan issues")
        assert len(revised) > 0


@pytest.mark.asyncio
async def test_writer_result():
    mock = MagicMock()
    mock.call = AsyncMock(return_value="Article content")
    mock.usage = MagicMock(input_tokens=500, output_tokens=2000, calls=1)

    with patch("src.agents.writer.BaseAgent", return_value=mock):
        writer = WriterAgent()
        result = await writer.write_and_revise("outline", "research")
        assert isinstance(result, WriterResult)
        assert len(result.draft) > 0


def test_writer_result_defaults():
    result = WriterResult()
    assert result.draft == ""
    assert result.revision_count == 0
