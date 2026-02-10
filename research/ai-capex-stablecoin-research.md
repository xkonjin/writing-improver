# AI Capex and Stablecoin Second-Order Effects — Raw Research Data

## Track 1: AI Capital Expenditure Specifics

### Total Capex by Company (2025-2026 Announced/Planned)

- **Stargate (OpenAI/Oracle/SoftBank):** $400B+ over 3 years, 7GW planned capacity, 450,000 GB200 GPUs at Abilene TX flagship
  - Abilene campus: 1.2GW, operational Sep 2025 (first 2 buildings), remaining 6 by mid-2026
  - 5 additional sites announced Sep 2025
- **Amazon:** $30B+ in new US data center investments
  - Project Rainier (Indiana): $11B, 30 buildings, 2.2GW, 7 buildings online
  - Pennsylvania: $20B "AI innovation campuses"
  - North Carolina: $10B expansion (total >$22B since 2010)
  - Mississippi: $3B (Warren County) + $10B (Madison County)
  - 241 known locations, 83 under construction
- **Meta:** "hundreds of billions" for superintelligence compute
  - Prometheus (New Albany, OH): World's first 1GW data center, online 2026
  - Nuclear deals: TerraPower, Oklo, Vistra
  - Multiple multi-GW clusters planned
- **Apple:** $500B US investment over 4 years
  - Houston server manufacturing (250K sq ft, shipping Oct 2025)
  - Data center expansion: NC, Iowa, Oregon, Arizona, Nevada
  - Project ACDC: custom AI servers for Apple Intelligence
- **xAI (Musk):** Colossus in Memphis
  - 200,000 GPUs operational (doubled from 100K)
  - 150MW → 300MW Phase 2
  - Targeting 1 million GPUs
  - Built in 122 days

### GPU Supply Chain

- **Nvidia Blackwell GB200:** 150-200K units Q4 2024, 750-800K Q1 2025, 1.5-2M full year 2025
  - B200 TDP: 1,200W (vs H100 700W = 71% increase)
  - Blackwell Ultra: 1,400W TDP
  - GB200 NVL72 rack: ~140kW
- **Google TPUs:** 2.5M units shipped 2025 (v5 = 1.9M, v6 = 600K)
  - Anthropic deal: up to 1M TPUs, ≥1GW capacity
- **HBM Memory:** SK Hynix sold out through 2026, overtook Samsung in annual profit first time (47.2T won vs 43.6T)
  - HBM3E prices hiked 20% for 2026
  - Global HBM market: projected $43B by 2027
- **US data center construction:** $31.5B in 2024

---

## Track 2: Tether AI Investments

### Northern Data AG (~$2B total exposure)

- €1.1B total exposure (reached Jan 2024)
- $610M unsecured debt financing (matures 2030)
- Three business units:
  - **Taiga Cloud:** 22,400+ GPUs (20,480 H100s + 2,048 H200s), €120-150M revenue 2024
  - **Ardent Data Centers:** ~250MW across 8 data centers by 2027, Maysville GA 180MW
  - **Peak Mining:** SOLD for $200M to companies controlled by Devasini and Ardoino (related-party transaction)
- Northern Data Group: €200-240M revenue 2024 (~3x 2023)

### Rumble ($925M total)

- $775M equity investment (Dec 2024)
- $150M GPU services commitment (2-year)
- $100M advertising agreement ($50M/year 2026-2027)
- Rumble acquiring Northern Data for ~$767M (Tether owns 54% of Northern Data, becomes largest Rumble shareholder)

### QVAC Project

- **Genesis I (Oct 2025):** 41B tokens synthetic STEM dataset
- **Genesis II (Dec 2025):** 107B new tokens (148B total across 19 domains)
- **QVAC Fabric:** World's first edge-first LLM inference runtime
  - Runs on: iOS, Android, Windows, macOS, Linux
  - Hardware: NVIDIA, AMD, Intel, Apple Silicon, Qualcomm, ARM Mali
  - First framework enabling LLM training on smartphone-class hardware
  - License: Apache 2.0
