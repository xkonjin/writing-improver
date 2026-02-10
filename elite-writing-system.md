# Elite Writing System v2

## The Problem This Solves

Article 04 (Compression Substitution) had better research and a stronger insight than articles 02 and 03. It still sounded AI-written. The insight generation pipeline produced clean, organized intermediate artifacts (anomaly clusters, numbered mechanisms, coined terms). The writing step presented those artifacts. Presenting organized thinking sounds like AI. Showing the process of thinking sounds human.

**Core diagnosis:** Articles 02 and 03 read like someone thinking. Article 04 reads like someone presenting their thinking. The structural difference is PROCESS vs PRODUCT.

This system fixes the gap between organized research and human-sounding prose.

---

## PHASE 1: INSIGHT GENERATION

_(No changes from existing system — see `research/insight-generation-system.md` and `research/insight-generation-architectures-v3.md`)_

The pipeline produces:

- Saturated research data
- Anomaly list
- Cross-referenced mechanism
- Coined term
- Falsifiable predictions
- Elevator pitch

**The output of Phase 1 is your PRIVATE NOTES. Not your article structure.**

---

## PHASE 2: DISORDER THE RESEARCH

This is the critical phase that was missing. The insight generation system produces organized artifacts. You need to BREAK that organization before writing.

### Step 1: Identify Your Discovery Sequence

Look at your research notes and ask: **In what order did I actually encounter these ideas?** Not the logical order. The chronological order of your own thinking.

For article 02, the real sequence was:

1. Started with AI payments thesis
2. Found x402 data ($1.2M total) — thesis fell apart
3. Found Circle's $908M Coinbase payment — new direction
4. Berkshire Hathaway comparison emerged
5. Realized Tether = holding company, not AI play
6. AI payments prediction narrowed

The article follows this sequence: thesis → stress test → new direction → comparison → realization → narrowed prediction. That's why it sounds human — it shows the JOURNEY of the thinking.

### Step 2: Find Your 2-3 "Direction Changes"

Every article needs at least 2 moments where the argument pivots. These should be real — places where the evidence pushed you somewhere you didn't expect.

Templates for direction changes:

- "Most of it fell apart." (02, line 9)
- "I should have been looking at..." (04, line 7)
- Self-correction: acknowledging what V1 got wrong

If you don't have genuine direction changes, your insight isn't ready. Go back to Phase 1.

### Step 3: Map Asymmetric Attention

Decide which sections get the MOST space based on what's MOST INTERESTING, not what's most important to the argument. Specifically:

- **Longest section:** The most interesting/uncertain material (NOT counterarguments)
- **Medium sections:** Core evidence and mechanism
- **Shortest sections:** Predictions, solutions, and counterarguments
- **At least one 30-50 word digression**

Target ratio of longest to shortest section: 2.5x to 4.5x.

Rule from voice model: Solution sections under 100 words. Prediction sections under 160 words. If your counterargument section is your longest, you're in defensive mode — AI's default posture.

### Step 4: Write a Messy Outline

NOT a structured outline. A sequence of thoughts in discovery order:

```
Bad (organized, will sound AI):
1. Introduction: LLMs and cognitive compression
2. Evidence: METR study, MIT EEG, GitClear
3. Mechanism: Compression substitution defined
4. Counterarguments: Calculator panic
5. Predictions: Three falsifiable claims
6. Conclusion

Good (discovery order, will sound human):
- Start with the METR result — the 39-point gap
- What changed my direction: not the data, the 69% who kept using it
- The Schmidhuber connection (this was the "aha" — put it 60-70% through)
- Evidence that complicates: novice boost, entry-level job data
- The thing that actually worries me (pipeline, not individuals)
- What breaks the calculator dismissal (keep short — 4 specific points, no section header)
- How to check if I'm wrong
```

### Step 5: Plant Open Loops

Open loops create the feeling of live thinking. Introduce a question or reference early, don't resolve it, move to something else, return to it later.

