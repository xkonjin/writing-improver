# Writing Improver: Full Production Spec

## What This Is

An automated multi-agent content pipeline for **@xkonjin** (Jin Fernando, marketing @ Plasma) that takes a topic and produces publication-ready content across newsletter, LinkedIn, and X/Twitter. The system enforces high Kolmogorov complexity (non-derivable insights) and passes structural AI detection.

## What Exists Today

23 research documents + 4 content drafts + 1 elite writing system document. All markdown. No automation. The intellectual system is mature — the 6-phase pipeline, 12 structural rules, 9 insight frameworks, data verification, topic selection, title craft, and anti-AI detection are all documented. **Nothing is code yet.**

## What We're Building

A Python CLI application (`writing-improver`) with multi-agent orchestration that automates the full pipeline:

```
Topic → Research → Insight → DISORDER → Draft → Structural Scan → Vocabulary Scan → Final Revision → Platform Output
```

---

## Architecture

### Core: Orchestrator + Specialist Agents

```
┌─────────────────────────────────────────────────────────┐
│                   ORCHESTRATOR (Opus)                     │
│  Routes tasks, manages state, synthesizes results        │
│  Runs the DISORDER phase (requires strongest reasoning)  │
└──────────┬──────────────┬───────────────┬───────────────┘
           │              │               │
    ┌──────▼──────┐ ┌────▼─────┐ ┌───────▼──────┐
    │  RESEARCH   │ │ QUALITY  │ │  PUBLISHING  │
    │  AGENTS     │ │ AGENTS   │ │  AGENTS      │
    │  (Sonnet)   │ │ (Haiku)  │ │  (Sonnet)    │
    ├─────────────┤ ├──────────┤ ├──────────────┤
    │ Track 1:    │ │ AI Tell  │ │ Newsletter   │
    │ Money Flow  │ │ Scanner  │ │ Formatter    │
    │             │ │          │ │              │
    │ Track 2:    │ │ Vocab    │ │ LinkedIn     │
    │ Power/Gov   │ │ Scanner  │ │ Formatter    │
    │             │ │          │ │              │
    │ Track 3:    │ │ Data     │ │ X/Twitter    │
    │ Regulatory  │ │ Verifier │ │ Formatter    │
    │             │ │          │ │              │
    │ Track 4:    │ │ Struct   │ │ Title        │
    │ Comparative │ │ Analyzer │ │ Generator    │
    │             │ │          │ │              │
    │ Track 5:    │ │ Burstiness│ │             │
    │ Practitioner│ │ Checker  │ │              │
    └─────────────┘ └──────────┘ └──────────────┘
```

### Tech Stack

| Component    | Technology                           | Why                                                                       |
| ------------ | ------------------------------------ | ------------------------------------------------------------------------- |
| Language     | Python 3.12+                         | Best Claude SDK, async support, rich ecosystem                            |
| CLI          | Click + Rich                         | Clean CLI with progress indicators                                        |
| AI           | Claude API (anthropic SDK)           | Opus for orchestration/writing, Sonnet for research, Haiku for validation |
| Web Research | Perplexity API / Exa API             | Structured web search for research agents                                 |
| Storage      | Local filesystem (markdown) + SQLite | Content versions, topic backlog, facts database                           |
| Config       | YAML                                 | Pipeline configuration, model assignments, prompts                        |
| Testing      | pytest + custom quality metrics      | Automated quality gates                                                   |
| CI/CD        | GitHub Actions                       | Lint, test, quality checks on every PR                                    |

### Directory Structure

