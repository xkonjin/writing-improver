---
title: "feat: Content Distribution System"
type: feat
date: 2026-02-09
deepened: 2026-02-09
---

# Content Distribution System

## Enhancement Summary

**Deepened on:** 2026-02-09
**Agents used:** architecture-strategist, kieran-python-reviewer, security-sentinel, performance-oracle, code-simplicity-reviewer, pattern-recognition-specialist, agent-native-reviewer, best-practices-researcher (x2), framework-docs-researcher, product-thinking

### Critical Changes from Original Plan

1. **Drop `repurposer.py`** — contradicts extending `PublisherAgent`. Keep one agent, not two.
2. **Collapse 8 CLI commands → 4** (`distribute`, `status`, `edit`, `publish`). Auto-approve on validation pass.
3. **Simplify state machine from 6 states → 3** (`ready`, `scheduled`, `published`). No `staged`/`approved` distinction needed at 1-2 articles/week.
4. **Move `PlatformValidator` to `src/distribution/validator.py`** — it validates platform compliance, not article quality.
5. **Use `StrEnum` for `PublishStatus` and `Platform`** — type safety, exhaustive match.
6. **Use Pillow for carousel rendering, fpdf2 only for PDF packaging** — pixel-perfect slides need raster, not vector.
7. **Use raw `httpx` for Telegram** — not python-telegram-bot. Already a dependency.
8. **X API Basic tier is now $200/mo** (increased from $100). Free tier: 500 posts/mo, sufficient for threads.
9. **X API requires dual auth**: OAuth 2.0 PKCE for tweets, OAuth 1.0a for media upload.
10. **Add Python API layer** (`DistributionAPI`) for agent-native access. CLI wraps API, not the other way around.
11. **Use `zoneinfo` (stdlib)** — not pytz (deprecated).
12. **Engagement reminders: Telegram DM only for v1** — drop osascript/launchd complexity.

### Cuts from v1 (per simplicity review)

- `CarouselAgent` + `CarouselRenderer` — defer to v2. LinkedIn accepts image posts (6.60% engagement) without carousels.
- `ImageExporter` as separate module — inline 4 lines of Pillow in the publisher.
- `config/guardrails.yaml` — 11 strings, use a constant in `src/distribution/validator.py`.
- `Scheduler` module — at 1-2 articles/week, a `calculate_dates()` function is enough.
- Engagement reminders via osascript/launchd — phone alarm or Telegram DM.
- `cli calendar` command — `cli status` covers it.

---

## Overview

Build a content distribution system that takes thesis card articles and stages them for publishing across 5 platforms (Substack, Substack Notes, X, LinkedIn, Telegram) with correct timing, platform-specific formatting, and image variants.

**Key architectural decision:** v1 is a **staging + clipboard tool**, not a fully automated publisher. Substack has no public API, LinkedIn personal posting requires partner-level OAuth, and X API Free tier (500 posts/mo) is sufficient but media upload needs OAuth 1.0a. The system generates platform-ready content, validates it, and automates only Telegram (Bot API). Everything else: clipboard + browser open.

## Problem Statement

Jin has 6 thesis cards written, a working generation pipeline, quality gates, and image generation — but no way to get content from `output/` to audiences. Every publish is manual: copy-paste to each platform, resize images, write hooks, schedule timing. At 2-3 hrs/week, this is unsustainable for 5 platforms at 1-2 articles/week.

## Proposed Solution

Extend the existing pipeline with distribution capabilities:

