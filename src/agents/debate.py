import asyncio
from dataclasses import dataclass, field

from src.agents.base import AgentUsage, BaseAgent

HYPOTHESIS_SYSTEM = """You are hypothesis generator #{agent_id} in a 3-agent debate.

Given research data and anomalies, propose a DISTINCT hypothesis about the key dynamic.
Your hypothesis MUST:
1. Be specific to this domain (not a generic framework application)
2. Name specific entities and cite specific data
3. Make a falsifiable prediction
4. Differ from obvious conclusions

You are agent #{agent_id}. Be intellectually bold. Propose something non-obvious."""

CHALLENGER_SYSTEM = """You are the challenger in a hypothesis debate.

Given 3 competing hypotheses, identify:
1. The weakest assumption in each hypothesis
2. What data would falsify each one
3. Where two hypotheses are actually saying the same thing differently
4. Which hypothesis best explains ALL the anomalies, not just some

Be adversarial. Attack each hypothesis on its weakest point."""

JUDGE_SYSTEM = """You are the judge in a hypothesis debate.

Given the hypotheses and the challenger's critique, select the winning hypothesis.

CRITERIA:
1. Explanatory power — does it explain the anomalies better than alternatives?
2. Specificity — is it domain-specific or a generic framework?
3. Falsifiability — can it be clearly proven wrong?
4. Non-obviousness — would a smart person be surprised by this?

Output:
WINNER: [hypothesis number]
REASON: [why it won]
SYNTHESIS: [improved version incorporating challenger's best critiques]"""


@dataclass
class DebateResult:
    hypotheses: list[str] = field(default_factory=list)
    challenge: str = ""
    winner: str = ""
    synthesis: str = ""
    usage: AgentUsage = field(default_factory=AgentUsage)


class DebateAgent:
    def __init__(self, model: str = "claude-opus-4-6"):
        self.model = model
        self.usage = AgentUsage()

    async def _generate_hypothesis(self, agent_id: int, research: str, anomalies: str) -> str:
        agent = BaseAgent(model=self.model)
        system = HYPOTHESIS_SYSTEM.replace("{agent_id}", str(agent_id))
        result = await agent.call(
            system,
            f"Research:\n{research[:8000]}\n\nAnomalies:\n{anomalies}",
            max_tokens=2048,
            temperature=0.7 + agent_id * 0.1,
        )
        self.usage.input_tokens += agent.usage.input_tokens
        self.usage.output_tokens += agent.usage.output_tokens
        self.usage.calls += agent.usage.calls
        return result

    async def _challenge(self, hypotheses: list[str]) -> str:
        agent = BaseAgent(model=self.model)
        hyp_text = "\n\n".join(f"HYPOTHESIS {i+1}:\n{h}" for i, h in enumerate(hypotheses))
        result = await agent.call(CHALLENGER_SYSTEM, hyp_text, max_tokens=3072)
        self.usage.input_tokens += agent.usage.input_tokens
        self.usage.output_tokens += agent.usage.output_tokens
        self.usage.calls += agent.usage.calls
        return result

    async def _judge(self, hypotheses: list[str], challenge: str) -> str:
        agent = BaseAgent(model=self.model)
        hyp_text = "\n\n".join(f"HYPOTHESIS {i+1}:\n{h}" for i, h in enumerate(hypotheses))
        result = await agent.call(
            JUDGE_SYSTEM,
            f"Hypotheses:\n{hyp_text}\n\nChallenger's critique:\n{challenge}",
            max_tokens=3072,
        )
        self.usage.input_tokens += agent.usage.input_tokens
        self.usage.output_tokens += agent.usage.output_tokens
        self.usage.calls += agent.usage.calls
        return result

    async def run(self, research: str, anomalies: str) -> DebateResult:
        # Phase 1: 3 parallel hypothesis generators
        tasks = [self._generate_hypothesis(i + 1, research, anomalies) for i in range(3)]
        hypotheses = await asyncio.gather(*tasks)

        # Phase 2: Challenger
        challenge = await self._challenge(list(hypotheses))

        # Phase 3: Judge
        winner = await self._judge(list(hypotheses), challenge)

        return DebateResult(
            hypotheses=list(hypotheses),
            challenge=challenge,
            winner=winner,
            synthesis=winner,
            usage=self.usage,
        )
