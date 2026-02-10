"""Falsification, inversion, and bisociation agents for Socratic insight stress-testing."""

import asyncio
from dataclasses import dataclass, field

from src.agents.base import AgentUsage, BaseAgent
from src.prompts.falsification import (
    BISOCIATION_SYSTEM,
    FALSIFICATION_SYSTEM,
    INVERSION_SYSTEM,
)


@dataclass
class FalsificationResult:
    survival_score: float = 0.0
    weaknesses: str = ""
    strongest_attack: str = ""
    refined_thesis: str = ""
    raw_output: str = ""
    usage: AgentUsage = field(default_factory=AgentUsage)


@dataclass
class InversionResult:
    divergences: str = ""
    novel_predictions: str = ""
    raw_output: str = ""
    usage: AgentUsage = field(default_factory=AgentUsage)


@dataclass
class BisociationResult:
    foreign_domains: list[str] = field(default_factory=list)
    strongest_bisociation: str = ""
    combined_insight: str = ""
    raw_output: str = ""
    usage: AgentUsage = field(default_factory=AgentUsage)


@dataclass
class SocraticResult:
    """Combined output from all three Socratic stress-tests."""
    falsification: FalsificationResult = field(default_factory=FalsificationResult)
    inversion: InversionResult = field(default_factory=InversionResult)
    bisociation: BisociationResult = field(default_factory=BisociationResult)
    passed: bool = False
    usage: AgentUsage = field(default_factory=AgentUsage)


class FalsificationAgent:
    def __init__(self, model: str = "claude-sonnet-4-5-20250929"):
        self.agent = BaseAgent(model=model)

    async def stress_test(self, mechanism: str, predictions: str, research: str) -> FalsificationResult:
        user_prompt = (
            f"THESIS MECHANISM:\n{mechanism}\n\n"
            f"PREDICTIONS:\n{predictions}\n\n"
            f"RESEARCH DATA:\n{research[:10000]}\n\n"
            "Now DESTROY this thesis. Find every weakness."
        )
        raw = await self.agent.call(FALSIFICATION_SYSTEM, user_prompt, max_tokens=4096)

        # Extract survival score from output
        score = 0.5  # default
        for line in raw.split("\n"):
            if "SURVIVAL_SCORE" in line:
                try:
                    score = float(line.split(":")[-1].strip())
                except ValueError:
                    pass

        return FalsificationResult(
            survival_score=score,
            raw_output=raw,
            usage=self.agent.usage,
        )


class InversionAgent:
    def __init__(self, model: str = "claude-opus-4-6"):
        self.agent = BaseAgent(model=model)

    async def invert(self, mechanism: str, predictions: str) -> InversionResult:
        user_prompt = (
            f"THESIS MECHANISM:\n{mechanism}\n\n"
            f"PREDICTIONS:\n{predictions}\n\n"
            "Invert every key claim. Find where forward and inverted answers diverge."
        )
        raw = await self.agent.call(INVERSION_SYSTEM, user_prompt, max_tokens=4096)

        return InversionResult(
            raw_output=raw,
            usage=self.agent.usage,
        )


class BisociationAgent:
    def __init__(self, model: str = "claude-opus-4-6"):
        self.agent = BaseAgent(model=model)

    async def cross_domain(self, mechanism: str, anomalies: str) -> BisociationResult:
        user_prompt = (
            f"DOMAIN MECHANISM:\n{mechanism}\n\n"
            f"ANOMALIES:\n{anomalies}\n\n"
            "Find 3+ genuinely foreign domains with structurally identical dynamics. "
            "Extract predictions invisible from within the original domain."
        )
        raw = await self.agent.call(BISOCIATION_SYSTEM, user_prompt, max_tokens=4096, temperature=0.3)

        return BisociationResult(
            raw_output=raw,
            usage=self.agent.usage,
        )


class SocraticEngine:
    """Orchestrates falsification + inversion + bisociation in parallel."""

    def __init__(self) -> None:
        self.falsification = FalsificationAgent()
        self.inversion = InversionAgent()
        self.bisociation = BisociationAgent()

    async def stress_test(
        self,
        mechanism: str,
        predictions: str,
        anomalies: str,
        research: str,
    ) -> SocraticResult:
        result = SocraticResult()

        # Run all three stress-tests in parallel
        fals_task = self.falsification.stress_test(mechanism, predictions, research)
        inv_task = self.inversion.invert(mechanism, predictions)
        bis_task = self.bisociation.cross_domain(mechanism, anomalies)

        fals, inv, bis = await asyncio.gather(fals_task, inv_task, bis_task)

        result.falsification = fals
        result.inversion = inv
        result.bisociation = bis

        # Thesis passes if survival score >= 0.6
        result.passed = fals.survival_score >= 0.6

        # Aggregate usage
        for agent in [self.falsification.agent, self.inversion.agent, self.bisociation.agent]:
            result.usage.input_tokens += agent.usage.input_tokens
            result.usage.output_tokens += agent.usage.output_tokens
            result.usage.calls += agent.usage.calls

        return result
