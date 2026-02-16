# First-Principles Frameworks — Quick Reference

One-page lookup for applying each framework to your pipeline.

---

## The 9 Frameworks at a Glance

| Framework | Creator | Core Principle | Your Pipeline Stage | Test For |
|-----------|---------|----------------|-------------------|----------|
| **Latticework of Mental Models** | Charlie Munger | Insight from cross-domain collision (3+ models converging) | SATURATE | Do 3+ models from different disciplines reach the same conclusion? |
| **Inversion** | Munger | Work backwards from failure to clarify thinking | SATURATE → DISORDER | What would make this thesis false? How could this collapse? |
| **The Feynman Technique** | Richard Feynman | Simplicity = understanding (explain without jargon or don't understand) | DRAFT | Can you explain each major claim in 2 sentences without jargon? |
| **Falsificationism** | Karl Popper | Test by trying to disprove (not trying to confirm) | DISORDER | State thesis falsifiably. List conditions that would break it. Seek counter-evidence. |
| **Data Journalism Workflow** | ProPublica, Bloomberg | Data → Pattern → Story (not Theory → Evidence) | SATURATE | Is the insight data-driven or framework-applied? Do you have Tier 1-2 sources? |
| **Renaissance Pattern Discovery** | Jim Simons | Patterns in data at microstructure level (where intuition fails) | SATURATE → IDENTIFY ANOMALIES | What patterns in the data would a human miss without systematic analysis? |
| **Bridgewater Disagreement** | Ray Dalio | Radical truth via structured disagreement (not confirmation) | NEW PHASE | What's the strongest counter-argument? Does thesis survive it? |
| **Cognitive Science of Aha** | Neuroscience research | Surprise = gap between expectation and reality (genuine only) | STRUCTURAL SCAN | Is this genuine surprise (hippocampus mismatch) or manufactured (announced)? |
| **Novelty vs. Originality** | Academic peer review | Novel = changes how people think; Original = just new | SYNTHESIS | Does removing any single data point weaken the thesis? If yes → novel. If no → derivative. |

---

## SATURATION PHASE: The 6-Model Checklist

Before entering DISORDER, ensure research covers all 6 of Munger's mental models:

```
Research Track 1: MECHANISM (How does it work?)
├─ Money/value flow: Where does capital move? Who touches it?
├─ System internals: What's the plumbing? What breaks the circuit?
└─ Feedback loops: What's the reinforcing mechanism?
Status: ___ / 1000 words minimum

Research Track 2: ECONOMICS (Who makes money? Who loses?)
├─ Unit economics: Margins, revenue, costs, market size
├─ Value capture: Who benefits from the current structure?
└─ Incentive structure: What rewards exist for which behaviors?
Status: ___ / 1000 words minimum

Research Track 3: HISTORY (Has something similar happened before?)
├─ Direct precedent: Eurodollars? S&Ls? Mutual funds?
├─ Structural parallels: What was the same mechanism in the past?
└─ How did it end: What killed the previous version?
Status: ___ / 1000 words minimum

Research Track 4: PSYCHOLOGY (What narratives drive behavior?)
├─ User motivation: What incentives drive adoption?
├─ Trust: What creates or erodes belief in the system?
└─ In-group dynamics: What's the narrative that binds users together?
Status: ___ / 1000 words minimum

Research Track 5: REGULATION (Who benefits from the rules? Why?)
├─ Current rules: What does the law actually say?
├─ Loopholes: What exemptions exist and why?
└─ Incentive alignment: Who lobbied for which rules?
Status: ___ / 1000 words minimum

Research Track 6: INVERSION (How would this collapse?)
├─ Failure modes: What breaks the system?
├─ Fragility: What single point of failure exists?
└─ Tail risk: Under what conditions does it go to zero?
Status: ___ / 1000 words minimum

TOTAL: ___ / 6000 words minimum (1000 per track)
```

All sources must be Tier 1-2 (SEC filings, regulatory text, academic papers, attestations).

---

## DISORDER → DRAFT PHASE: Falsification Worksheet

Before writing, fill this out:

**Candidate Thesis:**
[State in one sentence. Must be falsifiable.]

**Falsifying Conditions:**
What evidence would prove this false?
1. _______
2. _______
3. _______

**Counter-Evidence Search:**
Did you actively look for evidence that breaks the thesis?
- Where: _______
- Findings: _______

**Confidence Assessment:**
- Thesis survives: _____ (which conditions?
- Thesis weakens: _____ (which conditions?)
- Overall confidence: _____ / 100

**Mechanism Clarity:**
For each major claim:

| Claim | Jargon? | Mechanism (no jargon) | Circular reasoning? |
|-------|---------|----------------------|-------------------|
| Example: "Regulatory arbitrage" | Yes | Banks pay $X/year compliance; Tether doesn't; that's the edge | No |
| | | | |
| | | | |

---

## NOVELTY TEST: Is This Data-Driven or Framework-Applied?

**Green flags (data-driven):**
- Remove any single data point and thesis weakens ✓
- Thesis requires specific numbers (not generic percentages)
- Thesis doesn't apply if you swap domain (Stablecoins-specific, not generic payments)
- Can't be reached from frameworks alone
- Falsifiable with specific test conditions

**Red flags (framework-applied):**
- Same structure works with different domain ("X industry follows disruption pattern")
- Thesis survives with only framework, loses all data
- Vague thesis that could apply to most companies/countries
- Pattern matches known framework perfectly (too perfectly)
- Could be written without domain expertise

**Questions to ask:**
1. If I removed the 3 most specific data points, does the thesis collapse? (Should be yes)
2. Could a generalist who knows the frameworks but not the domain reach this? (Should be no)
3. Does this thesis only work for this specific case? (Should be yes)

---

## SURPRISE VALIDATION: Cognitive Science Checklist

Before final revision, verify genuine surprise:

**Expectation Test:**
What's the standard narrative readers likely believe?
- Standard view: _______
- Your view: _______
- Gap: _______ (this is your surprise)

**Mismatch Validation:**
Is the gap real (hippocampus would trigger) or manufactured (announced as surprising)?

| Question | Answer |
|----------|--------|
| Did readers have a coherent mental model before reading? | ___ |
| Does the article violate that model? | ___ |
| Without the article, would readers have predicted this? | ___ |
| Is the surprise stated or demonstrated through data? | ___ |
| Are there clues earlier in the piece that hint at it? | ___ |

**Falsifiability Test:**
Could a reader point to evidence that disproves your surprising claim?
- Falsifier: _______
- Evidence addressing it: _______

---

## KOLMOGOROV COMPRESSION GATE

**Final test before publishing:**

State your core insight in exactly 50 words or fewer. If you can't, rewrite it.

```
Core Insight (50 words max):

_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

Word count: ___ / 50
```

If you exceed 50 words:
1. Is every word load-bearing? (Cut anything ornamental)
2. Are there two insights here instead of one? (Split into separate articles)
3. Does this need reframing? (The thesis might not be crystallized yet)

**Litmus test:** If a smart reader could have reached this conclusion by themselves using only the data you present, rewrite to add mechanism or remove something.

---

## PRE-PUBLICATION CHECKLIST

Run this before submitting any article:

**Research Quality:**
- [ ] 3000+ words per research track (6 tracks = 18,000+ minimum)
- [ ] All major claims traceable to Tier 1-2 sources
- [ ] Devil's advocate review completed (strongest counter-argument documented)
- [ ] Counter-evidence actively sought and documented

**Mechanism Clarity:**
- [ ] Each major claim explainable in 2 sentences without jargon
- [ ] No circular reasoning ("X because X")
- [ ] No required frame-switching ("like...")
- [ ] Flow chart or diagram test passed (could you draw it?)

**Novelty:**
- [ ] Thesis collapses if any single data point removed
- [ ] Can't be reached from frameworks alone
- [ ] Domain-specific (doesn't apply if you swap industries)
- [ ] Falsifiable with specific test conditions

**Surprise:**
- [ ] Genuine gap between standard narrative and your view
- [ ] Not announced; demonstrated through data
- [ ] Falsifiable (reader can point to evidence that disproves it)
- [ ] Foreshadowed (clues planted early)

**Style:**
- [ ] Structural AI tell scan passed (no signposting, parallelism)
- [ ] Vocabulary scan passed (no banned words)
- [ ] Core insight states in <50 words
- [ ] Voice matches domain expert precedent (Levine, Hobart, Housel, Campbell)

**Final Gate:**
- [ ] Could a smart reader reach this conclusion from just the data alone? (If yes, your framing/mechanism needs work)
- [ ] Presented to domain expert who disagrees — what survives? (Feedback integrated or defensible?)

---

## Quick Lookup: Which Framework to Apply When You're Stuck

**The article feels obvious:**
→ Apply Novelty Test. Is it data-driven or framework-applied? If framework-applied, add more specific data or find a different angle.

**The article explains what but not why:**
→ Apply Feynman test. Can you explain without jargon? Likely missing mechanism.

**The article lacks convincingness:**
→ Apply Falsificationism. State thesis falsifiably. What's the counter-evidence? Did you actively seek it?

**The article feels AI-like despite no banned words:**
→ Apply Surprise validation. Is the surprise genuine (gap between expectation and reality) or manufactured (announced as surprising)?

**The research is exhausting and you have no clear thesis yet:**
→ Apply Inversion. Instead of "What makes this work?" ask "How would this collapse?" The path to failure is often clearer.

**You have multiple candidate theses:**
→ Apply Bridgewater disagreement. Which thesis survives the strongest counter-argument?

**The article is well-written but unmemorable:**
→ Apply Kolmogorov compression. State the core insight in <50 words. If you can't, it's not crystallized.