```
writing-improver/
├── src/
│   ├── __init__.py
│   ├── cli.py                    # Click CLI entrypoint
│   ├── orchestrator.py           # Main Opus orchestrator
│   ├── config.py                 # YAML config loading
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base.py               # Base agent class
│   │   ├── research.py           # Research track agents (Sonnet)
│   │   ├── insight.py            # Insight generation (Opus)
│   │   ├── disorder.py           # DISORDER phase (Opus)
│   │   ├── writer.py             # Draft writing (Opus)
│   │   ├── publisher.py          # Platform formatters (Sonnet)
│   │   └── debate.py             # Multi-agent debate (Opus)
│   ├── quality/
│   │   ├── __init__.py
│   │   ├── structural_scanner.py # 12-rule structural analysis
│   │   ├── vocabulary_scanner.py # Banned words, patterns, voice targets
│   │   ├── burstiness.py         # Sentence/paragraph variation analysis
│   │   ├── kolmogorov.py         # Compression ratio scoring
│   │   ├── ai_tell_detector.py   # Structural AI tell detection
│   │   └── data_verifier.py      # Fact freshness + Chain-of-Verification
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── web_search.py         # Perplexity/Exa integration
│   │   ├── onchain.py            # Dune/Artemis stablecoin data
│   │   └── regulatory.py         # SEC EDGAR, Congress.gov
│   ├── storage/
│   │   ├── __init__.py
│   │   ├── content_store.py      # Version-controlled content
│   │   ├── facts_db.py           # SQLite facts database with freshness tracking
│   │   └── topic_backlog.py      # Topic backlog management
│   └── prompts/
│       ├── research_track.py     # Research agent system prompts
│       ├── insight_generation.py # Insight pipeline prompts
│       ├── disorder.py           # DISORDER phase prompts
│       ├── writing.py            # 12-rule writing prompts
│       ├── quality_check.py      # Scanner prompts
│       └── platform_format.py    # Newsletter/LinkedIn/X prompts
├── research/                     # Existing research docs (unchanged)
├── content/                      # Existing content (unchanged)
├── config/
│   ├── pipeline.yaml             # Pipeline configuration
│   ├── models.yaml               # Model assignments per phase
│   ├── prompts.yaml              # Customizable prompt templates
│   └── quality_thresholds.yaml   # Quality gate thresholds
├── tests/
│   ├── test_quality/
│   │   ├── test_structural_scanner.py
│   │   ├── test_vocabulary_scanner.py
│   │   ├── test_burstiness.py
│   │   ├── test_kolmogorov.py
│   │   └── test_ai_tell_detector.py
│   ├── test_agents/
│   │   ├── test_research.py
│   │   ├── test_insight.py
│   │   └── test_writer.py
│   ├── test_integration/
│   │   ├── test_full_pipeline.py
│   │   └── test_quality_gates.py
│   └── fixtures/
│       ├── article_02.md         # Known-good (human-sounding)
│       ├── article_03.md         # Known-good (human-sounding)
│       └── article_04.md         # Known-bad (AI-flagged)
├── elite-writing-system.md       # Existing system doc
├── SPEC.md                       # This file
├── pyproject.toml
└── README.md
```

---

## Pipeline Phases (What the Code Does)

### Phase 1: SATURATE (Research)

**Input:** Topic string + optional angle hint
**Output:** 4-5 research tracks, each 3000+ words of facts
**Model:** Sonnet (parallel execution)

```python
# Pseudocode
async def saturate(topic: str) -> list[ResearchTrack]:
    tracks = await asyncio.gather(
        research_agent("money_flow", topic, model="sonnet"),
        research_agent("power_structure", topic, model="sonnet"),
        research_agent("regulatory", topic, model="sonnet"),
        research_agent("comparative", topic, model="sonnet"),
        research_agent("practitioner", topic, model="sonnet"),
    )
    # Verify each track has >3000 words of specific facts
    for track in tracks:
        assert track.word_count > 3000
        assert track.data_point_count > 15
    return tracks
```

### Phase 2: FIND ANOMALIES

**Input:** Research tracks
**Output:** Numbered list of anomalies (factual statements, no interpretation)
**Model:** Sonnet

### Phase 2.5: FORCED IMPASSE (Tier 2+)

**Input:** Best current explanation + anomalies
**Output:** Restructured explanation after removing load-bearing assumption
**Model:** Opus

### Phase 3A: CROSS-REFERENCE

**Input:** Research tracks + anomalies
**Output:** Cross-track connections with mechanism candidates
**Model:** Opus

### Phase 3B: BISOCIATE (Tier 2+)

**Input:** Top anomalies
**Output:** Foreign-domain structural parallels
**Model:** Opus

### Phase 3E: MULTI-AGENT DEBATE (Tier 3)

**Input:** All research + anomalies + cross-references
**Output:** Winning hypothesis selected by evidence fit
**Model:** Opus (3 agents)

### Phase 4: ARTICULATE MECHANISM

**Input:** Cross-references + winning hypothesis
**Output:** Causal chain tracing value flow through named entities
**Model:** Opus

### Phase 5: PREDICT

**Input:** Mechanism
**Output:** 3-5 falsifiable predictions (entity + action + timeframe)
**Model:** Sonnet

### Phase 6: VALIDATE

**Input:** Complete insight
**Output:** Pass/fail on Kolmogorov test, template test, pre-mortem
**Model:** Haiku (mechanical) + Sonnet (pre-mortem)

### Phase 7: DISORDER

**Input:** Organized research artifacts + validated insight
**Output:** Messy outline in discovery order with direction changes mapped
**Model:** Opus (or human)

Steps:

