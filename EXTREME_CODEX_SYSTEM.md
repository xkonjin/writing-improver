# Extreme Codex Multi-Agent Swarm System

## Overview

Advanced multi-agent orchestration system that generates articles at "Settlers" quality level through parallel research, mechanism extraction, and iterative refinement.

## Architecture

```
┌─────────────────────────────────────────────────────┐
│              EXTREME CODEX SWARM                     │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Phase 1: Parallel Research (10 Specialist Agents)  │
│  ┌──────────┬──────────┬──────────┬──────────┐     │
│  │Threshold │ Paradox  │Timeline  │Mechanism │     │
│  │ Hunter   │Detective │Predictor │Archaeol. │     │
│  ├──────────┼──────────┼──────────┼──────────┤     │
│  │Visibility│Generation│ Network  │ Capital  │     │
│  │Calculator│   Gap    │ Physicist│  Flow    │     │
│  ├──────────┼──────────┼──────────┴──────────┤     │
│  │Neurosci. │Historical│                      │     │
│  │  Mapper  │  Rhymer  │                      │     │
│  └──────────┴──────────┴──────────────────────┘     │
│                        ↓                             │
│  Phase 2: Consolidation & Extraction                 │
│  ┌────────────────────────────────────────────┐     │
│  │ • Extract 15 mechanisms with thresholds    │     │
│  │ • Extract 8 inversions with numbers        │     │
│  │ • Extract 8 predictions with timeframes    │     │
│  │ • Build personal layer (8 elements)        │     │
│  └────────────────────────────────────────────┘     │
│                        ↓                             │
│  Phase 3: Parallel Draft Generation (5 Drafts)       │
│  ┌──────────┬──────────┬──────────┬──────────┐     │
│  │Mechanism │Inversion │Personal  │  Data    │     │
│  │  First   │   Led    │Embedded  │ Density  │     │
│  └──────────┴──────────┴──────────┴──────────┘     │
│                        ↓                             │
│  Phase 4: Quality Validation (Settlers Metrics)      │
│  ┌────────────────────────────────────────────┐     │
│  │ ✓ 7+ mechanisms with thresholds            │     │
│  │ ✓ 3+ inversions with numbers               │     │
│  │ ✓ 3+ falsifiable predictions               │     │
│  │ ✓ Personal confession/admission            │     │
│  │ ✓ 0 em-dashes, 0 AI transitions            │     │
│  │ ✓ Surprise score > 0.7                     │     │
│  │ ✓ Compression score > 7.0                  │     │
│  └────────────────────────────────────────────┘     │
│                        ↓                             │
│  Phase 5: Targeted Revision Loop (Max 5 rounds)      │
│  ┌────────────────────────────────────────────┐     │
│  │ • Mechanism Injector                       │     │
│  │ • Inversion Enhancer                       │     │
│  │ • Prediction Builder                       │     │
│  │ • Personal Authenticator                   │     │
│  │ • AI Tell Eliminator                       │     │
│  │ • Surprise Amplifier                       │     │
│  └────────────────────────────────────────────┘     │
│                        ↓                             │
│              Final Article (8.5+ score)              │
└─────────────────────────────────────────────────────┘
```

## Key Components

### 1. OpenRouter Swarm (`src/agents/openrouter_swarm.py`)

- Multi-model orchestration using 2026's best models
- Premium: Claude Opus 4.5, Kimi K2.5, GPT-5.2
- Fast: DeepSeek v3.2, Claude 3.5 Haiku, Mistral Large
- Specialized: Gemini 3 Pro, MiniMax M2.1, Devstral 2

### 2. Codex Orchestrator (`src/agents/openrouter_codex_orchestrator.py`)

- Autonomous multi-agent pipeline
- Parallel artifact building (mechanisms, inversions, predictions)
- Self-correction loops based on quality failures
- Settlers-quality validation gates

### 3. Extreme Codex Swarm (`src/agents/extreme_codex_swarm.py`)

- 10 specialist research agents with specific data-hunting roles
- Parallel draft generation with 5 different strategies
- Comprehensive quality metrics (Settlers + compression + surprise)
- Targeted revision system with up to 5 refinement rounds

### 4. Settlers Validator (`src/quality/settlers_validator.py`)

- Enforces 7+ mechanisms with thresholds and causal verbs
- Requires 3+ inversions with specific numbers
- Requires 3+ falsifiable predictions with timeframes
- Checks for personal layer (confession/admission + we/us/our)
- Zero tolerance for AI tells (em-dashes, transitions, narratives)