- **Micro loops** (closed within 1-2 paragraphs): "The number that matters" → data → implication
- **Macro loops** (closed 3+ paragraphs later): Introduce a comparison early ("Air France 447 keeps coming back to me here") → develop other evidence → return to it with new context

Article 02 does this naturally: the Berkshire Hathaway comparison is introduced in the "Two models" section but pays off in the "What the $4 billion actually is" section. The reader carries the comparison forward, which creates engagement.

The Zeigarnik Effect: unfinished tasks occupy our minds more than completed ones. Open loops pull attention forward through curiosity, not signposting.

---

## PHASE 3: WRITE THE DRAFT

### The 12 Structural Rules

These are extracted from quantitative comparison of articles 02/03 (human-sounding) vs article 04 (flagged as AI). See `research/voice-model-structural-rules.md` for full detail.

#### RULE 1: Transition Distribution

- 30-40% signposted ("This is where...", "The question isn't...")
- 20-25% associative ("The comparison that keeps coming to mind", "I keep seeing this pattern")
- 25-30% narrative/self-corrective ("I spent the week stress-testing", "I was wrong about...")
- 10-15% abrupt (single-sentence paragraphs that pivot direction)
- **FAIL IF:** More than 45% signposted

#### RULE 2: Paragraph Opening Distribution

- 30-35% with data, integrated into narrative voice ("In 2024, Circle paid..." not "A study found...")
- 30-35% with narrative/opinion ("I spent the week...", "Most of it fell apart")
- 20-25% with framing ("This sounds like...", "The question isn't...")
- 10% with questions
- **FAIL IF:** More than 25% conceptual framing openings, or fewer than 28% narrative openings

#### RULE 3: Evidence Density

- 1.5-2.3 data points per paragraph in data-heavy sections
- 50-60% of data woven into prose without study citations
- Zero consecutive study citations — always interpret between evidence points
- Data follows narrative arc — numbers appear when writer encounters them
- **FAIL IF:** More than 2.5 data points per paragraph, or any consecutive study citations

#### RULE 4: Theory Introduction Method

- 0 explicit "I'm calling this X" moments (seriously — zero)
- 70% of theoretical ideas embedded in narrative
- 20% introduced through analogy
- 10% as synthesis
- Key insight appears 60-70% through the section, not at the start
- **FAIL IF:** Any instance of "I'm calling this..." or theory-first structure

#### RULE 5: Section Length Asymmetry

- Longest sections explore most interesting/uncertain material
- Ratio of longest to shortest: 2.5-4.5:1
- Prediction sections: 100-160 words max
- Solution sections: under 100 words, or absent entirely
- At least one 30-50 word marked digression
- **FAIL IF:** Longest section is counterargument/defense, or solution section exceeds 225 words

#### RULE 6: Personal Voice Frequency

- 1 self-reference per 190-210 words
- 60% present-tense process ("I'm looking at", "keeps coming to mind")
- 30% past-tense investigation ("I spent the week")
- 10% uncertainty admission ("I don't know", "I can't tell yet")
- Uncertainty appears MID-SECTION as catalyst, not just at end
- **FAIL IF:** Fewer than 1 per 250 words, or uncertainty only at section ends

#### RULE 7: Paragraph Length Variation

- Shortest: 1-2 sentences, 9-21 words
- Longest: 7-9 sentences, 140-165 words
- At least 3 single-sentence paragraphs per article
- Variation is clustered: groups of short paragraphs, then sustained long ones
- Single-sentence paragraphs are pivots or punchlines
- **FAIL IF:** Fewer than 3 single-sentence paragraphs, or no paragraph exceeding 130 words

#### RULE 8: Data Introduction Style

- 60% direct integration: "In 2024, Circle paid Coinbase $908 million"
- 25% following emphasis: "The number that matters" then data
- 15% parenthetical or embedded
- 0% formal study citation format ("A study by [researcher] at [institution] found...")
- Numbers first, source later or never
- **FAIL IF:** Any formal "A study by X found..." citations

#### RULE 9: Section Ending Types

