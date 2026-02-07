# Implementation Plan: Ralph Loop Execution

## The Ralph Loop

```
Plan → Build → PR → Review → Fix → Test → Merge → Next PR → [Loop]
```

Each loop iteration produces one mergeable PR. The Opus orchestrator drives the loop. Codex/Sonnet subagents handle implementation. Review agents validate.

---

## Execution Order: 18 PRs

### PR 1: Project Scaffold

**Branch:** `feat/project-scaffold`
**Files:**

- `pyproject.toml` — Python package with dependencies (click, rich, anthropic, pyyaml, nltk, pytest)
- `src/__init__.py`
- `src/cli.py` — Click CLI skeleton with `run`, `scan`, `topics`, `facts` command groups
- `src/config.py` — YAML config loader
- `config/pipeline.yaml` — Pipeline phases and model assignments
- `config/quality_thresholds.yaml` — All quality gate thresholds from SPEC
- `tests/conftest.py` — pytest fixtures
- `.github/workflows/test.yml` — CI: lint + test on every PR

**Tests:** `cli.py` responds to `--help`, config loads without error
**Review focus:** Package structure, dependency choices, config schema

---

### PR 2: Quality Scanners — Pure Python

**Branch:** `feat/quality-scanners-python`
**Files:**

- `src/quality/__init__.py`
- `src/quality/structural_scanner.py` — Sentence length CV, paragraph word std, single-sentence para count, section ratios, solution %, self-refs/1k
- `src/quality/vocabulary_scanner.py` — Banned words (regex), banned patterns, fragment count, conjunction starts, contraction frequency, em-dash count
- `src/quality/burstiness.py` — Sentence length variance clustering, burstiness score
- `src/quality/kolmogorov.py` — Gzip compression ratio scoring
- `tests/test_quality/test_structural_scanner.py`
- `tests/test_quality/test_vocabulary_scanner.py`
- `tests/test_quality/test_burstiness.py`
- `tests/test_quality/test_kolmogorov.py`

**Test fixtures:** Use articles 02, 03 (should score well) and 04 (should score poorly)
**Key validation:** Article 02 structural score > 7/10, article 04 < 5/10

---

### PR 3: Quality Scanners — LLM-Assisted

**Branch:** `feat/quality-scanners-llm`
**Files:**

- `src/quality/ai_tell_detector.py` — Signposting detection, parallelism detection, performative introspection, summarizing conclusion, data density per paragraph
- `src/quality/data_verifier.py` — Chain-of-Verification for factual claims, freshness checking
- `src/agents/__init__.py`
- `src/agents/base.py` — Base agent class wrapping Claude API (model selection, retry, cost tracking, streaming)
- `tests/test_quality/test_ai_tell_detector.py`

**Tests:** Mock Claude API responses, validate detection logic
**Review focus:** Prompt engineering quality, detection accuracy

---

### PR 4: Research Agents

**Branch:** `feat/research-agents`
**Files:**

- `src/agents/research.py` — 5 research track agents (money flow, power/governance, regulatory, comparative, practitioner)
- `src/tools/__init__.py`
- `src/tools/web_search.py` — Perplexity API / web search integration
- `src/prompts/research_track.py` — System prompts for each research track
- `tests/test_agents/test_research.py`

**Key logic:** Parallel execution of 5 research tracks, each returning structured facts with sources and dates. Validation: each track > 3000 words, > 15 data points.

---

### PR 5: Anomaly + Cross-Reference Agents

**Branch:** `feat/anomaly-crossref`
**Files:**

- `src/agents/insight.py` — Anomaly detection agent, cross-reference agent, mechanism articulation agent
- `src/prompts/insight_generation.py` — System prompts for anomaly detection, cross-referencing, mechanism
- `tests/test_agents/test_insight.py`

**Key logic:** Anomaly agent (Sonnet) identifies 5-10 anomalies. Cross-ref agent (Opus) finds intersections between tracks. Mechanism agent (Opus) writes causal chain.

---

### PR 6: Advanced Insight Agents

**Branch:** `feat/advanced-insight`
**Files:**

- `src/agents/debate.py` — Multi-agent debate (3 Opus agents: hypothesis generator, challenger, judge)
- Updates to `src/agents/insight.py` — Forced impasse, bisociation, prediction, validation agents
- `src/prompts/insight_generation.py` — Additional prompts