- **Wallet Integration:** QVAC connects to WDK for Bitcoin/USDT payments

### WDK (Wallet Development Kit)

- Open-source, self-custodial, multi-chain wallet toolkit
- Chains: Bitcoin, Lightning, Ethereum, Arbitrum, Polygon, TON, Solana
- Free at wallet.tether.io
- AI agent use case: Ardoino demonstrated agents autonomously sending Bitcoin without human intervention
- Quote: "Every single AI agent will have a wallet" within 15 years, "one trillion agents"

### Tether Financial Profile

- **2024 profits:** $13B
- **T-bill holdings:** $113B+ (Dec 2024)
- **Tether Investments (proprietary arm):** $12.5B in assets, deployed $13.7B across 120+ companies
- **AI-specific:** ~$4B deployed
- **Bitcoin mining:** $2B+ across 15 sites, 3 countries

### Economics: Bitcoin Mining vs AI Compute

- AI generates **25x higher revenue per MW** than Bitcoin mining
- 10 MW of H100 GPUs ≈ revenue of 100 MW of Bitcoin mining
- AI annualized revenue: ~$9.11M per MW at 80% utilization
- Bitcoin miner valuation: ~$4.5M/MW vs $30M+/MW for AI data centers
- Conversion cost: $5-11M per MW

---

## Track 3: Energy & Infrastructure Economics

### Power Consumption Trajectory

- H100: 700W → B200: 1,200W → Blackwell Ultra: 1,400W
- GB200 Superchip: 2,700W total (2x B200 + Grace CPU)
- GB200 NVL72 rack: ~140kW
- Liquid cooling now mandatory for Blackwell and beyond

### Major Data Center Power

