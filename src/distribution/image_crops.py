"""Platform-specific image cropping from a single source image."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageOps

# (width, height) per platform
PLATFORM_SIZES: dict[str, tuple[int, int]] = {
    "substack": (1600, 900),
    "linkedin": (1200, 628),
    "x": (1200, 628),
    "telegram": (1200, 800),
    "og": (1200, 630),
}


def crop_for_platforms(
    source: Path | str,
    output_dir: Path | str,
    platforms: list[str] | None = None,
) -> dict[str, str]:
    """Crop source image to platform-specific sizes.

    Returns dict mapping platform name to output file path.
    """
    source = Path(source)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    targets = platforms or list(PLATFORM_SIZES.keys())
    results: dict[str, str] = {}

    img = Image.open(source)

    for platform in targets:
        size = PLATFORM_SIZES.get(platform)
        if not size:
            continue
        cropped = ImageOps.fit(img, size, method=Image.Resampling.LANCZOS)
        out_path = output_dir / f"{platform}_{source.stem}.png"
        cropped.save(str(out_path), "PNG")
        results[platform] = str(out_path)

    return results
