#!/usr/bin/env python3
"""
Simple Perplexity-based live search analysis.
Uses Perplexity's native search capabilities for current data.
"""

import asyncio
import httpx
import os
from datetime import datetime
from dotenv import load_dotenv
import json

load_dotenv()

async def call_perplexity(query: str, model: str = "perplexity/sonar-pro") -> dict:
    """Call Perplexity with live search."""
    
    api_key = os.getenv("OPENROUTER_API_KEY")
    
    async with httpx.AsyncClient(timeout=120.0) as client:
        try:
            response = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": model,
                    "messages": [
                        {"role": "user", "content": query}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 2000
                }
            )
            
            result = response.json()
            return result
            
        except Exception as e:
            return {"error": str(e)}

async def main():
    """Run Perplexity analysis."""
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting Perplexity live search analysis...")
    
    queries = [
        "Coinbase Super Bowl 2026 Backstreet Boys karaoke ad controversy - what was the specific negative reaction and why did people hate it?",
        
        "Super Bowl 2026 Coinbase ad viewer reactions booing social media response - find specific statistics and sentiment data",
        
        "Coinbase Super Bowl 60 ad Backstreet Boys Everybody karaoke commercial failure analysis - what mechanisms caused the hatred?",
    ]
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = f"content/perplexity_coinbase_{timestamp}.md"
    
    with open(results_file, 'w') as f:
        f.write("# Coinbase Super Bowl 2026 - Live Perplexity Analysis\n\n")
        f.write(f"**Analysis Time**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for i, query in enumerate(queries, 1):
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Query {i}/3...")
            
            result = await call_perplexity(query)
            
            if "choices" in result:
                content = result["choices"][0]["message"]["content"]
                citations = result.get("citations", [])
                
                f.write(f"## Query {i}\n")
                f.write(f"**Question**: {query}\n\n")
                f.write(f"{content}\n\n")
                
                if citations:
                    f.write("**Sources**:\n")
                    for j, cite in enumerate(citations, 1):
                        f.write(f"{j}. {cite}\n")
                f.write("\n---\n\n")
                
            else:
                f.write(f"## Query {i} - ERROR\n")
                f.write(f"**Question**: {query}\n")
                f.write(f"**Error**: {result}\n\n---\n\n")
            
            # Rate limiting
            await asyncio.sleep(3)
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Analysis saved to {results_file}")
    
    # Create synthesis
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Creating synthesis...")
    
    synthesis_query = """Based on current 2026 data about Coinbase's Super Bowl Backstreet Boys karaoke ad:

1. What was the specific mechanism that caused widespread hatred?
2. What were the exact viewer reactions and statistics?
3. How did the karaoke format contribute to the backlash?
4. What underlying psychological or cultural factors explain the intensity of negative response?

Synthesize into core mechanisms with specific current data."""
    
    synthesis = await call_perplexity(synthesis_query)
    
    synthesis_file = f"content/perplexity_synthesis_{timestamp}.md"
    
    with open(synthesis_file, 'w') as f:
        f.write("# Coinbase Super Bowl 2026 - Synthesis Analysis\n\n")
        
        if "choices" in synthesis:
            content = synthesis["choices"][0]["message"]["content"]
            citations = synthesis.get("citations", [])
            
            f.write(f"{content}\n\n")
            
            if citations:
                f.write("## Sources Referenced:\n")
                for i, cite in enumerate(citations, 1):
                    f.write(f"{i}. {cite}\n")
        else:
            f.write(f"**Error**: {synthesis}\n")
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Synthesis saved to {synthesis_file}")
    print("✅ Live Perplexity analysis complete!")

if __name__ == "__main__":
    asyncio.run(main())