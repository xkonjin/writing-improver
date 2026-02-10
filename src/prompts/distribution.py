"""Prompts for distribution-specific platform formatting."""

SUBSTACK_NOTES_SYSTEM = """Write a Substack Notes post to promote a thesis card article.

Constraints:
- Maximum 280 characters for the hook line
- Structure: hook + blank line + 1-2 sentence key insight + blank line + "[LINK]"
- The hook should be a specific, surprising data point or claim from the article
- Do NOT use "New post:" or "Just published:" or any announcement framing
- Write like you're dropping an interesting fact into a conversation
- No hashtags, no emoji

Voice: Same as article — dense, specific, slightly opinionated."""

TELEGRAM_SYSTEM = """Write a Telegram channel post to share a thesis card article.

Constraints:
- Maximum 1024 characters (Telegram sendPhoto caption limit)
- Use HTML formatting: <b>bold</b>, <i>italic</i>, <a href="URL">link text</a>
- Structure: 2-3 sentence hook with the most surprising finding, then a blank line, then a one-line CTA
- The hook should make someone want to read the full analysis
- CTA: something like "Full analysis: [LINK]" — not "Read more!" or "Check it out!"
- No markdown (Telegram HTML mode, not MarkdownV2)
- No emoji
- No hashtags

Voice: Smart colleague sharing something they found. Specific numbers, company names, regulatory refs."""
