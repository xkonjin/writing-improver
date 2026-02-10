"""Platform-specific formatting prompts."""

NEWSLETTER_SYSTEM = """Format the article for newsletter distribution.

Requirements:
- Generate 3 title options following Matt Levine / Byrne Hobart style:
  Option A: Deadpan factual ("Circle Paid Coinbase $908 Million in 2024")
  Option B: Curious observation ("The Stablecoin Layer Nobody Owns")
  Option C: Conversational question ("Where Does the Money Actually Go?")
- Add a 2-sentence preview/hook for email subject
- Preserve the full article body unchanged
- Add a brief "What I'm reading" section with 2-3 links (placeholders)

Output format:
TITLE_A: [title]
TITLE_B: [title]
TITLE_C: [title]
PREVIEW: [2-sentence hook]
BODY:
[full article]
READING:
- [placeholder link 1]
- [placeholder link 2]"""

LINKEDIN_SYSTEM = """Convert this article into a LinkedIn post.

Constraints:
- Maximum 1300 characters total
- First line: hook that makes someone stop scrolling (NOT clickbait — use a specific number or surprising fact)
- Second line: blank (LinkedIn truncates after ~2 lines)
- Body: the single most surprising insight from the article, explained in 3-4 sentences
- End with a question that invites informed comment (NOT "What do you think?")
- End with 3-5 relevant hashtags on a separate line (e.g. #stablecoins #fintech #crypto)
- No emoji
- No "I'm excited to share..."
- Write like you're telling a colleague something interesting over coffee

Voice: Same as article — smart colleague, specific data, genuine uncertainty."""

X_THREAD_SYSTEM = """Convert this article into an X/Twitter thread.

Constraints:
- 5-8 tweets maximum
- Each tweet: max 280 characters
- Tweet 1: The single most surprising data point or claim. Add "1/" prefix.
- Tweets 2-N: Supporting evidence with "N/" prefix. Each tweet should contain at least one \
specific number, company name, or regulatory reference.
- Second-to-last tweet: The non-obvious implication or prediction
- Final tweet: One-sentence takeaway OR a question + [LINK] placeholder

Rules:
- Number every tweet (1/, 2/, 3/, etc.) — this signals thread length and boosts engagement
- No "Let me explain..." or "Here's why..."
- No emoji threads
- Each tweet must stand alone — someone seeing just that tweet should find it interesting
- Link to the full article in the final tweet only (use [LINK] placeholder)
- Separate each tweet with a blank line

Voice: Dense, specific, slightly opinionated. Like Austin Campbell's X presence."""
