# Stablecoin Payment Infrastructure Deep Dive — February 2026

**Research compiled:** February 9, 2026
**Target audience:** Stablecoin/payments infrastructure professionals
**Scope:** Complete competitive landscape, regulatory environment, geographic adoption, infrastructure buildout

---

## 1. Payment Infrastructure Companies — The Full Map

### Stripe/Bridge

**Acquisition:** October 2024 announcement, $1.1 billion, closed February 2025 — Stripe's largest acquisition to date

**What they do:** Bridge provides stablecoin payment infrastructure enabling businesses to accept stablecoin payments without directly handling digital tokens. Initially focused on cross-border payments, evolved to government aid disbursement across Latin America and Virtual Accounts for global USD holdings.

**Post-acquisition products (2025):**

- **Open Issuance:** Platform enabling businesses to launch custom stablecoins in days
- **Visa card integration:** First global card issuing product making stablecoin balances spendable as fiat. Ramp, Squads, Airtm issuing Visa cards linked to stablecoin wallets in dozens of countries
- **Payouts:** Partnership with Remote.com processing payouts via stablecoin infrastructure in 70+ countries

**Strategic rationale:** Stablecoins enable cheaper transactions in certain corridors, reduce transaction failures, improve conversion rates in countries with underdeveloped payment infrastructure

**Volume:** Not publicly disclosed

