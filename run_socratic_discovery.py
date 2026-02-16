#!/usr/bin/env python3
"""Run Socratic Bottom-Up Discovery Pipeline.

Pure discovery process:
1. Socratic questioning to depth
2. Multi-lens research (Paul Graham, Taleb, Matt Levine styles)  
3. Contradiction finding
4. Kolmogorov compression
5. Emergent thesis
6. Maximum-density writing
"""

import asyncio
import json
import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

from src.agents.socratic_bottom_up_swarm import SocraticBottomUpSwarm
from src.agents.openrouter_swarm import OpenRouterSwarm


async def main():
    """Run Socratic discovery process."""
    
    load_dotenv()
    
    # Configuration
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ OPENROUTER_API_KEY not set")
        return
    
    topic = os.getenv("SWARM_TOPIC", "Why Silicon Valley stopped building things")
    
    print("=" * 80)
    print("🔬 SOCRATIC BOTTOM-UP DISCOVERY SYSTEM")
    print("=" * 80)
    print(f"📝 Topic: {topic}")
    print(f"⏰ Started: {datetime.now().isoformat()}")
    print()
    
    # Initialize
    swarm = OpenRouterSwarm(api_key=api_key)
    
    # Test API key
    if not await swarm.test_api_key():
        print("❌ API key validation failed")
        return
    
    # Configure Socratic system
    socratic = SocraticBottomUpSwarm(
        swarm=swarm,
        max_socratic_depth=5,
        compression_target=10.0,
        writer_styles=[
            "paul_graham",      # First principles
            "nassim_taleb",     # Antifragility  
            "matt_levine",      # Absurdity
            "patrick_mckenzie", # Hidden systems
            "byrne_hobart",     # Historical rhymes
            "venkatesh_rao"     # 2x2 matrices
        ]
    )
    
    # Run discovery
    print("🚀 Starting Socratic Discovery Pipeline...")
    print()
    
    result = await socratic.run(topic)
    
    # Display results
    print("\n" + "=" * 80)
    print("📊 DISCOVERY RESULTS")
    print("=" * 80)
    
    print(f"\n📈 Compression Score: {result.compression_score:.1f}:1")
    print(f"🔍 Socratic Depth: {len(result.socratic_chain)} levels")
    print(f"💡 Deep Insights: {len(result.deep_insights)} compressed insights")
    print(f"📚 Raw Discoveries: {len(result.raw_discoveries)} research artifacts")
    
    # Show Socratic chain
    print("\n🤔 SOCRATIC CHAIN:")
    print("-" * 40)
    for i, q in enumerate(result.socratic_chain[:3], 1):
        print(f"\nLevel {q.depth}: {q.question}")
        print(f"  → Reveals: {q.reveals[:80]}...")
        print(f"  → Contradicts: {q.contradicts[:80]}...")
    
    # Show top insights by compression
    print("\n🗜️ TOP COMPRESSED INSIGHTS:")
    print("-" * 40)
    for i, insight in enumerate(result.deep_insights[:3], 1):
        print(f"\n{i}. {insight.insight}")
        print(f"   Compression: {insight.compression_ratio:.1f}:1")
        print(f"   Kolmogorov length: {insight.kolmogorov_length} words")
        if insight.predictions:
            print(f"   Predicts: {insight.predictions[0][:80]}...")
    
    # Show emergent thesis
    print("\n🌱 EMERGENT THESIS:")
    print("-" * 40)
    print(result.emergent_thesis)
    
    # Save outputs
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path("content")
    output_dir.mkdir(exist_ok=True)
    
    # Save article
    article_path = output_dir / f"socratic_{timestamp}_final.md"
    with open(article_path, "w") as f:
        f.write(f"# {topic}\n\n")
        f.write(f"## Emergent Thesis\n\n{result.emergent_thesis}\n\n")
        f.write("---\n\n")
        f.write(result.final_article)
        f.write("\n\n---\n\n")
        f.write("## Socratic Discovery Process\n\n")
        f.write(f"- Compression ratio: {result.compression_score:.1f}:1\n")
        f.write(f"- Socratic depth: {len(result.socratic_chain)} levels\n")
        f.write(f"- Deep insights: {len(result.deep_insights)}\n")
        f.write(f"- Research lenses: {len(result.raw_discoveries)}\n")
    
    print(f"\n📄 Article saved: {article_path}")
    
    # Save research artifacts
    research_path = output_dir / f"socratic_{timestamp}_research.json"
    research_data = {
        "topic": result.topic,
        "timestamp": timestamp,
        "compression_score": result.compression_score,
        "emergent_thesis": result.emergent_thesis,
        "socratic_chain": [
            {
                "depth": q.depth,
                "question": q.question,
                "answer": q.answer[:200],
                "reveals": q.reveals,
                "contradicts": q.contradicts
            }
            for q in result.socratic_chain
        ],
        "deep_insights": [
            {
                "insight": ins.insight,
                "compression_ratio": ins.compression_ratio,
                "kolmogorov_length": ins.kolmogorov_length,
                "predictions": ins.predictions[:2]
            }
            for ins in result.deep_insights
        ],
        "discovery_methods": [
            {
                "writer_style": disc.get("writer_style"),
                "question": disc.get("question"),
                "mechanisms_found": len(disc.get("mechanisms", [])),
                "numbers_found": len(disc.get("numbers", [])),
                "contradictions_found": len(disc.get("contradictions", []))
            }
            for disc in result.raw_discoveries
        ]
    }
    
    with open(research_path, "w") as f:
        json.dump(research_data, f, indent=2)
    
    print(f"🔬 Research saved: {research_path}")
    
    # Display article preview
    print("\n" + "=" * 80)
    print("📖 ARTICLE PREVIEW")
    print("=" * 80)
    preview_length = min(len(result.final_article), 800)
    print(result.final_article[:preview_length])
    if len(result.final_article) > preview_length:
        print("\n[...]")
    
    # Show discovery stats
    print("\n" + "=" * 80)
    print("📊 DISCOVERY STATISTICS")
    print("=" * 80)
    
    total_mechanisms = sum(
        len(d.get("mechanisms", [])) 
        for d in result.raw_discoveries
    )
    total_numbers = sum(
        len(d.get("numbers", []))
        for d in result.raw_discoveries  
    )
    total_contradictions = sum(
        len(d.get("contradictions", []))
        for d in result.raw_discoveries
    )
    
    print(f"⚙️  Total mechanisms discovered: {total_mechanisms}")
    print(f"🔢 Total data points found: {total_numbers}")
    print(f"⚡ Total contradictions revealed: {total_contradictions}")
    print(f"📏 Final article length: {len(result.final_article.split())} words")
    print(f"🗜️  Compression achieved: {result.compression_score:.1f}:1")
    
    # Success criteria
    print("\n✅ SUCCESS CRITERIA:")
    if result.compression_score >= 8.0:
        print("  ✓ Compression ratio ≥ 8:1")
    else:
        print(f"  ✗ Compression ratio {result.compression_score:.1f} < 8.0")
    
    if len(result.socratic_chain) >= 3:
        print("  ✓ Socratic depth ≥ 3 levels")
    else:
        print(f"  ✗ Socratic depth {len(result.socratic_chain)} < 3")
    
    if len(result.deep_insights) >= 3:
        print("  ✓ Deep insights ≥ 3")
    else:
        print(f"  ✗ Deep insights {len(result.deep_insights)} < 3")
    
    print("\n✨ Done!")


if __name__ == "__main__":
    asyncio.run(main())