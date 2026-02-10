"""
Enhanced OpenRouter swarm with live search capabilities.
Integrates Perplexity models, web search, and X API for real-time research.
"""

import asyncio
import httpx
import os
import json
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import random

@dataclass
class LiveSearchResult:
    """Result from live search agent."""
    agent_name: str
    model: str
    content: str
    search_queries: List[str] = None
    sources: List[Dict[str, str]] = None
    tokens_used: int = 0
    error: Optional[str] = None

class LiveSearchSwarm:
    """Multi-agent swarm with live search capabilities."""
    
    # Enhanced model pool with search capabilities
    SEARCH_MODELS = {
        "perplexity": [
            "perplexity/sonar-pro",
            "perplexity/sonar",
        ],
        "web_enabled": [
            "anthropic/claude-3.5-sonnet:online",
            "openai/gpt-4-turbo:online", 
        ],
        "hybrid": [
            "meta-llama/llama-3.1-70b-instruct:online",
            "mistralai/mistral-large-2407:online",
        ]
    }
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        self.x_bearer_token = os.getenv("X_BEARER_TOKEN")
        if not self.api_key:
            raise ValueError("OpenRouter API key required")
    
    async def call_search_model(
        self,
        model: str,
        system: str,
        user: str,
        search_config: Optional[Dict] = None,
        temperature: float = 0.7,
        max_tokens: int = 4000
    ) -> LiveSearchResult:
        """Call model with optional web search."""
        
        # Rate limiting
        await asyncio.sleep(2)
        
        # Build request payload
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user}
            ],
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        # Add search configuration if specified
        if search_config:
            payload["plugins"] = [search_config]
        
        async with httpx.AsyncClient(timeout=180.0) as client:
            try:
                response = await client.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                    },
                    json=payload
                )
                
                result = response.json()
                
                if "choices" in result:
                    # Extract search queries and sources if available
                    search_queries = []
                    sources = []
                    
                    # Parse annotations for search data
                    if "annotations" in result:
                        for annotation in result["annotations"]:
                            if annotation.get("type") == "web_search":
                                search_queries.append(annotation.get("query", ""))
                                sources.extend(annotation.get("results", []))
                    
                    return LiveSearchResult(
                        agent_name=system.split(".")[0][:50],
                        model=model,
                        content=result["choices"][0]["message"]["content"],
                        search_queries=search_queries,
                        sources=sources,
                        tokens_used=result.get("usage", {}).get("total_tokens", 0)
                    )
                else:
                    return LiveSearchResult(
                        agent_name="Error",
                        model=model,
                        content="",
                        error=str(result)
                    )
                    
            except Exception as e:
                return LiveSearchResult(
                    agent_name="Error",
                    model=model,
                    content="",
                    error=str(e)
                )
    
    async def search_x_api(self, query: str, max_results: int = 10) -> List[Dict]:
        """Search X (Twitter) API for recent posts."""
        if not self.x_bearer_token:
            return []
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    "https://api.twitter.com/2/tweets/search/recent",
                    headers={
                        "Authorization": f"Bearer {self.x_bearer_token}",
                    },
                    params={
                        "query": f"{query} -is:retweet lang:en",
                        "max_results": min(max_results, 100),
                        "tweet.fields": "created_at,public_metrics,context_annotations",
                        "user.fields": "verified,public_metrics"
                    }
                )
                
                if response.status_code == 200:
                    data = response.json()
                    return data.get("data", [])
                else:
                    print(f"X API error: {response.status_code}")
                    return []
                    
        except Exception as e:
            print(f"X API search failed: {e}")
            return []
    
    async def live_research_swarm(self, topic: str, num_agents: int = 4) -> List[LiveSearchResult]:
        """Run parallel research agents with live search capabilities."""
        
        search_perspectives = [
            {
                "role": "Real-Time News Hunter",
                "focus": "Find breaking news, recent developments, current sentiment from news sources and social media",
                "model_tier": "perplexity",
                "search_config": {
                    "id": "web",
                    "engine": "native",
                    "max_results": 5
                }
            },
            {
                "role": "Social Signal Detector", 
                "focus": "Analyze social media reactions, viral patterns, public sentiment shifts in real-time",
                "model_tier": "web_enabled",
                "search_config": {
                    "id": "web", 
                    "engine": "exa",
                    "max_results": 4,
                    "search_prompt": "Find social media discussions, reactions, and sentiment analysis"
                }
            },
            {
                "role": "Data Stream Miner",
                "focus": "Current statistics, market data, engagement metrics, performance numbers",
                "model_tier": "web_enabled", 
                "search_config": {
                    "id": "web",
                    "engine": "native",
                    "max_results": 3
                }
            },
            {
                "role": "Context Archaeologist",
                "focus": "Background context, historical parallels, industry analysis from current sources",
                "model_tier": "hybrid",
                "search_config": {
                    "id": "web",
                    "engine": "exa", 
                    "max_results": 5
                }
            },
            {
                "role": "Mechanism Detector",
                "focus": "Current expert analysis, technical explanations, causal mechanisms being discussed now",
                "model_tier": "perplexity",
                "search_config": {
                    "id": "web",
                    "engine": "native",
                    "max_results": 4
                }
            }
        ]
        
        # Select perspectives
        selected = random.sample(search_perspectives, min(num_agents, len(search_perspectives)))
        
        # Add X API search for social context
        x_results = await self.search_x_api(f"Coinbase Super Bowl ad Backstreet Boys", max_results=20)
        x_context = ""
        if x_results:
            x_context = f"\n\nRECENT X/TWITTER DISCUSSION:\n"
            for tweet in x_results[:10]:
                x_context += f"- {tweet.get('text', '')[:200]}...\n"
        
        # Create tasks
        tasks = []
        for perspective in selected:
            model_tier = perspective["model_tier"]
            model = random.choice(self.SEARCH_MODELS[model_tier])
            
            system = f"""You are a {perspective['role']}. {perspective['focus']} 
            
            Use live web search to find current, recent information. Focus on 2025-2026 timeframe.
            No narratives, just current findings and mechanisms."""
            
            user = f"""Research this topic with live search: {topic}
            
            {x_context}
            
            Find current information about:
            1. Recent news coverage and developments
            2. Current public reaction and sentiment 
            3. Latest statistics and engagement metrics
            4. Expert analysis and commentary
            5. Underlying mechanisms being discussed
            
            Use web search to verify and find latest information. Be specific with current data."""
            
            tasks.append(self.call_search_model(
                model, system, user, 
                search_config=perspective["search_config"],
                temperature=0.7
            ))
        
        results = await asyncio.gather(*tasks)
        return results
    
    async def synthesis_with_sources(self, research: List[LiveSearchResult]) -> LiveSearchResult:
        """Synthesize research with source tracking."""
        
        # Combine research and sources
        research_text = ""
        all_sources = []
        
        for r in research:
            if not r.error:
                research_text += f"\n\n[{r.agent_name} via {r.model}]\n{r.content}"
                if r.sources:
                    all_sources.extend(r.sources)
                if r.search_queries:
                    research_text += f"\n[Searched: {', '.join(r.search_queries)}]"
        
        system = """You are a Synthesis Engine. Find the core mechanism that explains the phenomenon.
        Use the live search results to build a data-driven analysis. Include specific numbers and sources."""
        
        user = f"""Synthesize this live research into the core insight:
        
        {research_text}
        
        Rules:
        1. Lead with the mechanism, not the story
        2. Use specific current data and numbers
        3. Reference sources and timeframes
        4. Find unexpected connections
        5. No AI transitions or narratives
        
        Maximum 1500 words. Start with the mechanism."""
        
        # Use Perplexity without additional search config (native search built-in)
        result = await self.call_search_model(
            "perplexity/sonar-pro",
            system, user,
            search_config=None,  # Perplexity has built-in search
            temperature=0.8
        )
        
        # Add accumulated sources
        if result and not result.error:
            if not result.sources:
                result.sources = []
            result.sources.extend(all_sources)
        
        return result
    
    async def run_live_swarm(self, topic: str) -> Dict[str, Any]:
        """Run complete live search swarm pipeline."""
        
        print("Phase 1: Live research swarm...")
        research = await self.live_research_swarm(topic, num_agents=4)
        
        print("Phase 2: Live synthesis...")
        synthesis = await self.synthesis_with_sources(research)
        
        return {
            "research": research,
            "synthesis": synthesis,
            "total_sources": len(synthesis.sources) if synthesis.sources else 0,
            "tokens_used": sum(r.tokens_used for r in research if not r.error) + 
                          (synthesis.tokens_used if not synthesis.error else 0)
        }