"""Run quality scanners against existing articles and print calibration data."""

from pathlib import Path

from src.config import load_quality_thresholds
from src.quality.burstiness import compute_burstiness
from src.quality.structural_scanner import scan_structural
from src.quality.vocabulary_scanner import scan_vocabulary

ARTICLES = {
    "02": Path("content/02-insight-ai-capex-stablecoins.md"),
    "03": Path("content/03-insight-what-ai-actually-means.md"),
    "04": Path("content/04-insight-compression-substitution.md"),
}


def main():
    thresholds = load_quality_thresholds()

    for name, path in ARTICLES.items():
        if not path.exists():
            print(f"\n{name}: FILE NOT FOUND ({path})")
            continue

        text = path.read_text()
        structural = scan_structural(text)
        vocab = scan_vocabulary(text)
        burstiness = compute_burstiness(text)

        print(f"\n{'='*60}")
        print(f"Article {name}: {path.name}")
        print(f"{'='*60}")
        print(f"Word count: {len(text.split())}")
        print()

        print("STRUCTURAL:")
        print(f"  sentence_length_cv:          {structural.sentence_length_cv:.3f}")
        print(f"  paragraph_word_std:          {structural.paragraph_word_std:.1f}")
        print(f"  single_sentence_paragraphs:  {structural.single_sentence_paragraphs}")
        print(f"  formal_transitions_per_1k:   {structural.formal_transitions_per_1k:.2f}")
        print(f"  self_refs_per_1k:            {structural.self_refs_per_1k:.2f}")
        print(f"  section_ratio:               {structural.section_ratio:.2f}")
        print(f"  solution_pct:                {structural.solution_pct:.1f}")
        print(f"  SCORE: {structural.score(thresholds):.1f}/10")
        if structural.issues:
            for issue in structural.issues:
                print(f"  ISSUE: {issue}")
        print()

        print("VOCABULARY:")
        print(f"  banned_word_count:           {vocab.banned_word_count}")
        if vocab.banned_words_found:
            print(f"  banned_words_found:          {vocab.banned_words_found}")
        print(f"  not_x_its_y_count:           {vocab.not_x_its_y_count}")
        print(f"  fragment_count:              {vocab.fragment_count}")
        print(f"  conjunction_starts:          {vocab.conjunction_starts}")
        print(f"  contractions_per_200w:       {vocab.contractions_per_200w:.2f}")
        print(f"  em_dashes_per_1k:            {vocab.em_dashes_per_1k:.2f}")
        print(f"  SCORE: {vocab.score(thresholds):.1f}/10")
        print()

        print("BURSTINESS:")
        print(f"  score: {burstiness:.3f}")
        print()


if __name__ == "__main__":
    main()
