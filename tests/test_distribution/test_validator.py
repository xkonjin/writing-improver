"""Tests for platform validation and guardrail scanning."""

from src.distribution.validator import (
    scan_guardrails,
    validate_all,
    validate_linkedin,
    validate_newsletter,
    validate_substack_notes,
    validate_telegram,
    validate_x_thread,
)


class TestValidateXThread:
    def test_valid_thread(self):
        tweets = "\n\n".join([f"{i}/ Tweet number {i} with content." for i in range(1, 7)])
        tweets += "\n\n6/ Final tweet with takeaway. [LINK]"
        warnings = validate_x_thread(tweets)
        # May have link warning for tweet 6 if it's not the last, but structure is valid
        assert not any("chars" in w for w in warnings)

    def test_too_few_tweets(self):
        thread = "1/ One tweet.\n\n2/ Two tweets.\n\n3/ Three. [LINK]"
        warnings = validate_x_thread(thread)
        assert any("minimum is 5" in w for w in warnings)

    def test_too_many_tweets(self):
        tweets = "\n\n".join([f"{i}/ Tweet {i}." for i in range(1, 11)])
        warnings = validate_x_thread(tweets)
        assert any("maximum is 8" in w for w in warnings)

    def test_tweet_over_280_chars(self):
        long_tweet = "x" * 300
        thread = f"{long_tweet}\n\n" + "\n\n".join([f"Tweet {i}." for i in range(2, 7)])
        warnings = validate_x_thread(thread)
        assert any("Tweet 1 is 300 chars" in w for w in warnings)

    def test_link_in_non_final_tweet(self):
        tweets = [
            "1/ First tweet.",
            "2/ Second with https://example.com link.",
            "3/ Third tweet.",
            "4/ Fourth tweet.",
            "5/ Fifth tweet. [LINK]",
        ]
        warnings = validate_x_thread("\n\n".join(tweets))
        assert any("Tweet 2 contains a link" in w for w in warnings)

    def test_link_in_final_tweet_ok(self):
        tweets = [
            "1/ First tweet.",
            "2/ Second tweet.",
            "3/ Third tweet.",
            "4/ Fourth tweet.",
            "5/ Final tweet with [LINK]",
        ]
        warnings = validate_x_thread("\n\n".join(tweets))
        link_warnings = [w for w in warnings if "contains a link" in w]
        assert len(link_warnings) == 0


class TestValidateLinkedin:
    def test_valid_post(self):
        post = "Short hook line\n\nBody of the post with some insight."
        warnings = validate_linkedin(post)
        assert len(warnings) == 0

    def test_over_length(self):
        post = "x" * 1400
        warnings = validate_linkedin(post)
        assert any("1400 chars" in w for w in warnings)

    def test_long_hook(self):
        post = ("x" * 150) + "\n\nBody text."
        warnings = validate_linkedin(post)
        assert any("Hook is 150 chars" in w for w in warnings)

    def test_external_link_warning(self):
        post = "Hook line\n\nCheck out https://example.com for more."
        warnings = validate_linkedin(post)
        assert any("External links detected" in w for w in warnings)


class TestValidateSubstackNotes:
    def test_valid_note(self):
        note = "Short hook under 280 chars.\n\nMore detail here.\n\n[LINK]"
        warnings = validate_substack_notes(note)
        assert len(warnings) == 0

    def test_long_hook(self):
        note = ("x" * 300) + "\n\nBody."
        warnings = validate_substack_notes(note)
        assert any("300 chars" in w for w in warnings)


class TestValidateTelegram:
    def test_valid_caption(self):
        caption = "Short caption for photo."
        warnings = validate_telegram(caption, photo=True)
        assert len(warnings) == 0

    def test_photo_caption_over_limit(self):
        caption = "x" * 1100
        warnings = validate_telegram(caption, photo=True)
        assert any("1100 chars" in w for w in warnings)

    def test_message_mode_higher_limit(self):
        msg = "x" * 2000
        warnings = validate_telegram(msg, photo=False)
        assert len(warnings) == 0  # Under 4096

    def test_message_over_limit(self):
        msg = "x" * 5000
        warnings = validate_telegram(msg, photo=False)
        assert any("5000 chars" in w for w in warnings)


class TestValidateNewsletter:
    def test_valid_subject(self):
        content = "TITLE_A: Something\nPREVIEW: This is a perfectly good subject line for email ok\nBODY:\nArticle here."
        warnings = validate_newsletter(content)
        assert len(warnings) == 0

    def test_subject_too_short(self):
        content = "PREVIEW: Too short\nBODY:\nArticle."
        warnings = validate_newsletter(content)
        assert any("minimum is 40" in w for w in warnings)

    def test_subject_too_long(self):
        content = f"PREVIEW: {'x' * 60}\nBODY:\nArticle."
        warnings = validate_newsletter(content)
        assert any("maximum is 55" in w for w in warnings)


class TestScanGuardrails:
    def test_no_issues(self):
        text = "Stablecoins are growing. Tether has 300 employees."
        warnings = scan_guardrails(text)
        assert len(warnings) == 0

    def test_competitor_mention(self):
        text = "Circle filed for an IPO in 2025."
        warnings = scan_guardrails(text)
        assert any("Circle" in w for w in warnings)

    def test_multiple_competitor_mentions(self):
        text = "Circle and Paxos both received OCC charters."
        warnings = scan_guardrails(text)
        assert any("Circle" in w for w in warnings)
        assert any("Paxos" in w for w in warnings)

    def test_blocked_pattern(self):
        text = "Plasma is better than Circle at everything."
        warnings = scan_guardrails(text)
        assert any("Blocked pattern" in w for w in warnings)

    def test_internal_data_pattern(self):
        text = "Internal data shows strong growth."
        warnings = scan_guardrails(text)
        assert any("internal data shows" in w.lower() for w in warnings)

    def test_case_insensitive(self):
        text = "CIRCLE is a competitor."
        warnings = scan_guardrails(text)
        assert any("Circle" in w for w in warnings)

    def test_word_boundary(self):
        # "Circular" should NOT trigger "Circle"
        text = "The circular economy is growing."
        warnings = scan_guardrails(text)
        assert len(warnings) == 0


class TestValidateAll:
    def test_runs_all_validators(self):
        results = validate_all(
            newsletter="PREVIEW: Good subject line for the newsletter edition\nBODY:\nArticle.",
            linkedin="Short hook\n\nBody text about stablecoins.",
            x_thread="\n\n".join([f"{i}/ Tweet {i}." for i in range(1, 7)]),
            substack_notes="Hook line.\n\nInsight.\n\n[LINK]",
            telegram="Short caption.",
        )
        # All should pass with no warnings
        for platform, warnings in results.items():
            assert len(warnings) == 0, f"{platform}: {warnings}"

    def test_guardrails_across_all_content(self):
        results = validate_all(
            linkedin="Circle is doing well.",
            x_thread="\n\n".join([f"{i}/ Tweet {i}." for i in range(1, 6)]),
        )
        assert "guardrails" in results
        assert any("Circle" in w for w in results["guardrails"])
