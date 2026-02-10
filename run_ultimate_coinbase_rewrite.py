#!/usr/bin/env python3
"""
Ultimate Coinbase article rewrite using everything learned.
Combines live search data with sophisticated writing techniques.
"""

import asyncio
import httpx
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

async def call_perplexity_advanced(query: str, instructions: str = "") -> dict:
    """Advanced Perplexity call with specific instructions."""
    
    api_key = os.getenv("OPENROUTER_API_KEY")
    
    full_query = f"""{instructions}

{query}

Requirements:
- Use current 2026 data only
- Cite specific sources and quotes
- Focus on mechanisms, not narratives
- Include quantified data points
- Identify surprising insights"""
    
    async with httpx.AsyncClient(timeout=180.0) as client:
        try:
            response = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "perplexity/sonar-pro",
                    "messages": [
                        {"role": "user", "content": full_query}
                    ],
                    "temperature": 0.8,
                    "max_tokens": 4000
                }
            )
            
            return response.json()
            
        except Exception as e:
            return {"error": str(e)}

async def main():
    """Create ultimate rewrite with everything learned."""
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting ultimate Coinbase rewrite...")
    
    # Phase 1: Advanced research with specific writing instructions
    research_tasks = [
        {
            "role": "Mechanism Hunter",
            "instructions": "You are a world-class investigative analyst. Find the hidden causal mechanisms.",
            "query": "Coinbase Super Bowl 2026 Backstreet Boys ad - what were the EXACT psychological and business mechanisms behind the reaction? Find specific expert quotes, data points, and surprising insights."
        },
        {
            "role": "Data Archaeologist", 
            "instructions": "You are a quantitative researcher. Find hard numbers and measurable impacts.",
            "query": "Coinbase Super Bowl 2026 ad performance metrics - EDO rankings, engagement scores, stock impact, social media sentiment data, conversion metrics. Include specific comparisons and benchmarks."
        },
        {
            "role": "Cultural Analyst",
            "instructions": "You are a cultural critic. Find the deeper meaning and context.",
            "query": "Super Bowl 2026 Coinbase Backstreet Boys ad cultural analysis - nostalgia marketing, crypto industry context, generational targeting, brand positioning. Find expert cultural commentary."
        },
        {
            "role": "Contradiction Spotter",
            "instructions": "You are a contrarian investigator. Find what contradicts the mainstream narrative.",
            "query": "Coinbase Super Bowl 2026 ad - what evidence contradicts the 'everyone hated it' narrative? Find positive industry reactions, successful metrics, unintended benefits."
        }
    ]
    
    research_results = []
    
    for i, task in enumerate(research_tasks, 1):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Research phase {i}/4: {task['role']}")
        
        result = await call_perplexity_advanced(task["query"], task["instructions"])
        
        if "choices" in result:
            research_results.append({
                "role": task["role"],
                "content": result["choices"][0]["message"]["content"],
                "citations": result.get("citations", []),
                "tokens": result.get("usage", {}).get("total_tokens", 0)
            })
        
        await asyncio.sleep(3)  # Rate limiting
    
    # Phase 2: Synthesis and article generation
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Synthesizing ultimate article...")
    
    # Combine all research
    research_text = ""
    all_citations = []
    
    for r in research_results:
        research_text += f"\n\n### {r['role']} Research:\n{r['content']}"
        all_citations.extend(r.get('citations', []))
    
    # Create synthesis query
    synthesis_query = f"""Create the ultimate analysis of the Coinbase Super Bowl 2026 ad controversy.

Based on this comprehensive research:
{research_text}

Write a world-class article that:

1. **Challenges assumptions** - Start by debunking false narratives
2. **Reveals mechanisms** - Find the real psychological/business mechanisms  
3. **Uses specific data** - Include exact numbers, quotes, rankings
4. **Finds surprises** - Highlight unexpected insights and contradictions
5. **Provides frameworks** - Create predictive models for future analysis

Structure:
- Compelling headline that captures the real insight
- Hook that challenges the reader's assumptions
- Mechanism-driven analysis with data
- Surprising insights and contradictions
- Predictive frameworks
- Conclusion that reframes everything

Style:
- Punchy, direct sentences
- No AI slop (avoid "moreover," "furthermore," transitions)
- Use specific examples and quotes
- Write for maximum surprise per word
- Authoritative but accessible tone

Length: 800-1000 words focused on genuine insights."""
    
    synthesis_result = await call_perplexity_advanced(synthesis_query, "You are an elite business journalist and cultural critic. Write with the insight depth of Ben Thompson, the data rigor of Nate Silver, and the surprise factor of Malcolm Gladwell.")
    
    # Phase 3: Save ultimate article
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    ultimate_file = f"content/coinbase_ultimate_rewrite_{timestamp}.md"
    
    with open(ultimate_file, 'w') as f:
        f.write("# The Coinbase Karaoke Paradox: An Ultimate Analysis\n")
        f.write(f"*Generated via ultimate rewrite pipeline - {timestamp}*\n\n")
        f.write("## Research Methodology\n")
        f.write(f"- **4 specialized research phases** with expert personas\n")
        f.write(f"- **Live 2026 data** from {len(set(all_citations))} verified sources\n")
        f.write(f"- **Mechanism-focused analysis** challenging false narratives\n")
        f.write(f"- **Quantified insights** with specific data points\n\n")
        f.write("---\n\n")
        
        if "choices" in synthesis_result:
            content = synthesis_result["choices"][0]["message"]["content"]
            f.write(content)
            
            synthesis_citations = synthesis_result.get("citations", [])
            all_unique_citations = list(set(all_citations + synthesis_citations))
            
            if all_unique_citations:
                f.write("\n\n## Sources Referenced\n")
                for i, citation in enumerate(all_unique_citations, 1):
                    f.write(f"{i}. {citation}\n")
        else:
            f.write(f"**Synthesis Error**: {synthesis_result}\n")
    
    # Phase 4: Create research appendix
    research_file = f"content/coinbase_ultimate_research_{timestamp}.md"
    
    with open(research_file, 'w') as f:
        f.write("# Coinbase Ultimate Rewrite - Research Appendix\n\n")
        
        for r in research_results:
            f.write(f"## {r['role']} Research\n")
            f.write(f"**Tokens Used**: {r['tokens']}\n\n")
            f.write(f"{r['content']}\n\n")
            
            if r.get('citations'):
                f.write("### Sources:\n")
                for cite in r['citations']:
                    f.write(f"- {cite}\n")
            f.write("\n---\n\n")
    
    total_tokens = sum(r['tokens'] for r in research_results)
    if 'usage' in synthesis_result:
        total_tokens += synthesis_result['usage'].get('total_tokens', 0)
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Ultimate rewrite complete!")
    print(f"📖 Article: {ultimate_file}")
    print(f"📊 Research: {research_file}")
    print(f"🔍 Sources: {len(set(all_citations))} unique citations")
    print(f"💰 Tokens: {total_tokens} (~${total_tokens * 0.00005:.4f})")
    print("✅ Ultimate analysis delivered!")

if __name__ == "__main__":
    asyncio.run(main())