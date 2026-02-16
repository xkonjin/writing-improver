# The Ultimate Writing System v3

**One document. Everything needed to produce Settlers-quality output across any channel.**

This supersedes `elite-writing-system.md`, `EXTREME_CODEX_SYSTEM.md`, and `thesis-generation-system.md` by unifying all three into a single executable pipeline. Those files remain for reference but this is the canonical system.

---

## Why AI Writing Fails (The Core Diagnosis)

AI writing fails for exactly one reason: **it presents organized thinking instead of showing the process of thinking.**

When you give an LLM organized research → clean clusters → numbered mechanisms → it PRESENTS them. Presenting organized thinking = AI. Showing the thinking process = human. The fix is architectural, not prompt engineering.

The second failure mode: **framework application instead of data-driven insight.** "Stablecoins have regulatory moats" applies to any industry. "GENIUS Act Section 4 mandates T-bill backing with ≤93 day maturity, creating $141B in mandatory Treasury demand from stablecoin issuers" does not. If you can swap the nouns, it's a template.

---

## The Pipeline (10 Phases)

```
SIGNAL → SATURATE ──┐→ FALSIFY → CROSS-REF → KOLMOGOROV → DISORDER → DRAFT → SCAN → ADAPT
  │          │      │      │          │          GATE          │         │       │       │
  │     6 Munger    │  Popper +    Opus only   50-word      Break the  12 Rules 4 scans Channel
  │      models     │ Bridgewater  (mechanism   ↓ or die    organization  +       │    compress
  │     (Sonnet)    │  (Sonnet)   + predict)                Discovery  Expert  Structural
  │                 │                                          order   quotes  Vocabulary
  Daily        X RESEARCH                                               from   Surprise
  habit        (parallel)                                              Phase   Compression
               x-search CLI                                             1.5       │
               Expert voices                                                Revision (max 3)
               Quotable takes
```

### Phase 0: SIGNAL DETECTION (Daily Habit)

**Not automated. This is the human part.**

Scan for anomalies — things that don't fit consensus narrative:

| Anomaly Type                            | Example                                            |
| --------------------------------------- | -------------------------------------------------- |
| Number moving wrong direction           | Revenue up, margins compressing                    |
| Gap between narrative and filing        | CEO says "AI-first," 10-K shows 90% legacy revenue |
| Hidden connections                      | Regulator → company revolving door                 |
| Consensus on thin evidence              | "X is next big thing" but adoption data flat       |
| Structural constraint money can't solve | Physical lead times, permitting queues             |

Write anomalies as factual statements. Don't interpret yet.

**Output:** One anomaly worth pursuing, stated as a factual contradiction.

---

### Phase 1: SATURATE (Parallel Research — Sonnet)

Run 6 parallel research tracks mapped to Munger's mental models. Each track returns **specific facts**: numbers, names, dates, mechanisms. Not narratives.

| Track         | Munger Model | Agent Persona           | Core Question                                             | Min Output  |
| ------------- | ------------ | ----------------------- | --------------------------------------------------------- | ----------- |
| 1. Mechanism  | Engineering  | System Engineer         | How does value physically move? What's the plumbing?      | 1,000 words |
| 2. Economics  | Economics    | Value Flow Analyst      | Who makes money? What's the unit economics? Margins?      | 1,000 words |
| 3. History    | History      | Pattern Precedent       | Has something similar happened? Eurodollars? S&Ls?        | 1,000 words |
| 4. Psychology | Psychology   | Behavior Analyst        | What incentives drive adoption? What builds/erodes trust? | 1,000 words |
| 5. Regulation | Regulatory   | Incentive Structuralist | What does the law say? Who wrote it? Who benefits?        | 1,000 words |
| 6. Inversion  | Inversion    | Failure Case Analyst    | How would this collapse? Single points of failure?        | 1,000 words |

**Source priority:** SEC filings, regulatory text > academic papers, attestations > industry reports > news/Twitter

