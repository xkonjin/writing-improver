# Writing Improver — Project Instructions

## OpenRouter Multi-Agent Swarm

**Writing Improver API**: Configured via environment variable (see API_SETUP.md)

### Running Bottom-Up Article Generation

```bash
python run_bottom_up_swarm.py
```

**Process:**

1. **Research Swarm** (5-7 agents): Data Archaeologist, Mechanism Hunter, Pattern Breaker, Crowd Physicist, Neuroscience Detective, Historical Rhymer, Inversion Spotter
2. **Model Diversity**: Claude 3.5 Sonnet, GPT-4 Turbo, Mistral Large, DeepSeek, Llama 3.1 via OpenRouter
3. **Synthesis Competition**: Multiple synthesis approaches compete for best insight compression
4. **Voice Editing**: Multi-pass editing to eliminate AI tells and maximize genuine voice

**Key Files:**

- `src/agents/openrouter_swarm.py` - Main swarm orchestration
- `run_bottom_up_swarm.py` - Execution script
- `test_swarm.py` - API connectivity test

**Outputs:**

- `content/10-swarm-research.md` - Raw research from all agents
- `content/10-swarm-synthesis.md` - Synthesis competition output
- `content/10-coinbase-bottom-up-final.md` - Final article

**Success Metrics:**

- Generates specific mechanisms (7% visibility threshold, 18-year generational gap)
- No AI tells (em-dashes, transitions, narratives)
- Surprising inversions (income vs holdings paradox: $111K income, $597 crypto)
- Falsifiable predictions based on discovered mechanisms

## Anti-Patterns

- Mix LLM clients/models (`AsyncOpenAI` → `gpt-*` only)
- Empty catch blocks, no emojis in marketing content
- Generate articles without using the swarm (produces AI slop)
