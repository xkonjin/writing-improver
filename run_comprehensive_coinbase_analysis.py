#!/usr/bin/env python3
"""
Comprehensive deep dive analysis of Coinbase Super Bowl 2026 ad controversy.
Uses multiple Perplexity queries and synthesis for maximum insight depth.
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
    
    async with httpx.AsyncClient(timeout=180.0) as client:
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
                    "max_tokens": 3000
                }
            )
            
            result = response.json()
            return result
            
        except Exception as e:
            return {"error": str(e)}

async def main():
    """Run comprehensive deep dive analysis."""
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting comprehensive Coinbase analysis...")
    
    # Deep dive research queries
    research_queries = [
        """Coinbase Super Bowl 2026 Backstreet Boys karaoke ad - find specific viewer reactions, social media data, sentiment analysis, and statistics about the backlash. What were the exact mechanisms of hatred?""",
        
        """Super Bowl 2026 Coinbase ad performance metrics - find viewership data, engagement statistics, stock price impact, website traffic, conversion rates, and business outcomes from the controversial ad""",
        
        """Coinbase Super Bowl 60 karaoke commercial psychological analysis - why did the Backstreet Boys format trigger negative reactions? Find expert analysis on nostalgia manipulation, crypto brand perception, and audience psychology""",
        
        """Super Bowl 2026 advertising analysis - how did Coinbase's karaoke ad compare to other ads? Find industry expert opinions, creative reviews, and contextual analysis of crypto advertising trends""",
        
        """Coinbase brand strategy 2026 - find company statements, CMO interviews, CEO responses about the Super Bowl ad strategy, and how it fits their broader marketing approach and crypto industry positioning"""
    ]
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    comprehensive_file = f"content/coinbase_comprehensive_{timestamp}.md"
    
    all_sources = []
    
    with open(comprehensive_file, 'w') as f:
        f.write("# Coinbase Super Bowl 2026 - Comprehensive Deep Dive Analysis\n\n")
        f.write(f"**Analysis Time**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Research Depth**: {len(research_queries)} specialized query phases\n\n")
        
        for i, query in enumerate(research_queries, 1):
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Deep dive phase {i}/{len(research_queries)}...")
            
            result = await call_perplexity(query)
            
            if "choices" in result:
                content = result["choices"][0]["message"]["content"]
                citations = result.get("citations", [])
                usage = result.get("usage", {})
                
                f.write(f"## Research Phase {i}: Specialized Analysis\n")
                f.write(f"**Query**: {query}\n")
                f.write(f"**Model**: perplexity/sonar-pro\n")
                f.write(f"**Tokens**: {usage.get('total_tokens', 'N/A')}\n\n")
                
                f.write(f"{content}\n\n")
                
                if citations:
                    f.write("### Sources Referenced:\n")
                    for j, cite in enumerate(citations, 1):
                        f.write(f"{j}. {cite}\n")
                        all_sources.append(cite)
                    f.write("\n")
                
                f.write("---\n\n")
                
            else:
                f.write(f"## Research Phase {i} - ERROR\n")
                f.write(f"**Query**: {query}\n")
                f.write(f"**Error**: {result}\n\n---\n\n")
            
            # Rate limiting
            await asyncio.sleep(4)
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Research complete. Creating mega-synthesis...")
    
    # Create comprehensive synthesis
    synthesis_query = f"""Based on comprehensive research into Coinbase's 2026 Super Bowl Backstreet Boys karaoke ad:

SYNTHESIS TASK: Analyze all available data to identify:

1. **Core Hatred Mechanisms**: What specific psychological, cultural, and technical factors caused widespread negative reaction?

2. **Quantified Impact**: Exact statistics on social media sentiment, business metrics, stock impact, and audience response data

3. **Industry Context**: How this fits into crypto advertising trends, Super Bowl ad performance, and brand strategy evolution

4. **Deeper Insights**: Unexpected connections, underlying patterns, and mechanisms that explain the intensity of backlash

5. **Predictive Framework**: What this reveals about crypto marketing, nostalgia advertising, and audience psychology going forward

Generate the deepest possible analysis with specific data points, mechanisms, and insights. Focus on surprise and genuine understanding rather than obvious observations.

Use current 2026 data and cite specific sources."""
    
    synthesis = await call_perplexity(synthesis_query)
    
    synthesis_file = f"content/coinbase_mega_synthesis_{timestamp}.md"
    
    with open(synthesis_file, 'w') as f:
        f.write("# Coinbase Super Bowl 2026 - Mega Synthesis Analysis\n\n")
        f.write(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Total Sources**: {len(set(all_sources))}\n")
        f.write(f"**Analysis Depth**: Multi-phase comprehensive research\n\n")
        
        if "choices" in synthesis:
            content = synthesis["choices"][0]["message"]["content"]
            citations = synthesis.get("citations", [])
            
            f.write(f"{content}\n\n")
            
            if citations:
                f.write("## Key Sources Referenced:\n")
                for i, cite in enumerate(citations, 1):
                    f.write(f"{i}. {cite}\n")
            
            # Add all sources from research
            unique_sources = list(set(all_sources))
            if unique_sources:
                f.write(f"\n## All Research Sources ({len(unique_sources)} total):\n")
                for i, source in enumerate(unique_sources, 1):
                    f.write(f"{i}. {source}\n")
        else:
            f.write(f"**Synthesis Error**: {synthesis}\n")
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Comprehensive analysis saved:")
    print(f"📊 Research file: {comprehensive_file}")
    print(f"🎯 Synthesis file: {synthesis_file}")
    print(f"🔍 Total unique sources: {len(set(all_sources))}")
    print("✅ Deep dive analysis complete!")

if __name__ == "__main__":
    asyncio.run(main())