#!/usr/bin/env python3
"""
Launch 20 parallel research agents to find ACTUALLY SURPRISING data and mechanisms 
about Coinbase/crypto that nobody has discovered.
"""

import asyncio
import json
from datetime import datetime
from src.agents.openrouter_swarm import OpenRouterSwarm, SwarmResult

# Use the Writing Improver API key from CLAUDE.md
API_KEY = "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"

class ExtremeResearchSwarm:
    """20 specialized extreme research agents."""
    
    # All 20 extreme research agents
    EXTREME_AGENTS = [
        {
            "name": "THERMODYNAMICS PHYSICIST",
            "prompt": """You are a physicist who applies entropy laws to financial systems.
            
            Research: Apply thermodynamics to Coinbase/crypto wealth distribution
            
            Find:
            - Exact entropy increase rate of crypto wealth dispersion
            - Energy states of different holder classes
            - Temperature of the market (kinetic energy of transactions)
            - Heat death predictions for crypto system
            - Gibbs free energy of maintaining crypto positions
            
            Calculate specific numbers. What's the entropy formula for crypto wealth?""",
            "model": "anthropic/claude-3.5-sonnet"
        },
        {
            "name": "EVOLUTIONARY BIOLOGIST", 
            "prompt": """You are a biologist studying crypto as an evolving organism.
            
            Research: Crypto evolution - what traits are actually being selected for?
            
            Find:
            - Which crypto traits survive vs die (not just price performance)
            - Mutation rate of new tokens vs survival rate
            - Sexual selection in crypto (what attracts investment?)
            - Parasites in the ecosystem (extractive mechanisms)
            - Convergent evolution examples across different chains
            
            Be specific about selection pressures. What's NOT competence that survives?""",
            "model": "openai/gpt-4-turbo"
        },
        {
            "name": "LINGUISTICS ARCHAEOLOGIST",
            "prompt": """You are a linguist tracking crypto language evolution.
            
            Research: Exact moments when crypto language shifted meaning
            
            Find:
            - Precise date when "HODL" stopped being ironic (scan Twitter/Reddit)
            - When "WAGMI" peaked and died (sentiment analysis)
            - First usage of "have fun staying poor" and spread pattern
            - Language extinction events in crypto communities
            - Semantic drift of technical terms into emotional ones
            
            Track specific phrases through time. What killed crypto's irony?""",
            "model": "mistralai/mistral-large-2407"
        },
        {
            "name": "CONTAGION EPIDEMIOLOGIST",
            "prompt": """You are an epidemiologist studying crypto adoption as disease spread.
            
            Research: R0 (basic reproduction number) of crypto adoption vs rejection
            
            Find:
            - R0 of crypto enthusiasm vs R0 of crypto skepticism - which spreads faster?
            - Superspreader events (what makes someone convert others?)
            - Immunity development (who becomes resistant to crypto appeal?)
            - Incubation period from first exposure to first purchase
            - Recovery rate (getting out permanently)
            
            Use actual epidemic models. Calculate transmission coefficients.""",
            "model": "deepseek/deepseek-chat"
        },
        {
            "name": "QUANTUM MECHANICS THEORIST",
            "prompt": """You are a quantum physicist analyzing observer effects in markets.
            
            Research: Does measuring crypto kill it? Quantum market mechanics
            
            Find:
            - Observer effect: How does price watching change price behavior?
            - Heisenberg uncertainty between price and true ownership volume
            - Schrödinger's trades: Positions that exist in superposition
            - Wave function collapse events in crypto markets
            - Quantum entanglement between related tokens
            
            Apply actual quantum mechanics equations to market behavior.""",
            "model": "google/gemini-pro-1.5"
        },
        {
            "name": "ARCHAEOLOGICAL DATA MINER",
            "prompt": """You are a data archaeologist finding crypto's first moments.
            
            Research: Track origin points of crypto cultural moments
            
            Find:
            - FIRST person to say "have fun staying poor" (exact post/tweet)
            - Patient zero of "diamond hands" meme
            - Original "number go up" technology reference
            - First "not financial advice" disclaimer usage
            - Genesis moments of major crypto phrases
            
            Dig through archives. Find the actual first instances, not popular ones.""",
            "model": "cohere/command-r-plus"
        },
        {
            "name": "NEUROTRANSMITTER MAPPER",
            "prompt": """You are a neuroscientist studying crypto's brain chemistry effects.
            
            Research: Exact neurochemical responses to crypto price movements
            
            Find:
            - Dopamine spike measurements from green vs red candles
            - Cortisol levels during different volatility periods  
            - Serotonin depletion patterns in long-term holders
            - Physical addiction threshold (what % gains trigger addiction?)
            - Neuroplasticity changes in day traders vs HODLers
            
            Use actual neurotransmitter research. What are the specific brain changes?""",
            "model": "anthropic/claude-3.5-sonnet"
        },
        {
            "name": "SOCIAL PHYSICS MODELER",
            "prompt": """You are a physicist who models social systems using physics equations.
            
            Research: Critical mass equations for crypto adoption/rejection
            
            Find:
            - Exact tipping point where adoption becomes rejection
            - Phase transition temperatures for different crypto communities
            - Critical mass formulas (how many adopters needed for cascade?)
            - Social pressure coefficients 
            - Network effect equations vs network rejection effects
            
            Apply actual physics models. What are the exact mathematical thresholds?""",
            "model": "openai/gpt-4o"
        },
        {
            "name": "MYTHOLOGY DECODER",
            "prompt": """You are a comparative mythology expert analyzing crypto as religion.
            
            Research: Crypto's religious structure and mythology patterns
            
            Find:
            - Creation myth variations across different crypto communities
            - Prophet figures and their specific teachings
            - Heretic classifications and persecution patterns
            - Schism events (hard forks as religious splits)
            - Pilgrimage sites (conferences, meet-ups as sacred spaces)
            
            Map exact parallels to historical religions. What's the cosmology?""",
            "model": "meta-llama/llama-3.1-70b-instruct"
        },
        {
            "name": "FORENSIC ACCOUNTANT",
            "prompt": """You are a forensic accountant tracking money flows.
            
            Research: Track a single dollar through the crypto ecosystem
            
            Find:
            - How many times does $1 get extracted as fees in its crypto lifetime?
            - Fee extraction rates by different ecosystem players
            - Value leakage points most people don't see
            - Hidden cost multipliers in "free" services
            - Actual profit margins of major crypto companies
            
            Follow the money precisely. Where does value actually go?""",
            "model": "anthropic/claude-3.5-haiku"
        },
        {
            "name": "COMPLEXITY SCIENTIST",
            "prompt": """You are a complexity theorist studying emergence in crypto markets.
            
            Research: When does collection of traders become mob behavior?
            
            Find:
            - Exact participant count where individual decisions become collective behavior
            - Emergence threshold measurements
            - Self-organization patterns in crypto communities
            - Edge of chaos conditions in markets
            - Butterfly effect amplification factors
            
            Use complexity science metrics. What are the exact emergence points?""",
            "model": "deepseek/deepseek-chat"
        },
        {
            "name": "INFORMATION THEORIST",
            "prompt": """You are an information theorist analyzing crypto data density.
            
            Research: Information content and entropy in crypto markets
            
            Find:
            - Bit rate of price discovery (how much info in one candle?)
            - Entropy measurements of order book configurations
            - Signal vs noise ratios in different timeframes
            - Information compression rates in market movements
            - Mutual information between crypto and traditional assets
            
            Apply information theory math. How much information is actually transmitted?""",
            "model": "mistralai/mistral-large-2407"
        },
        {
            "name": "NETWORK TOPOLOGIST",
            "prompt": """You are a network scientist analyzing crypto influence networks.
            
            Research: Shape and topology of crypto influence networks
            
            Find:
            - Is crypto influence network scale-free? Small world? What's the structure?
            - Network diameter (degrees of separation between any two crypto people)
            - Hub identification and centrality measures
            - Network robustness vs fragility points
            - Information flow bottlenecks
            
            Use actual network analysis. What's the mathematical topology?""",
            "model": "google/gemini-pro-1.5"
        },
        {
            "name": "GAME THEORY EXTREMIST",
            "prompt": """You are a game theorist analyzing crypto as multiplayer game.
            
            Research: Crypto as massive multiplayer prisoner's dilemma
            
            Find:
            - Nash equilibrium of crypto markets - what is it? Why doesn't anyone reach it?
            - Dominant strategies vs what people actually do
            - Coordination failure patterns
            - Multi-level game dynamics (whales vs retail vs institutions)
            - Mechanism design flaws in major protocols
            
            Apply rigorous game theory. What are the actual equilibrium points?""",
            "model": "cohere/command-r-plus"
        },
        {
            "name": "CHRONOBIOLOGIST",
            "prompt": """You are a chronobiologist studying time-based patterns in crypto behavior.
            
            Research: Circadian and temporal rhythms of crypto trading
            
            Find:
            - When do people capitulate? (exact hours, days)
            - Circadian rhythms of different trading behaviors
            - Seasonal affective patterns in crypto markets
            - Sleep deprivation effects on trading decisions
            - Time zone effects on global crypto behavior
            
            Use chronobiology research methods. What are the biological time patterns?""",
            "model": "openai/gpt-4-turbo"
        },
        {
            "name": "MATERIALS SCIENTIST",
            "prompt": """You are a materials scientist analyzing crypto's physical properties.
            
            Research: Energy costs and material properties of crypto vs traditional assets
            
            Find:
            - Exact joules per Bitcoin transaction vs joules per gold transaction
            - Energy density of different consensus mechanisms
            - Thermodynamic efficiency of various blockchains
            - Material transmutation happening (electricity → digital scarcity)
            - Physical infrastructure requirements per unit of value
            
            Use materials science metrics. What's the actual physical cost structure?""",
            "model": "anthropic/claude-3.5-sonnet"
        },
        {
            "name": "DEMOGRAPHIC ARCHAEOLOGIST",
            "prompt": """You are a demographic researcher finding the actual crypto owner profile.
            
            Research: Find the MEDIAN crypto owner (not average - median)
            
            Find:
            - Median age, income, location, education of crypto owners
            - Median loss amount vs median profit
            - Demographic transitions over crypto's lifespan
            - Geographic clustering patterns
            - Socioeconomic profiles that correlate with crypto behavior
            
            Use median statistics, not averages. Paint the actual middle person.""",
            "model": "meta-llama/llama-3.1-70b-instruct"
        },
        {
            "name": "SYSTEMS COLLAPSE EXPERT",
            "prompt": """You are an engineer who studies system failures.
            
            Research: Compare crypto to bridge/building collapse patterns
            
            Find:
            - Resonance frequency of crypto market systems
            - Structural failure points and cascade patterns
            - Load-bearing elements vs decorative elements
            - Fatigue accumulation in market structures
            - Critical failure modes and their warning signs
            
            Use structural engineering analysis. What are the failure mechanics?""",
            "model": "deepseek/deepseek-chat"
        },
        {
            "name": "SEMIOTICS DECODER",
            "prompt": """You are a semiotics expert decoding crypto visual language.
            
            Research: What do crypto symbols actually communicate?
            
            Find:
            - Bitcoin logo analysis: Why orange? Why circle? What does it semiotically encode?
            - Color psychology in different crypto branding
            - Symbol evolution and meaning drift
            - Visual memetic transmission patterns
            - Unconscious communication through crypto aesthetics
            
            Apply semiotics analysis. What messages are encoded in the visual language?""",
            "model": "mistralai/mistral-large-2407"
        },
        {
            "name": "PHILOSOPHICAL EXTREMIST",
            "prompt": """You are a philosopher analyzing crypto's ontological implications.
            
            Research: Crypto as pure nihilism and void creation
            
            Find:
            - How does trading nothing-backed-by-nothing for nothing create meaning?
            - Nihilistic properties of decentralized value
            - Void economics - what happens when scarcity is artificial?
            - Meaning-making in meaningless systems
            - The perfect void - crypto as pure abstraction
            
            Apply philosophical analysis. What existential implications does crypto create?""",
            "model": "google/gemini-pro-1.5"
        }
    ]
    
    def __init__(self):
        self.swarm = OpenRouterSwarm(api_key=API_KEY)
    
    async def run_all_agents(self) -> dict:
        """Run all 20 extreme research agents simultaneously."""
        
        print("🚀 Launching 20 extreme research agents...")
        print("⚡ Each agent will discover mechanisms nobody else has found")
        print("🎯 Target: ACTUALLY SURPRISING data that makes experts say 'wait, WHAT?'\n")
        
        # Create tasks for all 20 agents
        tasks = []
        for agent in self.EXTREME_AGENTS:
            task = self.swarm.call_model(
                model=agent["model"],
                system=f"You are an extreme researcher: {agent['name']}. Find mechanisms and data that would genuinely surprise crypto experts. NO NARRATIVES - just discoveries that collide into truth.",
                user=agent["prompt"],
                temperature=0.8,
                max_tokens=4000
            )
            tasks.append(task)
        
        print(f"⏳ Running {len(tasks)} agents in parallel...")
        start_time = datetime.now()
        
        # Execute all agents simultaneously
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        print(f"✅ All agents completed in {duration:.1f} seconds\n")
        
        # Process results
        successful_results = []
        errors = []
        
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                errors.append(f"Agent {i+1} ({self.EXTREME_AGENTS[i]['name']}): {str(result)}")
            elif result.error:
                errors.append(f"Agent {i+1} ({self.EXTREME_AGENTS[i]['name']}): {result.error}")
            else:
                successful_results.append({
                    "agent": self.EXTREME_AGENTS[i]['name'],
                    "model": result.model,
                    "content": result.content,
                    "tokens": result.tokens_used
                })
        
        return {
            "timestamp": datetime.now().isoformat(),
            "duration_seconds": duration,
            "successful_agents": len(successful_results),
            "failed_agents": len(errors),
            "results": successful_results,
            "errors": errors,
            "total_tokens": sum(r.get('tokens', 0) for r in successful_results)
        }