- 60-70% end with implications ("which means...")
- 20-25% end with new questions (opening to next section)
- 10-15% end with data points (letting evidence speak)
- 0% end with summarizing what was just said
- Many endings are inconclusive — trail off into uncertainty
- **FAIL IF:** Any section ending that summarizes the section

#### RULE 10: Argument Architecture

- Non-linear exploration: at least 2 major direction changes per article
- Self-correction frequency: 1-2 explicit "I was wrong about..." moments
- Tangent ratio: 5-8% of word count in acknowledged digressions
- Solution space: under 5% of word count, or absent entirely
- **FAIL IF:** Linear thesis-evidence-conclusion structure, or solution space exceeding 5%

#### RULE 11: Counterargument Handling

- Embedded, not sectioned — address objections within flow
- Brief acknowledgment: 30-50 words max per objection
- Usually parenthetical or tangent-marked: "And yes, X is concerning. But..."
- Move on quickly — don't linger in defensive posture
- **FAIL IF:** Dedicated counterargument section exceeding 150 words

#### RULE 12: Transition Phrase Patterns

**Use:**

- "This sounds like [X]. It isn't."
- "The comparison that keeps coming to mind is..."
- "I keep seeing this pattern"
- "Honestly, [qualification]"
- "Which is [probably/likely] why..."

**Avoid:**

- "The strongest objection to..."
- "Then there's..." (additive, more than once)
- "I'm calling this..."
- "This follows from..."
- "This distinction matters because..."

### Writing Process Guidelines

**Start with the most surprising data point.** Not the most important — the most surprising. Articles 02 and 03 both open with data that reframes the issue.

**Let the mechanism EMERGE.** Don't introduce your framework, then apply it. Show the evidence accumulating until the framework becomes inevitable. The reader should feel like they're discovering the pattern alongside you.

**Write in present tense where possible.** "I keep seeing this pattern" not "I noticed a pattern." "The comparison that keeps coming to mind" not "The comparison I thought of." Present tense signals active thinking. Past tense signals polished reporting.

**Break the paragraph every time your thinking pivots.** One thought per paragraph. If you're adding a new angle to the same point, new paragraph. Short paragraphs are free.

**Use fragments.** "Not a rounding error." "Same pattern in code." "No third-party deployments." Fragments break rhythmic predictability and signal conversational register.

**Mid-sentence qualifications.** "Honestly, most of it is probably just a holding company deploying profits." The qualification lives inside the thought, not in a separate hedging sentence.

---

## PHASE 4: STRUCTURAL AI TELL SCAN

Run this AFTER the draft, BEFORE final polish. This replaces the old surface-level vocabulary scan.

### Level 1: Quantitative Structure Check

Count these and compare against targets:

| Metric                                    | Target           | AI Red Flag                                     |
| ----------------------------------------- | ---------------- | ----------------------------------------------- |
| Sentence length std dev / mean            | > 0.4            | < 0.25 (uniform)                                |
| Paragraph word count std dev              | > 40             | < 20 (uniform)                                  |
| Single-sentence paragraphs                | >= 3 per article | 0-1                                             |
| Formal transitions per 1000 words         | < 2              | > 5 ("Furthermore," "Moreover," "Additionally") |
| Self-references per 1000 words            | 4.5-5.5          | < 3 or > 8                                      |
| Data points per paragraph (data sections) | 1.5-2.3          | > 3.0 (evidence clustering)                     |
| Longest/shortest section ratio            | 2.5-4.5:1        | < 2:1 (uniform coverage)                        |
| Solution/prediction word count            | < 5% of total    | > 10%                                           |

### Level 2: Pattern Detection

Check for these structural tells (more diagnostic than vocabulary):

**Signposting audit:**

- [ ] Count instances of text announcing what it will do before doing it
- [ ] "There are three reasons..." "Let me explain..." "Moving on to..."
- [ ] "I need to take a detour..." "This is where things get interesting..."
- [ ] Target: < 2 instances per article. Ideal: 0.

**Paragraph formula audit:**

