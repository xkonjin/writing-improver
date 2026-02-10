"""Tests for platform-specific image cropping."""

from PIL import Image

from src.distribution.image_crops import PLATFORM_SIZES, crop_for_platforms


class TestCropForPlatforms:
    def _make_source(self, tmp_path, size=(2000, 1500)):
        img = Image.new("RGB", size, color=(100, 150, 200))
        path = tmp_path / "source.png"
        img.save(str(path))
        return path

    def test_crops_all_platforms(self, tmp_path):
        source = self._make_source(tmp_path)
        out_dir = tmp_path / "crops"
        results = crop_for_platforms(source, out_dir)

        assert len(results) == len(PLATFORM_SIZES)
        for platform, path in results.items():
            img = Image.open(path)
            assert img.size == PLATFORM_SIZES[platform]

    def test_crops_subset(self, tmp_path):
        source = self._make_source(tmp_path)
        out_dir = tmp_path / "crops"
        results = crop_for_platforms(source, out_dir, platforms=["x", "telegram"])

        assert len(results) == 2
        assert "x" in results
        assert "telegram" in results
        assert "linkedin" not in results

    def test_creates_output_dir(self, tmp_path):
        source = self._make_source(tmp_path)
        out_dir = tmp_path / "nested" / "dir"
        results = crop_for_platforms(source, out_dir)

        assert out_dir.exists()
        assert len(results) > 0

    def test_output_filenames(self, tmp_path):
        source = self._make_source(tmp_path)
        out_dir = tmp_path / "crops"
        results = crop_for_platforms(source, out_dir)

        for platform, path in results.items():
            assert f"{platform}_source.png" in path

    def test_skips_unknown_platform(self, tmp_path):
        source = self._make_source(tmp_path)
        out_dir = tmp_path / "crops"
        results = crop_for_platforms(source, out_dir, platforms=["x", "tiktok"])

        assert len(results) == 1
        assert "x" in results