async def main():
    """Run the extreme discovery swarm."""
    
    # Initialize swarm
    swarm = ExtremeResearchSwarm()
    
    # Test API connection first
    print("🔧 Testing OpenRouter API connection...")
    is_valid = await swarm.swarm.test_api_key()
    
    if not is_valid:
        print("❌ OpenRouter API key validation failed!")
        print("🔑 Current key format:", API_KEY[:30] + "...")
        print("💡 Check if key is correct and has remaining credits")
        return
    
    print("✅ API key validated successfully!\n")
    
    # Run all agents
    results = await swarm.run_all_agents()
    
    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save raw research
    raw_file = f"content/extreme_coinbase_discovery_{timestamp}.md"
    with open(raw_file, 'w') as f:
        f.write(f"# Extreme Coinbase Discovery Research\n\n")
        f.write(f"Generated: {results['timestamp']}\n")
        f.write(f"Duration: {results['duration_seconds']:.1f} seconds\n")
        f.write(f"Successful Agents: {results['successful_agents']}/20\n")
        f.write(f"Total Tokens: {results['total_tokens']:,}\n\n")
        
        if results['errors']:
            f.write("## Errors\n\n")
            for error in results['errors']:
                f.write(f"- {error}\n")
            f.write("\n")
        
        f.write("## Research Findings\n\n")
        for result in results['results']:
            f.write(f"### {result['agent']}\n")
            f.write(f"*Model: {result['model']} | Tokens: {result['tokens']:,}*\n\n")
            f.write(f"{result['content']}\n\n")
            f.write("---\n\n")
    
    # Save JSON for programmatic access
    json_file = f"content/extreme_coinbase_discovery_{timestamp}.json"
    with open(json_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Print summary
    print("📊 DISCOVERY SUMMARY:")
    print(f"   • {results['successful_agents']}/20 agents completed successfully")
    print(f"   • {results['total_tokens']:,} total tokens used")
    print(f"   • {results['duration_seconds']:.1f} seconds execution time")
    
    if results['errors']:
        print(f"   • {len(results['errors'])} agents failed")
        print("\n❌ Errors:")
        for error in results['errors'][:3]:  # Show first 3 errors
            print(f"   • {error}")
    
    print(f"\n📁 Results saved to:")
    print(f"   • {raw_file}")
    print(f"   • {json_file}")
    
    print(f"\n🎯 NEXT: Review findings for genuinely surprising mechanisms and data points")

if __name__ == "__main__":
    asyncio.run(main())