- Stargate Abilene: 1.2GW (expandable), total program ~7GW
- Amazon Project Rainier: 2.2GW
- Meta Prometheus: 1GW (world's first)
- xAI Colossus Phase 2: 300MW
- Northern Data Maysville: 180MW

### Energy Sourcing

- Meta: Nuclear deals (TerraPower, Oklo, Vistra)
- Meta Prometheus: Gas turbines + behind-the-meter generation
- Apple NC: Renewable (82% solar, 12% wind, biogas fuel cells)
- Michigan: Tax exemptions for data centers through 2050
- Water cooling: up to 5M gallons/day per facility

---

## Track 4: AI Agent Payments & Stablecoins

### Stablecoin Market (2025)

- **Total volume:** $33T in 2025 (up 72% YoY)
- **USDC:** $18.3T transaction volume (leads by flow)
- **USDT:** $13.3T transaction volume
- **USDT market cap:** $187B (leads by holdings, 3x Circle)
- **Q4 2025 alone:** $11T
- **Projection:** $56T by 2030 (Bloomberg Intelligence)

### Key Anomaly: USDC Leads Volume, USDT Leads Market Cap

- USDC = transaction currency (high velocity, enterprise, regulated)
- USDT = deposit currency (held, developing markets, 51% on Tron)
- Different use cases, different dominant stablecoin

### x402 Protocol (Coinbase + Cloudflare)

- Revives HTTP 402 "Payment Required" status code
- 200ms stablecoin confirmation on Base (vs 2-3 day ACH)
- Coinbase + Cloudflare launching x402 Foundation
- First tool letting LLMs (Claude, Gemini, Codex) access a wallet

### Coinbase AgentKit + Payments MCP

- Toolkit for giving AI agents crypto wallets
- Fee-free stablecoin payments on Base
- Agents can: create wallets, execute payments, interact onchain
- Compliance controls and spending limits built in
- Use cases: pay for cloud services, API access, digital content automatically

### Real AI-to-AI Payments (Already Happening)

- **Fetch.ai (Dec 2025):** First AI-to-AI payment — Personal AIs coordinated dinner reservation + payment while users offline. Used Visa, USDC, FET token. LIVE production.
- **USD.AI:** Stablecoin-backed GPU loans. 7-day approval (vs 60-90 bank). 8% APR. Collateral = physical GPUs. $13M raised Aug 2025.
- **Google Cloud AP2 Protocol (Sep 2025):** Agent Payments Protocol for autonomous B2B procurement. Enterprise pilot.

### Solana AI Agent Ecosystem

- 77% of x402 transaction volume (Dec 2025)
- $0.00025/transaction (20x cheaper than Base)
- Sub-second finality
- Breakpoint 2025: demos of autonomous trading, liquidity, portfolio agents

### Tether's AI Agent Play

- WDK = wallet for AI agents
- QVAC Fabric = edge runtime
- Combined: AI agent on smartphone → processes locally → pays with USDT → no cloud needed
- Target: 534.5M existing USDT users, mostly developing markets

---

## Track 5: Supplementary Data (Late-Arriving Research)

### Hyperscaler Capex Totals (2025-2026)

- **Combined Big 4 (Microsoft/Google/Amazon/Meta):** >$600B planned for 2026 (36% increase over 2025)
- **Microsoft:** $80B+ in FY2025 alone
- **Google:** $185B cumulative plan through 2028
- **Amazon:** $200B through 2028 (data center focused)
- **Meta:** $600B cumulative by 2028
- **Apple:** $500B US investment over 4 years
- **Hyperscaler debt issuance:** $108B in 2025, $1.5T expected total
- **Capex as % of operating cash flow:** 94% for CoreWeave

### CoreWeave (GPU Cloud)

- $23B valuation (May 2025 IPO)
- $55.6B contracted backlog
- $14B in debt
- Capex at 94% of operating cash flow
- Largest non-hyperscaler GPU cloud provider

### Grid Constraints

- $64B in data center projects blocked or delayed in 2024 due to power availability
- Nuclear deals accelerating: Microsoft/Three Mile Island 835MW, Amazon/Talen $18B/1,920MW, Google/Kairos 500MW
- Water consumption: up to 5M gallons/day per facility

### AI Agent Payment Market Sizing

- AI agent market: $7.84B (2025) → $52.62B by 2030
- x402 protocol: 100M+ payment flows processed, 35M+ Solana transactions
- Solana captures 77% of x402 transaction volume (Dec 2025)

### Funded AI Agent Payment Startups

- Sapiom: $15M seed — AI agent payment rails
- Natural: $9.8M — autonomous agent commerce
- Lava: $5.8M — agent-native financial infrastructure
- Paid.ai: €10M — European AI agent payments
- Stripe Tempo: Internal stablecoin project (reported)
- Mastercard, Visa, PayPal all launched AI agent payment solutions in 2025

---

## Sources

### AI Capex

- NVIDIA Blackwell shipment estimates: Morgan Stanley, Ming-Chi Kuo, TweakTown
- Amazon Project Rainier: CNBC, Data Center Frontier
- Stargate: OpenAI blog, DCD, CNBC
- Meta Prometheus: NBC4 WCMH, DCD, Data Center Frontier
- xAI Colossus: HPCwire, Tom's Hardware, ServeTheHome
- Apple: Apple Newsroom, Tom's Hardware, CIO Dive
- Google TPU: SemiAnalysis, Global Semi Research
- SK Hynix: CNBC, TrendForce, NotebookCheck
- US data center construction: ConstructionOwners.com

### Tether AI

- Northern Data: Tether.io, CoinTelegraph, Amy Castor, Data Center Dynamics
- QVAC: Tether.io, CryptoBriefing
- Rumble: Rumble Corp blog, Yellow.com
- WDK: TheBlock, Tether.io
- Tether financials: Tether.io attestation, CoinDesk

### AI Agent Payments

- Stablecoin volumes: Bloomberg, Artemis Analytics, Yahoo Finance
- x402: Coinbase blog
- Fetch.ai: Fetch.ai blog
- USD.AI: CoinDesk
- Solana agents: Alchemy, Crossmint, BingX
- Coinbase AgentKit: Coinbase blog, GitHub
