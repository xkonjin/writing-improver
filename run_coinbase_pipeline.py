#!/usr/bin/env python3
"""
Multi-agent pipeline for Coinbase Super Bowl article.
Uses OpenRouter API for diverse model perspectives.
"""

import asyncio
import httpx
import json
from typing import List, Dict, Any
import os

OPENROUTER_API_KEY = "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"

async def call_model(model: str, system: str, user: str, temperature: float = 0.7) -> str:
    """Call a specific model via OpenRouter."""
    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user}
                ],
                "temperature": temperature,
                "max_tokens": 4000
            }
        )
        result = response.json()
        if "choices" in result:
            return result["choices"][0]["message"]["content"]
        else:
            return f"Error from {model}: {result}"

async def research_agent_swarm():
    """Run parallel research agents with different perspectives."""
    
    research_tasks = [
        # Financial mechanism researcher
        call_model(
            "anthropic/claude-3.5-sonnet",
            "You are a quantitative finance researcher. Find specific numerical mechanisms.",
            """Research the Coinbase Super Bowl ad failure. Find:
            1. Exact viewer demographics vs crypto owner demographics
            2. The neurological mechanism of collective booing
            3. QR code 2022 (20M scans) vs karaoke 2026 (booing) - what changed structurally?
            4. Actual data on who owns crypto wealth (Gini coefficient 0.92)
            5. The mechanism by which nostalgia + finance = rejection
            No narratives. Just data and mechanisms."""
        ),
        
        # Behavioral economist
        call_model(
            "google/gemini-pro-1.5",
            "You are a behavioral economist studying crowd dynamics and financial trauma.",
            """Analyze the Coinbase Super Bowl booing as a phase transition. Research:
            1. How collective financial trauma encodes neurologically
            2. The difference between loss aversion and betrayal aversion
            3. Mirror neuron activation in crowd rejection
            4. Why QR codes trigger curiosity but karaoke triggers disgust
            5. Historical parallels (Enron ads, Wells Fargo campaigns)
            Focus on mechanisms, not stories."""
        ),
        
        # Cultural anthropologist
        call_model(
            "meta-llama/llama-3.1-70b-instruct",
            "You are a cultural anthropologist studying American financial mythology.",
            """Study the Coinbase ad as cultural violation. Research:
            1. Why Backstreet Boys (1999) + crypto (2026) = rage
            2. The demographic mismatch (viewers age 49 vs owners age 31)
            3. How 'vibe' purchases fail neurologically
            4. The settler/native dynamic (crypto wealth in Dubai/Singapore)
            5. What Americans encode as 'scam' vs 'innovation'
            Find the anthropological mechanism, not the narrative."""
        ),
        
        # Data analyst
        call_model(
            "openai/gpt-4-turbo-preview",
            "You are a data scientist. Find anomalies and surprising connections.",
            """Find the non-obvious data about Coinbase Super Bowl:
            1. 97% of viewers 45+ never owned crypto, 71% who did sold at loss
            2. Nigerian stablecoin adoption inversely correlates with US sentiment
            3. The $16M ad cost vs $32B FTX loss vs 192k Bitcoin millionaires
            4. Infrastructure crash 2022 = scarcity signal; logo reveal 2026 = disgust
            5. Stablecoin growth in Argentina while US rejects crypto
            What mechanism explains these inversions?"""
        )
    ]
    
    results = await asyncio.gather(*research_tasks)
    return results

async def synthesis_agent(research_results: List[str]) -> str:
    """Synthesize research into compressed insights."""
    
    combined_research = "\n\n---\n\n".join(research_results)
    
    synthesis = await call_model(
        "anthropic/claude-3.5-sonnet",
        """You are Matt Levine crossed with a physicist. Write with maximum compression and surprise.
        No AI tells: no em-dashes, no 'moreover', no 'fundamentally', no balanced views.
        Write sentences that couldn't be written about anything else.
        Every paragraph should contain a mechanism or number that surprises.""",
        f"""Synthesize this research into the REAL story of why Coinbase Super Bowl failed.
        
        Research findings:
        {combined_research}
        
        Write 1000 words max. Start with the most surprising mechanism.
        No throat-clearing. No narrative arc. Just mechanisms and surprises.
        The reader should think 'I never would have connected that' at least 5 times."""
    )
    
    return synthesis

async def voice_editor(draft: str) -> str:
    """Remove AI tells and maximize genuine voice."""
    
    edited = await call_model(
        "mistralai/mistral-large",
        """You are an editor who removes AI slop. Your job:
        1. Kill every em-dash that isn't essential
        2. Remove all transition words (moreover, furthermore, indeed)
        3. Delete any sentence that could be about something else
        4. Compress ruthlessly - if it takes 10 words, use 5
        5. Make sure every sentence earns its place through specificity""",
        f"""Edit this to remove ALL AI tells:
        
        {draft}
        
        Return only the edited version. Make it impossible to detect as AI-written."""
    )
    
    return edited

async def run_pipeline():
    """Run the full multi-agent pipeline."""
    
    print("Stage 1: Research swarm running...")
    research = await research_agent_swarm()
    
    print("\nStage 2: Synthesizing insights...")
    synthesis = await synthesis_agent(research)
    
    print("\nStage 3: Voice editing...")
    final = await voice_editor(synthesis)
    
    return final

async def main():
    """Run pipeline and save output."""
    
    print("Running Coinbase Super Bowl multi-agent pipeline...\n")
    
    article = await run_pipeline()
    
    # Save the output
    with open("/Users/001/Dev/writing-improver/content/08-coinbase-pipeline-output.md", "w") as f:
        f.write("# Coinbase Super Bowl: Pipeline Output\n\n")
        f.write(article)
    
    print("\n\nArticle generated and saved to content/08-coinbase-pipeline-output.md")
    print("\nFirst 500 characters:")
    print(article[:500])

if __name__ == "__main__":
    asyncio.run(main())