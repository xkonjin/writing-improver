"""Kolmogorov Compression Maximizer: Find the shortest true description.

The goal: Maximum insight per word.

Techniques:
1. Find the generating function (what simple rule creates complex patterns)
2. Identify the phase transition (where small change → big effect)
3. Extract the conservation law (what stays constant while everything changes)
4. Find the duality (where opposite descriptions are same thing)
5. Identify the fixed point (what doesn't change under transformation)

This is pure information theory applied to writing.
"""

import re
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Tuple
import math


@dataclass
class CompressionPattern:
    """A pattern that compresses multiple observations."""
    pattern: str
    observations_explained: List[str]
    compression_ratio: float
    generating_function: str  # The simple rule that generates complexity
    is_conserved: bool  # Does this hold across transformations
    is_phase_transition: bool  # Does this mark a critical point


@dataclass
class KolmogorovInsight:
    """An insight with maximum Kolmogorov compression."""
    core_statement: str
    word_count: int
    facts_compressed: int
    compression_ratio: float
    generating_rule: str
    falsifiable_prediction: str
    surprisal_score: float  # Information theoretic surprise


@dataclass
class DualDescription:
    """Two descriptions that are actually the same."""
    description_a: str
    description_b: str
    unifying_principle: str
    compression_gain: float