- [ ] Count paragraphs following topic sentence → evidence → implication
- [ ] More than 30% in this pattern = AI structural tell
- [ ] Check: does every paragraph serve clear structural purpose? (Some shouldn't)

**Transition regularity audit:**

- [ ] Are transitions at predictable intervals (every 3-4 sentences)?
- [ ] Do they use the same syntactic pattern?
- [ ] Look for: "Furthermore" + "Moreover" + "Additionally" in same piece

**Section structure audit:**

- [ ] Does the article follow thesis → evidence → conclusion? (AI default)
- [ ] Are counterarguments in a dedicated section? (Should be embedded)
- [ ] Is the conclusion a restatement of the introduction? (Should be inconclusive)
- [ ] Is the introduction a thesis statement? (Should be narrative entry)

**Evidence presentation audit:**

- [ ] Any "A study by [X] at [Y] found..."? (Kill these)
- [ ] Any consecutive data citations without interpretation between them?
- [ ] Are all evidence types presented the same way? (Should vary)
- [ ] Do numbers come with institutional sourcing? (Numbers first, source later or never)

**Performative introspection audit:**

- [ ] "I've been sitting with this" / "I can't stop thinking about" / "this scares me"
- [ ] These TELL the reader the writer has emotions instead of SHOWING through content choice
- [ ] Replace with: spending more words on the thing you find interesting (asymmetric attention)

### Level 3: Discourse Pattern Check

**Entity reference clustering:**

- Human text refers back to entities introduced earlier, even with long separations
- AI clusters same-entity mentions close together
- Check: are your callbacks spread across the article, or clustered within sections?

**Event transition logic:**

- AI connects events in predictable logical sequence
- Humans make associative jumps ("The comparison that keeps coming to mind...")
- Check: could someone predict your next paragraph from your current one? If yes, add an unexpected pivot.

**Burstiness pattern:**

- AI: uniform sentence lengths throughout
- Human: clusters of short sentences, then sustained long ones
- Check: do you have at least one cluster of 3+ short sentences (< 15 words each)?

---

## PHASE 5: VOCABULARY SCAN

_(Quick pass — catch surface-level tells that survive structural editing)_

### Banned Words

delve, leverage, robust, comprehensive, seamless, transformative, landscape, journey, navigate, harness, foster, pivotal, crucial, moreover, furthermore, additionally, consequently, subsequently, facilitates, optimizes, underscores, illuminates, elucidates, paradigm, synergy, nuanced, tapestry, beacon, intersection, testament, multifaceted, myriad, plethora, embark, endeavor, realm, unveil

### Banned Patterns

- "It's not X, it's Y" more than once per piece
- "In today's [anything]..."
- "It's important to note..."
- "When it comes to..."
- Parallelism: same sentence structure repeated 3+ times
- Motivational/inspiring endings
- Both-sides hedging without taking a position
- "This distinction matters because..."
- Sentences starting with "This" more than twice in sequence

### Voice Targets

- Fragments in prose (at least 3 per article)
- Sentences starting with "And," "But," "So" (at least 5 per article)
- At least one contraction per 200 words
- Mid-sentence qualifications with dashes or commas
- At least one genuinely uncertain statement ("I don't know", "I can't tell yet")

---

## PHASE 6: FINAL REVISION CHECKLIST

Before publishing, verify:

### Structure

- [ ] Article follows discovery order, not logical order
- [ ] At least 2 direction changes / self-corrections
- [ ] No dedicated counterargument section (embedded in flow)
- [ ] Solution/prediction space under 5% of word count
- [ ] Longest section covers most interesting material, not defense
- [ ] Ending is inconclusive or opens a new question

### Voice

- [ ] Self-reference roughly every 200 words
- [ ] 60% present-tense process language
- [ ] At least one uncertainty admission mid-section (not just at end)
- [ ] At least 3 fragments
- [ ] At least 5 sentences starting with conjunctions (And, But, So)

### Evidence

- [ ] Zero formal study citations ("A study by X found...")
- [ ] Zero consecutive data points without interpretation
- [ ] Data introduced in varied ways (direct, emphasis, parenthetical)
- [ ] Numbers first, sources later or never

### Anti-AI

- [ ] Zero banned vocabulary words
- [ ] Zero signposting (announcing what text will do)
- [ ] Zero performative introspection (telling reader you have feelings)
- [ ] "It's not X, it's Y" used at most once
- [ ] No parallelism (same structure repeated)
- [ ] No summarizing conclusion

---

## MODEL USAGE

| Phase                                   | Model  | Rationale                           |
| --------------------------------------- | ------ | ----------------------------------- |
| Research (Phase 1: SATURATE)            | Sonnet | Web search + fact compilation       |
| Anomaly detection (Phase 1)             | Sonnet | Pattern matching against heuristics |
| Cross-referencing + mechanism (Phase 1) | Opus   | Insight quality lives here          |
| Predictions (Phase 1)                   | Sonnet | Structured work given mechanism     |
| DISORDER step (Phase 2)                 | Human  | YOU must decide discovery order     |
| Draft writing (Phase 3)                 | Opus   | Voice and rhythm need it            |
| Structural AI tell scan (Phase 4)       | Haiku  | Mechanical checklist work           |
| Vocabulary scan (Phase 5)               | Haiku  | Mechanical checklist work           |
| Final revision (Phase 6)                | Opus   | Structural rewriting needs quality  |

**Critical:** Phase 2 (DISORDER) should be done by the human writer, or if AI-assisted, the AI should be given ONLY the discovery sequence and told to write as if discovering each point for the first time. Never give the AI the organized research artifacts directly — it will present them.

---

## WHAT WENT WRONG WITH ARTICLE 04 (Post-Mortem)

1. **Insight pipeline produced organized artifacts** → writing step received clusters, mechanisms, coined terms in clean format
2. **Writing step presented the organized thinking** → thesis-evidence-conclusion structure, even with narrative language
3. **Specific failures:**
   - "I'm calling this compression substitution" (Rule 4: zero explicit naming)
   - "Why this isn't the calculator panic" section header (Rule 11: dedicated counterargument section, 445 words)
   - "Three patterns keep showing up" (signposting)
   - "I need to take a detour through information theory" (signposting)
   - Theory introduced at start of section, then evidence applied (Rule 4: key insight should appear 60-70% through)
   - 1 self-reference per 267 words (Rule 6: should be 1 per 190-210)
   - Data density of 3.1 per paragraph (Rule 3: should be 1.5-2.3)
   - 60% signposted transitions (Rule 1: should be 30-40%)

4. **Root cause:** The DISORDER phase didn't exist. Organized research went directly to writing.

---

## REFERENCE: What "Thinking on Paper" Looks Like

From articles 02 and 03, the patterns that read as human:

**Opening with a confession:** "I spent the week stress-testing that thesis. Most of it fell apart." — This is a writer showing you their process, not presenting conclusions.

**Real-time comparisons:** "The comparison that keeps coming to mind is Berkshire Hathaway." — Present tense, associative, emerging from thought rather than planned.

**Embedded uncertainty:** "Honestly, most of it is probably just a holding company deploying profits." — Three hedges in one sentence (honestly, most, probably), none of them performative.

**Asymmetric attention:** Article 02 spends ~250 words on the Coinbase fee structure (interesting, non-obvious) and ~80 words on predictions (obvious, just stating them). The ratio reveals what the writer actually finds interesting.

**Abrupt pivots:** "And yes, the Northern Data self-dealing is concerning." — Brief, parenthetical acknowledgment of a counterargument, then moves on in 50 words. No defensive posture.

**Trailing uncertainty:** "When AI payments reach meaningful scale, they won't split neatly between USDC and USDT the way I predicted." — Not resolving, opening up.

**Data as narrative:** "In 2024, Circle paid Coinbase $908 million in distribution fees. That was 54% of Circle's total revenue." — Number first, no sourcing apparatus, integrated into the thought flow.