**Key logic:** Debate uses 3 parallel Opus agents. Forced impasse removes load-bearing assumption. Bisociation finds foreign-domain parallels.

---

### PR 7: DISORDER Agent

**Branch:** `feat/disorder-agent`
**Files:**

- `src/agents/disorder.py` — Discovery sequence identification, direction change mapping, asymmetric attention mapping, messy outline generation, open loop planting
- `src/prompts/disorder.py` — System prompts for each DISORDER step

**Key logic:** Takes organized research artifacts and BREAKS the organization. Outputs messy outline in discovery order. This is the most important agent — it prevents "presenting organized thinking."

---

### PR 8: Writer Agent

**Branch:** `feat/writer-agent`
**Files:**

- `src/agents/writer.py` — Draft writing agent with all 12 structural rules as constraints
- `src/prompts/writing.py` — The master writing prompt (includes all 12 rules, voice model, discovery-order instructions)

**Key logic:** Single Opus call with messy outline + full rule set. Generates draft that follows discovery order, not logical order.

---

### PR 9: Revision Agent

**Branch:** `feat/revision-agent`
**Files:**

- `src/agents/writer.py` — Add revision method that takes scan results and rewrites flagged sections
- Updates to writing prompts

**Key logic:** Takes structural scan + vocabulary scan results, identifies specific sections to rewrite, produces revised draft. Loops up to 3 times until quality gates pass.

---

### PR 10: Platform Formatters

**Branch:** `feat/platform-formatters`
**Files:**

- `src/agents/publisher.py` — Newsletter formatter, LinkedIn formatter, X thread formatter
- `src/prompts/platform_format.py` — Platform-specific prompts (newsletter voice, LinkedIn hooks, X thread structure)
- `tests/test_agents/test_publisher.py`

**Key logic:** Takes final article, produces 3 platform-specific versions. Newsletter: full article with title options. LinkedIn: 1300-char hook + key insight. X: 5-8 tweet thread with specific data points.

---

### PR 11: Pipeline Orchestrator

**Branch:** `feat/orchestrator`
**Files:**

- `src/orchestrator.py` — Full pipeline orchestrator with state management, phase execution, quality gate enforcement, cost tracking
- `src/storage/__init__.py`
- `src/storage/content_store.py` — Version-controlled content storage (markdown files with metadata)

**Key logic:** Runs all phases in order. Manages state between phases. Enforces quality gates. Tracks cost. Supports tier 1/2/3 configurations. Supports resuming from any phase.

---

### PR 12: CLI Interface

**Branch:** `feat/cli`
**Files:**

- `src/cli.py` — Full CLI implementation with all commands, Rich progress display, cost tracking output
- Rich-formatted output for scan results, pipeline progress, cost summary

---

### PR 13: Topic Selection System

**Branch:** `feat/topic-selection`
**Files:**

- `src/storage/topic_backlog.py` — SQLite-backed topic backlog with columns from SPEC
- `src/tools/regulatory.py` — Regulatory signal checking (Congress.gov, Federal Register)
- `src/tools/onchain.py` — On-chain data checking (Dune/Artemis APIs)
- CLI commands: `topics scan`, `topics backlog`, `topics add`

---

### PR 14: Facts Database

**Branch:** `feat/facts-db`
**Files:**

- `src/storage/facts_db.py` — SQLite facts database with freshness tracking, alert scheduling, source hierarchy
- CLI commands: `facts check`, `facts add`, `facts list`

---

### PR 15: Integration Tests

**Branch:** `feat/integration-tests`
**Files:**

- `tests/test_integration/test_full_pipeline.py` — End-to-end pipeline test with mocked API
- `tests/test_integration/test_quality_gates.py` — Quality gate integration tests
- `tests/fixtures/` — Mock API responses for each phase

---

### PR 16: Calibration

**Branch:** `feat/calibration`
**Work:**

- Run quality scanners against ALL existing articles (02, 03, 04)
- Tune thresholds so 02/03 pass and 04 fails
- Run full pipeline on a test topic
- Compare output quality to existing articles
- Adjust prompts based on output

---

### PR 17: End-to-End Testing

**Branch:** `feat/e2e-testing`
**Work:**

- Run full Tier 1 pipeline on real topic
- Run full Tier 2 pipeline on real topic
- Measure: cost, time, quality scores, manual assessment
- Fix any issues found

---

### PR 18: Documentation

**Branch:** `feat/docs`
**Files:**

