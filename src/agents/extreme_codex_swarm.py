"""Extreme Codex-style multi-agent swarm with parallel execution and quality gates.

This system targets Settlers-level quality through:
1. Parallel research agents with specific data-hunting roles
2. Mechanism/inversion/prediction extraction in parallel
3. Multiple draft candidates with different approaches
4. Strict quality validation against Settlers metrics
5. Targeted self-correction loops
"""

import asyncio
import json
import random
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from datetime import datetime

from src.agents.openrouter_swarm import OpenRouterSwarm, SwarmResult
from src.quality.settlers_validator import (
    SettlersQualityResult,
    SettlersThresholds,
    validate_settlers_quality,
)
from src.quality.compression_scanner import scan_compression
from src.quality.surprise_detector import detect_surprise
from src.quality.vocabulary_scanner import scan_vocabulary


@dataclass
class ResearchArtifact:
    """Specialized research output from an agent."""
    agent_role: str
    model: str
    content: str
    data_points: List[Dict[str, Any]] = field(default_factory=list)
    mechanisms: List[str] = field(default_factory=list)
    inversions: List[str] = field(default_factory=list)
    predictions: List[str] = field(default_factory=list)
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())


@dataclass
class QualityMetrics:
    """Comprehensive quality metrics for article evaluation."""
    settlers: SettlersQualityResult
    compression_score: float
    surprise_score: float
    banned_words: int
    em_dashes_per_1k: float
    specific_data_count: int
    named_entities: int
    personal_touches: int
    overall_score: float = 0.0
    failures: List[str] = field(default_factory=list)


@dataclass
class ExtremePipelineResult:
    """Complete result from the extreme codex pipeline."""
    topic: str
    research_artifacts: List[ResearchArtifact]
    consolidated_mechanisms: List[str]
    consolidated_inversions: List[str]
    consolidated_predictions: List[str]
    personal_layer_elements: List[str]
    draft_candidates: List[str]
    final_article: str
    quality_metrics: QualityMetrics
    revision_history: List[Dict[str, Any]] = field(default_factory=list)
    total_attempts: int = 0
    tokens_used: int = 0
    elapsed_time: float = 0.0


