#!/usr/bin/env python3
"""
Full Bottom-Up Swarm using local Claude API
No external APIs needed - uses system Claude
"""

import subprocess
import json
import sys
from pathlib import Path
from datetime import datetime
import random

class LocalClaudeSwarm:
    """Bottom-up swarm using local Claude installation."""
    
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.discoveries = []
        
    def call_claude(self, prompt: str, role: str = "researcher") -> str:
        """Call local Claude with a specific prompt."""
        
        # Format for claude CLI
        full_prompt = f"""You are a {role}. {prompt}
        
Be specific. Use numbers. Find mechanisms, not stories.
Output your findings in 500 words or less."""
        
        try:
            # Call claude CLI directly with --print flag
            result = subprocess.run(
                ["claude", "--print", full_prompt],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0:
                return result.stdout
            else:
                return f"Error: {result.stderr}"
                
        except Exception as e:
            return f"Failed to call Claude: {str(e)}"
    
    def run_discovery_agents(self, topic: str):
        """Run multiple discovery agents with different perspectives."""
        
        print("\n🔍 DISCOVERY PHASE: Multiple Agents")
        print("=" * 60)
        
        agents = [
            {
                "role": "Data Archaeologist",
                "prompt": f"For {topic}, find the hidden numbers. What data inversions exist? What statistics contradict the narrative? Look for: percentages that don't add up, thresholds where behavior changes, correlations that invert at certain points."
            },
            {
                "role": "Mechanism Hunter",
                "prompt": f"For {topic}, trace the mechanical sequence. Not why it happened but HOW - the actual gears turning. What was the cascade? What triggered what? Be specific about the chain reaction."
            },
            {
                "role": "Pattern Breaker", 
                "prompt": f"For {topic}, find where the expected pattern breaks. Where does the normal rule fail? What should correlate but doesn't? Find the violation that proves the rule wrong."
            },
            {
                "role": "Crowd Physicist",
                "prompt": f"Model {topic} as physics. What's the critical mass? The activation energy? The phase transition point? Describe it as particles, waves, fields - not people."
            },
            {
                "role": "Historical Rhymer",
                "prompt": f"Find the EXACT historical parallel to {topic}. Not similar - the same mechanism in different clothes. What year, place, names? How did that one end? Be specific enough I could verify it."
            }
        ]
        
        # Run each agent
        for agent in agents:
            print(f"\n🤖 {agent['role']}...")
            discovery = self.call_claude(agent['prompt'], agent['role'])
            
            self.discoveries.append({
                "role": agent['role'],
                "content": discovery
            })
            
            # Show preview
            preview = discovery[:200] + "..." if len(discovery) > 200 else discovery
            print(f"   Preview: {preview}")
    
    def synthesize_mechanisms(self):
        """Collide discoveries to find core mechanisms."""
        
        print("\n💥 SYNTHESIS PHASE: Collision")
        print("=" * 60)
        
        # Combine all discoveries
        all_discoveries = "\n\n---\n\n".join([
            f"{d['role']}:\n{d['content']}" 
            for d in self.discoveries
        ])
        
        synthesis_prompt = f"""Take these different perspectives and CRASH them together:

{all_discoveries}

Find:
1. The core mechanism that explains everything
2. The specific threshold or tipping point
3. The hidden variable everyone missed
4. The cascade sequence

Write the collision result. Start mid-thought. No setup. Just the crash point where insights collide.
500 words max."""
        
        synthesis = self.call_claude(synthesis_prompt, "Synthesis Engine")
        
        return synthesis
    
    def inject_authentic_voice(self, synthesis: str):
        """Transform synthesis into authentic voice."""
        
        print("\n🎤 VOICE INJECTION PHASE")
        print("=" * 60)
        
        voice_prompt = f"""Rewrite this with maximum authenticity:

{synthesis}

Rules:
- Start mid-sentence like continuing a conversation
- Add specific details only insiders would know (Poloniex trollbox, MtGox, etc)
- Fragment sentences where humans would
- Include parenthetical asides
- Reference things without explaining them
- Use specific numbers but make them feel casual
- Write like you're explaining to someone who gets it

Keep all facts. Change everything about how it's written.
No AI tells. No transitions. Just voice."""
        
        final = self.call_claude(voice_prompt, "Voice Injector")
        
        return final
    
    def run_full_swarm(self, topic: str):
        """Run the complete bottom-up swarm."""
        
        print(f"\n{'='*70}")
        print(f"🧬 LOCAL CLAUDE BOTTOM-UP SWARM")
        print(f"{'='*70}")
        print(f"Topic: {topic}")
        print(f"Time: {self.timestamp}")
        print(f"{'='*70}")
        
        # Phase 1: Discovery
        self.run_discovery_agents(topic)
        
        # Phase 2: Synthesis
        print("\nSynthesizing discoveries...")
        synthesis = self.synthesize_mechanisms()
        
        # Phase 3: Voice Injection
        print("\nInjecting authentic voice...")
        final = self.inject_authentic_voice(synthesis)
        
        # Save outputs
        self.save_outputs(topic, synthesis, final)
        
        print(f"\n{'='*70}")
        print("✅ SWARM COMPLETE")
        print(f"{'='*70}")
        
        # Show preview
        print("\n📄 FINAL OUTPUT (first 500 chars):")
        print("-" * 70)
        print(final[:500])
        if len(final) > 500:
            print(f"... [{len(final)-500} more chars]")
        
        return {
            "discoveries": self.discoveries,
            "synthesis": synthesis,
            "final": final
        }
    
    def save_outputs(self, topic: str, synthesis: str, final: str):
        """Save all outputs to files."""
        
        # Save discoveries
        discoveries_path = f"content/claude_swarm_{self.timestamp}_discoveries.md"
        with open(discoveries_path, "w") as f:
            f.write(f"# Bottom-Up Discoveries\n")
            f.write(f"*Topic: {topic}*\n")
            f.write(f"*Generated: {self.timestamp}*\n\n")
            
            for d in self.discoveries:
                f.write(f"## {d['role']}\n\n")
                f.write(d['content'])
                f.write("\n\n---\n\n")
        
        # Save synthesis
        synthesis_path = f"content/claude_swarm_{self.timestamp}_synthesis.md"
        with open(synthesis_path, "w") as f:
            f.write(f"# Mechanism Synthesis\n\n")
            f.write(synthesis)
        
        # Save final
        final_path = f"content/claude_swarm_{self.timestamp}_final.md"
        with open(final_path, "w") as f:
            f.write(f"# {topic}\n\n")
            f.write(f"*Generated via Local Claude Bottom-Up Swarm - {self.timestamp}*\n\n")
            f.write("---\n\n")
            f.write(final)
        
        print(f"\n📁 Files saved:")
        print(f"  - {discoveries_path}")
        print(f"  - {synthesis_path}")
        print(f"  - {final_path}")

def main():
    """Main entry point."""
    
    # Test topic
    topic = "Why Coinbase's Super Bowl 2026 karaoke ad triggered mass booing when the logo appeared"
    
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
    
    print(f"🎯 Topic: {topic}")
    
    # Check if claude CLI is available
    try:
        result = subprocess.run(
            ["claude", "--version"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print("❌ Error: claude CLI not found")
            print("Install with: pip install claude-cli")
            return
    except:
        print("❌ Error: claude CLI not available")
        return
    
    # Run swarm
    swarm = LocalClaudeSwarm()
    swarm.run_full_swarm(topic)

if __name__ == "__main__":
    main()