**Model:** Sonnet. This is fact compilation, not reasoning.

**Output:** 6,000+ words of sourced facts across 6 tracks.

---

### Phase 1.5: X RESEARCH (Live Signal + Voice Mining — x-search CLI)

Runs in parallel with Phase 1 SATURATE. Two purposes: (1) find real-time signal that static sources miss, (2) mine expert voices for quotable takes and structural patterns.

**Step 1: Topic pulse check**

```bash
x-search search "<topic>" --quick --limit 10
x-search search "<topic>" --sort likes --since 7d --quality --limit 15
```

What you're looking for: who's talking about this, what angle they're taking, what data they're citing that you don't have.

**Step 2: Expert voice mining**

| Expert Type                 | Search Pattern                                                          | What You Extract                                   |
| --------------------------- | ----------------------------------------------------------------------- | -------------------------------------------------- |
| Domain practitioners        | `x-search search "<topic>" --from austinc_eth --limit 10`               | Specific claims with numbers, mechanisms           |
| Best writers (voice models) | `x-search profile mattlevine`                                           | Structural patterns, how they frame similar topics |
| Contrarians                 | `x-search search "<topic> wrong OR overrated OR actually" --sort likes` | Counter-arguments you haven't considered           |
| Data posters                | `x-search search "<topic> $" --quality --min-likes 50`                  | Charts, numbers, filing references                 |

**Watchlist (domain experts to always check):**

```bash
x-search watchlist check   # runs all at once
```

Recommended watchlist for stablecoin/crypto/fintech:

- `austinc_eth` (Austin Campbell — stablecoin mechanisms)
- `paborak` (patio11 — fintech/payments infrastructure)
- `mattlevine` (Matt Levine — financial structure)
- `byrnehobart` (Byrne Hobart — structural analysis)
- `nic__carter` (Nic Carter — stablecoin data)
- `jerallaire` (Jeremy Allaire — Circle/issuer perspective)

**Step 3: Thread deep-dives**
When a tweet references a thread with specific data:

```bash
x-search thread <TWEET_ID>   # follow the full argument
```

**Step 4: Find quotable takes**

```bash
x-search search "<thesis keyword>" --sort likes --min-likes 100 --quality --save
```

Usage in article: Quote specific people by name with their take. "Austin Campbell pointed out that [specific mechanism]" is anti-AI — it's timestamped, attributable, and falsifiable. Never paraphrase into generic framing.

**Integration rules:**

- X data is Tier 4 (narrative layer) — use for psychology track and voice, not as primary evidence
- Exception: when a domain expert posts specific numbers from a filing/report, that's Tier 2 if you can verify the source
- Save notable tweets with `--save` for article footnotes and embeds
- Mine 2-3 expert voices per article to quote directly (attribution = anti-AI)

**Model:** None (CLI tool, no LLM cost).

**Output:** Expert quotes, contrarian takes, real-time data points, voice patterns.

---

### Phase 2: FALSIFY (Popper + Bridgewater — Sonnet)

The phase that was missing from the original system. Explicitly try to break the emerging thesis.

**Step 1: State thesis falsifiably**

| Bad (unfalsifiable)                   | Good (falsifiable)                                                                               |
| ------------------------------------- | ------------------------------------------------------------------------------------------------ |
| "Stablecoins are important to crypto" | "Removing USDT would reduce exchange volume by 60%+"                                             |
| "Regulation creates moats"            | "GENIUS Act Section 4 mandates ≤93-day T-bill backing, creating $141B mandatory Treasury demand" |

**Step 2: List falsifying conditions**
What evidence would prove this false? List 3+ specific conditions.

**Step 3: Actively seek counter-evidence (Bridgewater disagreement)**
Have a devil's advocate agent rewrite the thesis as false. Not a strawman — the _strongest_ counter-argument.

**Step 4: Rate confidence**

