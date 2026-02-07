from dataclasses import dataclass, field

import anthropic


@dataclass
class AgentUsage:
    input_tokens: int = 0
    output_tokens: int = 0
    calls: int = 0

    @property
    def total_tokens(self) -> int:
        return self.input_tokens + self.output_tokens

    def estimated_cost(self, model: str) -> float:
        """Estimate cost in USD based on model pricing."""
        rates = {
            "claude-opus-4-6": (15.0, 75.0),
            "claude-sonnet-4-5-20250929": (3.0, 15.0),
            "claude-haiku-4-5-20251001": (0.80, 4.0),
        }
        input_rate, output_rate = rates.get(model, (3.0, 15.0))
        return (self.input_tokens * input_rate + self.output_tokens * output_rate) / 1_000_000


class BaseAgent:
    def __init__(self, model: str = "claude-sonnet-4-5-20250929"):
        self.client = anthropic.AsyncAnthropic()
        self.model = model
        self.usage = AgentUsage()

    async def call(self, system: str, user: str, max_tokens: int = 4096, temperature: float = 0.0) -> str:
        response = await self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        self.usage.input_tokens += response.usage.input_tokens
        self.usage.output_tokens += response.usage.output_tokens
        self.usage.calls += 1
        block = response.content[0]
        return block.text  # type: ignore[union-attr]

    @property
    def cost(self) -> float:
        return self.usage.estimated_cost(self.model)


@dataclass
class AgentResult:
    content: str
    usage: AgentUsage = field(default_factory=AgentUsage)
    model: str = ""
    phase: str = ""
