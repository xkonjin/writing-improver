#!/usr/bin/env python3
"""Run the Extreme Codex Swarm for ultra-high-quality article generation."""

import asyncio
import json
import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

from src.agents.extreme_codex_swarm import ExtremeCodexSwarm
from src.agents.openrouter_swarm import OpenRouterSwarm
from src.quality.settlers_validator import SettlersThresholds


async def main():
    """Run the extreme codex pipeline."""
    
    load_dotenv()
    
    # Get API key
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ OPENROUTER_API_KEY not set in environment")
        print("Get one from https://openrouter.ai/keys")
        return
    
    # Get topic from environment or use default
    topic = os.getenv("SWARM_TOPIC", "The rise of AI agents in 2026: from chatbots to economic actors")
    
    print(f"🚀 Extreme Codex Swarm Pipeline")
    print(f"📝 Topic: {topic}")
    print(f"⏰ Started: {datetime.now().isoformat()}")
    print("=" * 80)
    
    # Initialize swarm and orchestrator
    swarm = OpenRouterSwarm(api_key=api_key)
    
    # Test API key first
    print("Testing API key...")
    if not await swarm.test_api_key():
        print("❌ API key validation failed")
        return
    print("✅ API key validated")
    
    # Configure quality thresholds for Settlers-level quality
    thresholds = SettlersThresholds(
        min_mechanisms=7,      # At least 7 mechanism sentences with thresholds
        min_inversions=3,       # At least 3 inversions with numbers
        min_predictions=3,      # At least 3 falsifiable predictions
        min_inclusion_pronouns=5,  # At least 5 we/us/our instances
        require_confession=True    # Must have confession or admission
    )
    
    # Initialize extreme swarm with high quality target
    extreme_swarm = ExtremeCodexSwarm(
        swarm=swarm,
        thresholds=thresholds,
        max_revision_rounds=5,
        parallel_drafts=5,
        quality_target=8.5  # Target score of 8.5/10
    )
    
    # Run the pipeline
    print("\n🔬 Running Extreme Pipeline...")
    print("  Phase 1: Specialist research agents")
    print("  Phase 2: Mechanism extraction")
    print("  Phase 3: Personal layer building")
    print("  Phase 4: Parallel draft generation")
    print("  Phase 5: Quality evaluation")
    print("  Phase 6: Revision loops")
    print()
    
    result = await extreme_swarm.run(
        topic=topic,
        num_research_agents=10,
        enable_search=False  # Set to True if you have search API configured
    )
    
    # Display results
    print("\n" + "=" * 80)
    print("📊 RESULTS")
    print("=" * 80)
    
    print(f"\n✅ Pipeline completed in {result.elapsed_time:.1f} seconds")
    print(f"📈 Quality Score: {result.quality_metrics.overall_score:.2f}/10")
    print(f"🔄 Revision Rounds: {result.total_attempts}")
    print(f"💾 Tokens Used: {result.tokens_used:,}")
    
    print("\n📋 Quality Metrics:")
    print(f"  - Mechanisms: {result.quality_metrics.settlers.mechanism_count}/{thresholds.min_mechanisms}")
    print(f"  - Inversions: {result.quality_metrics.settlers.inversion_count}/{thresholds.min_inversions}")
    print(f"  - Predictions: {result.quality_metrics.settlers.prediction_count}/{thresholds.min_predictions}")
    print(f"  - Surprise Score: {result.quality_metrics.surprise_score:.2f}")
    print(f"  - Compression Score: {result.quality_metrics.compression_score:.1f}")
    print(f"  - Data Points: {result.quality_metrics.specific_data_count}")
    print(f"  - Named Entities: {result.quality_metrics.named_entities}")
    print(f"  - Personal Touches: {result.quality_metrics.personal_touches}")
    print(f"  - AI Tells (banned words): {result.quality_metrics.banned_words}")
    print(f"  - Em-dashes/1k: {result.quality_metrics.em_dashes_per_1k:.1f}")
    
    if result.quality_metrics.failures:
        print(f"\n⚠️  Remaining Issues:")
        for failure in result.quality_metrics.failures:
            print(f"  - {failure}")
    else:
        print(f"\n✨ All quality checks passed!")
    
    # Save outputs
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path("content")
    output_dir.mkdir(exist_ok=True)
    
    # Save final article
    article_path = output_dir / f"extreme_codex_{timestamp}_final.md"
    with open(article_path, "w") as f:
        f.write(f"# {topic}\n\n")
        f.write(result.final_article)
        f.write("\n\n---\n\n")
        f.write("## Quality Metrics\n\n")
        f.write(f"- Overall Score: {result.quality_metrics.overall_score:.2f}/10\n")
        f.write(f"- Mechanisms: {result.quality_metrics.settlers.mechanism_count}\n")
        f.write(f"- Inversions: {result.quality_metrics.settlers.inversion_count}\n")
        f.write(f"- Predictions: {result.quality_metrics.settlers.prediction_count}\n")
        f.write(f"- Surprise: {result.quality_metrics.surprise_score:.2f}\n")
        f.write(f"- Compression: {result.quality_metrics.compression_score:.1f}\n")
        f.write(f"- Data Points: {result.quality_metrics.specific_data_count}\n")
    
    print(f"\n📄 Article saved to: {article_path}")
    
    # Save detailed research artifacts
    research_path = output_dir / f"extreme_codex_{timestamp}_research.json"
    research_data = {
        "topic": result.topic,
        "timestamp": timestamp,
        "quality_score": result.quality_metrics.overall_score,
        "mechanisms": result.consolidated_mechanisms,
        "inversions": result.consolidated_inversions,
        "predictions": result.consolidated_predictions,
        "personal_layer": result.personal_layer_elements,
        "revision_history": result.revision_history,
        "research_agents": [
            {
                "role": a.agent_role,
                "model": a.model,
                "content_preview": a.content[:500] if a.content else ""
            }
            for a in result.research_artifacts
        ]
    }
    
    with open(research_path, "w") as f:
        json.dump(research_data, f, indent=2)
    
    print(f"🔬 Research saved to: {research_path}")
    
    # Display article preview
    print("\n" + "=" * 80)
    print("📖 ARTICLE PREVIEW (first 500 chars)")
    print("=" * 80)
    print(result.final_article[:500])
    print("...")
    
    # Display some extracted mechanisms
    if result.consolidated_mechanisms:
        print("\n🔧 Sample Mechanisms:")
        for mechanism in result.consolidated_mechanisms[:3]:
            print(f"  • {mechanism}")
    
    # Display some predictions
    if result.consolidated_predictions:
        print("\n🔮 Sample Predictions:")
        for prediction in result.consolidated_predictions[:3]:
            print(f"  • {prediction}")
    
    print("\n✅ Done!")


if __name__ == "__main__":
    asyncio.run(main())