- Thesis survives: which conditions tested and held?
- Thesis weakens: which conditions revealed fragility?
- Overall confidence: \_\_/100

**Model:** Sonnet (structured disagreement against heuristics).

**Output:** Falsification worksheet with confidence-rated thesis.

---

### Phase 3: CROSS-REFERENCE (Where The Thesis Emerges — Opus)

This is the ONLY step that requires deep reasoning. Look for connections BETWEEN research tracks.

**Productive intersections:**

- Money flow + Power structure = who benefits from the plumbing being this way?
- Regulation + Structural constraints = does the law exploit a constraint that can't be arbitraged?
- Money flow + Regulation = does the law create a closed loop in value chain?
- Power structure + Constraints = who controls the scarce resource? Can they be displaced?

**The mechanism test:** Can you trace value from origin to destination, naming every entity and what they gain at each step? If yes, you understand the mechanism. If you can only describe the pattern ("value is shifting from X to Y"), you're still at the surface.

**Model:** Opus. This is where insight quality lives.

**Output:** One non-obvious structural mechanism with causal chain.

---

### Phase 4: KOLMOGOROV GATE (Hard Stop — No Model Needed)

**State the core insight in ≤50 words.** If you can't, go back to Phase 3.

This is a hard gate. Not a soft suggestion.

**Tests:**

1. Remove any single data point — does the thesis weaken? (Must be yes)
2. Swap the nouns — does the argument still work? (Must be no)
3. Could a generalist with frameworks but no domain expertise reach this? (Must be no)

**Examples:**

FAIL (22 words, but template): "Regulation creates barriers that benefit incumbents with compliance infrastructure, increasing switching costs and consolidating market share among established players."

PASS (48 words): "Tether's $122B in T-bills funded by $17B in growing secured loans means any disruption to the loan book (regulatory ban, rate inversion) forces T-bill liquidation, which would remove $122B in Treasury demand overnight — making the US government a structural defender of Tether's solvency."

**Output:** ≤50-word thesis statement. If it fails, loop back.

---

### Phase 5: DISORDER (Break the Organization — Opus)

**The #1 reason AI writing sounds AI:** organized research artifacts go directly to writing.

**Step 1: Identify discovery sequence**
In what order did the thinking actually happen? Not the logical order — the chronological order of discovery.

**Step 2: Find 2-3 direction changes**
Every article needs ≥2 moments where evidence pushed the argument somewhere unexpected.

- "Most of it fell apart."
- "I should have been looking at..."
- Self-correction: acknowledging what the first interpretation got wrong

If you don't have genuine direction changes, the insight isn't ready. Go back to Phase 3.

**Step 3: Map asymmetric attention**

- Longest section: most interesting/uncertain material (NOT counterarguments)
- Medium sections: core evidence and mechanism
- Shortest sections: predictions, solutions, counterarguments
- Target ratio longest:shortest = 2.5x to 4.5x

**Step 4: Write messy outline**
In discovery order, not logical order. Include the "wrong turns."

**Step 5: Plant open loops**
Introduce a question early, don't resolve it, return later.

**Model:** Opus. Discovery sequencing requires narrative intelligence.

**Output:** Messy outline in discovery order with planted direction changes.

**CRITICAL: Never give the AI organized research artifacts as writing input.** Give it: (1) the discovery sequence, (2) the most surprising data point to open with, (3) instructions to write as if discovering each point for the first time.

---

### Phase 6: DRAFT (12 Structural Rules — Opus)

Write from the messy outline, not from the organized research. The 12 Rules are quantitative targets:

| #   | Rule                           | Target                               | Metric               |
| --- | ------------------------------ | ------------------------------------ | -------------------- |
| 1   | Transition variety             | ≥3 types per article                 | transition_diversity |
| 2   | Evidence density               | ≥1 specific data point per 200 words | evidence_per_200w    |
| 3   | Paragraph word count variation | std dev ≥20                          | paragraph_word_std   |
| 4   | Section length ratio           | longest ≥2.5x shortest               | section_ratio        |
| 5   | Sentence length variety        | ≥3 sentence lengths                  | sentence_variety     |
| 6   | Counterargument embedding      | ≤50 words, no dedicated section      | embedded_counter     |
| 7   | Theory emergence               | 60-70% through the piece             | theory_position      |
| 8   | Open loop count                | ≥1 planted and resolved              | open_loops           |
| 9   | Direction changes              | ≥2 genuine pivots                    | direction_changes    |
| 10  | Paragraph with >120 words      | ≥1                                   | long_paragraph       |
| 11  | Paragraph with <10 words       | ≥1                                   | short_paragraph      |
| 12  | Solution section               | <100 words                           | solution_brevity     |

**Additional constraints:**

- At least one fragment or sentence starting with "And," "But," "So"
- At least one mid-sentence qualification
- No signposting ("In this section we will explore...")
- No performative introspection ("I've been sitting with this...")
- ≥2 direct attributions to named experts (from Phase 1.5 X research)
- ≥1 reference to a specific filing, act, or regulatory document

**Voice injection from X research:**
Use the expert quotes from Phase 1.5 as anchors. Instead of "analysts believe X," write "Austin Campbell's point about [mechanism] holds up when you check Circle's S-1." Direct attribution to a named human with a specific claim is maximally anti-AI.

**Finding example articles to learn from:**
Before drafting, search X for how the best writers covered the same or adjacent topics:

```bash
x-search search "<topic>" --from mattlevine --limit 5
x-search search "<topic>" --from byrnehobart --limit 5
x-search search "<adjacent topic>" --sort likes --min-likes 200 --quality
```

Study their structural choices: where do they put the surprise? How do they handle the counterargument? What's their evidence density? Don't copy — extract the structural move and adapt it.

**Model:** Opus. Voice and rhythm need it.

**Output:** Full draft following discovery-order outline with named expert attributions.

---

### Phase 7: SCAN (4 Automated Scanners — Python)

Run all four in parallel:

| Scanner     | File                                 | What It Catches                                                        | Pass Threshold |
| ----------- | ------------------------------------ | ---------------------------------------------------------------------- | -------------- |
| Structural  | `src/quality/structural_scanner.py`  | Signposting, parallelism, uniform sections, thesis-evidence-conclusion | Score ≥7.0     |
| Vocabulary  | `src/quality/vocabulary_scanner.py`  | Banned words, em-dashes, AI transitions                                | 0 violations   |
| Surprise    | `src/quality/surprise_detector.py`   | Template application, obvious analysis, no gap                         | Score ≥0.6     |
| Compression | `src/quality/compression_scanner.py` | Information density, zero-info transitions                             | Score ≥7.0     |

**Plus Settlers Validator** (`src/quality/settlers_validator.py`):

- ≥7 mechanisms with thresholds and causal verbs
- ≥2 inversions with numbers
- ≥2 falsifiable predictions with timeframes
- Personal layer (confession/admission + we/us/our)
- 0 em-dashes, 0 AI transitions, 0 narrative markers

**If any scanner fails:** Go to Phase 8 (revision) with specific failure data.

**Output:** Pass/fail per scanner with specific failure locations.

---

### Phase 8: REVISION (Targeted Rewrite — Opus, Max 3 Rounds)

Don't rewrite the whole article. Fix only what the scanners flagged.

| Failure Type           | Fix Strategy                                                              |
| ---------------------- | ------------------------------------------------------------------------- |
| Structural parallelism | Vary lead-ins: numbered, transitional, direct data                        |
| Uniform paragraphs     | Add one >120 words, one <10 words                                         |
| Low surprise score     | Find the gap between expectation and reality; demonstrate, don't announce |
| Banned words           | Replace with specific data references                                     |
| Missing mechanisms     | Add threshold numbers and causal verbs to existing claims                 |
| Low compression        | Remove ornamental words; each word must be load-bearing                   |

