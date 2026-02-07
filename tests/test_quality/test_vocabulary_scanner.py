from src.quality.vocabulary_scanner import scan_vocabulary


def test_no_banned_words_article_02(article_02):
    result = scan_vocabulary(article_02)
    # Good articles should have very few banned words
    assert result.banned_word_count < 3, f"Article 02 has {result.banned_word_count} banned words: {result.banned_words_found}"


def test_conjunction_starts_human(article_02):
    result = scan_vocabulary(article_02)
    assert result.conjunction_starts >= 1, f"Article 02 conjunction starts={result.conjunction_starts}"


def test_contractions_human(article_02):
    result = scan_vocabulary(article_02)
    assert result.contractions_per_200w >= 0.5, f"Article 02 contractions={result.contractions_per_200w}/200w"


def test_em_dashes_present(article_02):
    result = scan_vocabulary(article_02)
    assert result.em_dashes_per_1k > 0, f"Article 02 em-dashes={result.em_dashes_per_1k}/1k"


def test_vocab_score_article_02(article_02, quality_thresholds):
    result = scan_vocabulary(article_02)
    score = result.score(quality_thresholds)
    assert score >= 4.0, f"Article 02 vocab score={score}"


def test_banned_words_detection():
    text = "Let's delve into the tapestry of this landscape and leverage our synergy."
    result = scan_vocabulary(text)
    assert result.banned_word_count >= 4
    assert "delve" in result.banned_words_found
    assert "tapestry" in result.banned_words_found


def test_not_x_its_y_detection():
    text = "It's not about the money. It's about the principle. And it's not about timing; it's about readiness."
    result = scan_vocabulary(text)
    assert result.not_x_its_y_count >= 1


def test_empty_text():
    result = scan_vocabulary("")
    assert result.banned_word_count == 0
    assert result.conjunction_starts == 0


def test_conjunction_starts():
    text = "And then it happened. But nobody saw it coming. So we pivoted. Yet the problem remained. Still, we pushed."
    result = scan_vocabulary(text)
    assert result.conjunction_starts >= 4


def test_contraction_counting():
    text = "It's clear that they've done this before. We can't ignore it. He'd know. She'll agree. I'm sure."
    result = scan_vocabulary(text)
    assert result.contractions_per_200w > 0
