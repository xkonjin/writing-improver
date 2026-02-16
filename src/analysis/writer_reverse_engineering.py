"""Reverse-engineer techniques from the best writers.

This module analyzes and extracts patterns from:
- Paul Graham: Contradiction-based reasoning, simplicity
- Nassim Taleb: Convexity detection, skin in the game
- Matt Levine: Finding absurdity, mechanism explanation
- Patrick McKenzie: System revelation, infrastructure
- Byrne Hobart: Historical pattern matching, capital flows
- Venkatesh Rao: Conceptual inversion, 2x2 thinking
- Matt Taibbi: Corruption mechanics, follow the money
- Michael Lewis: Character-driven mechanism revelation
- Tyler Cowen: Marginal revolution, economic reasoning
- Scott Alexander: Bayesian reasoning, steel-manning

Each writer has specific techniques for finding truth.
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
import re


@dataclass
class WriterTechnique:
    """A specific technique used by a writer."""
    writer: str
    technique_name: str
    description: str
    signature_phrases: List[str]
    detection_patterns: List[str]
    compression_method: str
    truth_finding_approach: str
    example_application: str


@dataclass
class WriterAnalysis:
    """Analysis of a text using a writer's techniques."""
    writer: str
    techniques_detected: List[str]
    truth_mechanisms: List[str]
    compression_score: float
    signature_elements: List[str]


