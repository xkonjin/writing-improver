#!/usr/bin/env python3
"""
Run Coinbase analysis with web search context injection.
Provides current news context to OpenRouter models.
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

from agents.openrouter_swarm import OpenRouterSwarm

# Search results context (from your WebSearch)
SEARCH_CONTEXT = """
REAL 2026 COINBASE SUPER BOWL AD FACTS:
- Coinbase DID air a Super Bowl 2026 ad featuring Backstreet Boys karaoke
- Used "Everybody (Backstreet's Back)" with lo-fi karaoke-style subtitles  
- Basic computer animation, bright blue backdrop
- Ended with "Coinbase" and "Crypto. For Everybody"
- Viewers at Super Bowl parties BOOED when Coinbase name appeared
- Social media reported "rooms burst into groans and shouts of 'f**k you'"
- Called "textbook example of scaring the hoes"
- Described as "really fun until it wasn't"
- Created confusion because T-Mobile also used Backstreet Boys in same game
- Critics called it "bait-and-switch" and "emotional hijacking"
- Coinbase CMO said it was designed to grab attention vs polished Super Bowl ads
- CEO Brian Armstrong called it "antidote to polarization"  
- Company defended with "If you're talking about it, it worked"
"""

async def main():
    """Run Coinbase analysis with search context."""
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting Coinbase analysis with search context...")
    
    # Initialize swarm
    swarm = OpenRouterSwarm()
    
    topic_with_context = f"""Analyze this topic with the following VERIFIED FACTS:

{SEARCH_CONTEXT}

Research question: Why did everyone hate the Coinbase Super Bowl 2026 Backstreet Boys karaoke ad?

Use the facts above as your foundation. Find the mechanisms behind the hatred."""
    
    try:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting research with search context...")
        research = await swarm.research_swarm(topic_with_context, num_agents=3)
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Research completed.")
        
        # Save research
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        research_file = f"content/coinbase_search_research_{timestamp}.md"
        
        with open(research_file, 'w') as f:
            f.write("# Coinbase Super Bowl 2026 Research (With Search Context)\n\n")
            f.write(f"## Search Context Used:\n{SEARCH_CONTEXT}\n\n")
            for i, result in enumerate(research, 1):
                if not result.error:
                    f.write(f"## Agent {i}: {result.agent_name}\n")
                    f.write(f"**Model**: {result.model}\n")
                    f.write(f"**Tokens**: {result.tokens_used}\n\n")
                    f.write(f"{result.content}\n\n---\n\n")
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Research saved to {research_file}")
        
        # Synthesis
        if any(not r.error for r in research):
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting synthesis...")
            synthesis = await swarm.synthesis_swarm(research)
            
            if not synthesis.error:
                synthesis_file = f"content/coinbase_search_synthesis_{timestamp}.md"
                with open(synthesis_file, 'w') as f:
                    f.write("# Coinbase 2026 Analysis Synthesis (With Search)\n\n")
                    f.write(synthesis.content)
                
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Synthesis saved to {synthesis_file}")
                
                # Final article
                final = await swarm.editor_swarm(synthesis.content)
                final_file = f"content/coinbase_search_final_{timestamp}.md"
                with open(final_file, 'w') as f:
                    f.write("# Why Everyone Hated the Coinbase Super Bowl Ad\n")
                    f.write(f"*Generated with search context - {timestamp}*\n\n")
                    f.write(final)
                
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Final article: {final_file}")
                
            else:
                print(f"❌ Synthesis failed: {synthesis.error}")
        else:
            print("❌ All research agents failed")
            
    except Exception as e:
        print(f"❌ Pipeline failed: {e}")

if __name__ == "__main__":
    asyncio.run(main())