1. Identify discovery sequence (chronological, not logical)
2. Find 2-3 direction changes
3. Map asymmetric attention (longest section = most interesting)
4. Write messy outline
5. Plant open loops (micro and macro)

### Phase 8: WRITE DRAFT

**Input:** Messy outline + 12 structural rules
**Output:** Draft article
**Model:** Opus

The writing prompt includes ALL 12 rules as constraints:

- Transition distribution targets
- Paragraph opening distribution
- Evidence density limits
- Theory introduction method
- Section length asymmetry
- Personal voice frequency
- Paragraph length variation
- Data introduction style
- Section ending types
- Argument architecture
- Counterargument handling
- Transition phrase patterns

### Phase 9: STRUCTURAL AI TELL SCAN

**Input:** Draft
**Output:** Scored report with specific fix instructions
**Model:** Haiku (counting/pattern matching)

Automated checks:

```python
@dataclass
class StructuralScanResult:
    sentence_length_cv: float      # Target: > 0.4
    paragraph_word_std: float      # Target: > 40
    single_sentence_paragraphs: int # Target: >= 3
    formal_transitions_per_1k: float # Target: < 2
    self_refs_per_1k: float        # Target: 4.5-5.5
    data_per_paragraph: float      # Target: 1.5-2.3
    section_ratio: float           # Target: 2.5-4.5
    solution_pct: float            # Target: < 5%
    signposting_count: int         # Target: < 2
    parallelism_detected: bool     # Target: False
    burstiness_score: float        # Target: > 0.6
    compression_ratio: float       # Kolmogorov proxy
```

Many of these can be computed WITHOUT an LLM — pure Python text analysis:

- Sentence length statistics (nltk/spacy)
- Paragraph word counts
- Single-sentence paragraph count
- Formal transition detection (regex)
- Self-reference counting (regex: I/I'm/I've/my/me)
- Section length ratios
- Burstiness (sentence length variance clustering)
- Compression ratio (gzip)

### Phase 10: VOCABULARY SCAN

**Input:** Draft
**Output:** Flagged banned words/patterns + voice target compliance
**Model:** Haiku (or pure Python regex)

This is almost entirely automatable without LLM:

- Banned word detection (regex against word list)
- Banned pattern detection (regex)
- Fragment count
- Conjunction-start count
- Contraction frequency
- Em-dash count per 1000 words

### Phase 11: FINAL REVISION

**Input:** Draft + scan results
**Output:** Revised article passing all quality gates
**Model:** Opus

### Phase 12: PLATFORM FORMATTING

**Input:** Final article
**Output:** Newsletter version + LinkedIn post + X thread
**Model:** Sonnet

---

## Quality Gates

Every draft must pass these automated gates before publication:

### Gate 1: Structural Quality (Phase 9)

| Metric                  | Min  | Max | Method |
| ----------------------- | ---- | --- | ------ |
| Sentence CV             | 0.35 | -   | Python |
| Para word std           | 35   | -   | Python |
| Single-sentence paras   | 3    | -   | Python |
| Formal transitions/1k   | -    | 2.5 | Regex  |
| Self-refs/1k words      | 4.0  | 6.0 | Regex  |
| Data points/para        | 1.3  | 2.5 | LLM    |
| Section ratio (max/min) | 2.0  | 5.0 | Python |
| Solution % of total     | -    | 7%  | Python |

### Gate 2: Anti-AI (Phase 9-10)

| Check                           | Threshold | Method |
| ------------------------------- | --------- | ------ |
| Banned words                    | 0         | Regex  |
| Signposting instances           | < 2       | LLM    |
| "Not X, it's Y" pattern         | <= 1      | Regex  |
| Parallelism (3+ same structure) | 0         | LLM    |
| Summarizing conclusion          | No        | LLM    |
| Performative introspection      | 0         | LLM    |
| Burstiness score                | > 0.5     | Python |

### Gate 3: Voice (Phase 10)

| Check                  | Target | Method |
| ---------------------- | ------ | ------ |
| Fragments              | >= 3   | Python |
| And/But/So starts      | >= 5   | Regex  |
| Contractions per 200w  | >= 1   | Regex  |
| Uncertainty statements | >= 1   | LLM    |
| Direction changes      | >= 2   | LLM    |

### Gate 4: Data Integrity (Phase 6)

| Check                                    | Method |
| ---------------------------------------- | ------ |
| Every stat has date                      | LLM    |
| Every claim has source                   | LLM    |
| No data > 6 months without justification | LLM    |
| Zero formal study citations              | Regex  |

---

## CLI Interface