class WriterReverseEngineering:
    """Extract and apply techniques from master writers."""
    
    WRITER_TECHNIQUES = {
        "paul_graham": [
            WriterTechnique(
                writer="Paul Graham",
                technique_name="Contradiction Hunt",
                description="Find where everyone is wrong about the same thing",
                signature_phrases=[
                    "What do you believe that most people disagree with?",
                    "The opposite is actually true",
                    "Everyone assumes X, but actually Y"
                ],
                detection_patterns=[
                    r"everyone (?:thinks?|believes?|assumes?) (.+) but (?:actually|really) (.+)",
                    r"the (?:real|actual) (.+) is (?:not|opposite)",
                    r"contrary to (?:popular|common) (?:belief|wisdom)"
                ],
                compression_method="Find the simplest explanation that invalidates complex ones",
                truth_finding_approach="Start from first principles, ignore social proof",
                example_application="'Startup ideas are not million dollar ideas' contradicts 'you need a great idea'"
            ),
            WriterTechnique(
                writer="Paul Graham",
                technique_name="Simplicity Maximization",
                description="Express complex ideas in simple language",
                signature_phrases=[
                    "Put simply",
                    "In other words",
                    "What this really means"
                ],
                detection_patterns=[
                    r"(?:simply|basically|essentially) (.+)",
                    r"in (?:simple|plain) (?:terms|english)",
                    r"what .+ (?:really|actually) means?"
                ],
                compression_method="Remove every word that doesn't add information",
                truth_finding_approach="If you can't explain it simply, you don't understand it",
                example_application="'Wealth is stuff we want' instead of complex economic definitions"
            )
        ],
        
        "nassim_taleb": [
            WriterTechnique(
                writer="Nassim Taleb",
                technique_name="Skin in the Game Detection",
                description="Identify who bears risk vs who transfers it",
                signature_phrases=[
                    "Skin in the game",
                    "Downside for thee, upside for me",
                    "Socializing losses, privatizing gains"
                ],
                detection_patterns=[
                    r"(?:bears?|takes?|assumes?) (?:the )?(?:risk|downside)",
                    r"(?:upside|profit) without (?:risk|downside)",
                    r"(?:heads|win) .+ (?:tails|lose) .+"
                ],
                compression_method="Reduce to risk transfer mechanics",
                truth_finding_approach="Follow who pays when things go wrong",
                example_application="Bankers get bonuses, taxpayers get bailouts = no skin in game"
            ),
            WriterTechnique(
                writer="Nassim Taleb",
                technique_name="Antifragility Identification",
                description="Find what gains from disorder",
                signature_phrases=[
                    "Antifragile",
                    "Gains from volatility",
                    "Disorder strengthens"
                ],
                detection_patterns=[
                    r"(?:gains?|benefits?|strengthens?) from (?:disorder|chaos|volatility)",
                    r"(?:better|stronger) (?:after|from) (?:stress|shocks?)",
                    r"convex(?:ity)? (?:to|in|of)"
                ],
                compression_method="Identify convexity in payoff structures",
                truth_finding_approach="Look for asymmetric upside",
                example_application="Restaurants are fragile (one bad review kills), books are antifragile (controversy sells)"
            )
        ],
        
        "matt_levine": [
            WriterTechnique(
                writer="Matt Levine",
                technique_name="Absurdity Revelation",
                description="Show how normal things are actually insane",
                signature_phrases=[
                    "This is fine",
                    "Everything is securities fraud",
                    "The machine works exactly as designed"
                ],
                detection_patterns=[
                    r"(?:somehow|apparently|inexplicably) (?:legal|allowed|fine)",
                    r"(?:technically|legally) (?:correct|true) (?:but|and) (?:insane|absurd)",
                    r"this is (?:just|exactly) how .+ works?"
                ],
                compression_method="Juxtapose mundane description with absurd reality",
                truth_finding_approach="Explain the mechanism until absurdity becomes obvious",
                example_application="'Banks create money by typing numbers' - true and insane"
            ),
            WriterTechnique(
                writer="Matt Levine",
                technique_name="Incentive Archaeology",
                description="Trace weird outcomes to rational incentives",
                signature_phrases=[
                    "The incentives are",
                    "They're paid to",
                    "The game theory is"
                ],
                detection_patterns=[
                    r"incentiv(?:es?|ized) to (.+)",
                    r"paid (?:to|for) (.+) not (.+)",
                    r"rational(?:ly)? (.+) because (.+)"
                ],
                compression_method="Reduce behavior to incentive structures",
                truth_finding_approach="Assume rationality, find the hidden payoff",
                example_application="SPACs exist because sponsors get 20% for finding any deal, not good deals"
            )
        ],
        
        "patrick_mckenzie": [
            WriterTechnique(
                writer="Patrick McKenzie",
                technique_name="Infrastructure X-Ray",
                description="Reveal the hidden systems running everything",
                signature_phrases=[
                    "The plumbing is",
                    "Behind the scenes",
                    "The actual system"
                ],
                detection_patterns=[
                    r"(?:actually|really) (?:runs on|powered by|built on) (.+)",
                    r"the (?:real|actual) (?:system|infrastructure) is (.+)",
                    r"(?:hidden|invisible) (?:infrastructure|system|plumbing)"
                ],
                compression_method="Map the actual vs perceived system",
                truth_finding_approach="Trace data/money flows to find real architecture",
                example_application="Credit cards are a telecommunications network with a banking license"
            ),
            WriterTechnique(
                writer="Patrick McKenzie",
                technique_name="Spreadsheet Reality",
                description="Show how everything reduces to Excel somewhere",
                signature_phrases=[
                    "It's a spreadsheet",
                    "Someone's Excel file",
                    "The database is actually"
                ],
                detection_patterns=[
                    r"(?:just|actually|really) (?:a|an) (?:spreadsheet|excel file|csv)",
                    r"(?:stored|kept|maintained) in (?:excel|sheets|csv)",
                    r"the (?:database|system) is (?:really|actually) (.+)"
                ],
                compression_method="Find the mundane technical reality",
                truth_finding_approach="Look for the boring technical truth",
                example_application="Global finance runs on Excel sheets emailed between banks"
            )
        ],
        
        "byrne_hobart": [
            WriterTechnique(
                writer="Byrne Hobart",
                technique_name="Historical Rhyming",
                description="Find exact historical precedents",
                signature_phrases=[
                    "This happened before in",
                    "The 1920s version was",
                    "History rhymes with"
                ],
                detection_patterns=[
                    r"(?:happened|occurred) (?:before|previously) (?:in|during) (.+)",
                    r"the (\d{4}s?) version (?:was|of)",
                    r"(?:historically|previously) (.+) (?:did|had) (?:the same|similar)"
                ],
                compression_method="Extract the recurring pattern across time",
                truth_finding_approach="Find the structural similarity across eras",
                example_application="Crypto is 1920s bucket shops with better technology"
            ),
            WriterTechnique(
                writer="Byrne Hobart",
                technique_name="Capital Flow Tracing",
                description="Follow money to find true dynamics",
                signature_phrases=[
                    "Capital flows from",
                    "The money goes",
                    "Value accrues to"
                ],
                detection_patterns=[
                    r"(?:capital|money|value) (?:flows?|goes?|moves?) (?:from|to) (.+)",
                    r"(?:captures?|accrues?) (?:value|profit|surplus)",
                    r"\$(\d+[BMK]?) (?:from|to) (.+)"
                ],
                compression_method="Map value creation vs value capture",
                truth_finding_approach="Follow the money to find real power dynamics",
                example_application="Google captures value from content it doesn't create"
            )
        ],
        
        "venkatesh_rao": [
            WriterTechnique(
                writer="Venkatesh Rao",
                technique_name="2x2 Matrix Thinking",
                description="Find two axes that explain everything",
                signature_phrases=[
                    "On one axis",
                    "The two dimensions are",
                    "Four quadrants"
                ],
                detection_patterns=[
                    r"(?:axis|dimension) (?:is|represents?) (.+)",
                    r"(?:quadrant|corner) (?:where|with) (.+) and (.+)",
                    r"(?:high|low) (.+) (?:and|vs) (?:high|low) (.+)"
                ],
                compression_method="Reduce complex space to two critical dimensions",
                truth_finding_approach="Find orthogonal axes that separate phenomena",
                example_application="Legibility vs Fertility explains modernist failures"
            ),
            WriterTechnique(
                writer="Venkatesh Rao",
                technique_name="Liminal Space Identification",
                description="Find the productive space between categories",
                signature_phrases=[
                    "Neither X nor Y",
                    "The space between",
                    "Liminal zone"
                ],
                detection_patterns=[
                    r"(?:neither|not) (.+) (?:nor|or) (.+)",
                    r"(?:between|among) (?:categories|classifications|types)",
                    r"(?:liminal|boundary|edge) (?:space|zone|area)"
                ],
                compression_method="Identify value in category violations",
                truth_finding_approach="Look where classifications break down",
                example_application="Consultants live between employee and entrepreneur"
            )
        ],
        
        "tyler_cowen": [
            WriterTechnique(
                writer="Tyler Cowen",
                technique_name="Marginal Analysis",
                description="Focus on the next unit, not the average",
                signature_phrases=[
                    "On the margin",
                    "The marginal",
                    "One more"
                ],
                detection_patterns=[
                    r"(?:marginal|next|additional) (?:unit|person|dollar)",
                    r"on the margin",
                    r"(?:cost|benefit|value) of (?:one more|the next)"
                ],
                compression_method="Reduce to marginal effects",
                truth_finding_approach="Ignore averages, study changes",
                example_application="Immigration debate: focus on marginal immigrant, not average"
            ),
            WriterTechnique(
                writer="Tyler Cowen",
                technique_name="Signaling Identification",
                description="Separate signaling from genuine value",
                signature_phrases=[
                    "This is signaling",
                    "Signal that",
                    "Costly signal"
                ],
                detection_patterns=[
                    r"(?:signals?|signaling) (?:that|about) (.+)",
                    r"(?:costly|expensive) (?:signal|display)",
                    r"(?:shows?|demonstrates?|proves?) (?:status|ability|commitment)"
                ],
                compression_method="Identify what's signaling vs substantial",
                truth_finding_approach="Ask what remains if nobody's watching",
                example_application="College is 80% signaling, 20% human capital"
            )
        ],
        
        "scott_alexander": [
            WriterTechnique(
                writer="Scott Alexander",
                technique_name="Bayesian Reasoning",
                description="Update priors with evidence systematically",
                signature_phrases=[
                    "Update toward",
                    "Prior probability",
                    "Evidence suggests"
                ],
                detection_patterns=[
                    r"(?:prior|posterior) (?:probability|belief)",
                    r"(?:update|adjust) (?:toward|away from)",
                    r"(?:evidence|data) (?:suggests?|indicates?|points to)"
                ],
                compression_method="Reduce to likelihood ratios",
                truth_finding_approach="Start with base rates, update with specifics",
                example_application="Most medical studies wrong = high prior on any study being false"
            ),
            WriterTechnique(
                writer="Scott Alexander",
                technique_name="Steel-Manning",
                description="Find the strongest version of opposing views",
                signature_phrases=[
                    "The strongest version",
                    "Steel man",
                    "Best case for"
                ],
                detection_patterns=[
                    r"(?:strongest|best) (?:version|argument|case) (?:for|of)",
                    r"steel[- ]?man",
                    r"if we (?:assume|grant) (.+) then (.+)"
                ],
                compression_method="Strengthen opposing arguments before defeating",
                truth_finding_approach="Truth survives strongest counterarguments",
                example_application="Steel-man flat earth to understand epistemology"
            )
        ]
    }
    
    @classmethod
    def analyze_text(cls, text: str, writer: str) -> WriterAnalysis:
        """Analyze text for specific writer's techniques."""
        
        techniques = cls.WRITER_TECHNIQUES.get(writer, [])
        techniques_detected = []
        truth_mechanisms = []
        signature_elements = []
        
        for technique in techniques:
            # Check for detection patterns
            for pattern in technique.detection_patterns:
                if re.search(pattern, text.lower()):
                    techniques_detected.append(technique.technique_name)
                    truth_mechanisms.append(technique.truth_finding_approach)
                    break
            
            # Check for signature phrases
            for phrase in technique.signature_phrases:
                if phrase.lower() in text.lower():
                    signature_elements.append(phrase)
        
        # Calculate compression score
        compression_score = cls._calculate_compression(text, techniques_detected)
        
        return WriterAnalysis(
            writer=writer,
            techniques_detected=techniques_detected,
            truth_mechanisms=truth_mechanisms,
            compression_score=compression_score,
            signature_elements=signature_elements
        )
    
    @classmethod
    def extract_all_techniques(cls, text: str) -> Dict[str, WriterAnalysis]:
        """Extract techniques from all writers."""
        
        results = {}
        
        for writer in cls.WRITER_TECHNIQUES.keys():
            analysis = cls.analyze_text(text, writer)
            if analysis.techniques_detected:
                results[writer] = analysis
        
        return results
    
    @classmethod
    def get_compression_methods(cls, writers: List[str]) -> List[str]:
        """Get compression methods for specified writers."""
        
        methods = []
        
        for writer in writers:
            techniques = cls.WRITER_TECHNIQUES.get(writer, [])
            for technique in techniques:
                if technique.compression_method not in methods:
                    methods.append(technique.compression_method)
        
        return methods
    
    @classmethod
    def get_truth_finding_approaches(cls, writers: List[str]) -> List[str]:
        """Get truth-finding approaches for specified writers."""
        
        approaches = []
        
        for writer in writers:
            techniques = cls.WRITER_TECHNIQUES.get(writer, [])
            for technique in techniques:
                if technique.truth_finding_approach not in approaches:
                    approaches.append(technique.truth_finding_approach)
        
        return approaches
    
    @classmethod
    def generate_writing_prompt(cls, writers: List[str], topic: str) -> str:
        """Generate a writing prompt using specified writers' techniques."""
        
        prompt_parts = [f"Write about {topic} using these techniques:\n"]
        
        for writer in writers:
            techniques = cls.WRITER_TECHNIQUES.get(writer, [])
            if techniques:
                prompt_parts.append(f"\nFrom {writer}:")
                for tech in techniques[:2]:  # Use top 2 techniques per writer
                    prompt_parts.append(f"- {tech.technique_name}: {tech.description}")
                    prompt_parts.append(f"  Approach: {tech.truth_finding_approach}")
        
        prompt_parts.append("\nCompression requirements:")
        methods = cls.get_compression_methods(writers)
        for method in methods[:3]:
            prompt_parts.append(f"- {method}")
        
        return "\n".join(prompt_parts)
    
    @classmethod
    def _calculate_compression(cls, text: str, techniques_detected: List[str]) -> float:
        """Calculate compression score based on techniques used."""
        
        base_score = 1.0
        
        # Each technique adds compression
        base_score += len(techniques_detected) * 0.5
        
        # Short sentences = higher compression
        sentences = text.split('.')
        avg_sentence_length = sum(len(s.split()) for s in sentences) / max(len(sentences), 1)
        if avg_sentence_length < 15:
            base_score += 2.0
        elif avg_sentence_length < 20:
            base_score += 1.0
        
        # Specific numbers = higher compression
        numbers = re.findall(r'\d+[%$BMK]?', text)
        base_score += min(len(numbers) * 0.2, 3.0)
        
        return min(base_score, 10.0)