```
Existing Pipeline              New Distribution System
┌──────────────┐              ┌──────────────────────────────────────────────┐
│ Research     │              │                                              │
│ Insight      │              │  ┌─────────────┐  ┌─────────────────────┐   │
│ Falsification│──article──►  │  │ Publisher    │──│ Platform Validator  │   │
│ DISORDER     │              │  │ (5 formats)  │  │ (char/link/guard)   │   │
│ Write        │              │  └─────────────┘  └─────────────────────┘   │
│ Quality Gate │              │         │                    │               │
│ Revision     │              │         ▼                    ▼               │
└──────────────┘              │  ┌─────────────┐  ┌─────────────────────┐   │
                              │  │ Image Crop   │  │ Distribution State  │   │
                              │  │ (Pillow,     │  │ (JSON, 3 states)    │   │
                              │  │  inline)     │  │                     │   │
                              │  └─────────────┘  └─────────────────────┘   │
                              │                            │                │
                              │                   ┌────────┴────────┐       │
                              │                   │  Publish Layer  │       │
                              │                   │  TG=auto, rest  │       │
                              │                   │  =clipboard+open│       │
                              │                   └─────────────────┘       │
                              └──────────────────────────────────────────────┘
```

## Technical Approach

### Architecture

#### New Files

| File                            | Purpose                                                                |
| ------------------------------- | ---------------------------------------------------------------------- |
| `src/distribution/__init__.py`  | Package init                                                           |
| `src/distribution/api.py`       | `DistributionAPI` — Python API layer (CLI wraps this)                  |
| `src/distribution/state.py`     | `DistributionState` + `PublishStatus` (StrEnum) + `Platform` (StrEnum) |
| `src/distribution/validator.py` | Per-platform validation + Plasma guardrail constants                   |
| `src/distribution/telegram.py`  | Telegram Bot API publisher (raw httpx)                                 |
| `src/distribution/clipboard.py` | Manual publish helper (pbcopy + browser open)                          |
| `src/prompts/distribution.py`   | System prompts for Substack Notes + Telegram                           |
| `config/distribution.yaml`      | Platform configs, timing offsets, image sizes                          |

#### Modified Files

| File                             | Changes                                                                    |
| -------------------------------- | -------------------------------------------------------------------------- |
| `src/agents/publisher.py`        | Add `format_substack_notes()`, `format_telegram()`, run all 5 in parallel  |
| `src/prompts/platform_format.py` | Update X (add numbering) and LinkedIn (add 3-5 hashtags) per 2026 research |
| `src/orchestrator.py`            | Add `run_distribute()` phase after `run_publish()`                         |
| `src/storage/content_store.py`   | Add distribution state persistence                                         |
| `src/cli.py`                     | Add `dist` Click group with 4 commands                                     |
| `pyproject.toml`                 | Add `Pillow` dependency                                                    |

#### Research Insights: File Architecture

> **Architecture strategist:** `src/distribution/` package is justified — distribution is a bounded context separate from quality scanning. But keep it flat (no sub-packages).
>
> **Pattern recognition:** The codebase uses flat `src/quality/` with `*_scanner.py` naming. New package should follow: `src/distribution/validator.py` (not `platform_validator.py`), `src/distribution/state.py`, etc.
>
> **Agent-native reviewer:** Without a Python API layer, the 4 CLI commands are the only entry point — no agent can call them programmatically. `DistributionAPI` in `src/distribution/api.py` fixes this. CLI becomes a thin wrapper. All methods return typed dataclasses, not Rich tables.

### Implementation Phases

#### Phase 1: Publisher Extensions + Validator (Foundation)

Extend the content formatting pipeline to cover all 5 platforms with validation.

**Tasks:**

- [ ] Add `format_substack_notes()` to `PublisherAgent` — `src/agents/publisher.py`
  - Short-form hook (280 chars) + key insight + link placeholder
- [ ] Add `format_telegram()` to `PublisherAgent` — `src/agents/publisher.py`
  - HTML parse_mode (not MarkdownV2 — Telegram MarkdownV2 is notoriously painful)
  - Caption: 2-3 sentence hook + link + organic CTA
  - 1,024 char limit when sending with photo (sendPhoto), 4,096 for text-only (sendMessage)
