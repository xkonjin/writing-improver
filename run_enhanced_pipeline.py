#!/usr/bin/env python3
"""
Enhanced multi-agent pipeline that generates full-length articles.
Uses diverse models via OpenRouter for maximum insight density.
"""

import asyncio
import httpx
import json
import random
from typing import List, Dict, Any

OPENROUTER_API_KEY = "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"

# Model pool for diversity
RESEARCH_MODELS = [
    "anthropic/claude-3.5-sonnet",
    "google/gemini-pro-1.5", 
    "meta-llama/llama-3.1-405b-instruct",
    "openai/gpt-4-turbo-preview",
    "mistralai/mistral-large",
    "deepseek/deepseek-chat"
]

async def call_model(model: str, system: str, user: str, temperature: float = 0.8, max_tokens: int = 4000) -> str:
    """Call a specific model via OpenRouter."""
    async with httpx.AsyncClient(timeout=120.0) as client:
        try:
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
                    "max_tokens": max_tokens
                }
            )
            result = response.json()
            if "choices" in result:
                return result["choices"][0]["message"]["content"]
            else:
                print(f"Error from {model}: {result}")
                # Fallback to Claude
                return await call_model("anthropic/claude-3.5-sonnet", system, user, temperature, max_tokens)
        except Exception as e:
            print(f"Exception with {model}: {e}")
            # Fallback
            if model != "anthropic/claude-3.5-sonnet":
                return await call_model("anthropic/claude-3.5-sonnet", system, user, temperature, max_tokens)
            return f"Error: {e}"

async def deep_research_phase():
    """Phase 1: Deep multi-perspective research."""
    
    perspectives = [
        {
            "model": "anthropic/claude-3.5-sonnet",
            "role": "Neurological mechanism hunter",
            "prompt": """Find the exact neurological and psychological mechanisms behind the Coinbase Super Bowl failure:
            
            1. The neuroscience of collective booing - which brain regions activate during group rejection
            2. Mirror neuron contagion in crowds - how rejection spreads below conscious awareness  
            3. Betrayal aversion vs loss aversion - why crypto triggers disgust not just loss
            4. Nostalgia + finance = violation - the specific neural circuits this breaks
            5. The 'vibe purchase' failure mechanism - why abstract value claims fail
            
            Find specific studies, brain regions, neurotransmitters. No narratives."""
        },
        {
            "model": "google/gemini-pro-1.5",
            "role": "Data anomaly detector",
            "prompt": """Find the surprising data inversions in the Coinbase story:
            
            1. 2022: 20M scans, app crash = success story. 2026: Perfect tech, crowd rejection = failure
            2. Super Bowl viewers (age 49, $75K) vs crypto owners (age 31, $111K) vs actual holdings ($597 median)
            3. American rejection (-67%) vs Nigerian adoption ($92B P2P) - the exact inversion point
            4. 192,205 Bitcoin millionaires vs 123.7M viewers - the visibility threshold problem
            5. Stablecoin growth (318B) during crypto hatred peak - the mechanism disconnect
            
            Find the mathematical relationships between these inversions."""
        },
        {
            "model": "meta-llama/llama-3.1-405b-instruct", 
            "role": "Historical pattern matcher",
            "prompt": """Find exact historical parallels to the Coinbase failure mechanism:
            
            1. Enron's 2000 Super Bowl ad before collapse - the hubris signal pattern
            2. Pets.com sock puppet 1999 - whimsy replacing fundamentals
            3. E*Trade baby 2008 - finance + entertainment before crisis
            4. Theranos ads 2014 - revolutionary claims without product
            5. Wells Fargo 2016 "Together we'll go far" during fraud scandal
            
            What's the exact pattern? When does financial advertising trigger backlash?"""
        },
        {
            "model": "openai/gpt-4-turbo-preview",
            "role": "Crowd dynamics physicist", 
            "prompt": """Model the booing as a phase transition:
            
            1. Critical mass theory - at what percentage does individual rejection become collective?
            2. The 7% threshold - why this specific number triggers cascade
            3. Emotional contagion velocity - how fast does rejection spread in crowds?
            4. The karaoke visibility problem - forced participation vs private choice
            5. Status competition dynamics - zero-sum wealth display mechanics
            
            Find the physics. This is about crowd crystallization, not psychology."""
        },
        {
            "model": "deepseek/deepseek-chat",
            "role": "Mechanism extractor",
            "prompt": """Extract the core mechanisms without any narrative:
            
            QR code 2022: Mystery → Curiosity → Private action → Scarcity signal → FOMO
            Karaoke 2026: Recognition → Forced choice → Public display → Status threat → Rejection
            
            Why does private exploration work but public participation fail?
            What's the mechanism where wealth display triggers opposition past 7% visibility?
            How does nostalgic music + financial product = neural violation?
            
            Just mechanisms. No story."""
        }
    ]
    
    tasks = [call_model(p["model"], f"You are a {p['role']}. Be specific, use numbers, find mechanisms.", p["prompt"], 0.7, 3000) 
             for p in perspectives]
    
    results = await asyncio.gather(*tasks)
    return results

