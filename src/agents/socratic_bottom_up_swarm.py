"""Socratic Bottom-Up Swarm: Deep research → Emergent insights → Maximum compression.

This system reverse-engineers techniques from the best writers:
- Paul Graham: First principles reasoning, contradiction hunting
- Nassim Taleb: Antifragility, convexity, skin in the game detection
- Matt Levine: Finding absurdity in mundane, mechanism explanation
- Patrick McKenzie: System design revelation, hidden infrastructure
- Byrne Hobart: Historical rhyming, capital flow analysis
- Venkatesh Rao: 2x2 matrices, narrative violation, conceptual inversions

The pipeline:
1. SOCRATIC QUESTIONING: Why 5 times, what breaks, who benefits
2. DATA ARCHAEOLOGY: Find buried numbers, hidden mechanisms  
3. PATTERN BREAKING: Where consensus is wrong
4. KOLMOGOROV COMPRESSION: Find the shortest true description
5. EMERGENT SYNTHESIS: Let insights arise, don't force narrative
"""

import asyncio
import json
import re
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime

from src.agents.openrouter_swarm import OpenRouterSwarm, SwarmResult


@dataclass
class SocraticQuestion:
    """A question that reveals mechanism."""
    question: str
    answer: str
    reveals: str  # What mechanism this reveals
    contradicts: str  # What assumption this breaks
    depth: int  # How many "why"s deep


@dataclass  
class DeepInsight:
    """An insight with maximum compression."""
    insight: str
    compression_ratio: float  # How much this explains vs word count
    supporting_data: List[str]
    contradictions: List[str]
    predictions: List[str]
    kolmogorov_length: int  # Shortest possible description


@dataclass
class BottomUpResult:
    """Complete bottom-up research and synthesis."""
    topic: str
    socratic_chain: List[SocraticQuestion]
    raw_discoveries: List[Dict[str, Any]]
    deep_insights: List[DeepInsight]
    emergent_thesis: str
    final_article: str
    compression_score: float
    tokens_used: int