- [ ] Add `SUBSTACK_NOTES_SYSTEM` and `TELEGRAM_SYSTEM` prompts — `src/prompts/distribution.py`
- [ ] Update `PublisherResult` dataclass to include `substack_notes` and `telegram` fields
- [ ] Update `PublisherAgent.format_all()` to run all 5 formats via single `asyncio.gather`
- [ ] Update `run_publish()` in orchestrator to include new formats
- [ ] Update `X_THREAD_SYSTEM` prompt: add tweet numbering per 2026 research (1/N format)
- [ ] Update `LINKEDIN_SYSTEM` prompt: add 3-5 hashtags at end per 2026 research
- [ ] Build `PlatformValidator` — `src/distribution/validator.py`
  - X: per-tweet 280-char check, thread length 5-8 tweets, link in final tweet only
  - LinkedIn: 1,300-char check, no external links in body (flag if found), hook first 140 chars
  - Substack Notes: 280-char hook check
  - Telegram sendPhoto: 1,024-char caption check
  - Telegram sendMessage: 4,096-char check
  - Newsletter: subject line 40-55 chars
- [ ] Add Plasma guardrail scanner as constants in `src/distribution/validator.py`
  - `COMPETITOR_KEYWORDS`: `["Circle", "Stripe stablecoins", "PayPal stablecoins", "Paxos", "Ripple", "Stellar"]`
  - `BLOCKED_PATTERNS`: `["Plasma is better than", "unlike {competitor}", "internal data shows", "we're building"]`
  - Scan ALL outputs for competitor mentions + negative sentiment
  - Return warnings (not blocks) — human makes final call
- [ ] Tests — `tests/test_agents/test_publisher.py`, `tests/test_distribution/test_validator.py`

**Research Insights:**

> **Kieran Python reviewer:** `PlatformValidator` should be module-level functions, not a class. `validate_x_thread(content: str) -> list[str]` returning a list of error strings. No state needed.
>
> **Security sentinel:** Guardrail scanner using keyword-only matching is trivially bypassable ("C1rcle"). Acceptable for v1 — this is a human-review flag, not a security boundary.
>
> **Framework docs researcher:** Telegram `sendPhoto` caption limit is 1,024 chars (not 4,096). Use `sendMessage` + inline keyboard with image URL for longer captions. HTML parse_mode is strongly preferred over MarkdownV2.

**Acceptance criteria:**

- [ ] `PublisherAgent.format_all()` returns 5 platform outputs
- [ ] `PlatformValidator` catches over-length tweets, LinkedIn link violations
- [ ] Guardrail scanner flags competitor mentions
- [ ] All tests pass

#### Phase 2: Distribution State + CLI + API Layer

Add state tracking, Python API, and CLI commands for the human-in-the-loop workflow.

**Tasks:**

- [ ] Design distribution state model — `src/distribution/state.py`

  ```python
  from enum import StrEnum

  class Platform(StrEnum):
      SUBSTACK = "substack"
      SUBSTACK_NOTES = "substack_notes"
      X = "x"
      LINKEDIN = "linkedin"
      TELEGRAM = "telegram"

  class PublishStatus(StrEnum):
      READY = "ready"        # validated, content approved
      SCHEDULED = "scheduled" # date assigned
      PUBLISHED = "published" # live on platform

  @dataclass
  class PlatformStatus:
      status: PublishStatus
      content: str
      scheduled_at: datetime | None
      published_at: datetime | None
      published_url: str | None
      validation_warnings: list[str]

  @dataclass
  class DistributionState:
      run_id: str
      article_path: str
      platforms: dict[Platform, PlatformStatus]
      created_at: datetime
  ```

- [ ] Build `DistributionAPI` — `src/distribution/api.py`
  - `distribute(article_path: str) -> DistributionState` — format + validate + save state
  - `get_status(run_id: str) -> DistributionState` — load state
  - `edit_content(run_id: str, platform: Platform, content: str) -> list[str]` — update + revalidate
  - `publish(run_id: str, platform: Platform | None) -> dict[Platform, str]` — publish one or all
  - All methods return typed dataclasses (agent-readable)
  - Add `--json` output option for machine consumption

