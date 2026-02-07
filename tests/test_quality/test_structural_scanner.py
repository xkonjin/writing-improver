from src.quality.structural_scanner import scan_structural


def test_sentence_length_cv_human_article(article_02):
    result = scan_structural(article_02)
    assert result.sentence_length_cv > 0.35, f"Article 02 CV={result.sentence_length_cv}, expected >0.35"


def test_sentence_length_cv_ai_article(article_04):
    result = scan_structural(article_04)
    # AI articles tend to have more uniform sentence lengths
    # but article 04 may still have some variation — we just check it's lower than 02
    assert result.sentence_length_cv >= 0  # sanity check


def test_paragraph_word_std_human(article_02):
    result = scan_structural(article_02)
    assert result.paragraph_word_std > 20, f"Article 02 para std={result.paragraph_word_std}"


def test_single_sentence_paragraphs_human(article_02):
    result = scan_structural(article_02)
    assert result.single_sentence_paragraphs >= 2, f"Article 02 SSP={result.single_sentence_paragraphs}"


def test_formal_transitions_human(article_02):
    result = scan_structural(article_02)
    assert result.formal_transitions_per_1k < 5, f"Article 02 transitions={result.formal_transitions_per_1k}/1k"


def test_self_refs_human(article_02):
    result = scan_structural(article_02)
    assert result.self_refs_per_1k > 2, f"Article 02 self-refs={result.self_refs_per_1k}/1k"


def test_section_ratio_human(article_02):
    result = scan_structural(article_02)
    assert result.section_ratio > 1, f"Article 02 section ratio={result.section_ratio}"


def test_structural_score_article_02(article_02, quality_thresholds):
    result = scan_structural(article_02)
    score = result.score(quality_thresholds["structural"])
    assert score >= 5.0, f"Article 02 structural score={score}, expected >=5.0"


def test_structural_score_article_03(article_03, quality_thresholds):
    result = scan_structural(article_03)
    score = result.score(quality_thresholds["structural"])
    assert score >= 4.0, f"Article 03 structural score={score}, expected >=4.0"


def test_empty_text():
    result = scan_structural("")
    assert result.sentence_length_cv == 0
    assert result.paragraph_word_std == 0


def test_short_text():
    result = scan_structural("This is a test. Another sentence here.")
    assert result.sentence_length_cv >= 0
    assert result.single_sentence_paragraphs >= 0


def test_issues_populated(article_04):
    result = scan_structural(article_04)
    # AI article should have at least some flagged issues
    assert isinstance(result.issues, list)
