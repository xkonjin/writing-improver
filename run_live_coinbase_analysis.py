#!/usr/bin/env python3
"""
Run Coinbase analysis with live search integration.
Uses Perplexity models, web search, and X API for real-time insights.
"""

import asyncio
import os
import sys
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from agents.live_search_swarm import LiveSearchSwarm

async def main():
    """Run live search Coinbase analysis."""
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting live search Coinbase analysis...")
    
    # Initialize live search swarm
    swarm = LiveSearchSwarm()
    
    topic = "Coinbase Super Bowl 2026 Backstreet Boys karaoke ad controversy hatred negative reaction"
    
    try:
        # Run live search swarm
        results = await swarm.run_live_swarm(topic)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save research results
        research_file = f"content/coinbase_live_research_{timestamp}.md"
        with open(research_file, 'w') as f:
            f.write("# Coinbase Live Search Research Results\n\n")
            f.write(f"**Analysis Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Topic**: {topic}\n\n")
            
            for i, result in enumerate(results["research"], 1):
                if not result.error:
                    f.write(f"## Agent {i}: {result.agent_name}\n")
                    f.write(f"**Model**: {result.model}\n")
                    f.write(f"**Tokens**: {result.tokens_used}\n")
                    
                    if result.search_queries:
                        f.write(f"**Search Queries**: {', '.join(result.search_queries)}\n")
                    
                    if result.sources:
                        f.write(f"**Sources Found**: {len(result.sources)}\n")
                        for j, source in enumerate(result.sources[:5], 1):
                            f.write(f"  {j}. {source.get('title', 'N/A')} - {source.get('url', 'N/A')}\n")
                    
                    f.write(f"\n{result.content}\n\n---\n\n")
                else:
                    f.write(f"## Agent {i}: ERROR\n")
                    f.write(f"**Error**: {result.error}\n\n---\n\n")
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Live research saved to {research_file}")
        
        # Save synthesis
        synthesis = results["synthesis"]
        if not synthesis.error:
            synthesis_file = f"content/coinbase_live_synthesis_{timestamp}.md"
            with open(synthesis_file, 'w') as f:
                f.write("# Coinbase Live Analysis Synthesis\n\n")
                f.write(f"**Model**: {synthesis.model}\n")
                f.write(f"**Tokens**: {synthesis.tokens_used}\n")
                f.write(f"**Total Sources**: {results['total_sources']}\n\n")
                
                if synthesis.sources:
                    f.write("## Key Sources Referenced:\n")
                    for i, source in enumerate(synthesis.sources[:10], 1):
                        f.write(f"{i}. [{source.get('title', 'N/A')}]({source.get('url', '#')})\n")
                    f.write("\n")
                
                f.write(f"{synthesis.content}\n")
            
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Live synthesis saved to {synthesis_file}")
            
            # Create final article
            final_file = f"content/coinbase_live_final_{timestamp}.md"
            with open(final_file, 'w') as f:
                f.write("# Why Everyone Hated the Coinbase Super Bowl Ad\n")
                f.write(f"*Generated via live search swarm - {timestamp}*\n\n")
                f.write("## Analysis Summary\n")
                f.write(f"- **Live research agents**: {len(results['research'])}\n")
                f.write(f"- **Sources analyzed**: {results['total_sources']}\n")
                f.write(f"- **Total tokens**: {results['tokens_used']}\n")
                f.write(f"- **Models used**: Perplexity Sonar, Claude 3.5 Sonnet, GPT-4\n\n")
                f.write("---\n\n")
                f.write(synthesis.content)
            
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Final analysis: {final_file}")
            print(f"\n✅ Live search analysis complete!")
            print(f"📊 Total tokens: {results['tokens_used']}")
            print(f"🔍 Sources analyzed: {results['total_sources']}")
            print(f"💰 Estimated cost: ~${results['tokens_used'] * 0.00005:.4f}")
            
        else:
            print(f"❌ Live synthesis failed: {synthesis.error}")
            
    except Exception as e:
        print(f"❌ Live search pipeline failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())