```bash
# Full pipeline from topic to published content
writing-improver run "Stablecoin Distribution Economics" --tier 2

# Individual phases
writing-improver research "Topic" --tracks 4
writing-improver insight research-output.md
writing-improver disorder insight-output.md
writing-improver write disorder-output.md
writing-improver scan draft.md
writing-improver revise draft.md --scan-results scan.json
writing-improver format final.md --platforms newsletter,linkedin,x

# Quality scanning standalone
writing-improver quality-check content/02-insight-ai-capex-stablecoins.md

# Topic selection
writing-improver topics scan          # Run intelligence scan
writing-improver topics backlog       # View topic backlog
writing-improver topics add "Topic"   # Add to backlog

# Facts database
writing-improver facts check          # Run freshness audit
writing-improver facts add "claim" --source "url" --date "2026-01-15"
```

---

## Model Cost Optimization

| Phase               | Model          | Est. Cost  | Parallelizable   |
| ------------------- | -------------- | ---------- | ---------------- |
| Research (5 tracks) | Sonnet         | $2-3       | Yes (5 parallel) |
| Anomaly detection   | Sonnet         | $0.50      | No               |
| Forced impasse      | Opus           | $1-2       | No               |
| Cross-reference     | Opus           | $1-2       | No               |
| Bisociation         | Opus           | $1-2       | No               |
| Debate (3 agents)   | Opus           | $3-5       | Partially        |
| Mechanism           | Opus           | $1-2       | No               |
| Predictions         | Sonnet         | $0.50      | No               |
| Validation          | Haiku          | $0.25      | Yes              |
| DISORDER            | Opus           | $1-2       | No               |
| Writing             | Opus           | $2-3       | No               |
| Structural scan     | Haiku + Python | $0.25      | Yes              |
| Vocabulary scan     | Python         | $0         | Yes              |
| Revision            | Opus           | $2-3       | No               |
| Platform formatting | Sonnet         | $1         | Yes (3 parallel) |
| **TOTAL (Tier 2)**  |                | **$12-18** |                  |
| **TOTAL (Tier 1)**  |                | **$5-8**   |                  |
| **TOTAL (Tier 3)**  |                | **$20-30** |                  |

---

## Implementation Plan (Build Order)

### Milestone 1: Foundation (PR #1-3)

1. **Project scaffold** — pyproject.toml, Click CLI, config loading, directory structure
2. **Quality scanners (Python-only)** — The scanners that need NO LLM: sentence stats, paragraph stats, banned words, burstiness, compression ratio, regex patterns
3. **Quality scanners (LLM-assisted)** — Signposting detection, parallelism detection, data density counting, summarizing conclusion check

**Why first:** The quality scanners can be tested against existing articles (02, 03, 04). Article 02/03 should score well, article 04 should score poorly. This validates the system before building the generation pipeline.

### Milestone 2: Research Pipeline (PR #4-6)

4. **Base agent class** — Claude API wrapper with model selection, retry, streaming, cost tracking
5. **Research agents** — 5 parallel research tracks with web search tool integration
6. **Anomaly + cross-reference agents** — Anomaly detection (Sonnet), cross-referencing (Opus)

### Milestone 3: Insight Pipeline (PR #7-9)

7. **Insight agents** — Mechanism articulation, prediction, validation
8. **DISORDER agent** — Discovery sequence, direction changes, asymmetric attention
9. **Debate agents** — Multi-agent hypothesis generation and selection

### Milestone 4: Writing Pipeline (PR #10-12)

10. **Writer agent** — Draft generation with 12-rule constraints
11. **Revision agent** — Takes scan results, rewrites flagged sections
12. **Platform formatters** — Newsletter, LinkedIn, X thread generators

### Milestone 5: Integration + CLI (PR #13-15)

13. **Full pipeline orchestrator** — Ties all phases together with state management
14. **CLI interface** — All commands, progress display, cost tracking
15. **Topic selection + facts database** — Intelligence scanning, backlog, freshness tracking

### Milestone 6: Testing + Polish (PR #16-18)

16. **Integration tests** — Full pipeline tests with mocked API calls
17. **Calibration** — Run against existing articles, tune thresholds
18. **Documentation** — README, usage examples, configuration guide

---

## Success Criteria

1. **Quality scanner accuracy:** Article 02 and 03 score > 7/10, article 04 scores < 5/10
2. **Pipeline output:** Given a topic, produces a draft that scores > 7/10 on the quality scanner
3. **Cost per article:** Tier 2 pipeline under $20
4. **Time per article:** Under 30 minutes wall clock (with parallel research)
5. **AI detection:** Output passes GPTZero with < 20% AI probability
6. **Voice consistency:** Output matches Jin's voice model (assessed manually initially)