- [ ] Extend `ContentStore` with distribution state persistence — `src/storage/content_store.py`
  - Atomic JSON writes: write to tmp file, then `os.replace()` (atomic on POSIX)
  - `save_distribution(state: DistributionState) -> None`
  - `load_distribution(run_id: str) -> DistributionState`
  - `update_platform(run_id: str, platform: Platform, status: PlatformStatus) -> None`

- [ ] CLI: Add `dist` Click group — `src/cli.py`
  - `cli dist run <file>` — repurpose article → validate → save state (auto-marks as READY if all pass)
  - `cli dist status [run_id]` — Rich table showing per-platform state + schedule
  - `cli dist edit <run_id> --platform <name>` — open in `$EDITOR`, revalidate on save
  - `cli dist publish <run_id> [--platform <name>]` — publish to Telegram (auto) or clipboard+open (manual)

- [ ] Tests — `tests/test_distribution/test_state.py`, `tests/test_distribution/test_api.py`

**Research Insights:**

> **Product thinking:** Auto-approve on validation pass eliminates a manual step. If all 5 platforms pass validation, mark as READY immediately. Only require explicit approval if there are warnings (guardrail flags, near-limit content).
>
> **Code simplicity reviewer:** 6 states (`pending`→`staged`→`approved`→`scheduled`→`published`→`failed`) is overkill for 1-2 articles/week. 3 states: `ready` (validated), `scheduled` (date set), `published` (live). Failed publishes just stay in prior state with an error message.
>
> **Performance oracle:** JSON state I/O < 1ms. Atomic write with `os.replace()` prevents corruption from interrupted writes. No need for SQLite.
>
> **Agent-native reviewer:** Every CLI command must have a Python API equivalent. The API returns dataclasses; the CLI wraps them with Rich formatting. This lets agents call `DistributionAPI.distribute()` directly without shell parsing.

**Acceptance criteria:**

- [ ] `DistributionAPI.distribute("content/06-*.md")` returns state with 5 platforms at READY
- [ ] `cli dist status` shows Rich table with per-platform status
- [ ] `cli dist edit` opens editor and revalidates on save
- [ ] State persists across CLI invocations (atomic JSON)

#### Phase 3: Image Crops + Publishing Layer

Generate platform-specific image variants and connect Telegram Bot API.

**Tasks:**

- [ ] Add image cropping to publisher flow (inline, not a separate module)
  - Input: master image (1200x800 from ImageGenAgent)
  - Crops using `Pillow` `ImageOps.fit()` with `Image.Resampling.LANCZOS`:
    - `x_header.png` — 1600x900 (upscale + crop — apply mild `ImageFilter.SHARPEN` after)
    - `linkedin_single.png` — 1200x628 (center crop)
    - `substack_og.png` — 1200x800 (copy master)
  - Save alongside distribution state artifacts

- [ ] Build `TelegramPublisher` — `src/distribution/telegram.py`
  - Raw `httpx.AsyncClient` (not python-telegram-bot)
  - `sendPhoto` with caption (HTML parse_mode) + inline keyboard for "Read full analysis" link
  - Credentials: `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHANNEL_ID` from env
  - Return message URL on success

- [ ] Build clipboard helper — `src/distribution/clipboard.py`
  - `copy_to_clipboard(content: str)` — `subprocess.run(["pbcopy"], input=content.encode())`
  - `open_url(url: str)` — `subprocess.run(["open", url])`
  - Platform URLs: `https://substack.com/home`, `https://linkedin.com/feed/`, etc.
  - **Never use `shell=True`** in subprocess calls

