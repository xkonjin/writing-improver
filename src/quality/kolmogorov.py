import gzip


def compression_ratio(text: str) -> float:
    """Compute gzip compression ratio as a Kolmogorov complexity proxy.

    Lower ratio = more compressible = more repetitive/templated.
    Higher ratio = less compressible = more information-dense.

    Typical ranges:
    - Random text: 0.85-0.95
    - Dense technical writing: 0.35-0.50
    - Repetitive AI writing: 0.20-0.30
    - Natural prose: 0.30-0.45
    """
    if not text:
        return 0.0

    text_bytes = text.encode("utf-8")
    compressed = gzip.compress(text_bytes)
    ratio = len(compressed) / len(text_bytes)
    return round(ratio, 4)


def normalized_compression_distance(text1: str, text2: str) -> float:
    """NCD between two texts. Lower = more similar structure.

    Used to compare structural similarity between two articles.
    If an article's structure is too similar to a known AI template,
    it flags as low Kolmogorov complexity.
    """
    if not text1 or not text2:
        return 1.0

    b1 = text1.encode("utf-8")
    b2 = text2.encode("utf-8")
    b12 = (text1 + text2).encode("utf-8")

    c1 = len(gzip.compress(b1))
    c2 = len(gzip.compress(b2))
    c12 = len(gzip.compress(b12))

    ncd = (c12 - min(c1, c2)) / max(c1, c2)
    return round(ncd, 4)