class KolmogorovMaximizer:
    """Find maximum compression insights."""
    
    # Information patterns that compress reality
    COMPRESSION_PATTERNS = [
        {
            "name": "Power Law",
            "template": "{X} follows {exponent} power law",
            "explains": ["inequality", "concentration", "tail events"],
            "generator": "Preferential attachment",
            "signature": r"(\d+)% (?:controls?|owns?|has) (\d+)%"
        },
        {
            "name": "Phase Transition", 
            "template": "At {threshold}, {system} shifts from {A} to {B}",
            "explains": ["sudden change", "criticality", "emergence"],
            "generator": "Critical point dynamics",
            "signature": r"(?:threshold|tipping point|critical) (?:at|of) (\d+)"
        },
        {
            "name": "Conservation Law",
            "template": "{quantity} remains constant while {variables} change",
            "explains": ["invariance", "symmetry", "constraint"],
            "generator": "Noether's theorem analog",
            "signature": r"(?:constant|conserved|invariant) (?:despite|while|as)"
        },
        {
            "name": "Duality",
            "template": "{A} and {B} are same phenomenon viewed differently",
            "explains": ["equivalence", "perspective", "unification"],
            "generator": "Change of basis",
            "signature": r"(?:same as|equivalent to|dual to|isomorphic)"
        },
        {
            "name": "Recursive Structure",
            "template": "{pattern} contains smaller copies of itself",
            "explains": ["self-similarity", "fractals", "emergence"],
            "generator": "Recursive definition",
            "signature": r"(?:recursive|self-similar|fractal|contains itself)"
        },
        {
            "name": "Information Asymmetry",
            "template": "{A} knows {info} that {B} doesn't",
            "explains": ["market inefficiency", "principal-agent", "selection"],
            "generator": "Hidden information",
            "signature": r"(?:knows?|information|asymmetr)"
        },
        {
            "name": "Convexity",
            "template": "Upside of {X} > downside, creating {optionality}",
            "explains": ["antifragility", "options", "asymmetry"],
            "generator": "Nonlinear payoff",
            "signature": r"(?:convex|upside|option|asymmetric)"
        },
        {
            "name": "Emergence",
            "template": "{macro} emerges from {micro} without central control",
            "explains": ["spontaneous order", "swarm behavior", "markets"],
            "generator": "Local interactions",
            "signature": r"(?:emerges?|spontaneous|self-organiz)"
        }
    ]
    
    # Compression operators
    OPERATORS = {
        "generalize": "Find pattern that explains multiple instances",
        "abstract": "Remove specific details, keep structure",
        "dualize": "Find equivalent opposite description",
        "recurse": "Find self-referential structure",
        "conserve": "Find what doesn't change",
        "threshold": "Find critical transition point",
        "generate": "Find simple rule producing complexity"
    }
    
    def compress_observations(
        self,
        observations: List[str],
        max_words: int = 20
    ) -> KolmogorovInsight:
        """Compress observations into minimal insight."""
        
        # Extract all numbers and patterns
        patterns = self._extract_patterns(observations)
        
        # Find generating function
        generator = self._find_generator(patterns)
        
        # Find conservation law
        conserved = self._find_conserved(patterns)
        
        # Find phase transition
        transition = self._find_phase_transition(patterns)
        
        # Combine into minimal statement
        insight = self._build_minimal_statement(
            generator, conserved, transition, max_words
        )
        
        # Calculate compression metrics
        total_words = sum(len(obs.split()) for obs in observations)
        insight_words = len(insight.split())
        compression_ratio = total_words / max(insight_words, 1)
        
        # Calculate surprisal (information content)
        surprisal = self._calculate_surprisal(insight, observations)
        
        # Generate falsifiable prediction
        prediction = self._generate_prediction(generator, transition)
        
        return KolmogorovInsight(
            core_statement=insight,
            word_count=insight_words,
            facts_compressed=len(observations),
            compression_ratio=compression_ratio,
            generating_rule=generator,
            falsifiable_prediction=prediction,
            surprisal_score=surprisal
        )
    
    def find_dualities(self, statements: List[str]) -> List[DualDescription]:
        """Find statements that are dual descriptions."""
        
        dualities = []
        
        for i, stmt1 in enumerate(statements):
            for stmt2 in statements[i+1:]:
                if self._are_dual(stmt1, stmt2):
                    unifying = self._find_unifying_principle(stmt1, stmt2)
                    
                    # Calculate compression gain
                    original_length = len(stmt1.split()) + len(stmt2.split())
                    unified_length = len(unifying.split())
                    compression_gain = original_length / max(unified_length, 1)
                    
                    dualities.append(DualDescription(
                        description_a=stmt1,
                        description_b=stmt2,
                        unifying_principle=unifying,
                        compression_gain=compression_gain
                    ))
        
        return dualities
    
    def maximize_compression(
        self,
        text: str,
        target_ratio: float = 10.0
    ) -> str:
        """Rewrite text for maximum compression."""
        
        sentences = text.split('.')
        
        # Group related sentences
        groups = self._group_related(sentences)
        
        compressed = []
        
        for group in groups:
            # Find the shortest statement that implies all others
            kernel = self._find_kernel_statement(group)
            
            # Only keep if compression ratio exceeds target
            group_words = sum(len(s.split()) for s in group)
            kernel_words = len(kernel.split())
            
            if kernel_words > 0 and group_words / kernel_words >= target_ratio:
                compressed.append(kernel)
            else:
                # Keep most information-dense original
                densest = self._find_densest(group)
                compressed.append(densest)
        
        return '. '.join(compressed)
    
    def extract_generating_functions(self, text: str) -> List[str]:
        """Extract the simple rules generating complexity."""
        
        generators = []
        
        # Look for recursive patterns
        recursive = re.findall(
            r"(?:each|every) (\w+) (?:creates?|produces?|generates?) (\w+)",
            text.lower()
        )
        for match in recursive:
            generators.append(f"{match[0]} → {match[1]}")
        
        # Look for threshold rules
        thresholds = re.findall(
            r"(?:when|if|once) .+ (?:reaches?|hits?|exceeds?) (\d+[%$BMK]?)",
            text
        )
        for threshold in thresholds:
            generators.append(f"Rule triggers at {threshold}")
        
        # Look for conservation laws
        conserved = re.findall(
            r"(\w+) (?:remains?|stays?|is) (?:constant|same|fixed)",
            text.lower()
        )
        for item in conserved:
            generators.append(f"{item} = constant")
        
        return generators
    
    def _extract_patterns(self, observations: List[str]) -> List[CompressionPattern]:
        """Extract compressible patterns from observations."""
        
        patterns = []
        
        for obs_set in [observations[i:i+3] for i in range(len(observations)-2)]:
            # Check each compression pattern
            for pattern_def in self.COMPRESSION_PATTERNS:
                if self._matches_pattern(obs_set, pattern_def):
                    patterns.append(CompressionPattern(
                        pattern=pattern_def["name"],
                        observations_explained=obs_set,
                        compression_ratio=len(' '.join(obs_set)) / len(pattern_def["template"]),
                        generating_function=pattern_def["generator"],
                        is_conserved="Conservation" in pattern_def["name"],
                        is_phase_transition="Phase" in pattern_def["name"]
                    ))
        
        return patterns
    
    def _find_generator(self, patterns: List[CompressionPattern]) -> str:
        """Find the simplest generating rule."""
        
        if not patterns:
            return "Linear accumulation"
        
        # Find most common generator
        generators = [p.generating_function for p in patterns]
        
        if generators:
            # Return most frequent
            return max(set(generators), key=generators.count)
        
        return "Unknown generator"
    
    def _find_conserved(self, patterns: List[CompressionPattern]) -> str:
        """Find what stays constant."""
        
        conserved_patterns = [p for p in patterns if p.is_conserved]
        
        if conserved_patterns:
            return conserved_patterns[0].pattern
        
        # Look for invariants in observations
        all_obs = ' '.join([' '.join(p.observations_explained) for p in patterns])
        
        conserved_match = re.search(
            r"(\w+) (?:remains?|stays?|always|never changes?)",
            all_obs
        )
        
        if conserved_match:
            return conserved_match.group(1)
        
        return "Total value"
    
    def _find_phase_transition(self, patterns: List[CompressionPattern]) -> str:
        """Find critical transition point."""
        
        transition_patterns = [p for p in patterns if p.is_phase_transition]
        
        if transition_patterns:
            return transition_patterns[0].pattern
        
        # Look for threshold language
        all_obs = ' '.join([' '.join(p.observations_explained) for p in patterns])
        
        threshold_match = re.search(
            r"(?:at|above|below|when reaches?) (\d+[%$BMK]?)",
            all_obs
        )
        
        if threshold_match:
            return f"Phase transition at {threshold_match.group(1)}"
        
        return "No clear transition"
    
    def _build_minimal_statement(
        self,
        generator: str,
        conserved: str,
        transition: str,
        max_words: int
    ) -> str:
        """Build the minimal statement encoding all information."""
        
        components = []
        
        # Add generator if informative
        if generator != "Unknown generator":
            components.append(generator)
        
        # Add conservation if exists
        if conserved != "Total value":
            components.append(f"{conserved} conserved")
        
        # Add transition if exists
        if "Phase transition" in transition:
            components.append(transition)
        
        # Join and truncate to max words
        statement = ", ".join(components)
        words = statement.split()
        
        if len(words) > max_words:
            statement = " ".join(words[:max_words])
        
        return statement or "Pattern detected"
    
    def _calculate_surprisal(self, insight: str, observations: List[str]) -> float:
        """Calculate information-theoretic surprise."""
        
        # Surprisal = -log(probability)
        # Approximate by uniqueness of terms
        
        insight_terms = set(insight.lower().split())
        obs_terms = set(' '.join(observations).lower().split())
        
        # Unique terms in insight not in observations = surprise
        unique_terms = insight_terms - obs_terms
        
        if not insight_terms:
            return 0.0
        
        surprisal = len(unique_terms) / len(insight_terms)
        
        # Scale to 0-10
        return min(surprisal * 10, 10.0)
    
    def _generate_prediction(self, generator: str, transition: str) -> str:
        """Generate falsifiable prediction from patterns."""
        
        if "Phase transition" in transition:
            threshold = re.search(r"(\d+[%$BMK]?)", transition)
            if threshold:
                return f"Crossing {threshold.group(1)} will trigger qualitative change"
        
        if "attachment" in generator.lower():
            return "Future concentration will follow power law distribution"
        
        if "conserved" in generator.lower():
            return "Total sum remains constant under transformation"
        
        if "recursive" in generator.lower():
            return "Pattern repeats at smaller scales"
        
        return "Linear extrapolation will fail"
    
    def _matches_pattern(self, observations: List[str], pattern_def: Dict) -> bool:
        """Check if observations match a pattern."""
        
        combined = ' '.join(observations)
        return bool(re.search(pattern_def["signature"], combined, re.IGNORECASE))
    
    def _are_dual(self, stmt1: str, stmt2: str) -> bool:
        """Check if two statements are dual descriptions."""
        
        # Check for opposite terms describing same thing
        opposites = [
            ("increase", "decrease"),
            ("supply", "demand"),
            ("top-down", "bottom-up"),
            ("centralized", "distributed"),
            ("order", "chaos")
        ]
        
        for opp1, opp2 in opposites:
            if (opp1 in stmt1.lower() and opp2 in stmt2.lower()) or \
               (opp2 in stmt1.lower() and opp1 in stmt2.lower()):
                return True
        
        return False
    
    def _find_unifying_principle(self, stmt1: str, stmt2: str) -> str:
        """Find principle that unifies two statements."""
        
        # Extract common terms
        terms1 = set(stmt1.lower().split())
        terms2 = set(stmt2.lower().split())
        common = terms1 & terms2
        
        if common:
            return f"Both aspects of {' '.join(list(common)[:3])}"
        
        return "Two views of same phenomenon"
    
    def _group_related(self, sentences: List[str]) -> List[List[str]]:
        """Group related sentences for compression."""
        
        groups = []
        used = set()
        
        for i, sent1 in enumerate(sentences):
            if i in used:
                continue
            
            group = [sent1]
            used.add(i)
            
            # Find related sentences
            sent1_terms = set(sent1.lower().split())
            
            for j, sent2 in enumerate(sentences[i+1:], i+1):
                if j in used:
                    continue
                
                sent2_terms = set(sent2.lower().split())
                
                # Check term overlap
                overlap = len(sent1_terms & sent2_terms)
                
                if overlap >= 3:  # Threshold for relatedness
                    group.append(sent2)
                    used.add(j)
            
            groups.append(group)
        
        return groups
    
    def _find_kernel_statement(self, group: List[str]) -> str:
        """Find the statement that implies all others."""
        
        if len(group) == 1:
            return group[0]
        
        # Find statement with most information
        best_score = 0
        kernel = group[0]
        
        for stmt in group:
            # Count unique informative terms
            terms = [t for t in stmt.split() if len(t) > 3]
            numbers = re.findall(r'\d+[%$BMK]?', stmt)
            
            score = len(set(terms)) + len(numbers) * 2
            
            if score > best_score:
                best_score = score
                kernel = stmt
        
        return kernel
    
    def _find_densest(self, group: List[str]) -> str:
        """Find most information-dense statement."""
        
        max_density = 0
        densest = group[0] if group else ""
        
        for stmt in group:
            # Information = numbers + unique terms
            numbers = len(re.findall(r'\d+[%$BMK]?', stmt))
            unique_terms = len(set(stmt.lower().split()))
            words = len(stmt.split())
            
            if words > 0:
                density = (numbers * 2 + unique_terms) / words
                
                if density > max_density:
                    max_density = density
                    densest = stmt
        
        return densest