- [ ] Add `alt_text` generation to `ImageGenAgent` — LLM describes the diorama scene in 200-250 chars
- [ ] Add `Pillow` to `pyproject.toml` dependencies
- [ ] Tests (mocked API calls) — `tests/test_distribution/test_telegram.py`, `tests/test_distribution/test_clipboard.py`

**Research Insights:**

> **Best practices researcher (Pillow):** `ImageOps.fit(img, (1600, 900), method=Image.Resampling.LANCZOS)` handles resize+crop in one call. For the 1200→1600 upscale, apply `img.filter(ImageFilter.SHARPEN)` once after to compensate. Center crop is default — no need for smartcrop.py at this scale.
>
> **Framework docs researcher (Telegram):** Use `sendPhoto` with `parse_mode=HTML` for formatting. Caption limit is 1,024 chars. For longer text, use `sendMessage` with photo URL in an inline keyboard button. Bot token format: `123456789:ABCdefGhIjKlMnOpQrStUvWxYz`.
>
> **Security sentinel:** CRITICAL — `.env` is not in `.gitignore`. Add immediately. Never log API tokens. Use `httpx` directly (not `shell=True` with curl). Validate `TELEGRAM_CHANNEL_ID` format before sending.
>
> **Framework docs researcher (X API):** Free tier = 500 posts/mo (sufficient). BUT media upload requires OAuth 1.0a while tweet creation uses OAuth 2.0 PKCE. Two separate auth flows. For v1, X goes through clipboard — defer API integration to v2.

**Acceptance criteria:**

- [ ] Image crops produce correct dimensions (verify with `PIL.Image.open().size`)
- [ ] `TelegramPublisher` sends photo+caption to channel (mock test)
- [ ] Clipboard helper copies content and opens correct URL
- [ ] `cli dist publish <run_id> --platform telegram` sends to channel
- [ ] `cli dist publish <run_id> --platform linkedin` copies to clipboard + opens LinkedIn

#### Phase 4: Scheduling + Config + Integration

Wire everything together with timing calculations and config.

**Tasks:**

- [ ] Add `calculate_dates()` function to `src/distribution/api.py`
  - Input: Day 0 date + platform offsets from `config/distribution.yaml`
  - Skip weekends: if calculated date falls on Sat/Sun, push to Monday
  - Use `zoneinfo.ZoneInfo` (stdlib, not pytz)
  - Return `dict[Platform, datetime]`
  - Support `--reactive` mode: reversed order (X first for breaking news)

- [ ] Create `config/distribution.yaml` (see Config Schemas below)
- [ ] Update `PipelineOrchestrator.run_full()` to optionally chain into distribution
  - Add `--distribute` flag to `cli run` that triggers repurpose + stage after article generation
- [ ] Add scheduling to CLI: `cli dist run <file> --day0 <date>` sets schedule
  - Default `--day0`: next Tuesday (most common publish day)
  - `cli dist status` shows scheduled dates in table
- [ ] Engagement reminders: Telegram DM to Jin when platform goes live
  - Use same `TelegramPublisher` with Jin's personal chat ID
  - Message: "Your {platform} post on {topic} is live. Engage now. {link}"
  - Triggered manually: `cli dist publish` sends reminder after successful publish
- [ ] Add `.gitignore` with `.env`, `__pycache__/`, `*.pyc`, `output/` entries
- [ ] End-to-end integration test: article → distribute → validate → schedule → publish (Telegram)
- [ ] Ruff + mypy clean

**Research Insights:**

> **Performance oracle:** All 5 LLM formatting calls should run in a single `asyncio.gather()`. Total latency: ~5-10s (dominated by LLM calls). Image crops: < 100ms. JSON state: < 1ms.
>
> **Product thinking:** Make `--day0` optional with smart default (next Tuesday or Friday based on which is closer). `distribute` should be idempotent — running it twice on the same article updates content but preserves schedule.
>
> **Code simplicity reviewer:** A `calculate_dates()` function is ~15 lines. No need for a `Scheduler` class or separate module.

