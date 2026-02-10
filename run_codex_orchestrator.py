#!/usr/bin/env python3
"""Run the Codex-style OpenRouter orchestrator."""

import asyncio
import os
from datetime import datetime

from dotenv import load_dotenv

from src.agents.openrouter_codex_orchestrator import OpenRouterCodexOrchestrator
from src.agents.openrouter_swarm import OpenRouterSwarm


async def main() -> None:
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("OPENROUTER_API_KEY not set.")
        return

    topic = os.getenv("SWARM_TOPIC", "Why did the Coinbase Super Bowl 2026 ad get booed?")

    swarm = OpenRouterSwarm(api_key=api_key)
    orchestrator = OpenRouterCodexOrchestrator(swarm)

    print(f"Starting: {datetime.now().isoformat()}")
    result = await orchestrator.run(topic)
    print(f"Attempts: {result.attempts}")
    print(f"Failures: {result.evaluation.failures}")
    print("\nFinal Article:\n")
    print(result.draft)


if __name__ == "__main__":
    asyncio.run(main())