class SocraticBottomUpSwarm:
    """Pure bottom-up: Research → Questions → Insights → Compression → Article."""
    
    # Writer-specific analysis techniques
    WRITER_TECHNIQUES = {
        "paul_graham": {
            "method": "First principles breakdown",
            "questions": [
                "What would this look like if we started from scratch?",
                "What's the simplest version that could possibly work?",
                "Where is everyone making the same mistake?",
                "What would a 10-year-old understand that experts miss?"
            ]
        },
        "nassim_taleb": {
            "method": "Antifragility and skin detection",
            "questions": [
                "Who has skin in the game vs who is selling options?",
                "What gets stronger under stress vs breaks?",
                "Where is the hidden optionality?",
                "What's the fat tail everyone ignores?"
            ]
        },
        "matt_levine": {
            "method": "Absurdity in the mundane",
            "questions": [
                "What's the funniest possible explanation that's also true?",
                "Where does the official story not match the incentives?",
                "What would aliens find bizarre about this?",
                "How is this both legal and insane?"
            ]
        },
        "patrick_mckenzie": {
            "method": "Hidden infrastructure revelation",
            "questions": [
                "What systems run this that nobody sees?",
                "Where's the SQL database doing the real work?",
                "What would break if one person quit?",
                "How does the sausage actually get made?"
            ]
        },
        "byrne_hobart": {
            "method": "Historical pattern matching",
            "questions": [
                "When has exactly this happened before?",
                "What's the 1870s/1920s/1970s version?",
                "Which empire collapsed this way?",
                "What rhymes but doesn't repeat?"
            ]
        },
        "venkatesh_rao": {
            "method": "2x2 matrices and narrative violation",
            "questions": [
                "What are the two axes that explain everything?",
                "Where does the narrative break down?",
                "What's the liminal space between categories?",
                "How is this both true and its opposite?"
            ]
        }
    }
    
    # Socratic depth levels
    SOCRATIC_LEVELS = [
        "Surface: What is claimed?",
        "Mechanism: How does it actually work?",
        "Incentive: Who benefits from this working this way?",
        "Historical: When did this pattern emerge?",
        "Philosophical: What does this reveal about human nature?",
        "Prediction: What must happen next if this is true?"
    ]
    
    def __init__(
        self,
        swarm: OpenRouterSwarm,
        max_socratic_depth: int = 5,
        compression_target: float = 10.0,  # 10:1 insight to words ratio
        writer_styles: List[str] = None
    ):
        self.swarm = swarm
        self.max_socratic_depth = max_socratic_depth
        self.compression_target = compression_target
        self.writer_styles = writer_styles or ["paul_graham", "matt_levine", "byrne_hobart"]
    
    async def run(self, topic: str) -> BottomUpResult:
        """Execute pure bottom-up discovery process."""
        
        print(f"🔬 SOCRATIC BOTTOM-UP DISCOVERY")
        print(f"📝 Topic: {topic}")
        print("=" * 60)
        
        # Phase 1: Socratic questioning cascade
        print("\n🤔 Phase 1: Socratic Questioning...")
        socratic_chain = await self._socratic_cascade(topic)
        
        # Phase 2: Deep research with writer-specific lenses  
        print("\n🔍 Phase 2: Multi-lens Deep Research...")
        raw_discoveries = await self._deep_research(topic, socratic_chain)
        
        # Phase 3: Pattern breaking and contradiction finding
        print("\n⚡ Phase 3: Finding Contradictions...")
        contradictions = await self._find_contradictions(raw_discoveries)
        
        # Phase 4: Kolmogorov compression - find shortest truth
        print("\n🗜️ Phase 4: Kolmogorov Compression...")
        deep_insights = await self._compress_insights(raw_discoveries, contradictions)
        
        # Phase 5: Emergent synthesis - let thesis arise
        print("\n🌱 Phase 5: Emergent Synthesis...")
        emergent_thesis = await self._emergent_synthesis(deep_insights)
        
        # Phase 6: Write with maximum density
        print("\n✍️ Phase 6: High-Density Writing...")
        final_article = await self._write_compressed(
            emergent_thesis,
            deep_insights,
            socratic_chain
        )
        
        # Calculate compression score
        compression_score = self._calculate_compression(final_article, raw_discoveries)
        
        return BottomUpResult(
            topic=topic,
            socratic_chain=socratic_chain,
            raw_discoveries=raw_discoveries,
            deep_insights=deep_insights,
            emergent_thesis=emergent_thesis,
            final_article=final_article,
            compression_score=compression_score,
            tokens_used=0  # Would track in production
        )
    
    async def _socratic_cascade(self, topic: str) -> List[SocraticQuestion]:
        """Ask why recursively until we hit mechanism."""
        
        questions = []
        current_question = f"What is really happening with {topic}?"
        
        for depth in range(self.max_socratic_depth):
            # Ask the question using a premium model
            model = self.swarm.MODELS["premium"][0]
            
            system = f"""You are a Socratic questioner at depth {depth+1}.
            Previous questions: {[q.question for q in questions]}
            
            Rules:
            1. Answer with mechanisms and data, not descriptions
            2. Find what contradicts common belief
            3. Identify who benefits and who loses
            4. Use specific numbers and thresholds
            5. No narratives, only mechanisms"""
            
            user = f"Question: {current_question}\n\nProvide:\n1. Direct answer with data\n2. What this reveals\n3. What assumption this breaks\n4. Next deeper question"
            
            result = await self.swarm.call_model(
                model, system, user,
                temperature=0.7, max_tokens=1000
            )
            
            if result.error:
                break
            
            # Parse response
            lines = result.content.split('\n')
            answer = lines[0] if lines else ""
            reveals = self._extract_revelation(result.content)
            contradicts = self._extract_contradiction(result.content)
            
            questions.append(SocraticQuestion(
                question=current_question,
                answer=answer,
                reveals=reveals,
                contradicts=contradicts,
                depth=depth
            ))
            
            # Generate next question
            current_question = await self._next_why(answer, reveals)
            
            # Stop if we hit bedrock
            if "physics" in reveals.lower() or "thermodynamics" in reveals.lower():
                break
        
        return questions
    
    async def _deep_research(
        self,
        topic: str,
        socratic_chain: List[SocraticQuestion]
    ) -> List[Dict[str, Any]]:
        """Research using each writer's specific technique."""
        
        discoveries = []
        tasks = []
        
        for style in self.writer_styles:
            technique = self.WRITER_TECHNIQUES.get(style, {})
            if not technique:
                continue
            
            for question in technique.get("questions", []):
                task = self._research_with_lens(
                    topic, 
                    question,
                    technique["method"],
                    style,
                    socratic_chain
                )
                tasks.append(task)
        
        results = await asyncio.gather(*tasks)
        
        for result in results:
            if result:
                discoveries.append(result)
        
        return discoveries
    
    async def _research_with_lens(
        self,
        topic: str,
        question: str,
        method: str,
        writer_style: str,
        socratic_chain: List[SocraticQuestion]
    ) -> Dict[str, Any]:
        """Research through a specific writer's lens."""
        
        model = random.choice(self.swarm.MODELS["premium"])
        
        context = "\n".join([
            f"Q{q.depth}: {q.question} → {q.reveals}"
            for q in socratic_chain[:3]
        ])
        
        system = f"""You are researching like {writer_style.replace('_', ' ').title()}.
        Method: {method}
        
        Find:
        1. Specific mechanisms with numbers
        2. Hidden incentive structures  
        3. Historical parallels with dates
        4. Contradictions to consensus
        5. Absurdities that are true"""
        
        user = f"""Topic: {topic}
        
        Socratic context:
        {context}
        
        Specific question: {question}
        
        Research this deeply. Find:
        - Exact numbers, thresholds, percentages
        - Who wins and loses (names, amounts)
        - When this pattern occurred before
        - What everyone believes that's wrong
        - The shortest true explanation
        
        No narratives. Only mechanisms and data."""
        
        result = await self.swarm.call_model(
            model, system, user,
            temperature=0.8, max_tokens=2000
        )
        
        if result.error:
            return {}
        
        return {
            "writer_style": writer_style,
            "question": question,
            "content": result.content,
            "mechanisms": self._extract_mechanisms(result.content),
            "numbers": self._extract_numbers(result.content),
            "contradictions": self._extract_contradictions(result.content)
        }
    
    async def _find_contradictions(
        self,
        discoveries: List[Dict[str, Any]]
    ) -> List[str]:
        """Find where different analyses contradict each other."""
        
        contradictions = []
        
        # Compare each pair of discoveries
        for i, disc1 in enumerate(discoveries):
            for disc2 in discoveries[i+1:]:
                # Check if mechanisms conflict
                mechs1 = set(disc1.get("mechanisms", []))
                mechs2 = set(disc2.get("mechanisms", []))
                
                # Look for opposite claims
                content1 = disc1.get("content", "").lower()
                content2 = disc2.get("content", "").lower()
                
                if ("increases" in content1 and "decreases" in content2) or \
                   ("causes" in content1 and "prevents" in content2):
                    contradiction = f"{disc1['writer_style']} says X, {disc2['writer_style']} says NOT X"
                    contradictions.append(contradiction)
        
        # Find consensus-breaking insights
        model = self.swarm.MODELS["premium"][0]
        
        all_content = "\n---\n".join([d.get("content", "") for d in discoveries])
        
        system = "You find where discoveries contradict conventional wisdom."
        
        user = f"""Discoveries:
        {all_content}
        
        Find:
        1. Where these contradict common belief
        2. Where they contradict each other
        3. What everyone assumes that's false
        
        List specific contradictions with evidence."""
        
        result = await self.swarm.call_model(
            model, system, user,
            temperature=0.7, max_tokens=1000
        )
        
        if not result.error:
            contradictions.extend(result.content.split('\n'))
        
        return contradictions
    
    async def _compress_insights(
        self,
        discoveries: List[Dict[str, Any]],
        contradictions: List[str]
    ) -> List[DeepInsight]:
        """Compress findings to maximum insight density."""
        
        insights = []
        
        # Extract all mechanisms and data
        all_mechanisms = []
        all_numbers = []
        
        for disc in discoveries:
            all_mechanisms.extend(disc.get("mechanisms", []))
            all_numbers.extend(disc.get("numbers", []))
        
        # Find the shortest description that explains the most
        model = self.swarm.MODELS["premium"][0]
        
        system = """You are a Kolmogorov compressor.
        Find the SHORTEST true statement that explains the MOST observations.
        
        Compression rules:
        1. One sentence that explains 10+ observations
        2. Must include specific threshold or number
        3. Must make testable prediction
        4. Must contradict something widely believed"""
        
        user = f"""Mechanisms found:
        {chr(10).join(all_mechanisms[:20])}
        
        Numbers found:
        {chr(10).join(all_numbers[:20])}
        
        Contradictions:
        {chr(10).join(contradictions[:10])}
        
        Compress into 3-5 maximum-density insights.
        Each insight must explain multiple observations in fewest words."""
        
        result = await self.swarm.call_model(
            model, system, user,
            temperature=0.6, max_tokens=800
        )
        
        if not result.error:
            insight_lines = result.content.split('\n')
            
            for line in insight_lines:
                if len(line.strip()) > 10:
                    # Calculate compression ratio
                    observations_explained = len([m for m in all_mechanisms if self._relates_to(line, m)])
                    compression_ratio = observations_explained / len(line.split())
                    
                    insights.append(DeepInsight(
                        insight=line.strip(),
                        compression_ratio=compression_ratio,
                        supporting_data=all_numbers[:5],
                        contradictions=contradictions[:3],
                        predictions=self._derive_predictions(line),
                        kolmogorov_length=len(line.split())
                    ))
        
        # Sort by compression ratio
        insights.sort(key=lambda x: x.compression_ratio, reverse=True)
        
        return insights[:5]
    
    async def _emergent_synthesis(
        self,
        insights: List[DeepInsight]
    ) -> str:
        """Let the thesis emerge from insights, don't force it."""
        
        # Find the insight that explains the most
        best_insight = max(insights, key=lambda x: x.compression_ratio) if insights else None
        
        if not best_insight:
            return "No clear thesis emerged"
        
        # Expand the best insight slightly
        model = self.swarm.MODELS["premium"][0]
        
        system = """You reveal what emerges from the data.
        Don't add narrative. Don't smooth edges.
        State what is, with numbers."""
        
        user = f"""Core insight: {best_insight.insight}
        
        Supporting data: {', '.join(best_insight.supporting_data[:10])}
        
        Contradictions revealed: {', '.join(best_insight.contradictions[:5])}
        
        Write the emergent thesis in 2-3 sentences.
        Include the most surprising number.
        End with what this predicts."""
        
        result = await self.swarm.call_model(
            model, system, user,
            temperature=0.5, max_tokens=300
        )
        
        return result.content if not result.error else best_insight.insight
    
    async def _write_compressed(
        self,
        thesis: str,
        insights: List[DeepInsight],
        socratic_chain: List[SocraticQuestion]
    ) -> str:
        """Write with maximum compression and insight density."""
        
        model = self.swarm.MODELS["premium"][0]
        
        # Build insight block
        insight_block = "\n".join([
            f"• {ins.insight} [ratio: {ins.compression_ratio:.1f}]"
            for ins in insights[:5]
        ])
        
        # Build Socratic reveals
        socratic_reveals = "\n".join([
            f"• {q.reveals}"
            for q in socratic_chain[:5]
        ])
        
        system = """Write with maximum Kolmogorov complexity.
        Every sentence must deliver surprising mechanism.
        No transitions. No setup. No narrative.
        Start with the most surprising number."""
        
        user = f"""Thesis: {thesis}
        
        Compressed insights:
        {insight_block}
        
        Socratic revelations:
        {socratic_reveals}
        
        Write 1000-1500 words.
        
        Rules:
        1. Start with most surprising data point
        2. Each paragraph reveals new mechanism
        3. Include 50+ specific numbers
        4. No em-dashes, no transitions
        5. End with falsifiable prediction
        6. Weave in personal observation (I/we) naturally
        7. Every sentence changes reader's model of reality
        
        Begin with the number that breaks assumptions."""
        
        result = await self.swarm.call_model(
            model, system, user,
            temperature=0.7, max_tokens=2500
        )
        
        return result.content if not result.error else thesis
    
    def _extract_revelation(self, text: str) -> str:
        """Extract what this reveals about mechanism."""
        reveal_patterns = [
            r"reveals? that (.+)",
            r"shows? that (.+)",
            r"means? that (.+)",
            r"indicates? that (.+)"
        ]
        
        for pattern in reveal_patterns:
            match = re.search(pattern, text.lower())
            if match:
                return match.group(1)[:100]
        
        return "mechanism"
    
    def _extract_contradiction(self, text: str) -> str:
        """Extract what assumption this contradicts."""
        contra_patterns = [
            r"contradicts? (.+)",
            r"opposite of (.+)",
            r"not (.+) as believed",
            r"actually (.+) not"
        ]
        
        for pattern in contra_patterns:
            match = re.search(pattern, text.lower())
            if match:
                return match.group(1)[:100]
        
        return "common belief"
    
    def _extract_mechanisms(self, text: str) -> List[str]:
        """Extract mechanism statements."""
        mechanisms = []
        
        mech_patterns = [
            r"causes? (.+)",
            r"triggers? (.+)",
            r"leads? to (.+)",
            r"results? in (.+)",
            r"forces? (.+)"
        ]
        
        for pattern in mech_patterns:
            matches = re.findall(pattern, text.lower())
            mechanisms.extend(matches[:3])
        
        return mechanisms[:10]
    
    def _extract_numbers(self, text: str) -> List[str]:
        """Extract specific numbers with context."""
        number_pattern = r'(\$?[\d,]+\.?\d*[BMK%]?(?:\s+\w+)?)'
        matches = re.findall(number_pattern, text)
        return matches[:20]
    
    def _extract_contradictions(self, text: str) -> List[str]:
        """Extract contradictions to consensus."""
        contradictions = []
        
        contra_keywords = [
            "actually", "really", "in fact", "turns out",
            "opposite", "reverse", "inverse", "not"
        ]
        
        sentences = text.split('.')
        for sentence in sentences:
            if any(keyword in sentence.lower() for keyword in contra_keywords):
                contradictions.append(sentence.strip())
        
        return contradictions[:5]
    
    def _relates_to(self, insight: str, mechanism: str) -> bool:
        """Check if insight relates to mechanism."""
        insight_words = set(insight.lower().split())
        mechanism_words = set(mechanism.lower().split())
        
        # Check word overlap
        overlap = insight_words & mechanism_words
        return len(overlap) >= 2
    
    def _derive_predictions(self, insight: str) -> List[str]:
        """Derive testable predictions from insight."""
        predictions = []
        
        # Look for causal language
        if "causes" in insight or "leads to" in insight:
            predictions.append(f"If true, then increasing X should increase Y")
        
        if "threshold" in insight or "%" in insight:
            predictions.append(f"Crossing this threshold should trigger phase change")
        
        if "inverse" in insight or "opposite" in insight:
            predictions.append(f"Opposite intervention should have opposite effect")
        
        return predictions[:3]
    
    async def _next_why(self, answer: str, reveals: str) -> str:
        """Generate next deeper why question."""
        
        if "incentive" in reveals.lower():
            return f"Why does this incentive structure exist?"
        elif "mechanism" in reveals.lower():
            return f"Why does this mechanism work this way?"
        elif "benefit" in reveals.lower():
            return f"Why do they benefit while others don't?"
        elif "threshold" in reveals.lower():
            return f"Why this specific threshold and not another?"
        else:
            return f"Why does {reveals[:50]}?"
    
    def _calculate_compression(
        self,
        article: str,
        discoveries: List[Dict[str, Any]]
    ) -> float:
        """Calculate compression ratio of final article."""
        
        # Total discovery content
        total_discovery_words = sum(
            len(d.get("content", "").split())
            for d in discoveries
        )
        
        # Article words
        article_words = len(article.split())
        
        if article_words == 0:
            return 0.0
        
        # Compression ratio
        ratio = total_discovery_words / article_words
        
        return min(ratio, 100.0)  # Cap at 100:1


# Helper imports
import random