After each round, re-run Phase 7. Max 3 rounds — if it still fails, the insight needs work (go back to Phase 3).

**Output:** Revised article that passes all scanners.

---

### Phase 9: ADAPT (Channel Compression — Sonnet)

Same Kolmogorov core insight, different compression levels per platform.

| Channel                | Length            | Format                                                               | What Changes                                                      | What Stays                              |
| ---------------------- | ----------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------- |
| Newsletter (X Article) | 1,500-2,500 words | Full thesis with personal layer, direction changes, evidence cascade | Everything — this is the canonical version                        | —                                       |
| Telegram thesis card   | 400-800 words     | Core mechanism + 1 prediction + 1 data inversion                     | Remove personal layer, compress evidence to top 3 data points     | Mechanism, prediction, specific numbers |
| X thread               | 5-8 tweets        | Hook → mechanism → surprising data → prediction → call               | Remove all prose; each tweet = one specific claim with one number | Core insight, falsifiable prediction    |
| LinkedIn post          | 800-1,200 words   | Professional framing, industry implications                          | Add "what this means for [industry]" angle                        | Mechanism, data, prediction             |

**Compression rule:** The Kolmogorov core (≤50 words from Phase 4) appears in EVERY channel version. Everything else is expansion or compression around it.

**Model:** Sonnet. Structured compression, not reasoning.

**Output:** Platform-specific versions of the article.

---

## Personal Memory Bank

The anti-AI property that makes content unfakeable. These are specific, lived experiences that no AI can generate from a prompt.

### Categories to Maintain

| Category                 | Example from Article 06                      | Why It Works                                         |
| ------------------------ | -------------------------------------------- | ---------------------------------------------------- |
| Cultural touchstones     | "WOW MONERO WOW DASH WOW UNLIMITED COCAINE"  | Specific trollbox memory, high Kolmogorov complexity |
| Personal trading history | "Stellar bags you never meant to hold"       | Specific loss, emotionally grounded                  |
| Community membership     | "Boryoku Dragonz to basis trades"            | Named community, specific transition                 |
| Identity evolution       | "Runescape pseudonyms → Poloniex → BCH wars" | Chronological sequence only someone who lived it has |

### Usage Rules

1. Personal layer goes ON TOP of analytical foundation. V3 (pure data) scored 10.0/10.0. V4 added personal. Never personal _instead of_ analytical.
2. Callbacks weave the two layers: "when we were trading dragon JPEGs" connects personal opening to analytical body.
3. The "messiness" of lived experience IS the anti-AI property. Don't clean it up.

---

## Model Assignment (Cost Optimization)

| Phase                  | Model  | Why                                               | Estimated Cost |
| ---------------------- | ------ | ------------------------------------------------- | -------------- |
| 1. SATURATE (6 agents) | Sonnet | Fact compilation, not reasoning                   | ~$2-3          |
| 1.5 X RESEARCH         | None   | CLI tool (x-search), no LLM cost                  | $0             |
| 2. FALSIFY             | Sonnet | Structured disagreement against heuristics        | ~$1-2          |
| 3. CROSS-REFERENCE     | Opus   | This is where insight quality lives               | ~$3-5          |
| 4. KOLMOGOROV GATE     | None   | Human or simple word-count check                  | $0             |
| 5. DISORDER            | Opus   | Discovery sequencing needs narrative intelligence | ~$2-3          |
| 6. DRAFT               | Opus   | Voice and rhythm need it                          | ~$3-5          |
| 7. SCAN                | Python | Automated, deterministic                          | $0             |
| 8. REVISION            | Opus   | Targeted rewriting, max 3 rounds                  | ~$2-4          |
| 9. ADAPT               | Sonnet | Structured compression                            | ~$1-2          |

**Total per article:**

