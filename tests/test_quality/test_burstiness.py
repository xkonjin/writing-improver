from src.quality.burstiness import compute_burstiness


def test_burstiness_human_article(article_02):
    score = compute_burstiness(article_02)
    assert score > 0.2, f"Article 02 burstiness={score}, expected >0.2"


def test_burstiness_range(article_02):
    score = compute_burstiness(article_02)
    assert 0 <= score <= 1, f"Burstiness out of range: {score}"


def test_burstiness_empty():
    assert compute_burstiness("") == 0.0


def test_burstiness_short():
    score = compute_burstiness("Hello. World.")
    assert score >= 0.0


def test_burstiness_uniform_low():
    # Uniform sentence lengths should score lower
    uniform = ". ".join(["This is a five word sentence"] * 30) + "."
    score = compute_burstiness(uniform)
    assert score < 0.5, f"Uniform text burstiness={score}, expected <0.5"


def test_burstiness_varied_higher():
    # Mixed lengths should score higher
    varied = (
        "Short. "
        "This is a much longer sentence with many more words in it to create variation. "
        "Tiny. "
        "Another very long sentence that goes on and on and on to create real contrast with the short ones. "
        "Yes. "
    ) * 5
    score = compute_burstiness(varied)
    assert score > 0.1, f"Varied text burstiness={score}, expected >0.1"