class ExtremeCodexSwarm:
    """Ultra-high-quality article generation using parallel swarms."""
    
    # Enhanced agent profiles with specific data-hunting roles
    SPECIALIST_AGENTS = [
        {
            "role": "Threshold Hunter",
            "focus": "Find every number with a threshold. What percentage triggers change? What count causes collapse? Find the 7%, 147x, $43M per employee numbers.",
            "extraction": "mechanisms"
        },
        {
            "role": "Paradox Detective", 
            "focus": "Find contradictions with numbers. Where does more lead to less? What rises while another falls? Find income vs holdings paradoxes.",
            "extraction": "inversions"
        },
        {
            "role": "Timeline Predictor",
            "focus": "Make falsifiable predictions with dates and quantities. By Q4 2027, what measurable change? Within 18 months, what threshold crossed?",
            "extraction": "predictions"
        },
        {
            "role": "Mechanism Archaeologist",
            "focus": "Uncover causal chains. Not correlation - causation. What mechanical process makes this inevitable? Find the physics.",
            "extraction": "mechanisms"
        },
        {
            "role": "Visibility Calculator",
            "focus": "Calculate exact visibility percentages. Who sees what? 7% visibility means 93% invisible. Find the observation thresholds.",
            "extraction": "mechanisms"
        },
        {
            "role": "Generation Gap Analyst",
            "focus": "Find the 18-year gaps, the generational divides. What changed between cohorts? Specific years, specific percentages.",
            "extraction": "inversions"
        },
        {
            "role": "Network Physicist",
            "focus": "Model as contagion physics. R0 values, transmission rates, critical mass thresholds. When does 1 become 100 become 10,000?",
            "extraction": "mechanisms"
        },
        {
            "role": "Capital Flow Tracer",
            "focus": "Follow the money with exact amounts. $13B profit from 300 employees. $46T in volume. Who captures value, who doesn't?",
            "extraction": "mechanisms"
        },
        {
            "role": "Neuroscience Mapper",
            "focus": "Which brain regions activate? Dopamine at what threshold? Mirror neurons at what observation count? Biological mechanisms only.",
            "extraction": "mechanisms"
        },
        {
            "role": "Historical Rhymer",
            "focus": "Find exact historical parallels with dates and numbers. When did this precise pattern occur before? Specific years, specific outcomes.",
            "extraction": "predictions"
        }
    ]
    
    def __init__(
        self,
        swarm: OpenRouterSwarm,
        thresholds: Optional[SettlersThresholds] = None,
        max_revision_rounds: int = 5,
        parallel_drafts: int = 5,
        quality_target: float = 8.5
    ):
        self.swarm = swarm
        self.thresholds = thresholds or SettlersThresholds(
            min_mechanisms=7,
            min_inversions=3,
            min_predictions=3,
            min_inclusion_pronouns=5,
            require_confession=True
        )
        self.max_revision_rounds = max_revision_rounds
        self.parallel_drafts = parallel_drafts
        self.quality_target = quality_target
    
    async def run(
        self, 
        topic: str,
        num_research_agents: int = 10,
        enable_search: bool = True
    ) -> ExtremePipelineResult:
        """Execute the complete extreme pipeline."""
        
        start_time = datetime.utcnow()
        
        # Phase 1: Parallel specialized research
        print(f"Phase 1: Deploying {num_research_agents} specialist agents...")
        research_artifacts = await self._parallel_research(topic, num_research_agents, enable_search)
        
        # Phase 2: Extract and consolidate mechanisms/inversions/predictions
        print("Phase 2: Extracting data mechanisms...")
        consolidated = await self._consolidate_insights(research_artifacts)
        
        # Phase 3: Build personal layer
        print("Phase 3: Building personal layer...")
        personal_layer = await self._build_personal_layer(topic, research_artifacts)
        
        # Phase 4: Generate parallel draft candidates
        print(f"Phase 4: Generating {self.parallel_drafts} draft candidates...")
        draft_candidates = await self._parallel_drafting(
            topic,
            research_artifacts,
            consolidated,
            personal_layer
        )
        
        # Phase 5: Evaluate and select best draft
        print("Phase 5: Evaluating drafts...")
        best_draft, metrics = self._evaluate_drafts(draft_candidates)
        
        # Phase 6: Revision loops until quality target met
        print("Phase 6: Quality enhancement loops...")
        final_article, final_metrics, revision_history = await self._revision_loop(
            best_draft,
            metrics,
            consolidated,
            personal_layer
        )
        
        elapsed = (datetime.utcnow() - start_time).total_seconds()
        
        return ExtremePipelineResult(
            topic=topic,
            research_artifacts=research_artifacts,
            consolidated_mechanisms=consolidated["mechanisms"],
            consolidated_inversions=consolidated["inversions"],
            consolidated_predictions=consolidated["predictions"],
            personal_layer_elements=personal_layer,
            draft_candidates=draft_candidates,
            final_article=final_article,
            quality_metrics=final_metrics,
            revision_history=revision_history,
            total_attempts=len(revision_history) + 1,
            tokens_used=sum(r.tokens_used for r in research_artifacts if hasattr(r, 'tokens_used')),
            elapsed_time=elapsed
        )
    
    async def _parallel_research(
        self,
        topic: str,
        num_agents: int,
        enable_search: bool
    ) -> List[ResearchArtifact]:
        """Deploy parallel specialized research agents."""
        
        selected_agents = random.sample(
            self.SPECIALIST_AGENTS,
            min(num_agents, len(self.SPECIALIST_AGENTS))
        )
        
        tasks = []
        for agent in selected_agents:
            # Assign model based on role complexity
            if "Physicist" in agent["role"] or "Calculator" in agent["role"]:
                model = random.choice(self.swarm.MODELS["premium"])
            elif "Detective" in agent["role"] or "Archaeologist" in agent["role"]:
                model = random.choice(self.swarm.MODELS["premium"])
            else:
                model = random.choice(self.swarm.MODELS["fast"])
            
            system = f"You are a {agent['role']}. {agent['focus']} Return specific data only."
            
            user = f"""Research topic: {topic}

Your specialized lens: {agent['focus']}

Requirements:
1. Find specific numbers with units ($, %, counts)
2. Find thresholds and tipping points
3. Find causal mechanisms, not correlations
4. Find counterintuitive inversions
5. Make falsifiable predictions with dates

Format your response as:
- Data points with sources
- Mechanisms with thresholds
- Inversions with numbers
- Predictions with timeframes

No narratives. No stories. Just mechanisms and data."""
            
            tasks.append(self._research_task(model, system, user, agent))
        
        # Add web search agent if enabled
        if enable_search:
            search_task = self._web_search_task(topic)
            tasks.append(search_task)
        
        results = await asyncio.gather(*tasks)
        return [r for r in results if r and r.content]
    
    async def _research_task(
        self,
        model: str,
        system: str,
        user: str,
        agent: Dict[str, str]
    ) -> ResearchArtifact:
        """Execute a single research task."""
        
        result = await self.swarm.call_model(
            model,
            system,
            user,
            temperature=0.7,
            max_tokens=2000
        )
        
        if result.error:
            return ResearchArtifact(
                agent_role=agent["role"],
                model=model,
                content=""
            )
        
        # Extract structured data from response
        artifact = ResearchArtifact(
            agent_role=agent["role"],
            model=model,
            content=result.content
        )
        
        # Parse out mechanisms, inversions, predictions
        content_lower = result.content.lower()
        
        if agent["extraction"] == "mechanisms":
            artifact.mechanisms = self._extract_mechanisms(result.content)
        elif agent["extraction"] == "inversions":
            artifact.inversions = self._extract_inversions(result.content)
        elif agent["extraction"] == "predictions":
            artifact.predictions = self._extract_predictions(result.content)
        
        return artifact
    
    async def _web_search_task(self, topic: str) -> ResearchArtifact:
        """Perform web search for current data."""
        # Placeholder for actual web search integration
        return ResearchArtifact(
            agent_role="Web Searcher",
            model="search",
            content=f"Current data on {topic}"
        )
    
    async def _consolidate_insights(
        self,
        artifacts: List[ResearchArtifact]
    ) -> Dict[str, List[str]]:
        """Consolidate and deduplicate insights from all agents."""
        
        all_mechanisms = []
        all_inversions = []
        all_predictions = []
        
        for artifact in artifacts:
            all_mechanisms.extend(artifact.mechanisms)
            all_inversions.extend(artifact.inversions)
            all_predictions.extend(artifact.predictions)
        
        # Deduplicate while preserving best examples
        mechanisms = self._deduplicate_insights(all_mechanisms)[:15]
        inversions = self._deduplicate_insights(all_inversions)[:8]
        predictions = self._deduplicate_insights(all_predictions)[:8]
        
        return {
            "mechanisms": mechanisms,
            "inversions": inversions,
            "predictions": predictions
        }
    
    async def _build_personal_layer(
        self,
        topic: str,
        artifacts: List[ResearchArtifact]
    ) -> List[str]:
        """Build authentic personal layer elements."""
        
        model = random.choice(self.swarm.MODELS["premium"])
        
        system = "You are building an authentic personal voice layer. No AI tells."
        
        research_context = "\n".join([a.content[:500] for a in artifacts[:3]])
        
        user = f"""Topic: {topic}

Context from research:
{research_context}

Generate 8 personal layer elements:
1. A confession starting with "I remember" or "I got"
2. An admission starting with "I was wrong" or "I didn't understand"
3. A specific memory with a detail (screen name, forum, game)
4. An insider reference only community members would know
5. A "we/us/our" statement showing belonging
6. A specific failure or mistake you made
7. A detail about learning (where you first understood X)
8. A callback to the personal opening later in the piece

Requirements:
- Ultra-specific details
- No generic statements
- Include numbers where possible
- No em-dashes or transitions
- Short, punchy sentences

Return as 8 separate lines."""
        
        result = await self.swarm.call_model(
            model,
            system,
            user,
            temperature=0.8,
            max_tokens=800
        )
        
        if result.error:
            return []
        
        return [line.strip() for line in result.content.split('\n') if line.strip()]
    
    async def _parallel_drafting(
        self,
        topic: str,
        artifacts: List[ResearchArtifact],
        consolidated: Dict[str, List[str]],
        personal_layer: List[str]
    ) -> List[str]:
        """Generate multiple draft candidates in parallel."""
        
        # Different drafting strategies
        strategies = [
            {
                "approach": "Mechanism-First",
                "instruction": "Start with the strongest mechanism. Build everything from causation.",
                "model": random.choice(self.swarm.MODELS["premium"])
            },
            {
                "approach": "Inversion-Led",
                "instruction": "Open with the biggest paradox. Structure around inversions.",
                "model": random.choice(self.swarm.MODELS["premium"])
            },
            {
                "approach": "Personal-Embedded",
                "instruction": "Weave personal elements throughout. No separate personal section.",
                "model": random.choice(self.swarm.MODELS["premium"])
            },
            {
                "approach": "Data-Density",
                "instruction": "Maximum data per paragraph. Every sentence must have a number.",
                "model": random.choice(self.swarm.MODELS["specialized"])
            },
            {
                "approach": "Prediction-Focused",
                "instruction": "Build toward falsifiable predictions. Everything supports the forecast.",
                "model": random.choice(self.swarm.MODELS["fast"])
            }
        ]
        
        tasks = []
        for i, strategy in enumerate(strategies[:self.parallel_drafts]):
            task = self._draft_task(
                topic,
                artifacts,
                consolidated,
                personal_layer,
                strategy
            )
            tasks.append(task)
        
        drafts = await asyncio.gather(*tasks)
        return [d for d in drafts if d and len(d) > 500]
    
    async def _draft_task(
        self,
        topic: str,
        artifacts: List[ResearchArtifact],
        consolidated: Dict[str, List[str]],
        personal_layer: List[str],
        strategy: Dict[str, str]
    ) -> str:
        """Generate a single draft with a specific strategy."""
        
        # Combine research insights
        research_text = "\n\n".join([
            f"[{a.agent_role}]\n{a.content[:1500]}"
            for a in artifacts[:5]
        ])
        
        mechanisms_text = "\n".join(consolidated["mechanisms"][:10])
        inversions_text = "\n".join(consolidated["inversions"][:5])
        predictions_text = "\n".join(consolidated["predictions"][:5])
        personal_text = "\n".join(personal_layer[:5])
        
        system = f"You are writing with {strategy['approach']} strategy. {strategy['instruction']}"
        
        user = f"""Topic: {topic}

Research findings:
{research_text}

Mechanisms to include (use at least 7):
{mechanisms_text}

Inversions to include (use at least 2):
{inversions_text}

Predictions to include (use at least 2):
{predictions_text}

Personal elements to weave in:
{personal_text}

Write 1500-2000 words following these rules:
1. Include at least 7 mechanism sentences with thresholds and causal verbs
2. Include at least 2 inversion sentences with specific numbers
3. Include at least 3 falsifiable predictions with dates/timeframes
4. Embed personal elements naturally (no separate section)
5. Every paragraph must have specific numbers
6. NO em-dashes, NO transitions like "however/moreover", NO narrative language
7. NO bullet points or lists
8. Start strong with a mechanism or personal hook
9. End with prediction or "what proves me wrong"

Return only the article text."""
        
        result = await self.swarm.call_model(
            strategy["model"],
            system,
            user,
            temperature=0.75,
            max_tokens=3000
        )
        
        return result.content if not result.error else ""
    
    def _evaluate_drafts(self, drafts: List[str]) -> tuple[str, QualityMetrics]:
        """Evaluate all drafts and select the best one."""
        
        evaluations = []
        for draft in drafts:
            metrics = self._calculate_metrics(draft)
            evaluations.append((draft, metrics))
        
        # Sort by quality score
        evaluations.sort(key=lambda x: x[1].overall_score, reverse=True)
        
        return evaluations[0] if evaluations else ("", self._empty_metrics())
    
    def _calculate_metrics(self, text: str) -> QualityMetrics:
        """Calculate comprehensive quality metrics for text."""
        
        settlers = validate_settlers_quality(text, self.thresholds)
        compression = scan_compression(text)
        surprise = detect_surprise(text)
        vocabulary = scan_vocabulary(text)
        
        # Count specific data points
        import re
        number_pattern = re.compile(r'\$[\d,]+[BMK]?|\d+%|\d{1,3}(?:,\d{3})*')
        specific_data = len(number_pattern.findall(text))
        
        # Count named entities
        entity_pattern = re.compile(r'[A-Z][a-z]+ [A-Z][a-z]+|[A-Z]{2,}')
        named_entities = len(entity_pattern.findall(text))
        
        # Count personal touches
        personal_pattern = re.compile(r'\b(I|we|us|our)\b', re.IGNORECASE)
        personal_touches = len(personal_pattern.findall(text))
        
        # Calculate overall score
        score = 0.0
        score += min(settlers.mechanism_count / self.thresholds.min_mechanisms, 1.0) * 2.0
        score += min(settlers.inversion_count / self.thresholds.min_inversions, 1.0) * 1.5
        score += min(settlers.prediction_count / self.thresholds.min_predictions, 1.0) * 1.5
        score += (1.0 if settlers.confession_found else 0.0) * 1.0
        score += min(surprise.overall, 1.0) * 1.5
        score += min(compression.overall_score / 10.0, 1.0) * 1.5
        score += min(specific_data / 50.0, 1.0) * 1.0
        score -= vocabulary.banned_word_count * 0.2
        score -= vocabulary.em_dashes_per_1k * 0.5
        
        # Build failure list
        failures = list(settlers.failures)
        if surprise.overall < 0.6:
            failures.append(f"Low surprise: {surprise.overall:.2f}")
        if compression.overall_score < 7.0:
            failures.append(f"Low compression: {compression.overall_score:.1f}")
        if specific_data < 20:
            failures.append(f"Insufficient data points: {specific_data}")
        
        return QualityMetrics(
            settlers=settlers,
            compression_score=compression.overall_score,
            surprise_score=surprise.overall,
            banned_words=vocabulary.banned_word_count,
            em_dashes_per_1k=vocabulary.em_dashes_per_1k,
            specific_data_count=specific_data,
            named_entities=named_entities,
            personal_touches=personal_touches,
            overall_score=round(score, 2),
            failures=failures
        )
    
    async def _revision_loop(
        self,
        draft: str,
        metrics: QualityMetrics,
        consolidated: Dict[str, List[str]],
        personal_layer: List[str]
    ) -> tuple[str, QualityMetrics, List[Dict[str, Any]]]:
        """Iteratively revise draft until quality target is met."""
        
        current_draft = draft
        current_metrics = metrics
        revision_history = []
        
        for round_num in range(self.max_revision_rounds):
            if current_metrics.overall_score >= self.quality_target and not current_metrics.failures:
                break
            
            print(f"  Revision round {round_num + 1}: Score {current_metrics.overall_score:.2f}, Failures: {len(current_metrics.failures)}")
            
            # Generate targeted revisions
            revisions = await self._targeted_revisions(
                current_draft,
                current_metrics,
                consolidated,
                personal_layer
            )
            
            # Evaluate revisions
            best_revision = current_draft
            best_metrics = current_metrics
            
            for revision in revisions:
                revision_metrics = self._calculate_metrics(revision)
                if revision_metrics.overall_score > best_metrics.overall_score:
                    best_revision = revision
                    best_metrics = revision_metrics
            
            # Record history
            revision_history.append({
                "round": round_num + 1,
                "score_before": current_metrics.overall_score,
                "score_after": best_metrics.overall_score,
                "failures_before": len(current_metrics.failures),
                "failures_after": len(best_metrics.failures),
                "improvements": list(set(current_metrics.failures) - set(best_metrics.failures))
            })
            
            current_draft = best_revision
            current_metrics = best_metrics
        
        return current_draft, current_metrics, revision_history
    
    async def _targeted_revisions(
        self,
        draft: str,
        metrics: QualityMetrics,
        consolidated: Dict[str, List[str]],
        personal_layer: List[str]
    ) -> List[str]:
        """Generate targeted revisions based on specific failures."""
        
        tasks = []
        
        # Fix mechanism deficiency
        if metrics.settlers.mechanism_count < self.thresholds.min_mechanisms:
            needed = self.thresholds.min_mechanisms - metrics.settlers.mechanism_count
            task = self._revision_task(
                draft,
                "Mechanism Injector",
                f"Add {needed} mechanism sentences with thresholds and causal verbs",
                consolidated["mechanisms"]
            )
            tasks.append(task)
        
        # Fix inversion deficiency
        if metrics.settlers.inversion_count < self.thresholds.min_inversions:
            needed = self.thresholds.min_inversions - metrics.settlers.inversion_count
            task = self._revision_task(
                draft,
                "Inversion Enhancer",
                f"Add {needed} inversion sentences with paradoxes and numbers",
                consolidated["inversions"]
            )
            tasks.append(task)
        
        # Fix prediction deficiency
        if metrics.settlers.prediction_count < self.thresholds.min_predictions:
            needed = self.thresholds.min_predictions - metrics.settlers.prediction_count
            task = self._revision_task(
                draft,
                "Prediction Builder",
                f"Add {needed} falsifiable predictions with dates and quantities",
                consolidated["predictions"]
            )
            tasks.append(task)
        
        # Fix personal layer
        if not metrics.settlers.confession_found or metrics.personal_touches < 10:
            task = self._revision_task(
                draft,
                "Personal Authenticator",
                "Add confession/admission and we/us/our language naturally",
                personal_layer
            )
            tasks.append(task)
        
        # Fix AI tells
        if metrics.banned_words > 0 or metrics.em_dashes_per_1k > 0:
            task = self._revision_task(
                draft,
                "AI Tell Eliminator",
                "Remove all em-dashes, transitions, and AI language",
                []
            )
            tasks.append(task)
        
        # Boost surprise
        if metrics.surprise_score < 0.7:
            task = self._revision_task(
                draft,
                "Surprise Amplifier",
                "Add surprising inversions and unexpected data points",
                consolidated["inversions"]
            )
            tasks.append(task)
        
        if not tasks:
            return [draft]
        
        results = await asyncio.gather(*tasks)
        return [r for r in results if r and len(r) > 500]
    
    async def _revision_task(
        self,
        draft: str,
        role: str,
        instruction: str,
        reference_data: List[str]
    ) -> str:
        """Execute a single revision task."""
        
        model = random.choice(self.swarm.MODELS["fast"])
        
        system = f"You are a {role}. Fix only the specified issues. Keep everything else."
        
        reference_text = "\n".join(reference_data[:5]) if reference_data else ""
        
        user = f"""Task: {instruction}

Reference data to incorporate:
{reference_text}

Current draft to revise:
{draft}

Rules:
1. Fix only the specified issue
2. Keep the overall structure and voice
3. NO em-dashes, NO transition words, NO narrative language
4. Maintain the same length (within 5%)
5. Keep all existing good elements

Return the complete revised article."""
        
        result = await self.swarm.call_model(
            model,
            system,
            user,
            temperature=0.6,
            max_tokens=3000
        )
        
        return result.content if not result.error else draft
    
    def _extract_mechanisms(self, text: str) -> List[str]:
        """Extract mechanism statements from text."""
        import re
        
        lines = text.split('\n')
        mechanisms = []
        
        threshold_pattern = re.compile(r'(?:>=|<=|>|<|%|\$[\d,]+[BMK]?|\d+)')
        causal_pattern = re.compile(r'(?:causes?|triggers?|forces?|drives?|creates?|leads to)')
        
        for line in lines:
            if threshold_pattern.search(line) and causal_pattern.search(line):
                mechanisms.append(line.strip())
        
        return mechanisms[:15]
    
    def _extract_inversions(self, text: str) -> List[str]:
        """Extract inversion statements from text."""
        import re
        
        lines = text.split('\n')
        inversions = []
        
        inversion_pattern = re.compile(
            r'(?:inverse|opposite|reverses?|flips?|paradox|counterintuitive|'
            r'more.*less|less.*more|rises.*falls)'
        )
        number_pattern = re.compile(r'\d+|%|\$')
        
        for line in lines:
            if inversion_pattern.search(line.lower()) and number_pattern.search(line):
                inversions.append(line.strip())
        
        return inversions[:8]
    
    def _extract_predictions(self, text: str) -> List[str]:
        """Extract prediction statements from text."""
        import re
        
        lines = text.split('\n')
        predictions = []
        
        time_pattern = re.compile(r'(?:202\d|Q[1-4]|months?|years?|within|by)')
        predict_pattern = re.compile(r'(?:will|won\'t|expect|predict|forecast)')
        number_pattern = re.compile(r'\d+|%|\$')
        
        for line in lines:
            if (time_pattern.search(line) and 
                predict_pattern.search(line.lower()) and 
                number_pattern.search(line)):
                predictions.append(line.strip())
        
        return predictions[:8]
    
    def _deduplicate_insights(self, insights: List[str]) -> List[str]:
        """Deduplicate while preserving the best examples."""
        
        seen = set()
        unique = []
        
        for insight in insights:
            # Create a normalized key for deduplication
            key = ''.join(c.lower() for c in insight if c.isalnum())[:50]
            if key not in seen:
                seen.add(key)
                unique.append(insight)
        
        return unique
    
    def _empty_metrics(self) -> QualityMetrics:
        """Return empty metrics for failed drafts."""
        
        empty_settlers = validate_settlers_quality("", self.thresholds)
        
        return QualityMetrics(
            settlers=empty_settlers,
            compression_score=0.0,
            surprise_score=0.0,
            banned_words=0,
            em_dashes_per_1k=0.0,
            specific_data_count=0,
            named_entities=0,
            personal_touches=0,
            overall_score=0.0,
            failures=["No draft generated"]
        )