"""Ultimate Bottom-Up Discovery Pipeline.

This integrates:
1. Socratic questioning (5 levels deep)
2. Writer technique extraction (10 master writers)
3. Kolmogorov compression (10:1 minimum)
4. Multi-agent specialized research
5. Emergent thesis (not forced narrative)
6. Maximum density writing

The goal: Articles that match "The Settlers" quality through pure discovery.
"""

import asyncio
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

from src.agents.socratic_bottom_up_swarm import SocraticBottomUpSwarm, SocraticQuestion
from src.agents.extreme_codex_swarm import ExtremeCodexSwarm
from src.agents.openrouter_swarm import OpenRouterSwarm
from src.analysis.writer_reverse_engineering import WriterReverseEngineering
from src.compression.kolmogorov_maximizer import KolmogorovMaximizer, KolmogorovInsight
from src.quality.settlers_validator import validate_settlers_quality, SettlersThresholds


@dataclass
class UltimateDiscovery:
    """Complete bottom-up discovery result."""
    topic: str
    
    # Discovery phases
    socratic_depth: List[SocraticQuestion]
    writer_techniques_found: Dict[str, List[str]]
    kolmogorov_insights: List[KolmogorovInsight]
    
    # Research artifacts  
    specialized_research: List[Dict[str, Any]]
    contradictions_found: List[str]
    mechanisms_extracted: List[str]
    
    # Compression metrics
    compression_ratio: float
    insight_density: float
    surprisal_score: float
    
    # Final output
    emergent_thesis: str
    final_article: str
    quality_score: float
    settlers_validation: Dict[str, Any]


