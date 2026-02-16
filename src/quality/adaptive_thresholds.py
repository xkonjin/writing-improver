"""Adaptive, topic-specific thresholds that learn from successful outputs."""

from __future__ import annotations

import copy
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class MetricStats:
    count: int = 0
    mean: float = 0.0
    m2: float = 0.0

    def update(self, value: float) -> None:
        self.count += 1
        delta = value - self.mean
        self.mean += delta / self.count
        delta2 = value - self.mean
        self.m2 += delta * delta2

    def variance(self) -> float:
        if self.count < 2:
            return 0.0
        return self.m2 / (self.count - 1)

    def stddev(self) -> float:
        return self.variance() ** 0.5


@dataclass
class AdaptiveMetric:
    metric_key: str
    section: str
    field: str
    bound: str | None
    direction: str
    is_int: bool = False


class AdaptiveThresholds:
    """Topic-aware threshold adjustments using successful outputs."""

    METRICS: list[AdaptiveMetric] = [
        AdaptiveMetric("compression.lexical_density", "compression", "lexical_density_min", None, "min"),
        AdaptiveMetric(
            "compression.zero_info_transitions", "compression", "zero_info_transitions_max", None, "max", True
        ),
        AdaptiveMetric("compression.redundancy_count", "compression", "redundancy_max", None, "max", True),
        AdaptiveMetric("compression.specificity_ratio", "compression", "specificity_ratio_min", None, "min"),
        AdaptiveMetric("compression.filler_phrases", "compression", "filler_phrases_max", None, "max", True),
        AdaptiveMetric("surprise.overall", "surprise", "overall", "min", "min"),
        AdaptiveMetric("structural.sentence_length_cv", "structural", "sentence_length_cv", "min", "min"),
        AdaptiveMetric("structural.paragraph_word_std", "structural", "paragraph_word_std", "min", "min"),
        AdaptiveMetric("structural.single_sentence_paragraphs", "structural", "single_sentence_paragraphs", "min", "min", True),
        AdaptiveMetric("structural.formal_transitions_per_1k", "structural", "formal_transitions_per_1k", "max", "max"),
        AdaptiveMetric("structural.self_refs_per_1k", "structural", "self_refs_per_1k", "min", "min"),
        AdaptiveMetric("structural.self_refs_per_1k", "structural", "self_refs_per_1k", "max", "max"),
        AdaptiveMetric("structural.section_ratio", "structural", "section_ratio", "min", "min"),
        AdaptiveMetric("structural.section_ratio", "structural", "section_ratio", "max", "max"),
        AdaptiveMetric("structural.solution_pct", "structural", "solution_pct", "max", "max"),
        AdaptiveMetric("vocab.banned_words", "anti_ai", "banned_words", "max", "max", True),
        AdaptiveMetric("vocab.conjunction_starts", "voice", "conjunction_starts", "min", "min", True),
        AdaptiveMetric("vocab.fragments", "voice", "fragments", "min", "min", True),
        AdaptiveMetric("vocab.contractions_per_200w", "voice", "contractions_per_200w", "min", "min"),
        AdaptiveMetric("burstiness.score", "anti_ai", "burstiness_score", "min", "min"),
    ]

    def __init__(
        self,
        path: Path | None = None,
        min_samples: int = 3,
        alpha: float = 0.3,
        clamp: float = 0.2,
    ) -> None:
        self.path = path or Path("output") / "adaptive_thresholds.json"
        self.min_samples = min_samples
        self.alpha = alpha
        self.clamp = clamp
        self.store: dict[str, Any] = {"topics": {}}
        self._load()

    def thresholds_for_topic(self, base: dict[str, Any], topic: str) -> dict[str, Any]:
        adjusted = copy.deepcopy(base)
        topic_key = self._match_topic_key(topic)
        topic_entry = self.store.get("topics", {}).get(topic_key, {})
        metrics = topic_entry.get("metrics", {})

        for metric in self.METRICS:
            stat = metrics.get(metric.metric_key)
            if not stat or stat.get("count", 0) < self.min_samples:
                continue
            base_value = self._get_threshold(adjusted, metric)
            if base_value is None:
                continue
            mean = stat.get("mean", base_value)
            updated = self._adjust(base_value, mean)
            if metric.is_int:
                updated = int(round(updated))
            self._set_threshold(adjusted, metric, updated)

        return adjusted

    def record(self, topic: str, metrics: dict[str, float], passed: bool = True) -> None:
        if not passed:
            return
        key = self._match_topic_key(topic, create=True)
        topic_entry = self.store["topics"].setdefault(key, {"tokens": self._topic_tokens(topic), "metrics": {}})
        metric_store = topic_entry.setdefault("metrics", {})

        for metric in self.METRICS:
            if metric.metric_key not in metrics:
                continue
            value = float(metrics[metric.metric_key])
            if metric.metric_key not in metric_store:
                metric_store[metric.metric_key] = {"count": 0, "mean": 0.0, "m2": 0.0}
            stat = MetricStats(**metric_store[metric.metric_key])
            stat.update(value)
            metric_store[metric.metric_key] = {
                "count": stat.count,
                "mean": round(stat.mean, 4),
                "m2": round(stat.m2, 4),
            }

        self._save()

    def _adjust(self, base_value: float, mean: float) -> float:
        updated = base_value + self.alpha * (mean - base_value)
        lower = base_value * (1 - self.clamp)
        upper = base_value * (1 + self.clamp)
        if lower > upper:
            lower, upper = upper, lower
        if base_value == 0:
            return updated
        return round(min(max(updated, lower), upper), 4)

    def _get_threshold(self, base: dict[str, Any], metric: AdaptiveMetric) -> float | None:
        section = base.get(metric.section, {})
        field = section.get(metric.field)
        if metric.bound:
            if isinstance(field, dict):
                return field.get(metric.bound)
            return None
        if isinstance(field, (int, float)):
            return float(field)
        return None

    def _set_threshold(self, base: dict[str, Any], metric: AdaptiveMetric, value: float) -> None:
        section = base.setdefault(metric.section, {})
        if metric.bound:
            field = section.setdefault(metric.field, {})
            if isinstance(field, dict):
                field[metric.bound] = value
        else:
            section[metric.field] = value

    def _topic_tokens(self, topic: str) -> list[str]:
        tokens = re.findall(r"[a-z0-9]+", topic.lower())
        stop = {"the", "and", "of", "to", "a", "in", "for", "on", "with", "at", "by", "from"}
        return [t for t in tokens if t not in stop][:8]

    def _topic_key(self, topic: str) -> str:
        tokens = self._topic_tokens(topic)
        return "-".join(tokens) if tokens else "general"

    def _match_topic_key(self, topic: str, create: bool = False) -> str:
        key = self._topic_key(topic)
        if key in self.store.get("topics", {}):
            return key

        topic_tokens = set(self._topic_tokens(topic))
        best_key = key
        best_score = 0.0
        for existing_key, entry in self.store.get("topics", {}).items():
            existing_tokens = set(entry.get("tokens", []))
            if not existing_tokens:
                continue
            score = len(topic_tokens & existing_tokens) / len(topic_tokens | existing_tokens)
            if score > best_score:
                best_score = score
                best_key = existing_key

        if create and best_score < 0.4:
            self.store.setdefault("topics", {})[key] = {
                "tokens": list(topic_tokens),
                "metrics": {},
            }
            return key

        return best_key

    def _load(self) -> None:
        if not self.path.exists():
            return
        try:
            self.store = json.loads(self.path.read_text())
        except json.JSONDecodeError:
            self.store = {"topics": {}}

    def _save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.store, indent=2))
