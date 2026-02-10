# Writing Improver

Multi-agent content pipeline that generates newsletter articles, LinkedIn posts, and X threads with Kolmogorov complexity enforcement.

Built for stablecoin/fintech content. Voice model: Austin Campbell / patio11 / Matt Levine.

## Install

```bash
pip install -e ".[dev]"
```

## Commands

### Run full pipeline

```bash
writing-improver run "Stablecoin Distribution Economics" --tier 1
```

Tiers: 1 (quick, $5-8), 2 (deep, $12-18), 3 (maximum, $20-30).

### Scan a draft

```bash
writing-improver scan content/02-insight-ai-capex-stablecoins.md
```

Outputs a table with structural, vocabulary, and burstiness scores.

### Quality gate check

```bash
writing-improver quality-check content/02-insight-ai-capex-stablecoins.md
```

Pass/fail against calibrated thresholds.

### List previous runs

```bash
writing-improver list-runs
```

### Topic management

```bash
writing-improver topics add "GENIUS Act Impact on Stablecoin Issuers"
writing-improver topics backlog
writing-improver topics scan
```

### Facts database

```bash
writing-improver facts add "Circle paid Coinbase \$908M in 2024" --source "https://..." --date 2024-01-15
writing-improver facts check
```

## Pipeline Architecture

```
Research (5 tracks, Sonnet) → Anomaly Detection (Sonnet) → Cross-Reference (Opus)
→ Mechanism (Opus) → Prediction (Sonnet) → Validation (Haiku) → DISORDER (Opus)
→ Write (Opus, 12 rules) → Quality Scan (Python) → Revision (Opus, max 3x)
→ Platform Format (Sonnet: newsletter + LinkedIn + X thread)
```

Tier 2 adds: forced impasse, bisociation. Tier 3 adds: 3-agent debate.

## Quality Gates

| Category   | Metric             | Threshold  |
| ---------- | ------------------ | ---------- |
| Structural | sentence_length_cv | >= 0.35    |
| Structural | paragraph_word_std | >= 20      |
| Structural | section_ratio      | 2.0 - 12.0 |
| Anti-AI    | banned_words       | <= 2       |
| Anti-AI    | burstiness         | >= 0.3     |
| Voice      | conjunction_starts | >= 5       |
| Voice      | fragments          | >= 1       |

Calibrated against 3 human-written articles (02, 03, 04).

## Configuration

### Environment Variables

Create `.env` and `.env.local` files with:

```bash
# Required for OpenRouter multi-agent swarm
OPENROUTER_API_KEY=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

# Optional for other integrations
ANTHROPIC_API_KEY=your-api-key-here
GEMINI_KEY=your-gemini-key
X_API_KEY=your-x-api-key
X_API_KEY_SECRET=your-x-secret
X_BEARER_TOKEN=your-x-bearer-token
```

### Config Files

- `config/pipeline.yaml` — phases, model assignments, tier definitions
- `config/quality_thresholds.yaml` — quality gate thresholds (calibrated)

## OpenRouter Multi-Agent Swarm

Run bottom-up research with diverse models:

```bash
python run_bottom_up_swarm.py
```

This executes:
1. **Research Swarm**: 5-7 specialized agents (Data Archaeologist, Mechanism Hunter, Pattern Breaker, etc.)
2. **Model Diversity**: Claude, GPT-4, Llama, Mistral, DeepSeek via OpenRouter
3. **Synthesis Competition**: Multiple approaches compete for best insight
4. **Voice Editing**: Multi-pass editing to remove AI tells

Outputs:
- `content/10-swarm-research.md` (raw agent findings)
- `content/10-swarm-synthesis.md` (synthesis output)  
- `content/10-coinbase-bottom-up-final.md` (final article)

## Development

```bash
ruff check src/ tests/
mypy src/ --ignore-missing-imports
pytest tests/ -q
```

## Key Design Decisions

**DISORDER phase**: organized research → messy discovery-order outline before writing. This prevents the #1 AI tell: presenting organized thinking instead of showing thinking in progress.

**12 structural rules**: quantitative targets for transition types, paragraph variation, evidence density, section asymmetry, counterargument embedding. Not guidelines — constraints.

**Model cost optimization**: Sonnet for research/pattern-matching, Opus for insight/writing, Haiku for validation. ~3x cheaper than all-Opus.
