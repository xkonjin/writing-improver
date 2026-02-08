import asyncio
from dataclasses import dataclass, field

from src.agents.base import AgentUsage, BaseAgent
from src.prompts.insight_generation import (
    ANOMALY_DETECTION,
    CROSS_REFERENCE,
    MECHANISM,
    PREDICTION,
    VALIDATION,
)


@dataclass
class InsightResult:
    anomalies: str = ""
    cross_references: str = ""
    mechanism: str = ""
    predictions: str = ""
    validation: str = ""
    usage: AgentUsage = field(default_factory=AgentUsage)


class AnomalyAgent:
    def __init__(self, model: str = "claude-sonnet-4-5-20250929"):
        self.agent = BaseAgent(model=model)

    async def detect(self, research_text: str) -> str:
        return await self.agent.call(
            ANOMALY_DETECTION,
            f"Identify anomalies in this research:\n\n{research_text[:12000]}",
            max_tokens=4096,
        )


class CrossReferenceAgent:
    def __init__(self, model: str = "claude-opus-4-6"):
        self.agent = BaseAgent(model=model)

    async def find_connections(self, research_text: str, anomalies: str) -> str:
        return await self.agent.call(
            CROSS_REFERENCE,
            f"Research:\n{research_text[:10000]}\n\nAnomalies:\n{anomalies}",
            max_tokens=4096,
        )


class MechanismAgent:
    def __init__(self, model: str = "claude-opus-4-6"):
        self.agent = BaseAgent(model=model)

    async def articulate(self, cross_refs: str, anomalies: str) -> str:
        return await self.agent.call(
            MECHANISM,
            f"Cross-references:\n{cross_refs}\n\nAnomalies:\n{anomalies}",
            max_tokens=4096,
        )


class PredictionAgent:
    def __init__(self, model: str = "claude-sonnet-4-5-20250929"):
        self.agent = BaseAgent(model=model)

    async def predict(self, mechanism: str) -> str:
        return await self.agent.call(
            PREDICTION,
            f"Generate predictions from this mechanism:\n\n{mechanism}",
            max_tokens=2048,
        )


class ValidationAgent:
    def __init__(self, model: str = "claude-haiku-4-5-20251001"):
        self.agent = BaseAgent(model=model)

    async def validate(self, insight_text: str) -> str:
        return await self.agent.call(
            VALIDATION,
            f"Validate this insight:\n\n{insight_text}",
            max_tokens=2048,
        )


class InsightPipeline:
    def __init__(self) -> None:
        self.anomaly = AnomalyAgent()
        self.cross_ref = CrossReferenceAgent()
        self.mechanism = MechanismAgent()
        self.prediction = PredictionAgent()
        self.validation = ValidationAgent()

    async def run(self, research_text: str) -> InsightResult:
        result = InsightResult()

        # Sequential pipeline: each step feeds the next
        result.anomalies = await self.anomaly.detect(research_text)
        result.cross_references = await self.cross_ref.find_connections(
            research_text, result.anomalies
        )
        result.mechanism = await self.mechanism.articulate(
            result.cross_references, result.anomalies
        )

        # Predictions and validation can run in parallel
        pred_task = self.prediction.predict(result.mechanism)
        val_input = f"Mechanism:\n{result.mechanism}\n\nAnomalies:\n{result.anomalies}"
        val_task = self.validation.validate(val_input)
        result.predictions, result.validation = await asyncio.gather(pred_task, val_task)

        # Aggregate usage
        bases = [
            self.anomaly.agent, self.cross_ref.agent, self.mechanism.agent,
            self.prediction.agent, self.validation.agent,
        ]
        for base in bases:
            result.usage.input_tokens += base.usage.input_tokens
            result.usage.output_tokens += base.usage.output_tokens
            result.usage.calls += base.usage.calls

        return result
