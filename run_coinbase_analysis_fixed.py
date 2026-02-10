#!/usr/bin/env python3
"""
Run Coinbase Super Bowl analysis with working OpenRouter API.
Conservative approach to avoid rate limits.
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

async def main():
    """Run conservative Coinbase analysis."""
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting Coinbase analysis with working API...")
    
    # Initialize swarm
    swarm = OpenRouterSwarm()
    
    topic = "Why did everyone hate the Coinbase Super Bowl ad with the Backstreet Boys karaoke in 2026"
    
    try:
        # Run with reduced agents to conserve API calls
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting research phase (3 agents)...")
        research = await swarm.research_swarm(topic, num_agents=3)
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Research completed. {len(research)} results.")
        
        # Save research
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        research_file = f"content/coinbase_research_{timestamp}.md"
        
        with open(research_file, 'w') as f:
            f.write("# Coinbase Super Bowl Ad Research Results\n\n")
            for i, result in enumerate(research, 1):
                if not result.error:
                    f.write(f"## Agent {i}: {result.agent_name}\n")
                    f.write(f"**Model**: {result.model}\n")
                    f.write(f"**Tokens**: {result.tokens_used}\n\n")
                    f.write(f"{result.content}\n\n---\n\n")
                else:
                    f.write(f"## Agent {i}: ERROR\n")
                    f.write(f"**Model**: {result.model}\n")
                    f.write(f"**Error**: {result.error}\n\n---\n\n")
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Research saved to {research_file}")
        
        # Synthesis
        if any(not r.error for r in research):
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting synthesis...")
            synthesis = await swarm.synthesis_swarm(research)
            
            if not synthesis.error:
                synthesis_file = f"content/coinbase_synthesis_{timestamp}.md"
                with open(synthesis_file, 'w') as f:
                    f.write("# Coinbase Analysis Synthesis\n\n")
                    f.write(f"**Model**: {synthesis.model}\n")
                    f.write(f"**Tokens**: {synthesis.tokens_used}\n\n")
                    f.write(synthesis.content)
                
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Synthesis saved to {synthesis_file}")
                
                # Final article
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Creating final article...")
                final = await swarm.editor_swarm(synthesis.content)
                
                final_file = f"content/coinbase_final_{timestamp}.md"
                with open(final_file, 'w') as f:
                    f.write("# Why Everyone Hated the Coinbase Super Bowl Ad\n")
                    f.write(f"*Generated via OpenRouter multi-agent swarm - {timestamp}*\n\n")
                    f.write(final)
                
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Final article saved to {final_file}")
                
                # Token usage
                total_tokens = sum(r.tokens_used for r in research if not r.error) + synthesis.tokens_used
                print(f"\n✅ Analysis complete!")
                print(f"📊 Total tokens used: {total_tokens}")
                print(f"💰 Estimated cost: ~${total_tokens * 0.00003:.4f}")
                
            else:
                print(f"❌ Synthesis failed: {synthesis.error}")
        else:
            print("❌ All research agents failed")
            
    except Exception as e:
        print(f"❌ Pipeline failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())