**Sources:** [Stripe newsroom](https://stripe.com/newsroom/news/stripe-completes-bridge-acquisition), [CNBC](https://www.cnbc.com/2025/02/04/stripe-closes-1point1-billion-bridge-deal-prepares-for-stablecoin-push-.html), [a16z analysis](https://a16z.com/newsletter/what-stripes-acquisition-of-bridge-means-for-fintech-and-stablecoins-april-2025-fintech-newsletter/)

---

### Circle (USDC)

**Market cap:** $75.7 billion USDC in circulation (60.68% dominated by Tether, Circle #2)

**Circulation growth:**

- Q3 2025: $74B circulation, +97% YoY
- Q2 2025: $61.3B, +90% YoY
- Current (Feb 2026): $76B

**Payment volume:**

- Trailing 12-month total payment volume (TPV): $3.4B annualized, +101x growth
- Circle's Payments Network (CPN): $3.4B annualized transaction volume since May 2025 launch
- Cross-Chain Transfer Protocol (CCTP): $31B processed in Q3 2025, +740% YoY

**IPO/Valuation:**

- Listed NYSE June 4, 2025
- Sought $624M at up to $6.7B valuation
- Rejected $4-5B acquisition bid from Ripple Labs (April 2025) as too low

**Key partnerships:** Brex, Deutsche Börse Group, Finastra, Fireblocks, Hyperliquid, Kraken, Unibanco Itaú, Visa, Polymarket, Binance (Dec 2024), Coinbase

**Additional products:**

- USYC (tokenized money market fund): $1B, +200% from June 30 to November 8, 2025

**Regulatory:** Conditional OCC approval for First National Digital Currency Bank (Circle) national banking charter

**Sources:** [Circle Q3 2025 results](https://www.circle.com/pressroom/circle-reports-third-quarter-2025-results), [Circle Q2 2025 results](https://s206.q4cdn.com/265218871/files/doc_financials/2025/q2/Q2-2025-Earnings-Press-Release.pdf), [Coin Metrics](https://coinmetrics.io/state-of-the-network/circle-goes-public-valuation-and-economics-usdc/)

---

### Tether (USDT)

**Market cap:** $187.0B (60.68% market share, largest stablecoin)

**Payment volume (2025):**

- $156B in payments of $1,000 or less
- Average daily volumes for sub-$1,000 transfers: $500M+
- H1 2025: $8.9T settled on-chain, $400M monthly net inflows, 24.8% YoY growth
- 24-hour trading volume: regularly exceeds $128B

**Market position:** Controls 82.5% of global stablecoin trading volume

**Payment infrastructure expansion:**

- **Tether Pay:** Lightweight mobile payment system for emerging markets (launched 2025)
- **Telegram integration:** Native USDT support for 700M+ users, enabling instant P2P transfers
- **Speed investment:** $8M in Speed (payments infrastructure), which handles $1.5B annual payments and serves 1.2M users using Lightning + USDT

**Funding/Valuation:** Exploring $15-20B round at ~$500B valuation

**Strategic focus:** Evolution from trading instrument to functional payments rail for real-world transactions

**Sources:** [TRM Labs](https://www.trmlabs.com/reports-and-whitepapers/2025-crypto-adoption-and-stablecoin-usage-report), [BeInCrypto](https://beincrypto.com/tether-usdt-payments-crypto-adoption-2025/), [CoinDesk](https://www.coindesk.com/business/2025/12/16/tether-leads-usd8-million-investment-in-speed-to-push-usdt-further-into-everyday-payments), [insights4vc](https://insights4vc.substack.com/p/tether-explores-15-to-20b-round-at)

---

### PayPal (PYUSD)

**Market cap:** $3.6-3.9B (0.38% market share vs USDT 62.5%, USDC 24.21%)

**Growth trajectory:**

- Exploded from $500M to $3.9B in 2025
- Crossed $1B in June 2025
- Transaction volume tripled in Q3 2025
- Transactions increased 150% to 1.8M by September 2025

**Multi-chain expansion:** 9+ chains (Ethereum, Solana, Arbitrum, Stellar, etc.)

**Yield incentives:** Summer 2025 launch, variable APY currently 3.7% for holding PYUSD

**Key partnerships:**

- Visa + BVNK: PYUSD payouts via Visa Direct to digital wallets globally
- Target corridors: India, Nigeria
- Fee reduction: ~6% traditional → under 2% via PYUSD

**Competitive moat:** Multi-chain but dispersed liquidity, yield as user retention

**Sources:** [CoinMarketCap](https://coinmarketcap.com/cmc-ai/paypal-usd/latest-updates/), [PayPal newsroom](https://newsroom.paypal-corp.com/2025-06-11-PayPal-USD-PYUSD-Plans-to-Use-Stellar-for-New-Use-Cases), [OKX](https://www.okx.com/learn/pyusd-market-growth-paypal-stablecoin)

---

### Paxos

**Focus:** Stablecoin issuance-as-a-service, global dollar network expansion

**Regulatory:** Conditional OCC approval for conversion from state charter to national banking charter

**Recent partnerships:**

- Reap (Hong Kong fintech) integration for business payments (Dec 2025)
- Amina Bank integration

**Acquisition:** Acquired Fordefi (crypto wallet startup) November 2025 to expand custody services

**Issuance clients:** PayPal (PYUSD)

**Sources:** [Blockhead](https://www.blockhead.co/2025/12/03/hong-kong-fintech-reap-integrates-paxos-stablecoin-for-business-payments/), [CoinDesk](https://www.coindesk.com/business/2025/11/25/paxos-acquires-crypto-wallet-startup-fordefi-to-expand-custody-services), [Yahoo Finance](https://finance.yahoo.com/news/circle-ripple-paxos-fidelity-bitgo-164313047.html)

---

### Ripple (RLUSD)

**Launch:** December 2024

**Market cap:** Grew to $1.3B

**What it is:** Fully regulated stablecoin pegged 1:1 to USD, backed by US dollar deposits, short-term US Treasury bonds, cash equivalents in regulated financial institutions

**Strategic positioning:** Built for compliance, transparency, institutional trust (not rapid retail adoption)

**Multi-chain expansion:** December 2025 announced expansion to Ethereum L2s via Wormhole

**Regulatory:** Conditional OCC approval for Ripple National Trust Bank (national banking charter)

**Partnerships:** BNY Mellon serves as custody partner for RLUSD

**Sources:** [Eco Support Center](https://eco.com/support/en/articles/12005568-what-is-rlusd-stablecoin-complete-guide-to-ripple-s-new-digital-dollar), [CoinDesk](https://www.coindesk.com/tech/2025/12/15/ripple-expands-usd1-3b-rlusd-stablecoin-to-ethereum-l2s-via-wormhole-in-multichain-push), [Yahoo Finance](https://finance.yahoo.com/news/circle-ripple-paxos-fidelity-bitgo-164313047.html)

---

### Agora

**Funding:** $50M Series A led by Paradigm (July 2025)

**Business model:** White-labeled stablecoin platform — helps companies launch their own stablecoins

**Competitive difference vs Paxos:** Companies launch stablecoins on top of AUSD (Agora's token), reinforcing Agora's moat via liquidity and interoperability

**Strategic positioning:** Platform play rather than direct issuer (all launches benefit AUSD network effects)

**Sources:** [Fortune](https://fortune.com/crypto/2025/07/10/exclusive-agora-stablecoin-series-a-venture-paradigm-crypto-van-eck/), [CryptoNinjas](https://www.cryptoninjas.net/news/agora-unveils-white-labeled-stablecoin-platform-to-disrupt-crypto-finance/)

---

### Mountain Protocol (USDM)

**Product:** First permissionless yield-bearing stablecoin, backed exclusively by short-term US Treasuries

**Funding:** $12M total ($4M seed September, $8M Series A led by Multicoin Capital, Castle Island Ventures, Coinbase Ventures)

**Volume:** Launched late 2023, peaked at $150M supply, declined to $50M. Target: 10x growth to $500M by year-end

**Status:** Anchorage Digital acquired Mountain Protocol (May 2025). USDM Phase 2 wind down completed August 22, 2025 — primary market closed, remaining holders redeem via secondary markets

**Sources:** [The Block](https://www.theblock.co/post/298910/yield-bearing-stablecoin-mountain-protocol-funding), [CoinDesk](https://www.coindesk.com/business/2025/05/12/anchorage-digital-to-acquire-usdm-issuer-mountain-protocol-in-stablecoin-expansion-move), [The Block](https://www.theblock.co/post/354004/anchorage-acquires-mountain-protocol-sunset-usdm-token)

---

### Brale

**What they do:** US-regulated stablecoin issuance and orchestration platform (stablecoin-as-a-service)

**Platform features:**

- Custom stablecoin creation and management
- Full regulatory coverage, reserve management, banking connectivity
- Unified custody, compliance, mint/burn infrastructure, fiat on/off-ramps
- Operates under US money transmitter licenses

**Blockchain expansion:** Added Algorand blockchain support (enterprise-grade, quantum-resistant)

**Sources:** [PRNewswire](https://www.prnewswire.com/news-releases/brale-expands-custom-stablecoin-issuance-and-orchestration-platform-to-enterprise-grade-quantum-resistant-algorand-blockchain-302655564.html), [Brale](https://brale.xyz/)

---

### BVNK

**What they do:** Business and fintech stablecoin payment infrastructure — send, receive, store, convert stablecoins. Pay suppliers, partners, workers, customers globally in stablecoins from fiat balance or mixed stablecoin/fiat rails

**Target use case:** Cross-border payments acceleration for businesses and individuals

**Key partnership:** Visa + BVNK enable PYUSD payouts via Visa Direct

**Sources:** [BVNK](https://bvnk.com/letsgo), [Jas Shah analysis](https://jasshah.substack.com/p/bvnk-stablecoin-infrastructure)

---

### Mesh

**Funding:**

- January 2026: $75M Series C, $1B valuation (unicorn status)
- March 2025: $82M Series B
- Total raised: $200M+

**What they do:** Universal crypto payments network

**Investors:** PayPal Ventures backed

**Sources:** [PRNewswire](https://www.prnewswire.com/news-releases/mesh-secures-75m-series-c-reaches-1b-valuation-to-build-the-universal-crypto-payments-network-302670833.html), [CoinDesk](https://www.coindesk.com/business/2026/01/27/mesh-becomes-unicorn-raises-usd75-million-for-crypto-payments-infrastructure)

---

### Regional Payment Companies

**Yellow Card (Africa):**

- Africa among world's top stablecoin adopters (CEO statement)
- Visa partnership to launch stablecoin transactions in at least one African country in 2025, additional rollouts 2026
- Nigeria: continent's largest stablecoin market, $22B transactions July 2023 – June 2024

**Bitso (LATAM):**

- Total funding: $331M over 7 rounds (historical)
- Household name in Mexico alongside Mercado Bitcoin (Brazil), Ripio (Argentina)
- Launched BRL1 (Brazilian real stablecoin) with Mercado Bitcoin, Foxbit, Caivest
- Predicts stablecoins will account for 12% of money transfers by 2030

**Rain (MENA):**

- MENA shows highest centralized exchange activity at 66%

**Bancolombia (Colombia):**

- Launched Colombian peso-backed stablecoin ($COPW) via Wenia

**Sources:** [PYMNTS](https://www.pymnts.com/cryptocurrency/2025/yellow-card-ceo-sees-africa-boosting-global-stablecoin-adoption/), [Chainalysis](https://www.chainalysis.com/blog/latin-america-crypto-adoption-2025/), [Fireblocks](https://www.fireblocks.com/blog/execution-in-motion-how-latin-america-is-leading-stablecoin-adoption)

---

## 2. TradFi Integration Timeline

### Visa Stablecoin Settlement

**2023:** Initial stablecoin settlement pilots in parts of Latin America, Europe, Asia-Pacific, CEMEA

**July 2025:** Expansion to support USDC, PYUSD, USDG, EURC across 4 blockchains (Ethereum, Solana, Stellar, Avalanche)

- Volume by July 2025: $225M+ settled

**December 2025:** Launched USDC settlement in United States

- Initial banking participants: Cross River Bank, Lead Bank
- Settlement over Solana blockchain
- Broader US availability planned through 2026

**November 30, 2025:** Monthly stablecoin settlement volume reached annualized run rate of $3.5B+

**SIBOS 2025:** Announced stablecoin prefunding pilot via Visa Direct for global business money movement

- Limited availability: April 2026
- Expansion planned through 2026

**Sources:** [Visa newsroom](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21951.html), [The Asian Banker](https://www.theasianbanker.com/press-releases/visa-brings-usdc-settlement-to-the-us-expanding-stablecoins-into-core-institutional-payments), [tmmmacro](https://tmmmacro.com/visa-mastercard-stablecoin-war/)

---

### Mastercard

**June 2025:** Partnerships with Circle, Paxos, Fiserv, PayPal

- Supports multiple stablecoins across network
- Enables acquiring institutions to settle with merchants using stablecoins
- Pilots: Eastern Europe, Middle East, Africa

**2025:** Partnership with MoonPay enabling users to link stablecoin-funded digital wallet to Mastercard for stablecoin spend

**Merchant acceptance context:** Direct merchant stablecoin acceptance remains limited due to disputes, compliance, merchant tooling. Stablecoins increasingly power settlement instead.

**Crypto card spend:** Rose from ~$100M monthly (early 2023) to ~$1.5B (late 2025), implying $18B annualized via stablecoin-linked payment cards

**Sources:** [insights4vc](https://insights4vc.substack.com/p/the-state-of-stablecoin-cards), [Crossmint blog](https://blog.crossmint.com/stablecoins-visa-mastercard/)

---

### JPMorgan Onyx / JPM Coin

**Total volume since inception:** $1.5T+ in notional value, later reported as $2T+

**Daily volume:**

- Average: $2B daily
- More recent data: $3B daily (reflecting 2025 growth)

**Transactions growth:** +10x YoY

**JPM Coin USD deposit token:**

- Proof-of-concept launched June 2025
- Launched on Base (Coinbase L2), enabling 24/7 settlement and real-time liquidity for institutions
- Institutional clients: B2C2, Coinbase, Mastercard

**Platform rebrand:** Kinexys by J.P. Morgan

**Q4 2025 performance:** J.P. Morgan Payments revenue $5.1B, +9% YoY, driven by deposit growth and JPM Coin launch

**Sources:** [JPMorgan Kinexys](https://www.jpmorgan.com/kinexys/digital-payments/jpm-coin), [CoinDesk](https://www.coindesk.com/business/2025/12/18/jpmorgan-s-tokenized-dollars-are-quietly-rewiring-how-wall-street-moves-money), [The Edge Singapore](https://www.theedgesingapus.com/news/singapore-fintech-festival-2025/jpm-launches-usd-onchain-deposit-token-which-acts-bank-deposit)

---

### Banks Offering Stablecoin Services Directly

**BNY Mellon:**

- Launched BNY Dreyfus Stablecoin Reserves Fund (BSRXX) November 2025, money market fund supporting institutional digital asset adoption
- Custody partner for Ripple's RLUSD
- Offers custody for Bitcoin, Ethereum, plans to add additional tokens

**Citibank:**

- Targeting 2026 launch for crypto custody service
- Exploring stablecoins as next product after custody
- "Token Services" used for cross-border, 24/7 transfers
- Collaborating with Payoneer on payment settlement business

**State Street:**

- Building tokenized money-market funds, ETFs, cash instruments (tokenized deposits, stablecoins)
- Plans crypto custody launch 2026

**Banking consortium (Goldman Sachs, Deutsche Bank, Bank of America, Banco Santander, BNP Paribas, Citigroup, MUFG Bank, TD Bank Group, UBS):**

- Exploring issuing reserve-backed digital payment asset available on public blockchains

**Lead Bank:**

- Key partner for stablecoin and payment firms

**Sources:** [BNY newsroom](https://www.bny.com/corporate/global/en/about-us/newsroom/press-release/bny-launches-stablecoin-reserves-fund-expanding-bnys-leadership-digital-assets-130451.html), [CNBC](https://www.cnbc.com/2025/10/13/citi-aims-to-launch-crypto-custody-in-2026-exploring-stablecoin.html), [The Block](https://www.theblock.co/post/385818/state-street-tokenization-banks-bring-cash-funds-onchain-bloomberg), [Yahoo Finance](https://finance.yahoo.com/news/wall-street-banks-unite-launch-204638322.html)

---

## 3. Geographic Adoption Data

### Overall Stablecoin Transaction Volume (2024)

**Total:** $27.6T in 2024, surpassing Visa (~$14T) and Mastercard combined by 7.68%

**Breakdown warning:**

- Trading/settlements dominate: $25.8T+ is aggregated trading volume
- Bot activity: 77% of all stablecoin transfers (unadjusted volumes)
- Networks where USDC dominates (Solana, Base): 98%+ bot activity
- DeFi speculation is major contributor

**Payment-specific volume:** $5.7T (15% of global retail cross-border transactions)

**USDC vs USDT market share (transactions, not market cap):**

- USDC: 70% of total transfer volume
- USDT: 25% (down from 43% previous year despite total volume doubling)

**Sources:** [The Defiant](https://thedefiant.io/news/blockchains/stablecoins-process-27-6-trillion-2024-surpassing-visa-95-settled-on-ethereum-4b7c2671), [CryptoSlate](https://cryptoslate.com/stablecoins-surpass-visa-and-mastercard-with-27-6-trillion-transfer-volume-in-2024/), [TRM Labs](https://www.trmlabs.com/reports-and-whitepapers/2025-crypto-adoption-and-stablecoin-usage-report)

---

### Geographic Breakdown

**Asia and Pacific (highest absolute volume):**

- Inflows: $407B
- Outflows: $395B
- Tether USDT more popular in emerging economy regions

**Latin America (fastest growing):**

- Transaction volumes: $324B in 2025, +89% YoY
- Stablecoin-specific: $415B (June 2024 – June 2025), 9.1% of global crypto activity
- CEX activity: 64% (second only to MENA 66%)
- Stablecoin purchases >50% of all exchange purchases in Colombia, Argentina, Brazil (July 2024 – June 2025)
- Brazil: 90%+ of crypto flows are stablecoin-related

**Africa:**

- Nigeria: Largest stablecoin market, $22B transactions July 2023 – June 2024
- Relative to GDP: Africa and MENA stand out

**MENA:**

- Highest CEX activity: 66%

**South Asia:**

- Fastest-growing region for crypto adoption (Jan-July 2025): +80% from same period 2024

**Sources:** [Chainalysis](https://www.chainalysis.com/blog/latin-america-crypto-adoption-2025/), [IMF Working Paper](https://www.imf.org/-/media/files/publications/wp/2025/english/wpiea2025141-source-pdf.pdf), [Yellow Card](https://yellowcard.io/blog/impact-stablecoins-traditional-finance-2025/)

---

### Payment Corridors (Highest Stablecoin Traffic)

**Most active corridors:**

- Singapore-China (standout corridor)
- US-Mexico (5-10% of remittance flows already stablecoin)
- Origin countries: USA, Hong Kong SAR, Singapore, Japan, UK

**Remittance corridors:**

- US-Mexico: stablecoins = 5-10% of flows, fees under 1%
- India, Nigeria (via Visa/BVNK partnership with PYUSD)

**Cost advantage:** 50-70% cheaper than traditional rails (Bitwave data)

**Sources:** [fxcintel](https://www.fxcintel.com/research/reports/ct-stablecoins-2025-roundup), [Visa newsroom](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21696.html), [Stripe resources](https://stripe.com/resources/more/stablecoin-remittances-explained)

---

### Fastest Growing Markets (Payment Use Case)

**Latin America:**

- +89% YoY volume growth in 2025
- Keyrock + Bitso predict: 12% of money transfers by 2030

**Nigeria:**

- $22B transactions (July 2023 – June 2024)
- Stablecoins as remittance lifeline bypassing legacy inefficiencies

**Argentina:**

- Hyperinflation driver: stablecoin adoption >40% of adult population
- Stablecoin transfers used to preserve purchasing power

**Turkey:**

- $63B annually in stablecoin transfers (3.7% of GDP)
- Hyperinflation driver

**Venezuela:**

- > 40% adult stablecoin adoption rate
- People holding stablecoins for weeks/months to preserve purchasing power amid chronic inflation and capital controls

**Lebanon:**

- Same preservation-of-value use case as Venezuela

**Sources:** [Thunes](https://www.thunes.com/insights/trends/stablecoin-trends-shaping-global-payments/), [ainvest](https://www.ainvest.com/news/stablecoins-global-payment-infrastructure-explosive-growth-investment-opportunities-cross-border-markets-2509/), [Transak](https://transak.com/blog/stablecoin-playbook-2026)

---

## 4. Regulatory Landscape for Stablecoin Payments

### GENIUS Act (United States)

**Signed into law:** July 18, 2025

**Key provisions:**

- First comprehensive federal regulatory framework for stablecoins in US
- Dual regulatory system: issuers choose federal or state oversight
- Clear definition of "payment stablecoins"
- Restricted issuance to regulated institutions only

**Permitted issuers (only 3 types):**

1. Subsidiaries of insured depository institutions
2. Federally licensed nonbank stablecoin issuers
3. State-qualified issuers

**Regulator:** Office of the Comptroller of the Currency (OCC)

**Banking charters approved (conditional):**

- Circle: First National Digital Currency Bank
- Ripple: Ripple National Trust Bank
- Paxos Trust Company (state charter conversion)
- BitGo (state charter conversion)
- Fidelity Digital Assets (state charter conversion)

**Sources:** [Sumsub](https://sumsub.com/blog/global-stablecoin-compliance-guide/), [WEF](https://www.weforum.org/stories/2025/07/stablecoin-regulation-genius-act/), [stablecoininsider](https://stablecoininsider.org/stablecoin-regulations/)

---

### MiCA (European Union)

**Key dates:**

- Titles III & IV (stablecoin rules): Applied from June 30, 2024
- Full MiCA application: December 30, 2024
- Transitional measures for existing providers: Can extend to July 1, 2026 (depends on Member State)

**Scope:** Unified EU-wide rulebook covering crypto assets (not stablecoin-specific like GENIUS Act)

**Difference from GENIUS Act:** MiCA provides comprehensive crypto asset regulation; GENIUS Act focuses specifically on payment stablecoins

**Sources:** [BVNK blog](https://bvnk.com/blog/global-stablecoin-regulations-2026), [Hacken](https://hacken.io/discover/global-stablecoin-regulation/)

---

### Singapore

**Framework:** Tailored stablecoin framework finalized August 15, 2023

**Expected effective date:** Mid-2026

**Scope:** Single-currency stablecoins (SCS) issued in Singapore pegged to SGD or G10 currency (including USD)

**Positioning:** Clear framework balancing innovation with regulatory security

**Regulator:** Monetary Authority of Singapore (MAS)

**Sources:** [Sumsub](https://sumsub.com/blog/global-stablecoin-compliance-guide/), [Hacken](https://hacken.io/discover/global-stablecoin-regulation/)

---

### UAE

**Federal level:** Central Bank of the UAE (CBUAE) regulates fiat-backed stablecoins under Payment Token Services Regulation (effective August 2024)

**Regional coordination:** Layered but coordinated approach connecting federal oversight with regional innovation

**Sources:** [stablecoininsider](https://stablecoininsider.org/stablecoin-regulations/)

---

### Hong Kong

**Law:** Stablecoins Ordinance establishing regulatory regime for stablecoin issuers

**Effective date:** August 1, 2025

**Key provision:** Any person issuing fiat-referenced stablecoin in or outside Hong Kong that references Hong Kong dollar must be licensed with HKMA

**Regulator:** Hong Kong Monetary Authority (HKMA)

**Sources:** [BVNK blog](https://bvnk.com/blog/global-stablecoin-regulations-2026), [Sumsub](https://sumsub.com/blog/global-stablecoin-compliance-guide/)

---

### UK

**Regulatory developments:** HM Treasury published draft crypto legislation in 2025

**Financial Promotions rules:** In force for crypto

**Comprehensive regulation expected:** 2025-2026 window

**Sources:** [Sumsub](https://sumsub.com/blog/global-crypto-regulations/)

---

### Brazil

**Regulation:** Central Bank published new crypto regulations November 2025

**Effective date:** February 2, 2026

**Sources:** [Chainalysis](https://www.chainalysis.com/blog/2025-crypto-regulatory-round-up/)

---

### Most Favorable Jurisdictions for Stablecoin Payment Companies

**US (post-GENIUS Act):** Clear federal framework, banking charter path, largest market

**Singapore:** Balanced innovation + regulation, G10 currency support, mid-2026 clarity

**UAE:** Federal + regional coordination, early mover on Payment Token Services Regulation

**Hong Kong:** Clear licensing regime, strategic Asia gateway

**UK:** Mature financial system, comprehensive regulation incoming 2025-2026

**Sources:** [Elliptic](https://www.elliptic.co/blog/how-crypto-regulation-changed-in-2025), [Paxos blog](https://www.paxos.com/blog/regulatory-landscape-for-stablecoins)

---

## 5. The $27.6T Number — Breaking Down Stablecoin Volume

### Total Stablecoin Transaction Volume 2024: $27.6T

**Comparison to traditional rails:**

- Visa: ~$14T
- Stablecoins exceeded Visa + Mastercard combined by 7.68%

**Sources:** [The Defiant](https://thedefiant.io/news/blockchains/stablecoins-process-27-6-trillion-2024-surpassing-visa-95-settled-on-ethereum-4b7c2671), [CryptoSlate](https://cryptoslate.com/stablecoins-surpass-visa-and-mastercard-with-27-6-trillion-transfer-volume-in-2024/)

---

### Payments vs DeFi vs Speculation Breakdown

**Aggregated trading volume:** $25.8T+ (the majority)

**Payment-specific volume:** $5.7T (15% of global retail cross-border transactions)

**Bot activity (unadjusted transactions):** 77% of all stablecoin transfers in 2024

**Bot activity on USDC-dominated networks (Solana, Base):** 98%+ of total activity

**Real-economy stablecoin payments:** $122B

- Of which B2B transfers: $76B (largest use case by 2025)

**DeFi speculation:** Major contributor. Networks with high transaction speeds, low costs, booming DeFi ecosystems, rapid proliferation of meme tokens drove much of the activity

**Key takeaway:** Most volume is NOT payments. It's trading, settlements, DeFi, speculation, and bot activity. True payment volume is a fraction of the headline $27.6T.

**Sources:** [TRM Labs](https://www.trmlabs.com/reports-and-whitepapers/2025-crypto-adoption-and-stablecoin-usage-report), [BVNK blog](https://bvnk.com/blog/stablecoins-core-financial-infrastructure-2025), [Modern Treasury](https://www.moderntreasury.com/journal/stablecoins-in-action-b2b-and-b2c-payments)

---

### Breakdown by Stablecoin

**USDT (Tether):**

- Market cap: $187.0B (60.68% market share)
- Transaction volume market share: 25% (down from 43% previous year)
- Total volume: Doubled YoY despite market share decline

**USDC (Circle):**

- Market cap: $75.7B
- Transaction volume market share: 70% of total transfer volume (dominant)

**PYUSD (PayPal):**

- Market cap: $3.6-3.9B (0.38% market share)

**USDe (Ethena):**

- Market cap: $6.3B

**DAI:**

- Market cap: $5.3B

**Market concentration:** USDT + USDC = 93% of total stablecoin market cap

**Sources:** [MacroMicro](https://en.macromicro.me/charts/134292/world-stablecoin-market-cap), [DefiLlama](https://defillama.com/stablecoins), [Blockchain Reporter](https://blockchainreporter.net/stablecoin-market-tops-317-billion-as-usdt-tightens-its-grip-in-early-2026/)

---

## 6. What's Actually Being Built (February 2026)

### Stablecoin-to-Fiat Offramps — Best Coverage

**Infrastructure categories:**

1. Centralized exchanges (strong liquidity, varying UX)
2. Embedded aggregators
3. Issuer/treasury rails
4. Peer-to-peer platforms

**Global coverage leaders:**

**Ramp:**

- ~40 currencies
- 110 cryptocurrencies globally

**Transak:**

- 40 cryptocurrencies
- 27 currencies
- 64+ countries

**OpenPayd:**

- €130B processed annually
- 800+ enterprise clients (as of 2025)

**Mural Pay:**

- 40+ currency options
- Strong LATAM coverage (ARS, BRL, MXN)

**Settlement speed:**

- Real-time payment (RTP) rail markets: Minutes (e.g., MXN, BRL)
- Non-RTP markets: Same day or T+1

**Recent institutional partnerships:**

- WSPN (Worldwide Stablecoin Payment Network) + HIFI: Stablecoin-to-fiat conversion for institutional cross-border payment settlements (January 2026)

**Sources:** [OpenPayd](https://www.openpayd.com/blog/what-are-fiat-on-off-ramps-and-how-do-they-work-with-stablecoins/), [stablecoininsider](https://stablecoininsider.org/stablecoin-on-off-ramps/), [Mural](https://www.muralpay.com/blog/best-stablecoin-off-ramp-providers), [PRNewswire](https://www.prnewswire.com/in/news-releases/wspn-partners-with-hifi-to-enable-seamless-cross-border-stablecoin-fiat-conversion-for-institutional-clients-302664966.html)

---

### Merchant Acceptance Infrastructure

**Current state:** Direct merchant stablecoin acceptance remains limited due to disputes, compliance, merchant tooling

**Indirect acceptance (settlement layer):**

- Visa: Merchants don't accept stablecoins directly; banks/issuers settle with Visa in USDC
- Mastercard: Similar settlement-layer integration via Circle, Paxos, Fiserv, PayPal

**Crypto card spend (proxy for merchant acceptance):**

- Early 2023: ~$100M monthly
- Late 2025: ~$1.5B monthly
- Annualized 2025: ~$18B
- Mechanism: Stablecoin-linked payment cards, not direct merchant acceptance

**2026 trend:** Stablecoins function as payments infrastructure (settlement) rather than direct merchant payment method

**Sources:** [insights4vc](https://insights4vc.substack.com/p/the-state-of-stablecoin-cards), [Crossmint](https://blog.crossmint.com/stablecoins-visa-mastercard/), [FinTech Weekly](https://www.fintechweekly.com/magazine/articles/stablecoin-predictions-2026-payments-infrastructure-regulation)

---

### Cross-Border Payment Rails Using Stablecoins

**B2B stablecoin payment volume:**

- Early 2023: <$100M monthly
- 2025: $3B+ monthly
- Growth: 30x in 2 years

**Annual payment-specific volume:** $5.7T (15% of global retail cross-border transactions)

**Market penetration:** 3% of entire global cross-border payment value flows through stablecoins (Q1 2025)

**Cost advantage:** 50-70% cheaper than traditional rails (Bitwave)

**Speed advantage:**

- SWIFT: 1-5 business days (correspondent bank reconciliation, sanctions screening, liquidity management)
- Stablecoins: Minutes

**Key corridors:** US-Mexico, Singapore-China, USA/Hong Kong SAR/Singapore/Japan/UK outbound

**Visa Direct stablecoin prefunding pilot:** Announced SIBOS 2025, limited availability April 2026

**SWIFT position:** Began trials involving digital currencies early 2025, leveraging "unique position at heart of financial system to interlink disparate networks"

**Sources:** [fxcintel](https://www.fxcintel.com/research/reports/ct-stablecoins-2025-roundup), [Reap](https://reap.global/newsroom/b2b-stablecoin-payments-surge-30x-to-3-billion-monthly-volume-in-2025), [opendue](https://www.opendue.com/blog/stablecoins-in-cross-border-payments-benefits-risks-and-2025-trends)

---

### B2B Payment Use Cases

**Scale:** $76B in direct B2B flows out of $122B real-economy stablecoin payments (largest use case by 2025)

**Primary use cases:**

- Invoice settlements
- International supplier payments
- Treasury rebalancing across regions

**Speed:** Minutes vs days for traditional bank wires

**Enterprise adoption example:** Siemens implemented programmable payments via JPM Coin to automate internal treasury transfers

**2026 infrastructure providers:** Combine stablecoin rails with compliance, liquidity, approval controls, reconciliation tooling

**Sources:** [BVNK blog](https://bvnk.com/blog/stablecoins-core-financial-infrastructure-2025), [stablecoininsider](https://stablecoininsider.org/b2b-stablecoin-payment-solutions-in-2026/), [Modern Treasury](https://www.moderntreasury.com/journal/stablecoins-in-action-b2b-and-b2c-payments)

---

### Payroll/Freelancer Payments

**Stripe/Bridge + Remote.com:** Payouts using stablecoin infrastructure in 70+ countries

**Geographic focus:** Countries with underdeveloped payment infrastructure where stablecoins reduce transaction failures and improve conversion rates

**Cost structure:** Traditional remittance corridors ~6%, stablecoin rails <1% (US-Mexico data)

**Target corridors:** India, Nigeria (via Visa/BVNK/PYUSD partnership)

**Sources:** [Stripe newsroom](https://stripe.com/newsroom/news/stripe-completes-bridge-acquisition), [Visa newsroom](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21696.html)

---

### Treasury Management Using Stablecoins

**Institutional adoption:**

- 13% of financial institutions and corporations globally already using stablecoins (EY-Parthenon survey June 2025)
- 54% of non-users expect to adopt within 6-12 months
- 23% of CFOs anticipate treasury departments will engage with crypto within 2 years
- 39% of CFOs at companies with $10B+ annual revenue anticipate crypto engagement

**Market growth:**

- Stablecoin market cap: $308B+ (December 2025), up from ~$205B (start of 2025)
- Standard Chartered projection: $2T market by 2028

**Enterprise examples:**

- Siemens: Programmable payments via JPM Coin for internal treasury transfers
- SoFi: First national bank to issue own stablecoin (SoFiUSD) on public blockchain
- Ripple acquired GTreasury ($1B): Integrating digital asset infrastructure into Fortune 500 treasury tooling (cash forecasting, risk management)

**Primary use case:** Optimizing cross-border payment flows for organizations with international supplier networks, distributed workforces, multi-entity structures

**Speed advantage:** Minutes vs 2-5 business days (correspondent banking networks)

**Institutional banking involvement:**

- Barclays: First investment in stablecoin settlement platform
- BNY Mellon: Launched BNY Dreyfus Stablecoin Reserves Fund (BSRXX) for institutional liquidity
- Citibank: Crypto custody 2026 launch, stablecoins next
- State Street: Tokenized money-market funds, stablecoins, custody 2026

**Sources:** [AlphaPoint](https://alphapoint.com/blog/stablecoin-treasury-management-for-institutions-the-definitive-2026-guide), [B2Broker](https://b2broker.com/news/institutional-adoption-of-crypto/), [treasuryup](https://treasurup.com/stablecoins-for-banks-strategic-playbook-2025/), [ainvest](https://www.ainvest.com/news/strategic-opportunities-regulated-stablecoin-ecosystems-global-payment-infrastructure-evolves-2026-2601/)

---

## Summary Statistics (February 2026)

| Metric                            | Value                         | Source                                                                                                                                                     |
| --------------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Total stablecoin market cap**   | $317.94B                      | [Blockchain Reporter](https://blockchainreporter.net/stablecoin-market-tops-317-billion-as-usdt-tightens-its-grip-in-early-2026/)                          |
| **USDT market cap**               | $187.0B (60.68% share)        | [Blockchain Reporter](https://blockchainreporter.net/stablecoin-market-tops-317-billion-as-usdt-tightens-its-grip-in-early-2026/)                          |
| **USDC circulation**              | $75.7B                        | [Circle Q3 2025](https://www.circle.com/pressroom/circle-reports-third-quarter-2025-results)                                                               |
| **PYUSD market cap**              | $3.6-3.9B                     | [CoinMarketCap](https://coinmarketcap.com/cmc-ai/paypal-usd/latest-updates/)                                                                               |
| **2024 total transaction volume** | $27.6T                        | [The Defiant](https://thedefiant.io/news/blockchains/stablecoins-process-27-6-trillion-2024-surpassing-visa-95-settled-on-ethereum-4b7c2671)               |
| **Payment-specific volume**       | $5.7T (2025)                  | [fxcintel](https://www.fxcintel.com/research/reports/ct-stablecoins-2025-roundup)                                                                          |
| **Real-economy payments**         | $122B (B2B: $76B)             | [BVNK](https://bvnk.com/blog/stablecoins-core-financial-infrastructure-2025)                                                                               |
| **B2B monthly volume**            | $3B+ (2025)                   | [Reap](https://reap.global/newsroom/b2b-stablecoin-payments-surge-30x-to-3-billion-monthly-volume-in-2025)                                                 |
| **Active stablecoin wallets**     | 30M+ (Feb 2025), +53% YoY     | [Host Merchant Services](https://www.hostmerchantservices.com/2025/08/cross-border-payment/)                                                               |
| **Visa stablecoin settlement**    | $3.5B annualized (Nov 2025)   | [Visa newsroom](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21951.html)                                                              |
| **JPM Coin daily volume**         | $3B average                   | [The Edge Singapore](https://www.theedgesingapore.com/news/singapore-fintech-festival-2025/jpm-launches-usd-onchain-deposit-token-which-acts-bank-deposit) |
| **Circle CCTP volume**            | $31B Q3 2025, +740% YoY       | [Circle Q3 2025](https://www.circle.com/pressroom/circle-reports-third-quarter-2025-results)                                                               |
| **Tether sub-$1K payments**       | $156B (2025)                  | [BeInCrypto](https://beincrypto.com/tether-usdt-payments-crypto-adoption-2025/)                                                                            |
| **LATAM transaction volume**      | $324B (2025), +89% YoY        | [Chainalysis](https://www.chainalysis.com/blog/latin-america-crypto-adoption-2025/)                                                                        |
| **Nigeria transactions**          | $22B (July 2023 - June 2024)  | [Yellow Card](https://yellowcard.io/blog/impact-stablecoins-traditional-finance-2025/)                                                                     |
| **Turkey annual transfers**       | $63B (3.7% of GDP)            | [Thunes](https://www.thunes.com/insights/trends/stablecoin-trends-shaping-global-payments/)                                                                |
| **Crypto card monthly spend**     | $1.5B (late 2025)             | [insights4vc](https://insights4vc.substack.com/p/the-state-of-stablecoin-cards)                                                                            |
| **Cross-border market share**     | 3% of global value (Q1 2025)  | [fxcintel](https://www.fxcintel.com/research/reports/ct-state-of-stablecoins-cross-border-payments-2025)                                                   |
| **US-Mexico remittance share**    | 5-10%                         | [fxcintel](https://www.fxcintel.com/research/reports/ct-stablecoins-2025-roundup)                                                                          |
| **Institutional adoption**        | 13% currently using           | [AlphaPoint](https://alphapoint.com/blog/stablecoin-treasury-management-for-institutions-the-definitive-2026-guide)                                        |
| **Institutional intent**          | 54% plan adoption 6-12 months | [AlphaPoint](https://alphapoint.com/blog/stablecoin-treasury-management-for-institutions-the-definitive-2026-guide)                                        |

---

## Key Insights for Stablecoin/Payments Infrastructure Professional

### 1. The $27.6T is mostly NOT payments

- 77% bot activity, $25.8T+ is trading/settlements
- Real payment volume: $5.7T, real-economy B2B: $76B
- Industry headlines conflate trading with payments usage

### 2. Infrastructure war is settlement, not merchant acceptance

- Visa/Mastercard integrating stablecoins at settlement layer, not consumer-facing
- Direct merchant acceptance limited (disputes, compliance, tooling)
- Crypto cards ($18B annualized) are the consumer bridge

### 3. Regulatory clarity unlocked institutional adoption

- GENIUS Act (July 2025) created banking charter path
- OCC approved Circle, Ripple, Paxos, BitGo, Fidelity for national charters
- 54% of institutions plan stablecoin adoption within 6-12 months

### 4. TradFi integration accelerating 2025-2026

- Visa: $3.5B annualized settlement, US launch Dec 2025, expanding 2026
- JPM Coin: $3B daily, launched on Base, B2C2/Coinbase/Mastercard clients
- Banking consortium (Goldman, Deutsche, BofA, Santander, BNP, Citi, UBS) exploring reserve-backed digital payment asset
- BNY Mellon, Citi, State Street launching stablecoin services 2025-2026

### 5. Emerging markets = payment adoption, developed = speculation

- Nigeria, Argentina, Turkey, Venezuela: >40% adult adoption, preservation of value
- Turkey: $63B annually (3.7% GDP)
- Nigeria: $22B (July 2023 - June 2024)
- LATAM: +89% YoY growth, Brazil 90%+ flows are stablecoin

### 6. B2B largest real use case, not consumer

- $76B in B2B flows out of $122B real-economy payments
- Monthly B2B volume: $3B+ (30x growth 2023-2025)
- Invoice settlement, supplier payments, treasury rebalancing

### 7. Competitive moat question: who owns distribution?

- Circle: USDC 70% transaction volume share despite 24% market cap (vs USDT 60% market cap, 25% transaction share)
- Stripe/Bridge: Integrated into Stripe's merchant base
- JPM Coin: Embedded in JPM institutional banking relationships
- PayPal: 400M+ users but only 0.38% stablecoin market share
- Platform plays (Agora, Brale): White-label issuance, network effects via base layer

### 8. Treasury management emerging as Fortune 500 wedge

- 23% of CFOs (39% at $10B+ revenue companies) anticipate crypto engagement within 2 years
- Siemens, SoFi live examples
- Ripple acquired GTreasury ($1B) to embed in Fortune 500 treasury tooling
- Speed (minutes vs 2-5 days) + cost (50-70% cheaper) advantages for cross-border

### 9. Offramp coverage still fragmented

- RTP markets (BRL, MXN): Minutes settlement
- Non-RTP: Same day or T+1
- No single provider has comprehensive global coverage
- Opportunity for infrastructure consolidation

### 10. Next battleground: yield-bearing stablecoins vs payment stablecoins

- Mountain Protocol (USDM) wound down, acquired by Anchorage
- PayPal launched 3.7% APY on PYUSD (Summer 2025)
- Circle USYC (tokenized money market fund): $1B, +200% growth
- Regulatory question: Will payment stablecoins be allowed to offer yield, or does that create bank-like risk without bank regulation?
