#!/usr/bin/env python3
"""
Fresh end-to-end analysis of Coinbase Super Bowl ad failure.
No prior context - pure bottom-up mechanism discovery.
"""

import asyncio
import json
from src.agents.openrouter_swarm import OpenRouterSwarm
from datetime import datetime

async def main():
    """Run fresh analysis from scratch."""
    
    print("=" * 80)
    print("FRESH COINBASE SUPER BOWL ANALYSIS")
    print("Bottom-Up Mechanism Discovery - No Prior Context")
    print("=" * 80)
    print(f"Started: {datetime.now().isoformat()}\n")
    
    # Initialize swarm
    api_key = "your-openrouter-api-key-here"
    swarm = OpenRouterSwarm(api_key=api_key)
    
    # Define research target with minimal context
    topic = """Analysis target: Coinbase Super Bowl 2026 ad
    
    Basic facts to investigate:
    - Coinbase ran an ad during Super Bowl 2026
    - Ad featured Backstreet Boys karaoke format  
    - Immediate negative audience reaction (booing)
    - Cost approximately $16 million
    - Compare to their 2022 QR code ad which was considered successful
    
    Research mission: Find the mechanisms that explain this failure.
    Start with data. Find patterns. Extract causal chains.
    No narratives. No predetermined conclusions."""
    
    # Execute swarm analysis
    print("Deploying multi-agent research swarm...\n")
    result = await swarm.run_full_swarm(topic)
    
    # Save all outputs with fresh naming
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    print("Saving research phase...")
    with open(f"/Users/001/Dev/writing-improver/content/fresh_research_{timestamp}.md", "w") as f:
        f.write("# Fresh Coinbase Analysis - Research Phase\n\n")
        for i, r in enumerate(result["research"]):
            if not r.error:
                f.write(f"## Agent {i+1}: {r.agent_name}\n")
                f.write(f"*Model: {r.model} | Tokens: {r.tokens_used}*\n\n")
                f.write(r.content)
                f.write("\n\n" + "="*60 + "\n\n")
            else:
                f.write(f"## Agent {i+1}: ERROR\n")
                f.write(f"Error: {r.error}\n\n")
    
    print("Saving synthesis...")
    with open(f"/Users/001/Dev/writing-improver/content/fresh_synthesis_{timestamp}.md", "w") as f:
        f.write("# Fresh Coinbase Analysis - Synthesis\n\n")
        if result["synthesis"].content:
            f.write(f"*Model: {result['synthesis'].model}*\n\n")
            f.write(result["synthesis"].content)
        else:
            f.write("Synthesis failed\n")
            f.write(f"Error: {result['synthesis'].error}\n")
    
    print("Saving final article...")
    with open(f"/Users/001/Dev/writing-improver/content/fresh_article_{timestamp}.md", "w") as f:
        f.write("# Why Everyone Hated the Coinbase Super Bowl Ad\n")
        f.write("*Generated via fresh multi-agent analysis*\n\n")
        f.write(result["final"])
    
    # Performance metrics
    total_tokens = result["tokens_used"]
    successful_agents = len([r for r in result["research"] if not r.error])
    
    print(f"\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    print(f"Total tokens used: {total_tokens:,}")
    print(f"Successful agents: {successful_agents}/5")
    print(f"Synthesis model: {result['synthesis'].model}")
    
    print(f"\nOutput files:")
    print(f"- content/fresh_research_{timestamp}.md")
    print(f"- content/fresh_synthesis_{timestamp}.md") 
    print(f"- content/fresh_article_{timestamp}.md")
    
    print(f"\nFirst 400 characters of final article:")
    print("-" * 80)
    preview = result["final"][:400]
    print(preview)
    if len(result["final"]) > 400:
        print("...")
    
    return {
        "timestamp": timestamp,
        "tokens": total_tokens,
        "agents": successful_agents,
        "files": {
            "research": f"content/fresh_research_{timestamp}.md",
            "synthesis": f"content/fresh_synthesis_{timestamp}.md",
            "article": f"content/fresh_article_{timestamp}.md"
        }
    }

if __name__ == "__main__":
    result = asyncio.run(main())