- `README.md` — Usage, installation, configuration
- Update `SPEC.md` with any changes from implementation
- Update `MEMORY.md` with lessons learned

---

## The Orchestration Prompt

This is the prompt to give Claude Opus as the orchestrator that drives the ralph loop:

```
You are the orchestrator for building the writing-improver project. You drive a continuous build loop:

LOOP:
1. Read PLAN.md to identify the next PR to build
2. Create a feature branch
3. Implement all files for that PR
4. Run tests (pytest)
5. Fix any test failures
6. Run quality checks (ruff lint, mypy)
7. Fix any lint/type issues
8. Create a PR with a clear description
9. Self-review: read every file in the PR diff and check for:
   - Code simplicity (YAGNI, no premature abstractions)
   - Security (no hardcoded keys, no injection vectors)
   - Test coverage (every public function tested)
   - Prompt quality (for LLM-calling code: are prompts clear, specific, tested?)
10. Fix any issues found in self-review
11. Merge to main
12. Move to next PR

CONSTRAINTS:
- Each PR must be independently mergeable (no broken state on main)
- Tests must pass before merging
- Every agent prompt must include the relevant rules from elite-writing-system.md
- Quality scanner thresholds must match SPEC.md exactly
- Model assignments must match SPEC.md (Sonnet for research, Opus for insight/writing, Haiku for validation)
- Cost tracking must be built into every agent call
- Use async/await for parallel execution where specified in SPEC
- Keep files small and focused — one class per file, one responsibility per class

STATE TRACKING:
After each PR merge, update PLAN.md to mark the PR as complete.
Track cumulative: lines of code, test count, estimated API cost per run.

QUALITY BAR:
The ultimate test: run the full pipeline on "Stablecoin Distribution Economics" and compare output to content/02-insight-ai-capex-stablecoins.md. The automated output should score within 1 point of the human-written article on the quality scanner.
```

---

## Parallel Agent Assignments

For maximum speed, multiple agents can work simultaneously on independent PRs:

```
Timeline:
────────────────────────────────────────────────────
Week 1: PR 1 (scaffold) → PR 2 (python scanners) → PR 3 (llm scanners)
         │
         └── These are sequential (each depends on previous)

Week 2: PR 4 (research)  ←── can parallelize ──→  PR 5 (anomaly)
         │                                          │
         └── PR 6 (advanced insight) ◄──────────────┘

Week 3: PR 7 (disorder) → PR 8 (writer) → PR 9 (revision)
         │
         └── Sequential (each feeds into next)

Week 4: PR 10 (formatters)  ←── parallel ──→  PR 11 (orchestrator)
         │                                      │
         └── PR 12 (cli) ◄─────────────────────┘

Week 5: PR 13 (topics) ←── parallel ──→ PR 14 (facts)
         │                                │
         └── PR 15 (integration tests) ◄──┘

Week 6: PR 16 (calibration) → PR 17 (e2e) → PR 18 (docs)
```

---

## Success Metrics Per PR

| PR  | Key Metric         | Pass Condition                                    |
| --- | ------------------ | ------------------------------------------------- |
| 1   | CLI runs           | `writing-improver --help` works                   |
| 2   | Scanner accuracy   | Article 02 scores > 7, article 04 < 5             |
| 3   | Detection rate     | > 80% of known AI tells in article 04 detected    |
| 4   | Research quality   | Each track returns > 3000 words, > 15 data points |
| 5   | Anomaly count      | 5-10 anomalies identified from research           |
| 6   | Debate output      | 3 competing hypotheses generated and ranked       |
| 7   | DISORDER quality   | Output is in discovery order, not logical order   |
| 8   | Draft quality      | Passes > 60% of quality gates on first pass       |
| 9   | Revision quality   | Passes > 90% of quality gates after revision      |
| 10  | Format quality     | 3 platform outputs with correct constraints       |
| 11  | Pipeline completes | Full Tier 1 pipeline runs without error           |
| 12  | CLI complete       | All commands functional                           |
| 13  | Topic system       | Backlog CRUD operations work                      |
| 14  | Facts system       | Freshness checking identifies stale data          |
| 15  | Integration        | Full pipeline mocked test passes                  |
| 16  | Calibration        | Threshold tuning converges                        |
| 17  | E2E                | Real pipeline produces scoreable output           |
| 18  | Docs               | README covers all commands                        |