- Tier 1 (Quick): $5-8 — skip falsification, single revision round
- Tier 2 (Deep): $12-18 — full pipeline, 2 revision rounds
- Tier 3 (Maximum): $20-30 — full pipeline + multi-agent debate + 3 revision rounds

---

## Quality Hierarchy

Not all quality is equal. Ordered by diagnostic power:

1. **Insight quality** (Kolmogorov gate) — Is the thesis non-obvious and data-specific?
2. **Mechanism clarity** (Feynman test) — Can you explain each claim in 2 sentences without jargon?
3. **Falsifiability** (Popper test) — Is the thesis stated in a way that can be disproved?
4. **Structural tells** (scanner) — Does the writing structure itself signal AI?
5. **Vocabulary tells** (scanner) — Do specific words/phrases signal AI?

An article that passes 4 and 5 but fails 1 is "well-formatted mediocrity." An article that passes 1-3 but has a few vocabulary issues is fixable. **Always optimize top-down.**

---

## The Settlers Standard (What 10/10 Looks Like)

Article 06 — "The Settlers Lobbied for Terraforming" — is the benchmark. Why it works:

| Dimension               | What It Does                                 | How                                                                           |
| ----------------------- | -------------------------------------------- | ----------------------------------------------------------------------------- |
| Personal layer          | Unfakeable opening                           | 4 paragraphs: Runescape → Poloniex trollbox → BCH wars → Boryoku Dragonz      |
| Mechanism density       | 10+ mechanisms with thresholds               | "$6.87B daily volume," "7% visibility threshold," "$43M revenue per employee" |
| Data inversions         | 3+ counterintuitive findings                 | Income vs holdings paradox: $111K income, $597 crypto                         |
| Falsifiable predictions | 3+ with timeframes                           | Specific by-when claims that can be checked                                   |
| Discovery order         | Reads like thinking, not presenting          | Direction changes at ~30% and ~65% through                                    |
| Asymmetric sections     | Evidence section 3x conclusion               | Interesting material gets space; obvious material compressed                  |
| Callbacks               | Personal and analytical woven together       | "when we were trading dragon JPEGs" → connects opening to body                |
| Zero AI tells           | No em-dashes, no transitions, no signposting | Vocabulary and structural scans both pass                                     |

---

## Anti-Patterns (Things That Sound AI)

| Pattern                           | Why It's Bad                                 | Fix                                                 |
| --------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| Signposting                       | "In this section we'll explore..."           | Just start with the data                            |
| Performative introspection        | "I've been sitting with this data..."        | Show the data, not your feelings about it           |
| Thesis → evidence → conclusion    | AI's default organization                    | Use discovery order instead                         |
| Dedicated counterargument section | Defensive posture, AI default                | Embed in 30-50 words, no header                     |
| Uniform section lengths           | ~1.5:1 ratio (AI default)                    | Target 2.5-4.5:1 ratio                              |
| Theory announced then defended    | "The key insight is..." then evidence        | Theory should emerge 60-70% through                 |
| Consecutive data points           | "X is $1B. Y is $2B. Z is $3B."              | Interpret between each: what does this number mean? |
| Formal citations                  | "A study by X found..."                      | Weave naturally: "X's S-1 filing shows..."          |
| Motivational endings              | "The future belongs to..."                   | End with a specific prediction or question          |
| Em-dashes as connectors           | "The market — which grew 40% — now faces..." | Use commas, parentheses, or restructure             |

---

## Quick Reference: When You're Stuck

| Problem                                  | Framework to Apply       | Action                                                                            |
| ---------------------------------------- | ------------------------ | --------------------------------------------------------------------------------- |
| Article feels obvious                    | Novelty Test             | Is it data-driven or framework-applied? Add specific data or find different angle |
| Explains what, not why                   | Feynman Test             | Can you explain without jargon? You're missing the mechanism                      |
| Lacks conviction                         | Falsification            | State thesis falsifiably. What's the counter-evidence?                            |
| Feels AI despite clean vocabulary        | Surprise Validation      | Is surprise genuine (gap) or manufactured (announced)?                            |
| No clear thesis from exhausting research | Inversion                | "How would this collapse?" is often clearer than "what makes this work?"          |
| Multiple candidate theses                | Bridgewater Disagreement | Which survives the strongest counter-argument?                                    |
| Well-written but unmemorable             | Kolmogorov Compression   | State core insight in <50 words. If you can't, it's not crystallized              |

