"""
OpenRouter-based multi-agent swarm for bottom-up insight generation.
Uses diverse models to find mechanisms, not narratives.
"""

import asyncio
import httpx
import os
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
import random

@dataclass
class SwarmResult:
    """Result from swarm agent execution."""
    agent_name: str
    model: str
    content: str
    tokens_used: int = 0
    error: Optional[str] = None

class OpenRouterSwarm:
    """Multi-agent swarm using OpenRouter API."""
    
    # Model pool for diversity
    MODELS = {
        "premium": [
            "anthropic/claude-3.5-sonnet",
            "anthropic/claude-3-opus-20240229",
            "openai/gpt-4-turbo-preview",
        ],
        "fast": [
            "anthropic/claude-3-haiku-20240307",
            "mistralai/mistral-large",
            "meta-llama/llama-3.1-70b-instruct",
        ],
        "specialized": [
            "deepseek/deepseek-chat",
            "google/gemini-pro",
            "cohere/command-r-plus",
        ]
    }
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("OpenRouter API key required")
    
    async def call_model(
        self, 
        model: str, 
        system: str, 
        user: str, 
        temperature: float = 0.7,
        max_tokens: int = 4000
    ) -> SwarmResult:
        """Call a specific model via OpenRouter."""
        
        async with httpx.AsyncClient(timeout=120.0) as client:
            try:
                response = await client.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
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
                    return SwarmResult(
                        agent_name=system.split(".")[0][:50],  # First sentence as name
                        model=model,
                        content=result["choices"][0]["message"]["content"],
                        tokens_used=result.get("usage", {}).get("total_tokens", 0)
                    )
                else:
                    # Fallback to Claude if model fails
                    if model != "anthropic/claude-3.5-sonnet":
                        return await self.call_model(
                            "anthropic/claude-3.5-sonnet",
                            system, user, temperature, max_tokens
                        )
                    return SwarmResult(
                        agent_name="Error",
                        model=model,
                        content="",
                        error=str(result)
                    )
                    
            except Exception as e:
                return SwarmResult(
                    agent_name="Error",
                    model=model,
                    content="",
                    error=str(e)
                )
    
    async def research_swarm(self, topic: str, num_agents: int = 5) -> List[SwarmResult]:
        """Run parallel research agents with different perspectives."""
        
        perspectives = [
            {
                "role": "Data Archaeologist",
                "focus": "Find the numbers everyone missed. What data inversions exist? What correlations are hiding?",
                "model_tier": "premium"
            },
            {
                "role": "Mechanism Hunter", 
                "focus": "Find the causal chains. Not what happened, but what mechanical process made it inevitable?",
                "model_tier": "premium"
            },
            {
                "role": "Pattern Breaker",
                "focus": "Find where the expected pattern breaks. What should have happened but didn't?",
                "model_tier": "fast"
            },
            {
                "role": "Crowd Physicist",
                "focus": "Model this as physics, not psychology. Phase transitions, critical mass, contagion velocity.",
                "model_tier": "specialized"
            },
            {
                "role": "Neuroscience Detective",
                "focus": "Which exact brain regions fire? What neurotransmitters? What's the biological mechanism?",
                "model_tier": "premium"
            },
            {
                "role": "Historical Rhymer",
                "focus": "Find the exact historical parallel. When has this precise mechanism happened before?",
                "model_tier": "fast"
            },
            {
                "role": "Inversion Spotter",
                "focus": "Find the opposite correlations. Where does A cause B in one place but B cause A elsewhere?",
                "model_tier": "specialized"
            }
        ]
        
        # Select perspectives
        selected = random.sample(perspectives, min(num_agents, len(perspectives)))
        
        # Create tasks
        tasks = []
        for perspective in selected:
            model_tier = perspective["model_tier"]
            model = random.choice(self.MODELS[model_tier])
            
            system = f"You are a {perspective['role']}. {perspective['focus']} No narratives, just mechanisms and data."
            
            user = f"""Research this topic with your specific lens: {topic}
            
            Find:
            1. Specific numbers, percentages, thresholds
            2. Exact mechanisms, not descriptions
            3. Surprising inversions or breaks in pattern
            4. What others would miss from your perspective
            
            Be specific. Use examples. No story, just findings."""
            
            tasks.append(self.call_model(model, system, user, temperature=0.7))
        
        results = await asyncio.gather(*tasks)
        return results
    
    async def synthesis_swarm(self, research: List[SwarmResult]) -> SwarmResult:
        """Multiple synthesis agents compete to find the best insight."""
        
        # Combine research
        research_text = "\n\n---\n\n".join([
            f"[{r.agent_name} via {r.model}]\n{r.content}" 
            for r in research if not r.error
        ])
        
        synthesis_approaches = [
            {
                "approach": "Mechanism Extractor",
                "instruction": "Find the ONE mechanism that explains everything. What's the physics equation of this event?",
                "model": "anthropic/claude-3.5-sonnet"
            },
            {
                "approach": "Surprise Maximizer", 
                "instruction": "Find the fact that would most surprise an expert. What would make them say 'wait, what?'",
                "model": "openai/gpt-4-turbo-preview"
            },
            {
                "approach": "Compression Master",
                "instruction": "Express the core insight in minimum words. What's the haiku version that loses nothing?",
                "model": "mistralai/mistral-large"
            }
        ]
        
        approach = random.choice(synthesis_approaches)
        
        system = f"You are a {approach['approach']}. {approach['instruction']}"
        
        user = f"""Synthesize this research into the core insight:
        
        {research_text}
        
        Rules:
        1. Find the mechanism, not the story
        2. Use specific numbers from the research
        3. Connect findings others wouldn't connect
        4. Write for maximum surprise per word
        5. No transitions, no narratives
        
        1500 words max. Start with the mechanism."""
        
        return await self.call_model(
            approach["model"],
            system,
            user,
            temperature=0.8,
            max_tokens=2000
        )
    
    async def editor_swarm(self, draft: str) -> str:
        """Multiple editing passes to remove AI tells."""
        
        editing_passes = [
            {
                "focus": "AI Tell Killer",
                "task": "Remove every word that sounds like ChatGPT. Kill em-dashes, moreover, furthermore.",
                "model": "anthropic/claude-3-haiku-20240307"
            },
            {
                "focus": "Compression Maximizer",
                "task": "If it takes 10 words, say it in 5. Every word must add specific information.",
                "model": "deepseek/deepseek-chat"
            },
            {
                "focus": "Voice Authenticator",
                "task": "Make it impossible to detect as AI. Add genuine voice markers.",
                "model": "mistralai/mistral-large"
            }
        ]
        
        current_text = draft
        
        for pass_config in editing_passes:
            result = await self.call_model(
                pass_config["model"],
                f"You are a {pass_config['focus']}. {pass_config['task']}",
                f"Edit this text:\n\n{current_text}\n\nReturn only the edited version.",
                temperature=0.6,
                max_tokens=2000
            )
            
            if not result.error:
                current_text = result.content
        
        return current_text
    
    async def run_full_swarm(self, topic: str) -> Dict[str, Any]:
        """Run the complete swarm pipeline."""
        
        # Phase 1: Research
        print("Phase 1: Research swarm...")
        research = await self.research_swarm(topic, num_agents=5)
        
        # Phase 2: Synthesis
        print("Phase 2: Synthesis...")
        synthesis = await self.synthesis_swarm(research)
        
        # Phase 3: Editing
        print("Phase 3: Voice editing...")
        if synthesis.content:
            final = await self.editor_swarm(synthesis.content)
        else:
            final = "Synthesis failed"
        
        return {
            "research": research,
            "synthesis": synthesis,
            "final": final,
            "tokens_used": sum(r.tokens_used for r in research) + synthesis.tokens_used
        }