async def synthesis_phase(research: List[str]):
    """Phase 2: Synthesize into surprising insights."""
    
    combined = "\n\n=== RESEARCH FINDING ===\n\n".join(research)
    
    synthesis_prompt = f"""You have research from 5 different agents. Synthesize into the REAL story.

{combined}

Write 1500 words. Rules:
1. Start with the most surprising mechanism
2. Every paragraph must contain a number or specific mechanism  
3. No transitions, no narratives, no em-dashes
4. Write sentences that could ONLY be about this specific event
5. The reader should think "I never realized that" at least 7 times
6. Use short paragraphs, vary sentence length wildly
7. End with a prediction based on the mechanism you discovered

Do not write "The Coinbase ad failed because..." Just start with the mechanism."""

    synthesis = await call_model(
        "anthropic/claude-3.5-sonnet",
        "You write like Matt Levine if he was also a neuroscientist. Maximum surprise per word.",
        synthesis_prompt,
        0.8,
        2000
    )
    
    return synthesis

async def voice_refinement(draft: str):
    """Phase 3: Multiple editing passes for voice."""
    
    # First pass: Remove AI tells
    pass1 = await call_model(
        "mistralai/mistral-large",
        "You are an AI tell exterminator.",
        f"""Remove every AI tell from this text:
        - Kill unnecessary em-dashes
        - Remove moreover, furthermore, indeed, crucially, fundamentally
        - Delete any sentence that sounds like it's teaching
        - Compress by 20% without losing specificity
        
        Text:
        {draft}
        
        Return only edited text.""",
        0.6,
        2000
    )
    
    # Second pass: Maximize compression
    pass2 = await call_model(
        "deepseek/deepseek-chat", 
        "You maximize information density.",
        f"""Increase the insight-per-word ratio:
        - If something takes 10 words, say it in 5
        - Remove every word that doesn't add specific information
        - Keep all numbers and mechanisms
        - Make sentences impossible to skim
        
        Text:
        {pass1}
        
        Return compressed version.""",
        0.7,
        1800
    )
    
    return pass2

async def run_enhanced_pipeline():
    """Run the full enhanced pipeline."""
    
    print("Phase 1: Deep research swarm (5 agents)...")
    research = await deep_research_phase()
    
    print("Phase 2: Synthesis...")
    synthesis = await synthesis_phase(research)
    
    print("Phase 3: Voice refinement...")
    final = await voice_refinement(synthesis)
    
    return final

async def main():
    """Run pipeline and save output."""
    
    print("Running Enhanced Coinbase Pipeline\n")
    print("=" * 50)
    
    article = await run_enhanced_pipeline()
    
    # Save the output
    with open("/Users/001/Dev/writing-improver/content/09-coinbase-enhanced.md", "w") as f:
        f.write("# Why Everyone Hated the Coinbase Super Bowl Ad\n\n")
        f.write(article)
    
    print("\n" + "=" * 50)
    print("Article saved to content/09-coinbase-enhanced.md")
    print(f"\nWord count: {len(article.split())}")
    print("\nFirst 300 characters:")
    print(article[:300] + "...")

if __name__ == "__main__":
    asyncio.run(main())