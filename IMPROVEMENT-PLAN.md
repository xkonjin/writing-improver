# Jin Fernando Content Distribution System — Requirements Spec

_Updated Feb 9, 2026. Supersedes previous v3 improvement plan._

---

## Identity

- **Brand:** Jin Fernando (personal)
- **Positioning:** Independent analyst on stablecoins, AI, finance, culture, tech
- **Day job:** Marketing Lead @ Plasma (some guardrails — no competitor trashing, no non-public Plasma claims)
- **Website:** jin.contact → Next.js rebuild on Vercel → full media site (blog, prediction tracker, thesis archive, newsletter signup)

## Platforms (All Simultaneously)

| Platform                | Current State                  | Target                                |
| ----------------------- | ------------------------------ | ------------------------------------- |
| X (@xkonjin)            | 14.7K followers, active        | 50K+                                  |
| LinkedIn (xkonjin)      | Credential anchor, no articles | 10K+ with regular content             |
| Substack                | Doesn't exist yet              | Launch, build email list              |
| Telegram (Tickernomics) | Exists but dead                | Revive as article distribution + chat |
| jin.contact             | Outdated Framer portfolio      | Full media site (Next.js, Vercel)     |

## Time Budget: 2-3 hrs/week

- **Automation level:** Near-total. AI drafts everything. Jin edits for voice and publishes.
- **Pipeline:** Claude Code + this repo (writing-improver) is the only tool
- **Design:** All visuals AI-generated (extend diorama system → carousels, charts, diagrams)

## Content Model

- **Core output:** 1-2 thesis cards/week (400-800 words)
- **Repurposing:** Each thesis → X thread + LinkedIn post + Substack newsletter + Telegram post + isometric diorama image
- **Recurring:** Monthly prediction scorecard
- **Lead magnets:** Need to BUILD (nothing ready). Package thesis generation pipeline or Claude skills as giveaways
- **Video:** Not now. Clips from existing TickernomicsTV later.

## Revenue: None (brand building only)

- Free forever. Monetization = career capital, speaking, network, Telegram group credibility
- No paid Substack tier needed initially

## Technical Architecture

| Component          | Stack                    | Notes                                           |
| ------------------ | ------------------------ | ----------------------------------------------- |
| Content pipeline   | Python (this repo)       | Existing thesis gen + quality gates             |
| Image generation   | OpenRouter + Gemini      | Isometric diorama system (built)                |
| Carousel/chart gen | **New** — needs building | Programmatic LinkedIn carousels, data viz       |
| Website            | Next.js + Vercel         | jin.contact rebuild                             |
| Newsletter         | Substack                 | Free tier, cross-post from site                 |
| Scheduling         | TBD                      | Need automated posting to X, LinkedIn, Telegram |

## Funnel

```
X / LinkedIn / Substack Notes (discovery)
    → jin.contact articles (depth + SEO)
    → Substack email list (owned audience)
    → Telegram channel (community + thesis distribution)
    → Lead magnets (Claude skills, AI systems)
    → Private group (application-based, later)
```

## Key Constraints

- 2-3 hrs/week MAX human time
- Plasma guardrails on competitor/regulatory content
- Everything must flow from a single thesis card (one write, many outputs)
- Visual identity locked: isometric tilt-shift diorama (Wes Anderson style)
- Quality gates: existing structural + vocab + surprise scanners must pass

## What Needs Building

1. **Cross-platform repurposer** — Thesis card → X thread + LinkedIn post + Telegram caption + newsletter
2. **Carousel/diagram generator** — Programmatic LinkedIn carousels from thesis data
3. **jin.contact rebuild** — Next.js media site with blog, thesis archive, prediction tracker
4. **Substack setup** — Create publication, configure, first issue
5. **Scheduling/posting automation** — Auto-post or stage content across platforms
6. **Lead magnet packaging** — Clean up thesis gen system for public consumption
7. **Telegram integration** — Auto-post articles with captions to Tickernomics channel

## Existing Assets

- **6 thesis cards** written (content/02 through content/06)
- **Isometric diorama visual identity** locked in src/prompts/image_gen.py
- **Image generation agent** working (OpenRouter + Google SDK fallback)
- **Quality gate scanners** (structural, vocabulary, surprise, compression)
- **12 structural rules** for voice model
- **Content distribution research** (research/content-distribution-system.md)
- **LinkedIn algorithm research** (research/linkedin-algorithm-2026.md)
- **TickernomicsTV YouTube** interviews (existing video assets for future clips)

## Platform Research Summary

### X Algorithm (Key Numbers)

- Reply chains = 150x likes, bookmarks = 20x
- First 30 min critical for distribution
- Links INVISIBLE for non-Premium
- Premium = 10x reach efficiency
- Optimal: 3-5 tweets/day if <5K, threads 7-12 tweets

### LinkedIn Algorithm

- Dwell time 61+ sec = 15.6% engagement
- Expert comments 5-7x weight
- PDF carousels 6.60% engagement (highest)
- External links 25-60% reach penalty
- Best: Wed/Thu 10-11 AM

### Substack

- Notes drive 70% of new subscribers
- Internal traffic converts 4x higher
- Substack Network = 25% of paid subs
- Recommendation swaps = 1000+ new subs

### Publishing Order

1. Substack (Day 0, Tue/Fri) — SEO canonical
2. Substack Notes (Day 0) — discovery
3. X thread (Day 2-3) — discussion/virality
4. LinkedIn (Day 3-4) — professional reach
5. Telegram (Day 3-4) — community distribution

---

## Previous v3 Pipeline Improvements (Retained)

### Insight Engine (Built)

- Falsification agent (`src/agents/falsification.py`)
- Surprise detector (`src/quality/surprise_detector.py`)
- Compression scanner (`src/quality/compression_scanner.py`)

### Image Generation (Built)

- Content-type classification → style mapping → isometric diorama
- 7 content types: BULLISH, BEARISH, REGULATORY, CONTRARIAN, PARADOX, TECHNICAL, PARADIGM_SHIFT
- OpenRouter primary, Google SDK fallback

### Quality Gates (Built)

- Structural scanner (12 rules)
- Vocabulary scanner (banned words, AI tells)
- Surprise detector (Levine test, first principles, bidirectional, falsification)
- Compression scanner (lexical density, redundancy, filler)

### Still TODO from v3

- Predictions database + Brier score calculator + monthly scorecard generator
- Signal detection layer (automated topic discovery)
- Adversarial debate system (3-agent protocol)
