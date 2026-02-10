"""Platform-specific content validation and Plasma guardrails."""

import re

# Platform character limits (from config/distribution.yaml)
X_TWEET_LIMIT = 280
X_THREAD_MIN = 5
X_THREAD_MAX = 8
LINKEDIN_POST_LIMIT = 1300
LINKEDIN_HOOK_LIMIT = 140
SUBSTACK_NOTES_LIMIT = 280
TELEGRAM_PHOTO_CAPTION_LIMIT = 1024
TELEGRAM_MESSAGE_LIMIT = 4096
NEWSLETTER_SUBJECT_MIN = 40
NEWSLETTER_SUBJECT_MAX = 55

# Plasma guardrail constants
COMPETITOR_KEYWORDS = [
    "Circle",
    "Stripe stablecoins",
    "PayPal stablecoins",
    "Paxos",
    "Ripple",
    "Stellar",
]

BLOCKED_PATTERNS = [
    r"Plasma is better than",
    r"unlike (?:Circle|Paxos|Ripple|Stellar|Stripe|PayPal)",
    r"internal data shows",
    r"we're building",
    r"we are building",
]

# URL pattern for link detection
_URL_RE = re.compile(r"https?://\S+", re.IGNORECASE)


def _split_tweets(thread: str) -> list[str]:
    """Split an X thread into individual tweets by double newlines."""
    tweets = [t.strip() for t in re.split(r"\n{2,}", thread.strip()) if t.strip()]
    return tweets


def validate_x_thread(content: str) -> list[str]:
    """Validate an X/Twitter thread. Returns list of warning strings."""
    warnings: list[str] = []
    tweets = _split_tweets(content)

    if len(tweets) < X_THREAD_MIN:
        warnings.append(f"Thread has {len(tweets)} tweets, minimum is {X_THREAD_MIN}")
    if len(tweets) > X_THREAD_MAX:
        warnings.append(f"Thread has {len(tweets)} tweets, maximum is {X_THREAD_MAX}")

    for i, tweet in enumerate(tweets, 1):
        if len(tweet) > X_TWEET_LIMIT:
            warnings.append(f"Tweet {i} is {len(tweet)} chars, limit is {X_TWEET_LIMIT}")

    # Check links: should only be in the final tweet
    for i, tweet in enumerate(tweets[:-1], 1):
        if _URL_RE.search(tweet) or "[LINK]" in tweet:
            warnings.append(f"Tweet {i} contains a link — links should only be in the final tweet")

    return warnings


def validate_linkedin(content: str) -> list[str]:
    """Validate a LinkedIn post. Returns list of warning strings."""
    warnings: list[str] = []

    if len(content) > LINKEDIN_POST_LIMIT:
        warnings.append(f"Post is {len(content)} chars, limit is {LINKEDIN_POST_LIMIT}")

    # Check hook (first line before blank line)
    lines = content.split("\n")
    first_line = lines[0] if lines else ""
    if len(first_line) > LINKEDIN_HOOK_LIMIT:
        warnings.append(f"Hook is {len(first_line)} chars, should be under {LINKEDIN_HOOK_LIMIT} for preview")

    # Flag external links in body (LinkedIn penalizes them)
    if _URL_RE.search(content):
        warnings.append("External links detected — LinkedIn penalizes posts with links (25-60% reach drop)")

    return warnings


def validate_substack_notes(content: str) -> list[str]:
    """Validate a Substack Notes post. Returns list of warning strings."""
    warnings: list[str] = []

    # Check hook (first line)
    lines = content.split("\n")
    first_line = lines[0] if lines else ""
    if len(first_line) > SUBSTACK_NOTES_LIMIT:
        warnings.append(f"Hook is {len(first_line)} chars, limit is {SUBSTACK_NOTES_LIMIT}")

    return warnings


def validate_telegram(content: str, *, photo: bool = True) -> list[str]:
    """Validate a Telegram caption/message. Returns list of warning strings."""
    warnings: list[str] = []
    limit = TELEGRAM_PHOTO_CAPTION_LIMIT if photo else TELEGRAM_MESSAGE_LIMIT

    if len(content) > limit:
        label = "Photo caption" if photo else "Message"
        warnings.append(f"{label} is {len(content)} chars, limit is {limit}")

    return warnings


def validate_newsletter(content: str) -> list[str]:
    """Validate newsletter formatting. Returns list of warning strings."""
    warnings: list[str] = []

    # Check for PREVIEW line to extract subject
    for line in content.split("\n"):
        if line.startswith("PREVIEW:"):
            preview = line[len("PREVIEW:"):].strip()
            if len(preview) < NEWSLETTER_SUBJECT_MIN:
                warnings.append(f"Subject preview is {len(preview)} chars, minimum is {NEWSLETTER_SUBJECT_MIN}")
            if len(preview) > NEWSLETTER_SUBJECT_MAX:
                warnings.append(f"Subject preview is {len(preview)} chars, maximum is {NEWSLETTER_SUBJECT_MAX}")
            break

    return warnings


def scan_guardrails(content: str) -> list[str]:
    """Scan content for Plasma competitor mentions and blocked patterns.

    Returns list of warning strings. These are flags for human review,
    not hard blocks.
    """
    warnings: list[str] = []

    # Check competitor keywords (case-insensitive word boundary match)
    for keyword in COMPETITOR_KEYWORDS:
        pattern = re.compile(rf"\b{re.escape(keyword)}\b", re.IGNORECASE)
        matches = pattern.findall(content)
        if matches:
            warnings.append(f"Competitor mention: '{keyword}' ({len(matches)}x) — review for tone")

    # Check blocked patterns
    for pattern_str in BLOCKED_PATTERNS:
        pattern = re.compile(pattern_str, re.IGNORECASE)
        if pattern.search(content):
            warnings.append(f"Blocked pattern: '{pattern_str}' — may imply non-public Plasma info")

    return warnings


def validate_all(
    *,
    newsletter: str = "",
    linkedin: str = "",
    x_thread: str = "",
    substack_notes: str = "",
    telegram: str = "",
) -> dict[str, list[str]]:
    """Run all validators on platform content. Returns dict of platform -> warnings."""
    results: dict[str, list[str]] = {}

    if newsletter:
        results["newsletter"] = validate_newsletter(newsletter)
    if linkedin:
        results["linkedin"] = validate_linkedin(linkedin)
    if x_thread:
        results["x_thread"] = validate_x_thread(x_thread)
    if substack_notes:
        results["substack_notes"] = validate_substack_notes(substack_notes)
    if telegram:
        results["telegram"] = validate_telegram(telegram)

    # Scan guardrails across ALL content
    all_content = "\n\n".join(filter(None, [newsletter, linkedin, x_thread, substack_notes, telegram]))
    if all_content:
        guardrail_warnings = scan_guardrails(all_content)
        if guardrail_warnings:
            results["guardrails"] = guardrail_warnings

    return results
