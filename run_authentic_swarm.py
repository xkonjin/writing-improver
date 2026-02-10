#!/usr/bin/env python3
"""
Run the Authentic Voice Swarm - Fixed version that produces genuine voice.
Addresses root causes:
1. No templates in prompts
2. High temperature for creativity  
3. No fallbacks preserving diversity
4. Deep pattern detection
"""

import asyncio
import sys
import os
from datetime import datetime
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.agents.authentic_swarm import AuthenticSwarm

async def run_swarm_on_topic(topic: str):
    """Run authentic swarm on a specific topic."""
    
    print(f"\n{'='*60}")
    print(f"🚀 AUTHENTIC VOICE SWARM PIPELINE")
    print(f"{'='*60}")
    print(f"Topic: {topic}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")
    
    # Initialize swarm with API key
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ Error: OPENROUTER_API_KEY not found in environment")
        print("Add to ~/.env or export OPENROUTER_API_KEY=sk-or-...")
        return None
    
    try:
        swarm = AuthenticSwarm(api_key=api_key)
        
        # Run the pipeline
        result = await swarm.run_authentic_pipeline(topic)
        
        # Save outputs
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save discoveries
        discoveries_path = f"content/authentic_{timestamp}_discoveries.md"
        with open(discoveries_path, "w") as f:
            f.write(f"# Authentic Voice Discoveries\n")
            f.write(f"*Generated: {timestamp}*\n")
            f.write(f"*Topic: {topic}*\n\n")
            
            for discovery in result["discoveries"]:
                f.write(f"## {discovery.agent_name} ({discovery.model})\n\n")
                if discovery.error:
                    f.write(f"*Error: {discovery.error}*\n\n")
                else:
                    f.write(f"{discovery.content}\n\n")
                f.write("---\n\n")
        
        # Save synthesis
        synthesis_path = f"content/authentic_{timestamp}_synthesis.md"
        with open(synthesis_path, "w") as f:
            f.write(f"# Collision Synthesis\n")
            f.write(f"*Generated: {timestamp}*\n")
            f.write(f"*Model: {result['synthesis'].model}*\n\n")
            f.write(result['synthesis'].content)
        
        # Save final output
        final_path = f"content/authentic_{timestamp}_final.md"
        with open(final_path, "w") as f:
            f.write(f"# {topic}\n\n")
            f.write(f"*Generated via Authentic Voice Pipeline - {timestamp}*\n\n")
            f.write("---\n\n")
            f.write(result['final'])
            f.write("\n\n---\n\n")
            f.write("## Pipeline Metrics\n\n")
            f.write(f"- **Tokens Used**: {result['metrics']['tokens_used']:,}\n")
            f.write(f"- **Diversity Score**: {result['metrics']['diversity_score']:.1%}\n")
            f.write(f"- **Success Rate**: {result['metrics']['success_rate']:.1%}\n")
            f.write(f"- **Models Used**: {', '.join(result['metrics']['models_used'])}\n")
        
        print(f"\n✅ SUCCESS! Files saved:")
        print(f"  - {discoveries_path}")
        print(f"  - {synthesis_path}")
        print(f"  - {final_path}")
        
        print(f"\n📊 Metrics:")
        print(f"  - Tokens: {result['metrics']['tokens_used']:,}")
        print(f"  - Diversity: {result['metrics']['diversity_score']:.1%}")
        print(f"  - Success Rate: {result['metrics']['success_rate']:.1%}")
        
        return result
        
    except Exception as e:
        print(f"\n❌ Pipeline failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

def main():
    """Main entry point."""
    
    # Default topics for testing
    test_topics = [
        "Why Coinbase's Super Bowl karaoke ad was genius hiding as cringe",
        "The real mechanism behind venture capital meditation app acquisitions",
        "How TikTok's algorithm creates physical addiction patterns",
        "Why every startup founder is suddenly getting a executive coach"
    ]
    
    # Get topic from command line or use default
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
    else:
        print("Available test topics:")
        for i, t in enumerate(test_topics, 1):
            print(f"  {i}. {t}")
        
        choice = input(f"\nSelect topic (1-{len(test_topics)}) or enter custom: ").strip()
        
        if choice.isdigit() and 1 <= int(choice) <= len(test_topics):
            topic = test_topics[int(choice) - 1]
        elif choice:
            topic = choice
        else:
            topic = test_topics[0]
    
    print(f"\n🎯 Selected topic: {topic}")
    
    # Run the swarm
    result = asyncio.run(run_swarm_on_topic(topic))
    
    if result:
        print(f"\n{'='*60}")
        print("📄 FINAL OUTPUT PREVIEW (first 500 chars):")
        print(f"{'='*60}")
        print(result['final'][:500])
        if len(result['final']) > 500:
            print(f"... [{len(result['final'])-500} more characters]")
        print(f"{'='*60}\n")

if __name__ == "__main__":
    main()