## Specialist Agent Roles

| Agent                   | Focus                                    | Extraction  |
| ----------------------- | ---------------------------------------- | ----------- |
| Threshold Hunter        | Find 7%, 147x, $43M per employee numbers | mechanisms  |
| Paradox Detective       | Find income vs holdings paradoxes        | inversions  |
| Timeline Predictor      | Make falsifiable predictions with dates  | predictions |
| Mechanism Archaeologist | Uncover causal chains, not correlations  | mechanisms  |
| Visibility Calculator   | Calculate exact visibility percentages   | mechanisms  |
| Generation Gap Analyst  | Find 18-year gaps between cohorts        | inversions  |
| Network Physicist       | Model as contagion physics, R0 values    | mechanisms  |
| Capital Flow Tracer     | Follow money with exact amounts          | mechanisms  |
| Neuroscience Mapper     | Brain regions, dopamine thresholds       | mechanisms  |
| Historical Rhymer       | Find exact historical parallels          | predictions |

## Quality Metrics

### Required Minimums

- **Mechanisms**: 7+ sentences with numeric thresholds and causal verbs
- **Inversions**: 3+ paradoxes with specific numbers
- **Predictions**: 3+ falsifiable with timeframes and quantities
- **Personal Layer**: Confession/admission + 5+ we/us/our instances
- **Surprise Score**: > 0.7
- **Compression Score**: > 7.0
- **Data Density**: 50+ specific numbers
- **Zero AI Tells**: No em-dashes, no transitions, no narrative markers

### Scoring Formula

```python
score = mechanisms/7 * 2.0 + inversions/3 * 1.5 + predictions/3 * 1.5
      + confession * 1.0 + surprise * 1.5 + compression/10 * 1.5
      + data_points/50 * 1.0 - banned_words * 0.2 - em_dashes * 0.5
```

## Usage

### Basic Run

```bash
export OPENROUTER_API_KEY="sk-or-v1-..."
export SWARM_TOPIC="Your topic here"
python run_extreme_codex.py
```

### Programmatic Usage

```python
from src.agents.extreme_codex_swarm import ExtremeCodexSwarm
from src.agents.openrouter_swarm import OpenRouterSwarm

swarm = OpenRouterSwarm(api_key="...")
extreme = ExtremeCodexSwarm(
    swarm=swarm,
    quality_target=8.5,
    parallel_drafts=5
)

result = await extreme.run(
    topic="AI agents as economic actors",
    num_research_agents=10
)
```

## Output Files

- `content/extreme_codex_TIMESTAMP_final.md` - Final article with metrics
- `content/extreme_codex_TIMESTAMP_research.json` - Research artifacts and history

## Success Criteria

Article passes when:

1. Overall quality score ≥ 8.5/10
2. Zero failures in Settlers validation
3. Contains specific mechanisms like "7% visibility threshold"
4. Has surprising inversions like "$111K income, $597 crypto holdings"
5. Makes falsifiable predictions with dates and quantities
6. Includes authentic personal layer without being a separate section
7. Zero AI tells (no em-dashes, transitions, or narrative language)

## Comparison to Original System

| Feature            | Original Swarm | Codex Orchestrator | Extreme Codex  |
| ------------------ | -------------- | ------------------ | -------------- |
| Research Agents    | 5-7 generic    | 7 with roles       | 10 specialists |
| Draft Strategies   | 1 synthesis    | 3 candidates       | 5 parallel     |
| Quality Validation | Basic          | Settlers metrics   | Comprehensive  |
| Revision Rounds    | 1 edit pass    | 3 max              | 5 targeted     |
| Target Quality     | Good enough    | 7.0+ score         | 8.5+ score     |
| Parallelization    | Sequential     | Some parallel      | Full parallel  |
| Personal Layer     | Optional       | Required           | 8 elements     |

## Performance

- **Time**: 2-5 minutes depending on revision rounds
- **Tokens**: 50K-150K depending on research depth
- **Success Rate**: ~80% achieve 8.5+ score within 5 rounds
- **Best Models**: Claude Opus 4.5 and Kimi K2.5 for premium tasks

## Known Issues

- API rate limits may cause delays with many parallel agents
- Some models may not support all specialized prompts
- Quality validation is strict - may require multiple rounds

## Future Enhancements

1. **Web Search Integration**: Live data for current events
2. **Citation System**: Track sources for all data points
3. **Style Transfer**: Match specific author voices
4. **Multi-Topic Pipeline**: Generate article series
5. **A/B Testing**: Compare different orchestration strategies