**Acceptance criteria:**

- [ ] `cli run "topic" --distribute` runs full pipeline + stages all platforms
- [ ] `cli dist run content/06-*.md` works standalone
- [ ] `cli dist run content/06-*.md --day0 2026-02-11` sets correct dates (skipping weekends)
- [ ] Full integration test passes
- [ ] `.gitignore` exists and covers `.env`
- [ ] Zero ruff/mypy errors

---

## v2 Features (Deferred)

These were in the original plan but cut from v1 per simplicity review:

| Feature                     | Why Deferred                                                                                       | Trigger to Build                           |
| --------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| LinkedIn carousel PDF       | Pillow rendering + fpdf2 packaging is complex. Image posts get 6.60% engagement without carousels. | If LinkedIn becomes primary growth channel |
| X API integration           | $200/mo Basic tier. Free tier's 500/mo works but needs dual OAuth (PKCE + 1.0a for media).         | If clipboard workflow becomes bottleneck   |
| `Scheduler` as cron/launchd | At 1-2/week, manual trigger is fine.                                                               | If frequency increases to daily            |
| Engagement reminder system  | Phone alarm works. Telegram DM covers it for v1.                                                   | If engagement metrics show missed windows  |
| `config/guardrails.yaml`    | 11 strings as constants is simpler than YAML + loader.                                             | If guardrails become complex/user-editable |

---

## Alternative Approaches Considered

| Approach                    | Why Rejected                                                                     |
| --------------------------- | -------------------------------------------------------------------------------- |
| **Buffer/Hootsuite API**    | External dependency + $15-99/mo. Day-offset function is sufficient for 1-2/week. |
| **Substack unofficial API** | Fragile, breaks on any update. Clipboard helper is reliable.                     |
| **Full LinkedIn API**       | Requires partner-level OAuth. Clipboard + browser open is faster for 1-2/week.   |
| **Puppeteer/Playwright**    | Brittle, requires browser session. Clipboard is simpler.                         |
| **React-pdf for carousels** | Requires Node.js. Project is Python. (Deferred to v2 with Pillow+fpdf2 anyway.)  |
| **python-telegram-bot**     | Heavy dependency. Raw httpx is already available and sufficient.                 |
| **pytz for timezones**      | Deprecated. Use `zoneinfo` (stdlib since Python 3.9).                            |
| **SQLite for state**        | Overkill. JSON with atomic write handles 1-2 articles/week.                      |
| **Separate repurposer.py**  | Contradicts extending PublisherAgent. One agent, not two.                        |

## Acceptance Criteria

### Functional Requirements

- [ ] Single article → 5 platform-formatted outputs (newsletter, notes, X thread, LinkedIn, Telegram)
- [ ] Per-platform validation catches: over-length tweets, LinkedIn link violations, Telegram caption length
- [ ] Plasma guardrail scanner flags competitor mentions across all outputs
- [ ] Multi-size image crops: 3 variants from master diorama (Pillow)
- [ ] Distribution state tracks per-platform status (3 states: ready, scheduled, published)
- [ ] CLI workflow: `dist run` → `dist status` → `dist edit` → `dist publish`
- [ ] Telegram auto-publishes via Bot API
- [ ] All other platforms: clipboard + browser open
- [ ] `--reactive` flag reverses publishing order for breaking news
- [ ] Python API layer (`DistributionAPI`) exposes all operations programmatically

### Non-Functional Requirements

- [ ] All new agents follow existing pattern: compose `BaseAgent`, `@dataclass` result, async, usage tracking
- [ ] All prompts in `src/prompts/`, all config in `config/`
- [ ] Platform API calls use `httpx` (already a dependency)
- [ ] State persistence: atomic JSON write with `os.replace()`
- [ ] Type safety: `StrEnum` for status and platform, `datetime` for timestamps, `zoneinfo` for TZ
- [ ] All new code passes ruff + mypy
- [ ] Test coverage for all new modules
- [ ] `.gitignore` covers `.env`, `__pycache__/`, `output/`