---

## File Map

| File                                                     | Purpose                                            | When to Read                         |
| -------------------------------------------------------- | -------------------------------------------------- | ------------------------------------ |
| `config/pipeline.yaml`                                   | Phase config with model assignments and tier skips | When running automated pipeline      |
| `config/quality_thresholds.yaml`                         | Calibrated thresholds for all scanners             | When adjusting pass/fail criteria    |
| `src/agents/extreme_codex_swarm.py`                      | 10-agent research swarm implementation             | When modifying agent personas        |
| `src/quality/settlers_validator.py`                      | Mechanism/inversion/prediction counting            | When adjusting Settlers quality gate |
| `src/quality/surprise_detector.py`                       | Non-obviousness scoring (Levine test)              | When insight feels obvious           |
| `src/quality/structural_scanner.py`                      | Structural AI tell detection                       | When article "sounds AI"             |
| `src/quality/vocabulary_scanner.py`                      | Banned words and em-dash detection                 | When cleaning vocabulary             |
| `research/voice-model-structural-rules.md`               | The 12 Rules with quantitative targets             | During drafting                      |
| `research/frameworks-quick-reference.md`                 | 9 insight frameworks, one-page lookup              | When stuck on insight generation     |
| `research/applying-methodologies-to-writing-pipeline.md` | Tactical integration of frameworks to pipeline     | When enhancing pipeline phases       |
| `content/06-thesis-process-notes.md`                     | How the Settlers article was actually built        | Before touching article 06           |

---

## Implementation Status

| Phase               | Code Exists                                              | Status                                                            |
| ------------------- | -------------------------------------------------------- | ----------------------------------------------------------------- |
| 0. Signal Detection | No (manual)                                              | By design — human judgment                                        |
| 1. SATURATE         | Yes (`src/agents/research.py`, `extreme_codex_swarm.py`) | Working, needs Munger model mapping                               |
| 1.5 X RESEARCH      | Yes (`x-search` CLI)                                     | Working, needs watchlist setup + integration into pipeline runner |
| 2. FALSIFY          | Yes (`src/agents/falsification.py`)                      | Working, needs Bridgewater disagreement agent                     |
| 3. CROSS-REFERENCE  | Yes (`config/pipeline.yaml` cross_reference phase)       | Working                                                           |
| 4. KOLMOGOROV GATE  | Partial (`src/quality/kolmogorov.py`)                    | Needs ≤50-word hard gate                                          |
| 5. DISORDER         | Yes (`src/agents/disorder.py`)                           | Working                                                           |
| 6. DRAFT            | Yes (`src/agents/writer.py`)                             | Working                                                           |
| 7. SCAN             | Yes (4 scanners + settlers_validator)                    | Working                                                           |
| 8. REVISION         | Yes (`config/pipeline.yaml` revision phase)              | Working, max 3 rounds                                             |
| 9. ADAPT            | Partial (`src/distribution/`)                            | Needs channel-specific compression rules                          |

**Remaining implementation gaps:**

1. Map SATURATE agents to Munger's 6 models explicitly
2. Add Bridgewater disagreement agent to FALSIFY phase
3. Implement ≤50-word Kolmogorov hard gate
4. Build channel compression rules for Phase 9
5. Systematize personal memory bank as reusable asset
6. Integrate `x-search` into pipeline runner (auto-run watchlist + topic search in parallel with SATURATE)
7. Add expert attribution requirement to Settlers validator (≥2 named expert quotes)