class UltimateBottomUpPipeline:
    """The complete bottom-up discovery system."""
    
    def __init__(
        self,
        swarm: OpenRouterSwarm,
        socratic_depth: int = 5,
        writer_styles: List[str] = None,
        compression_target: float = 10.0,
        quality_threshold: float = 8.5
    ):
        self.swarm = swarm
        self.socratic_depth = socratic_depth
        self.writer_styles = writer_styles or [
            "paul_graham", "nassim_taleb", "matt_levine",
            "patrick_mckenzie", "byrne_hobart", "venkatesh_rao"
        ]
        self.compression_target = compression_target
        self.quality_threshold = quality_threshold
        
        # Initialize components
        self.socratic = SocraticBottomUpSwarm(
            swarm=swarm,
            max_socratic_depth=socratic_depth,
            compression_target=compression_target,
            writer_styles=self.writer_styles
        )
        
        self.codex = ExtremeCodexSwarm(
            swarm=swarm,
            quality_target=quality_threshold
        )
        
        self.compressor = KolmogorovMaximizer()
        self.writer_analyzer = WriterReverseEngineering()
        
        self.thresholds = SettlersThresholds(
            min_mechanisms=7,
            min_inversions=3, 
            min_predictions=3,
            min_inclusion_pronouns=5,
            require_confession=True
        )
    
    async def discover(self, topic: str) -> UltimateDiscovery:
        """Execute complete bottom-up discovery."""
        
        print(f"\n{'='*80}")
        print("🧬 ULTIMATE BOTTOM-UP DISCOVERY PIPELINE")
        print(f"{'='*80}")
        print(f"📝 Topic: {topic}")
        print(f"⏰ Started: {datetime.now().isoformat()}\n")
        
        # Phase 1: Socratic Descent
        print("=" * 60)
        print("PHASE 1: SOCRATIC DESCENT")
        print("=" * 60)
        socratic_chain = await self._socratic_descent(topic)
        
        # Phase 2: Multi-Writer Analysis  
        print("\n" + "=" * 60)
        print("PHASE 2: WRITER TECHNIQUE EXTRACTION")
        print("=" * 60)
        writer_insights = await self._extract_writer_insights(topic, socratic_chain)
        
        # Phase 3: Specialized Research Swarm
        print("\n" + "=" * 60)
        print("PHASE 3: SPECIALIZED RESEARCH SWARM")
        print("=" * 60)
        research_artifacts = await self._specialized_research(topic, socratic_chain, writer_insights)
        
        # Phase 4: Contradiction Mining
        print("\n" + "=" * 60)
        print("PHASE 4: CONTRADICTION MINING")
        print("=" * 60)
        contradictions = await self._mine_contradictions(research_artifacts)
        
        # Phase 5: Kolmogorov Compression
        print("\n" + "=" * 60)
        print("PHASE 5: KOLMOGOROV COMPRESSION")
        print("=" * 60)
        compressed_insights = self._maximum_compression(research_artifacts, contradictions)
        
        # Phase 6: Mechanism Extraction
        print("\n" + "=" * 60)
        print("PHASE 6: MECHANISM EXTRACTION")
        print("=" * 60)
        mechanisms = self._extract_mechanisms(research_artifacts, compressed_insights)
        
        # Phase 7: Emergent Synthesis
        print("\n" + "=" * 60)
        print("PHASE 7: EMERGENT SYNTHESIS")
        print("=" * 60)
        thesis = await self._emergent_synthesis(compressed_insights, mechanisms)
        
        # Phase 8: Maximum Density Writing
        print("\n" + "=" * 60)
        print("PHASE 8: MAXIMUM DENSITY WRITING")
        print("=" * 60)
        article = await self._write_maximum_density(
            thesis, compressed_insights, mechanisms,
            socratic_chain, contradictions
        )
        
        # Phase 9: Quality Validation & Enhancement
        print("\n" + "=" * 60)
        print("PHASE 9: QUALITY VALIDATION")
        print("=" * 60)
        final_article, quality_metrics = await self._validate_and_enhance(article)
        
        # Calculate final metrics
        compression_ratio = self._calculate_compression(final_article, research_artifacts)
        insight_density = len(compressed_insights) / max(len(final_article.split()) / 100, 1)
        surprisal = sum(i.surprisal_score for i in compressed_insights) / max(len(compressed_insights), 1)
        
        # Extract writer techniques used
        techniques_found = {}
        for style in self.writer_styles:
            analysis = self.writer_analyzer.analyze_text(final_article, style)
            if analysis.techniques_detected:
                techniques_found[style] = analysis.techniques_detected
        
        return UltimateDiscovery(
            topic=topic,
            socratic_depth=socratic_chain,
            writer_techniques_found=techniques_found,
            kolmogorov_insights=compressed_insights,
            specialized_research=research_artifacts,
            contradictions_found=contradictions,
            mechanisms_extracted=mechanisms,
            compression_ratio=compression_ratio,
            insight_density=insight_density,
            surprisal_score=surprisal,
            emergent_thesis=thesis,
            final_article=final_article,
            quality_score=quality_metrics.get("score", 0),
            settlers_validation=quality_metrics
        )
    
    async def _socratic_descent(self, topic: str) -> List[SocraticQuestion]:
        """Descend through Socratic questioning."""
        
        questions = []
        current_q = f"What is really happening with {topic}?"
        
        for depth in range(self.socratic_depth):
            print(f"  Level {depth+1}: {current_q}")
            
            # Ask with premium model
            model = self.swarm.MODELS["premium"][0]
            
            system = f"""You are at Socratic depth {depth+1}.
            Find the mechanism, not description.
            Find who benefits and who pays.
            Find the number that matters."""
            
            user = f"""Question: {current_q}
            
            Answer with:
            1. The mechanism (with specific threshold)
            2. What this reveals about the system
            3. What assumption this breaks
            4. The next deeper question"""
            
            result = await self.swarm.call_model(
                model, system, user,
                temperature=0.7, max_tokens=800
            )
            
            if result.error:
                break
            
            # Parse response
            lines = result.content.split('\n')
            answer = ' '.join(lines[:2]) if lines else ""
            
            # Extract components
            reveals = self._extract_reveals(result.content)
            contradicts = self._extract_contradicts(result.content)
            
            questions.append(SocraticQuestion(
                question=current_q,
                answer=answer,
                reveals=reveals,
                contradicts=contradicts,
                depth=depth
            ))
            
            print(f"    → Reveals: {reveals[:60]}...")
            
            # Generate next question
            if "thermodynamic" in reveals.lower() or "physical limit" in reveals.lower():
                print("    ✓ Hit bedrock mechanism")
                break
            
            current_q = f"Why does {reveals[:50]}?"
        
        return questions
    
    async def _extract_writer_insights(
        self,
        topic: str,
        socratic_chain: List[SocraticQuestion]
    ) -> Dict[str, List[str]]:
        """Extract insights using each writer's technique."""
        
        insights = {}
        
        for writer in self.writer_styles:
            print(f"  Analyzing through {writer.replace('_', ' ').title()} lens...")
            
            # Get writer's key questions
            prompts = self.writer_analyzer.get_truth_finding_approaches([writer])
            
            if prompts:
                model = self.swarm.MODELS["premium"][0]
                
                system = f"You think like {writer.replace('_', ' ').title()}."
                
                context = ' → '.join([q.reveals for q in socratic_chain[:3]])
                
                user = f"""Topic: {topic}
                Discovery chain: {context}
                
                Using {writer}'s approach: {prompts[0]}
                
                Find:
                1. The mechanism others miss
                2. The number that matters
                3. The contradiction to consensus
                4. The simple truth
                
                Be specific. Use data."""
                
                result = await self.swarm.call_model(
                    model, system, user,
                    temperature=0.8, max_tokens=500
                )
                
                if not result.error:
                    insights[writer] = self._extract_insights(result.content)
        
        return insights
    
    async def _specialized_research(
        self,
        topic: str,
        socratic_chain: List[SocraticQuestion],
        writer_insights: Dict[str, List[str]]
    ) -> List[Dict[str, Any]]:
        """Deploy specialized research agents."""
        
        # Use the extreme codex swarm for deep research
        codex_result = await self.codex.run(
            topic=topic,
            num_research_agents=10,
            enable_search=False
        )
        
        # Extract research artifacts
        artifacts = []
        
        for agent in codex_result.research_artifacts:
            artifacts.append({
                "agent": agent.agent_role,
                "content": agent.content,
                "mechanisms": agent.mechanisms,
                "inversions": agent.inversions,
                "predictions": agent.predictions
            })
        
        print(f"  Collected {len(artifacts)} research artifacts")
        
        return artifacts
    
    async def _mine_contradictions(
        self,
        research_artifacts: List[Dict[str, Any]]
    ) -> List[str]:
        """Find contradictions to consensus."""
        
        contradictions = []
        
        # Extract all content
        all_content = '\n'.join([a.get("content", "") for a in research_artifacts])
        
        model = self.swarm.MODELS["premium"][0]
        
        system = "You find contradictions to what everyone believes."
        
        user = f"""Research findings:
        {all_content[:3000]}
        
        Find:
        1. Where consensus is wrong (with evidence)
        2. Where opposite is true (with numbers)
        3. Where experts miss the obvious
        
        List specific contradictions."""
        
        result = await self.swarm.call_model(
            model, system, user,
            temperature=0.7, max_tokens=800
        )
        
        if not result.error:
            lines = result.content.split('\n')
            contradictions = [l.strip() for l in lines if l.strip() and len(l.strip()) > 20]
        
        print(f"  Found {len(contradictions)} contradictions")
        
        return contradictions[:10]
    
    def _maximum_compression(
        self,
        research_artifacts: List[Dict[str, Any]],
        contradictions: List[str]
    ) -> List[KolmogorovInsight]:
        """Compress to maximum insight density."""
        
        # Collect all observations
        observations = []
        
        for artifact in research_artifacts:
            observations.extend(artifact.get("mechanisms", []))
            observations.extend(artifact.get("inversions", []))
        
        observations.extend(contradictions)
        
        # Compress into insights
        insights = []
        
        # Process in batches
        for i in range(0, len(observations), 5):
            batch = observations[i:i+5]
            if batch:
                insight = self.compressor.compress_observations(batch, max_words=15)
                insights.append(insight)
        
        # Sort by compression ratio
        insights.sort(key=lambda x: x.compression_ratio, reverse=True)
        
        print(f"  Generated {len(insights)} compressed insights")
        print(f"  Best compression: {insights[0].compression_ratio:.1f}:1" if insights else "")
        
        return insights[:10]
    
    def _extract_mechanisms(
        self,
        research_artifacts: List[Dict[str, Any]],
        compressed_insights: List[KolmogorovInsight]
    ) -> List[str]:
        """Extract core mechanisms."""
        
        mechanisms = []
        
        # From research
        for artifact in research_artifacts:
            mechanisms.extend(artifact.get("mechanisms", []))
        
        # From compressed insights
        for insight in compressed_insights:
            if insight.generating_rule:
                mechanisms.append(insight.generating_rule)
        
        # Deduplicate and filter
        seen = set()
        unique_mechanisms = []
        
        for mech in mechanisms:
            key = mech[:30].lower()
            if key not in seen and len(mech) > 10:
                seen.add(key)
                unique_mechanisms.append(mech)
        
        print(f"  Extracted {len(unique_mechanisms)} unique mechanisms")
        
        return unique_mechanisms[:20]
    
    async def _emergent_synthesis(
        self,
        compressed_insights: List[KolmogorovInsight],
        mechanisms: List[str]
    ) -> str:
        """Let thesis emerge from insights."""
        
        if not compressed_insights:
            return "No clear pattern emerged"
        
        # Best insight by compression
        best = compressed_insights[0]
        
        model = self.swarm.MODELS["premium"][0]
        
        system = "You reveal what the data shows. No narrative. Just truth."
        
        user = f"""Core insight: {best.core_statement}
        Compression: {best.compression_ratio:.1f}:1
        
        Top mechanisms:
        {chr(10).join(mechanisms[:5])}
        
        What does this reveal?
        
        Write 2-3 sentences.
        Include the most surprising number.
        State what must happen next."""
        
        result = await self.swarm.call_model(
            model, system, user,
            temperature=0.6, max_tokens=200
        )
        
        thesis = result.content if not result.error else best.core_statement
        
        print(f"  Emergent thesis: {thesis[:100]}...")
        
        return thesis
    
    async def _write_maximum_density(
        self,
        thesis: str,
        compressed_insights: List[KolmogorovInsight],
        mechanisms: List[str],
        socratic_chain: List[SocraticQuestion],
        contradictions: List[str]
    ) -> str:
        """Write with maximum insight density."""
        
        model = self.swarm.MODELS["premium"][0]
        
        # Build components
        insights_text = '\n'.join([
            f"• {i.core_statement} [{i.compression_ratio:.0f}:1]"
            for i in compressed_insights[:7]
        ])
        
        mechanisms_text = '\n'.join(mechanisms[:10])
        
        socratic_reveals = ' → '.join([q.reveals[:50] for q in socratic_chain[:5]])
        
        contradictions_text = '\n'.join(contradictions[:5])
        
        system = """Write with maximum Kolmogorov compression.
        Every sentence must change the reader's model.
        Start with most surprising number.
        No transitions. No setup. Pure mechanism."""
        
        user = f"""Thesis: {thesis}
        
        Compressed insights:
        {insights_text}
        
        Core mechanisms:
        {mechanisms_text}
        
        Socratic descent:
        {socratic_reveals}
        
        Contradictions:
        {contradictions_text}
        
        Write 1200-1800 words.
        
        Requirements:
        1. Start with number that breaks assumptions
        2. 7+ mechanisms with thresholds
        3. 3+ inversions with data
        4. 3+ falsifiable predictions
        5. Personal observation woven naturally
        6. Zero em-dashes or transitions
        7. Every paragraph reveals new mechanism
        8. End with "what proves me wrong"
        
        Maximum density. Minimum words. Maximum truth."""
        
        result = await self.swarm.call_model(
            model, system, user,
            temperature=0.7, max_tokens=3000
        )
        
        return result.content if not result.error else thesis
    
    async def _validate_and_enhance(self, article: str) -> tuple[str, Dict[str, Any]]:
        """Validate against Settlers quality and enhance if needed."""
        
        current = article
        
        for round in range(3):
            # Validate
            validation = validate_settlers_quality(current, self.thresholds)
            
            if validation.passed:
                print(f"  ✓ Passed validation on round {round+1}")
                break
            
            print(f"  Round {round+1}: {len(validation.failures)} issues")
            
            # Enhance based on failures
            model = self.swarm.MODELS["fast"][0]
            
            issues = '\n'.join(validation.failures)
            
            system = "Fix only the listed issues. Keep everything else."
            
            user = f"""Issues to fix:
            {issues}
            
            Current article:
            {current}
            
            Rules:
            - Add mechanisms/inversions/predictions as needed
            - Remove all em-dashes and transitions
            - Add personal elements naturally
            - Keep same length
            
            Return complete fixed article."""
            
            result = await self.swarm.call_model(
                model, system, user,
                temperature=0.6, max_tokens=3000
            )
            
            if not result.error:
                current = result.content
        
        # Final validation
        final_validation = validate_settlers_quality(current, self.thresholds)
        
        metrics = {
            "passed": final_validation.passed,
            "mechanisms": final_validation.mechanism_count,
            "inversions": final_validation.inversion_count,
            "predictions": final_validation.prediction_count,
            "failures": final_validation.failures,
            "score": self._calculate_quality_score(final_validation)
        }
        
        return current, metrics
    
    def _extract_reveals(self, text: str) -> str:
        """Extract what this reveals."""
        import re
        
        patterns = [
            r"reveals? (?:that )?(.+?)(?:\.|$)",
            r"shows? (?:that )?(.+?)(?:\.|$)",
            r"mechanism is (.+?)(?:\.|$)"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text.lower())
            if match:
                return match.group(1)[:100]
        
        return "underlying mechanism"
    
    def _extract_contradicts(self, text: str) -> str:
        """Extract what this contradicts."""
        import re
        
        patterns = [
            r"contradicts? (.+?)(?:\.|$)",
            r"opposite of (.+?)(?:\.|$)",
            r"not (.+?) as (?:believed|thought)"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text.lower())
            if match:
                return match.group(1)[:100]
        
        return "common assumption"
    
    def _extract_insights(self, text: str) -> List[str]:
        """Extract key insights from text."""
        
        lines = text.split('\n')
        insights = []
        
        for line in lines:
            # Keep lines with numbers or strong claims
            if any(char.isdigit() for char in line) or \
               any(word in line.lower() for word in ['actually', 'really', 'mechanism', 'causes']):
                if len(line.strip()) > 20:
                    insights.append(line.strip())
        
        return insights[:5]
    
    def _calculate_compression(
        self,
        article: str,
        research_artifacts: List[Dict[str, Any]]
    ) -> float:
        """Calculate compression ratio."""
        
        # Total research words
        research_words = sum(
            len(a.get("content", "").split())
            for a in research_artifacts
        )
        
        # Article words
        article_words = len(article.split())
        
        if article_words == 0:
            return 0.0
        
        return min(research_words / article_words, 100.0)
    
    def _calculate_quality_score(self, validation) -> float:
        """Calculate overall quality score."""
        
        score = 0.0
        
        # Mechanisms (weight: 2.0)
        score += min(validation.mechanism_count / 7, 1.0) * 2.0
        
        # Inversions (weight: 1.5)
        score += min(validation.inversion_count / 3, 1.0) * 1.5
        
        # Predictions (weight: 1.5)
        score += min(validation.prediction_count / 3, 1.0) * 1.5
        
        # Personal layer (weight: 1.0)
        if validation.confession_found or validation.admission_found:
            score += 1.0
        
        # No AI tells (weight: 2.0)
        if validation.em_dash_count == 0 and validation.transition_count == 0:
            score += 2.0
        
        # Scale to 10
        score = min(score * 1.25, 10.0)
        
        return round(score, 1)