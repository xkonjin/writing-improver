#!/usr/bin/env python3
"""Run the Ultimate Bottom-Up Discovery Pipeline.

This is the complete system:
- Socratic questioning to bedrock
- Writer technique extraction  
- Kolmogorov compression
- Specialized research swarm
- Emergent thesis
- Maximum density writing
- Settlers-quality validation
"""

import asyncio
import json
import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

from src.pipeline.ultimate_bottom_up import UltimateBottomUpPipeline
from src.agents.openrouter_swarm import OpenRouterSwarm


async def main():
    """Run the ultimate discovery pipeline."""
    
    load_dotenv()
    
    # Configuration
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ OPENROUTER_API_KEY not set")
        print("Get one from https://openrouter.ai/keys")
        return
    
    topic = os.getenv(
        "SWARM_TOPIC",
        "Why AI agents will become primary economic actors by 2027"
    )
    
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 20 + "ULTIMATE BOTTOM-UP DISCOVERY" + " " * 30 + "║")
    print("╚" + "═" * 78 + "╝")
    print()
    print(f"📝 Topic: {topic}")
    print(f"⏰ Started: {datetime.now().isoformat()}")
    print()
    
    # Initialize swarm
    swarm = OpenRouterSwarm(api_key=api_key)
    
    # Test API key
    print("Testing API connection...")
    if not await swarm.test_api_key():
        print("❌ API key validation failed")
        return
    print("✅ API connected\n")
    
    # Configure pipeline
    pipeline = UltimateBottomUpPipeline(
        swarm=swarm,
        socratic_depth=5,
        writer_styles=[
            "paul_graham",       # Contradiction hunting
            "nassim_taleb",      # Skin in the game
            "matt_levine",       # Absurdity revelation
            "patrick_mckenzie",  # Infrastructure X-ray
            "byrne_hobart",      # Historical rhyming
            "venkatesh_rao",     # 2x2 thinking
            "tyler_cowen",       # Marginal analysis
            "scott_alexander"    # Bayesian reasoning
        ],
        compression_target=10.0,
        quality_threshold=8.5
    )
    
    # Run discovery
    print("🚀 INITIATING DISCOVERY PIPELINE")
    print("=" * 80)
    
    discovery = await pipeline.discover(topic)
    
    # Display results
    print("\n" + "=" * 80)
    print("📊 DISCOVERY COMPLETE")
    print("=" * 80)
    
    # Metrics
    print("\n📈 METRICS:")
    print(f"  Compression Ratio: {discovery.compression_ratio:.1f}:1")
    print(f"  Insight Density: {discovery.insight_density:.2f} insights/100 words")
    print(f"  Surprisal Score: {discovery.surprisal_score:.2f}/10")
    print(f"  Quality Score: {discovery.quality_score:.1f}/10")
    
    # Socratic depth
    print(f"\n🤔 SOCRATIC DEPTH: {len(discovery.socratic_depth)} levels")
    for q in discovery.socratic_depth[:3]:
        print(f"  L{q.depth}: {q.question[:60]}...")
        print(f"     → {q.reveals[:60]}...")
    
    # Writer techniques
    print(f"\n✍️ WRITER TECHNIQUES FOUND: {len(discovery.writer_techniques_found)}")
    for writer, techniques in list(discovery.writer_techniques_found.items())[:3]:
        print(f"  {writer}: {', '.join(techniques[:2])}")
    
    # Kolmogorov insights
    print(f"\n🗜️ TOP COMPRESSED INSIGHTS:")
    for i, insight in enumerate(discovery.kolmogorov_insights[:3], 1):
        print(f"  {i}. {insight.core_statement}")
        print(f"     Compression: {insight.compression_ratio:.0f}:1")
        print(f"     Prediction: {insight.falsifiable_prediction[:60]}...")
    
    # Contradictions
    print(f"\n⚡ CONTRADICTIONS FOUND: {len(discovery.contradictions_found)}")
    for contradiction in discovery.contradictions_found[:2]:
        print(f"  • {contradiction[:80]}...")
    
    # Mechanisms
    print(f"\n⚙️ MECHANISMS EXTRACTED: {len(discovery.mechanisms_extracted)}")
    for mechanism in discovery.mechanisms_extracted[:3]:
        print(f"  • {mechanism[:80]}...")
    
    # Emergent thesis
    print(f"\n🌱 EMERGENT THESIS:")
    print(f"  {discovery.emergent_thesis}")
    
    # Settlers validation
    print(f"\n✅ SETTLERS VALIDATION:")
    val = discovery.settlers_validation
    print(f"  Mechanisms: {val.get('mechanisms', 0)}/7")
    print(f"  Inversions: {val.get('inversions', 0)}/3")
    print(f"  Predictions: {val.get('predictions', 0)}/3")
    print(f"  Passed: {'✅' if val.get('passed', False) else '❌'}")
    
    if val.get('failures'):
        print(f"  Issues: {', '.join(val['failures'][:3])}")
    
    # Save outputs
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path("content")
    output_dir.mkdir(exist_ok=True)
    
    # Save article
    article_path = output_dir / f"ultimate_{timestamp}_final.md"
    with open(article_path, "w") as f:
        f.write(f"# {topic}\n\n")
        f.write(f"*Emergent Thesis: {discovery.emergent_thesis}*\n\n")
        f.write("---\n\n")
        f.write(discovery.final_article)
        f.write("\n\n---\n\n")
        f.write("## Discovery Metrics\n\n")
        f.write(f"- **Compression**: {discovery.compression_ratio:.1f}:1\n")
        f.write(f"- **Insight Density**: {discovery.insight_density:.2f}/100 words\n")
        f.write(f"- **Surprisal**: {discovery.surprisal_score:.2f}/10\n")
        f.write(f"- **Quality**: {discovery.quality_score:.1f}/10\n")
        f.write(f"- **Socratic Depth**: {len(discovery.socratic_depth)} levels\n")
        f.write(f"- **Writer Techniques**: {len(discovery.writer_techniques_found)} styles\n")
        f.write(f"- **Mechanisms**: {len(discovery.mechanisms_extracted)}\n")
        f.write(f"- **Contradictions**: {len(discovery.contradictions_found)}\n")
    
    print(f"\n📄 Article saved: {article_path}")
    
    # Save research data
    research_path = output_dir / f"ultimate_{timestamp}_research.json"
    research_data = {
        "topic": discovery.topic,
        "timestamp": timestamp,
        "metrics": {
            "compression_ratio": discovery.compression_ratio,
            "insight_density": discovery.insight_density,
            "surprisal_score": discovery.surprisal_score,
            "quality_score": discovery.quality_score
        },
        "socratic_chain": [
            {
                "depth": q.depth,
                "question": q.question,
                "reveals": q.reveals,
                "contradicts": q.contradicts
            }
            for q in discovery.socratic_depth
        ],
        "writer_techniques": discovery.writer_techniques_found,
        "kolmogorov_insights": [
            {
                "statement": i.core_statement,
                "compression": i.compression_ratio,
                "prediction": i.falsifiable_prediction,
                "surprisal": i.surprisal_score
            }
            for i in discovery.kolmogorov_insights[:10]
        ],
        "mechanisms": discovery.mechanisms_extracted[:20],
        "contradictions": discovery.contradictions_found[:10],
        "emergent_thesis": discovery.emergent_thesis,
        "validation": discovery.settlers_validation
    }
    
    with open(research_path, "w") as f:
        json.dump(research_data, f, indent=2)
    
    print(f"🔬 Research saved: {research_path}")
    
    # Display preview
    print("\n" + "=" * 80)
    print("📖 ARTICLE PREVIEW")
    print("=" * 80)
    
    preview = discovery.final_article[:1000]
    print(preview)
    if len(discovery.final_article) > 1000:
        print("\n[...continued...]")
    
    # Final summary
    print("\n" + "=" * 80)
    print("🎯 SUMMARY")
    print("=" * 80)
    
    word_count = len(discovery.final_article.split())
    print(f"Generated {word_count}-word article")
    print(f"Compression: {discovery.compression_ratio:.1f}:1")
    print(f"Quality: {discovery.quality_score:.1f}/10")
    
    if discovery.quality_score >= 8.5:
        print("\n✨ SETTLERS QUALITY ACHIEVED!")
    else:
        print(f"\n⚠️ Quality {discovery.quality_score:.1f} < 8.5 target")
    
    print("\n✅ Discovery complete!")


if __name__ == "__main__":
    asyncio.run(main())