### Security Requirements

- [ ] `.env` in `.gitignore` (CRITICAL — currently missing)
- [ ] Never log API tokens (Telegram, X)
- [ ] Never use `shell=True` in subprocess calls
- [ ] Validate `TELEGRAM_CHANNEL_ID` format before API calls
- [ ] No command injection vectors in clipboard/browser helpers

### Quality Gates

- [ ] Existing thesis card quality gates still pass (no regression)
- [ ] Platform validator catches 100% of over-length content
- [ ] CI passes: ruff, mypy, pytest

## Dependencies & Risks

| Risk                               | Mitigation                                                                |
| ---------------------------------- | ------------------------------------------------------------------------- |
| Substack changes web UI            | Clipboard copies markdown. Content is paste-ready regardless of UI.       |
| Telegram bot token expires         | Clear error + regeneration instructions. Channel ID is stable.            |
| 1200→1600 upscale quality          | LANCZOS resampling + mild sharpen. Or: generate master at 1600x900 in v2. |
| X API pricing increases further    | X publisher deferred to v2. Clipboard fallback is permanent.              |
| Pillow version breaks ImageOps.fit | Pin Pillow version in pyproject.toml.                                     |

## Config Schemas

### `config/distribution.yaml`

```yaml
publishing_order:
  substack:
    day_offset: 0
    optimal_time: "10:00"
    timezone: "US/Eastern"
  substack_notes:
    day_offset: 0
    optimal_time: "10:30"
    timezone: "US/Eastern"
  x:
    day_offset: 2
    optimal_time: "09:00"
    timezone: "US/Eastern"
  linkedin:
    day_offset: 3
    optimal_time: "10:00"
    timezone: "US/Eastern"
  telegram:
    day_offset: 3
    optimal_time: "16:00"
    timezone: "US/Eastern"

image_sizes:
  master: { width: 1200, height: 800 }
  x_header: { width: 1600, height: 900 }
  linkedin_single: { width: 1200, height: 628 }
  substack_og: { width: 1200, height: 800 }

platform_limits:
  x_tweet: 280
  x_thread_min: 5
  x_thread_max: 8
  linkedin_post: 1300
  linkedin_hook: 140
  substack_notes: 280
  telegram_photo_caption: 1024
  telegram_message: 4096
  newsletter_subject: 55

reactive_order: ["x", "telegram", "linkedin", "substack_notes", "substack"]
```

## References

### Internal

- Existing publisher agent: `src/agents/publisher.py:21`
- Platform format prompts: `src/prompts/platform_format.py:1-58`
- Orchestrator pipeline: `src/orchestrator.py:276-345`
- Image generation: `src/agents/image_gen.py:31`
- Content store: `src/storage/content_store.py:11`
- CLI structure: `src/cli.py:18-241`
- Agent base pattern: `src/agents/base.py:27-49`
- Quality thresholds: `config/quality_thresholds.yaml`

### Research

- Content distribution system: `research/content-distribution-system.md`
- X algorithm deep dive: `research/x-twitter-algorithm-deep-dive.md`
- LinkedIn algorithm 2026: `research/linkedin-algorithm-2026.md`
- Visual identity: `research/visual-identity-system.md`
- Requirements spec: `IMPROVEMENT-PLAN.md`

### External (from deepening research)

- Telegram Bot API sendPhoto: https://core.telegram.org/bots/api#sendphoto
- X API v2 tweet creation: https://developer.x.com/en/docs/x-api/tweets/manage-tweets
- Pillow ImageOps.fit: https://pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit
- fpdf2 (v2 carousel): https://py-pdf.github.io/fpdf2/
- zoneinfo (stdlib): https://docs.python.org/3/library/zoneinfo.html
