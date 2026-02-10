"""
Authentic Voice Swarm - Fixed version addressing root causes of mechanical output.
Key fixes:
1. No numbered lists in prompts - narrative flow only
2. High temperature for authentic voice (0.9+)
3. No fallbacks - let diversity emerge from failures
4. Pattern detection for deep structural AI tells
"""

import asyncio
import httpx
import os
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import random
import json

@dataclass
class AuthenticResult:
    """Result from authentic voice agent."""
    agent_name: str
    model: str
    content: str
    tokens_used: int = 0
    error: Optional[str] = None

class AuthenticSwarm:
    """Fixed multi-agent swarm that produces genuine voice."""
    
    # Diverse models without homogenization - UPDATED WITH ACTUAL OPENROUTER IDS
    MODELS = {
        "contrarian": [
            "mistralai/mistral-medium-3.1",  # Different reasoning style
            "mistralai/mixtral-8x22b-instruct",  # MoE architecture
            "openai/gpt-4",  # Different training
        ],
        "premium": [
            "anthropic/claude-3.5-sonnet",
            "openai/gpt-4-turbo",
            "mistralai/mistral-large-2411",
        ],
        "fast": [
            "mistralai/mistral-large-2407",
            "anthropic/claude-3.5-haiku",
            "openai/gpt-4o-mini",
        ]
    }
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("OpenRouter API key required")
    
    async def call_model_no_fallback(
        self, 
        model: str, 
        system: str, 
        user: str, 
        temperature: float = 0.9,  # Higher default for authenticity
        max_tokens: int = 4000
    ) -> AuthenticResult:
        """Call model WITHOUT fallback - preserve diversity even in failure."""
        
        # Stagger requests to avoid rate limits
        await asyncio.sleep(random.uniform(1, 3))
        
        async with httpx.AsyncClient(timeout=120.0) as client:
            try:
                response = await client.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                        "HTTP-Referer": "https://github.com/writing-improver",
                        "X-Title": "Writing Improver Authentic Swarm"
                    },
                    json={
                        "model": model,
                        "messages": [
                            {"role": "system", "content": system},
                            {"role": "user", "content": user}
                        ],
                        "temperature": temperature,
                        "max_tokens": max_tokens
                    }
                )
                
                result = response.json()
                
                if "choices" in result:
                    return AuthenticResult(
                        agent_name=system.split(".")[0][:50],
                        model=model,
                        content=result["choices"][0]["message"]["content"],
                        tokens_used=result.get("usage", {}).get("total_tokens", 0)
                    )
                else:
                    # NO FALLBACK - preserve failure as signal
                    return AuthenticResult(
                        agent_name="Failed-" + model.split("/")[-1],
                        model=model,
                        content=f"[Model {model} perspective unavailable]",
                        error=str(result)
                    )
                    
            except Exception as e:
                # Return failure as content, not error
                return AuthenticResult(
                    agent_name="Exception-" + model.split("/")[-1],
                    model=model,
                    content=f"[{model} failed with: {str(e)[:100]}]",
                    error=str(e)
                )
    
    async def voice_discovery_swarm(self, topic: str) -> List[AuthenticResult]:
        """Research with narrative prompts, not templates."""
        
        # Narrative perspectives without numbered constraints
        perspectives = [
            {
                "role": "Memory Archaeologist",
                "prompt": f"Tell me about {topic} through the lens of someone who was actually there. What small details would they remember that reports miss? What did it smell like, sound like? What were people actually saying to each other when the cameras were off?",
                "model_tier": "contrarian",
                "temperature": 0.95
            },
            {
                "role": "Mechanism Reverse-Engineer", 
                "prompt": f"If {topic} was a machine that broke, walk me through the failure backwards from the break point. Not why it happened but the actual mechanical sequence that made it inevitable. Like debugging code - trace the execution path.",
                "model_tier": "premium",
                "temperature": 0.9
            },
            {
                "role": "Pattern Violation Detector",
                "prompt": f"Every pattern has an exception that proves the rule false. For {topic}, find where the expected correlation inverts. Where does the thing that should help actually hurt? Don't explain why - just show me the inversion.",
                "model_tier": "fast",
                "temperature": 1.0
            },
            {
                "role": "Crowd Current Mapper",
                "prompt": f"Model {topic} as electrical current through a crowd. Where's the resistance? What's the voltage? When does the circuit complete? Describe the actual flow of energy person to person, not metaphorically but as measurable transmission.",
                "model_tier": "contrarian",
                "temperature": 0.92
            },
            {
                "role": "Neurotransmitter Tracker",
                "prompt": f"For {topic}, which specific neurotransmitters spike in which order? Dopamine, serotonin, cortisol, oxytocin - map the chemical cascade in the brain. What addiction pathways activate? What withdrawal symptoms manifest?",
                "model_tier": "premium",
                "temperature": 0.88
            },
            {
                "role": "Historical Echo Finder",
                "prompt": f"Find the exact historical moment that rhymes with {topic}. Not a similar event - the same mechanism in different clothes. What year, what place, what names? How did that one end? Be specific enough that I could look it up.",
                "model_tier": "fast",
                "temperature": 0.93
            },
            {
                "role": "Opposite Day Observer",
                "prompt": f"For {topic}, find where cause and effect swap places. Where does the symptom create the disease? The solution cause the problem? The cure become the poison? Show me the flip without explaining it.",
                "model_tier": "contrarian",
                "temperature": 0.96
            }
        ]
        
        # Select diverse perspectives
        selected = random.sample(perspectives, min(5, len(perspectives)))
        
        # Run in parallel without coordination
        tasks = []
        for perspective in selected:
            model_tier = perspective["model_tier"]
            models = self.MODELS[model_tier]
            model = random.choice(models)
            
            task = self.call_model_no_fallback(
                model=model,
                system=perspective["role"],
                user=perspective["prompt"],
                temperature=perspective["temperature"],
                max_tokens=3000
            )
            tasks.append(task)
        
        return await asyncio.gather(*tasks)
    
    async def collision_synthesis(self, research: List[AuthenticResult]) -> AuthenticResult:
        """Synthesis through collision, not aggregation."""
        
        # Extract only successful perspectives
        valid_research = [r for r in research if not r.error and len(r.content) > 100]
        
        if len(valid_research) < 2:
            return AuthenticResult(
                agent_name="Synthesis-Failed",
                model="none",
                content="Insufficient perspectives for collision synthesis",
                error="Not enough valid research"
            )
        
        # Collision prompt - no structure imposed
        collision_prompts = [
            {
                "style": "Violent Compression",
                "prompt": f"""Take these perspectives and CRASH them together. What breaks? What fuses? What new thing emerges from the collision?

{chr(10).join([r.content for r in valid_research])}

Write the collision result. Start mid-thought. No setup. Just the crash point where insights collide.""",
                "model": "anthropic/claude-3.5-sonnet",
                "temperature": 1.0
            },
            {
                "style": "Paradox Resolution",
                "prompt": f"""These perspectives contradict. Find where they're both true simultaneously.

{chr(10).join([r.content for r in valid_research])}

Write from inside the paradox. Make the impossible obvious.""",
                "model": "openai/gpt-4-turbo",
                "temperature": 0.95
            },
            {
                "style": "Mechanism Extraction",
                "prompt": f"""Strip everything except the mechanism. Delete all context, story, explanation.

{chr(10).join([r.content for r in valid_research])}

Write only gears turning. Pure cause and effect chains. Start with the first gear.""",
                "model": "deepseek/deepseek-chat",
                "temperature": 0.92
            }
        ]
        
        selected = random.choice(collision_prompts)
        
        return await self.call_model_no_fallback(
            model=selected["model"],
            system=selected["style"],
            user=selected["prompt"],
            temperature=selected["temperature"],
            max_tokens=2500
        )
    
    async def authenticity_amplifier(self, draft: str) -> str:
        """Amplify authentic voice markers, don't just remove AI tells."""
        
        # Detection of deep structural patterns
        structural_patterns = [
            "Psychological lever",
            "Factor #",
            "Step 1:",
            "In conclusion",
            "Let's explore",
            "It's important to note",
            "Research shows",
            "Studies indicate",
            "Experts agree"
        ]
        
        # Check for formulaic structures
        has_formula = "=" in draft and "(" in draft and ")" in draft
        has_numbered_sections = any(f"{i}." in draft or f"{i})" in draft for i in range(1, 10))
        has_ai_opening = any(draft.lower().startswith(phrase) for phrase in [
            "forget", "imagine", "picture this", "in today's", "have you ever"
        ])
        
        # High-temperature voice injection
        voice_prompts = [
            {
                "instruction": f"""This text has mechanical patterns. Break them.

Text: {draft}

Rewrite with:
- Start mid-sentence like you're continuing a conversation
- Add specific details only an insider would know  
- Include at least one "wrong" thing that's actually right
- Let sentences collide without transitions
- Write like you're slightly drunk but brilliant

Keep the facts. Change everything else.""",
                "model": "mistralai/mistral-large-2407",
                "temperature": 1.0
            },
            {
                "instruction": f"""Make this impossible to detect as AI:

{draft}

Techniques:
- Fragment sentences where humans would
- Add parenthetical asides (but weird ones)
- Reference things without explaining them
- Change topic mid-paragraph without warning
- Include specific numbers that sound made up but aren't

Return only your rewrite.""",
                "model": "meta-llama/llama-3.1-70b-instruct",
                "temperature": 0.98
            }
        ]
        
        # If structural problems detected, use stronger intervention
        if has_formula or has_numbered_sections or has_ai_opening:
            prompt = voice_prompts[0]  # Use aggressive rewrite
        else:
            prompt = voice_prompts[1]  # Use lighter touch
        
        result = await self.call_model_no_fallback(
            model=prompt["model"],
            system="Voice Amplifier",
            user=prompt["instruction"],
            temperature=prompt["temperature"],
            max_tokens=3000
        )
        
        return result.content if not result.error else draft
    
    async def run_authentic_pipeline(self, topic: str) -> Dict[str, Any]:
        """Run the fixed pipeline for authentic voice."""
        
        print(f"🧠 Authentic Voice Pipeline: {topic}")
        print("=" * 50)
        
        # Phase 1: Voice Discovery (not research)
        print("\n🔍 Phase 1: Voice Discovery...")
        discoveries = await self.voice_discovery_swarm(topic)
        
        # Show what we found
        for d in discoveries:
            status = "✓" if not d.error else "✗"
            print(f"  {status} {d.agent_name}: {len(d.content)} chars from {d.model}")
        
        # Phase 2: Collision Synthesis
        print("\n💥 Phase 2: Collision Synthesis...")
        synthesis = await self.collision_synthesis(discoveries)
        print(f"  Synthesis: {len(synthesis.content)} chars")
        
        # Phase 3: Authenticity Amplification  
        print("\n🎤 Phase 3: Authenticity Amplification...")
        if synthesis.content and len(synthesis.content) > 100:
            final = await self.authenticity_amplifier(synthesis.content)
            print(f"  Final: {len(final)} chars")
        else:
            final = "Pipeline failed - insufficient synthesis"
        
        # Calculate diversity score
        models_used = set(d.model for d in discoveries if not d.error)
        diversity_score = len(models_used) / len(discoveries) if discoveries else 0
        
        print(f"\n📊 Diversity Score: {diversity_score:.2%} ({len(models_used)} unique models)")
        print("=" * 50)
        
        return {
            "discoveries": discoveries,
            "synthesis": synthesis,
            "final": final,
            "metrics": {
                "tokens_used": sum(d.tokens_used for d in discoveries) + synthesis.tokens_used,
                "diversity_score": diversity_score,
                "models_used": list(models_used),
                "success_rate": sum(1 for d in discoveries if not d.error) / len(discoveries)
            }
        }

# Test function for immediate validation
async def test_authentic_voice():
    """Test the authentic voice pipeline."""
    swarm = AuthenticSwarm()
    
    # Test on a topic that previously produced formulaic output
    result = await swarm.run_authentic_pipeline(
        "Why venture capital firms are desperately buying meditation apps"
    )
    
    print("\n📝 FINAL OUTPUT:")
    print("-" * 50)
    print(result["final"])
    print("-" * 50)
    
    return result

if __name__ == "__main__":
    asyncio.run(test_authentic_voice())