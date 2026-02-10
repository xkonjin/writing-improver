#!/usr/bin/env python3
"""
Bottom-up swarm approach: Start with data, find mechanisms, then write.
No narrative structure. Pure mechanism discovery.
"""

import asyncio
import json
import os
from dotenv import load_dotenv
from src.agents.openrouter_swarm import OpenRouterSwarm
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

async def main():
    """Run bottom-up swarm for Coinbase Super Bowl article."""
    
    print("=" * 70)
    print("BOTTOM-UP SWARM: COINBASE SUPER BOWL AD FAILURE")
    print("=" * 70)
    print(f"Started: {datetime.now().isoformat()}\n")
    
    # Initialize swarm with API key from environment only (never hardcode!)
    api_key = os.getenv("OPENROUTER_API_KEY")
    
    if not api_key:
        print("❌ OPENROUTER_API_KEY not found in environment variables")
        print("\n🔧 TO FIX THIS:")
        print("1. Get an API key from https://openrouter.ai/keys")
        print("2. Create a .env file in this directory with:")
        print("   OPENROUTER_API_KEY=sk-or-v1-your-key-here")
        print("3. Or export it in your shell:")
        print("   export OPENROUTER_API_KEY=sk-or-v1-your-key-here")
        return
    
    print(f"🔑 Using API key: {api_key[:20]}...{api_key[-10:] if len(api_key) > 30 else '[short key]'}")
    
    try:
        swarm = OpenRouterSwarm(api_key=api_key)
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        print("\n🔧 Check that your API key is valid at https://openrouter.ai/keys")
        return
    
    # Define the research target
    topic = """Why did the Coinbase Super Bowl 2026 ad trigger collective booing?
    
    Context:
    - 2022: QR code ad, 20M scans, app crashed, seen as success
    - 2026: Backstreet Boys karaoke ad, instant booing when logo appeared
    - Viewers: median age 49, income $75K, 97% over 45 never owned crypto
    - Crypto owners: median age 31, income $111K, but median holdings only $597
    - Bitcoin Gini coefficient: 0.92 (worse than any country)
    - 192,205 Bitcoin millionaires vs 123.7M viewers
    
    Find the mechanism. Not the story."""
    
    # Run full swarm
    print("Running multi-agent swarm...\n")
    result = await swarm.run_full_swarm(topic)
    
    # Save research phase
    print("\nSaving research outputs...")
    with open("/Users/001/Dev/writing-improver/content/10-swarm-research.md", "w") as f:
        f.write("# Swarm Research Outputs\n\n")
        for r in result["research"]:
            if not r.error:
                f.write(f"## {r.agent_name}\n")
                f.write(f"*Model: {r.model}*\n\n")
                f.write(r.content)
                f.write("\n\n---\n\n")
    
    # Save synthesis
    print("Saving synthesis...")
    with open("/Users/001/Dev/writing-improver/content/10-swarm-synthesis.md", "w") as f:
        f.write("# Synthesis Output\n\n")
        if result["synthesis"].content:
            f.write(result["synthesis"].content)
    
    # Save final article
    print("Saving final article...")
    with open("/Users/001/Dev/writing-improver/content/10-coinbase-bottom-up-final.md", "w") as f:
        f.write("# The $16 Million Teaching Moment\n\n")
        f.write(result["final"])
    
    print(f"\nTokens used: {result['tokens_used']:,}")
    print(f"\nCompleted: {datetime.now().isoformat()}")
    
    print("\n" + "=" * 70)
    print("OUTPUT FILES:")
    print("- content/10-swarm-research.md (raw research)")
    print("- content/10-swarm-synthesis.md (synthesis)")  
    print("- content/10-coinbase-bottom-up-final.md (final article)")
    print("=" * 70)
    
    # Show preview
    print("\nFIRST 500 CHARACTERS OF FINAL:")
    print("-" * 70)
    print(result["final"][:500])

if __name__ == "__main__":
    asyncio.run(main())