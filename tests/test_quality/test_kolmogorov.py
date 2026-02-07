from src.quality.kolmogorov import compression_ratio, normalized_compression_distance


def test_compression_ratio_article(article_02):
    ratio = compression_ratio(article_02)
    assert 0.1 < ratio < 0.9, f"Article 02 compression ratio={ratio}"


def test_compression_ratio_empty():
    assert compression_ratio("") == 0.0


def test_compression_ratio_repetitive():
    text = "the same thing " * 500
    ratio = compression_ratio(text)
    assert ratio < 0.15, f"Repetitive text ratio={ratio}, expected <0.15"


def test_compression_ratio_random():
    import random
    import string
    random.seed(42)
    text = "".join(random.choices(string.ascii_letters + " ", k=5000))
    ratio = compression_ratio(text)
    assert ratio > 0.5, f"Random text ratio={ratio}, expected >0.5"


def test_ncd_identical():
    text = "This is a sample text for testing NCD."
    ncd = normalized_compression_distance(text, text)
    assert ncd < 0.5, f"Identical texts NCD={ncd}, expected <0.5"


def test_ncd_different():
    t1 = "The quick brown fox jumps over the lazy dog. " * 20
    t2 = "Machine learning transforms how we process natural language. " * 20
    ncd = normalized_compression_distance(t1, t2)
    assert ncd > 0.5, f"Different texts NCD={ncd}, expected >0.5"


def test_ncd_empty():
    assert normalized_compression_distance("", "test") == 1.0
    assert normalized_compression_distance("test", "") == 1.0


def test_articles_have_different_compression(article_02, article_04):
    r02 = compression_ratio(article_02)
    r04 = compression_ratio(article_04)
    # Both should be in reasonable range
    assert 0.1 < r02 < 0.9
    assert 0.1 < r04 < 0.9
