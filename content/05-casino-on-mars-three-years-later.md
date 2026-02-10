# Three Years on Mars

I re-read "The Casino on Mars" last week, almost three years after Matt Huang published it. It remains the best thing written about crypto speculation. Huang identified the correct mechanism: speculation bootstraps infrastructure. Carlota Perez documented this across five technological revolutions.[^1] The 1849 gold rush confirmed it in granular economic detail. Huang saw the pattern and made the case at a time when the industry had just lost $2 trillion in market cap and its most prominent exchange had turned out to be a fraud.[^2]

That took conviction.

The essay also contained zero numbers. Huang's most compressed formulation was nine words: "Speculation is the 'hello world' of digital property rights."[^2] Three years later, the numbers exist. I went looking for them. What I found extends the Mars metaphor in a direction that Kim Stanley Robinson predicted in fiction thirty years ago and that tells a more interesting story than either the bulls or bears expected.

---

## What the numbers say

The infrastructure build is not in dispute. Stablecoins went from $120 billion to $318 billion since Huang published.[^3] Stripe paid $1.1 billion for Bridge.[^6] BlackRock tokenized $2.9 billion in treasuries.[^7] Solana generates $603 million in annual fees.[^9] The GENIUS Act became law.[^11] The full data set is in the footnotes. What matters is what it means.

---

## The great reallocation

The VC story is more specific than "speculation turned real." Crypto VC peaked at $32.8 billion in 2021, collapsed to $9.5 billion in 2023, recovered to $22 billion in 2025.[^12] Infrastructure now commands 60% of all funding.[^13] This is capital redirecting from Installation-era speculation toward productive use, which is what Perez's model predicts but what Huang's essay doesn't name.

His firm put $225 million into Monad at a $3 billion valuation (now $1.7 billion), $150 million into Farcaster at a billion (pivoted from social to wallets), $70 million into Babylon at $800 million (now $180 million).[^14] Fund 1 returned 10.9x by being early to Uniswap, Lido, Optimism, Coinbase. The 2024 bets are collectively down 43 to 78%. I don't raise this to criticize. The firm also built Reth, Foundry, and the open-source tooling a huge percentage of the ecosystem depends on. samczsun's SEAL initiative has done more for crypto security than probably any other effort. But structurally, the window for crypto-native venture to capture infrastructure value narrowed once TradFi arrived with existing distribution.

Haseeb Qureshi wrote in 2017 that the serious builders would eventually "come in and do the graceless work of building the future."[^15] The biggest exit in 2025 wasn't a token. It was Stripe paying cash for Bridge. The most profitable product was pump.fun making $935 million in memecoin launchpad fees.[^16] The largest asset accumulation was BlackRock's IBIT reaching $100 billion faster than any ETF in history.[^8]

The entities capturing the next layer of value are not the ones who built it.

---

## The technology that came home

Robinson's Mars Trilogy (1992-1996) is the most detailed fictional account of what happens when you send engineers to a hostile planet. The settlers develop closed-loop life support, atmospheric processors, new materials science, a longevity treatment. Many die. The colony is chaotic, factional, violent.

But in _Blue Mars_, the technologies developed under Martian constraints turn out to be what Earth needs most. Ecological engineering, resource recycling, the longevity treatment. The technology transfer from colony to home world becomes more consequential than the colony itself. Robinson understood something Perez's framework misses: the value of a frontier isn't just what gets built there. It's what gets invented under pressure and then exported.

This is what happened to crypto since September 2023. And from where I sit in payments infrastructure, I can see why it exports so well. The reason is structural.

Crypto had to build trust from mathematics. No courts. No FDIC. No regulatory backstop. If you lose your keys, the money is gone. If the smart contract has a bug, there is no appeal. So the settlers built trust from cryptographic proofs, game theory, and economic incentives instead of from institutions. It turns out mathematical trust is more portable, more composable, and more scalable than institutional trust. That's the mechanism Robinson's metaphor captures but doesn't name.

**Stablecoin settlement** was developed entirely on-chain. USDC launched on Ethereum in 2018. Eight years later, Visa runs it on their existing network.[^4] Stripe runs cross-border payments through Bridge across 70+ countries.[^6] Patrick Collison called stablecoins "room-temperature superconductors for financial services"[^17] and then spent $1.1 billion proving it. Programmable settlement doesn't just move faster than SWIFT. It's composable: any application can call the same settlement function, the way any website can call the same HTTP protocol. SWIFT is a messaging network that tells banks to move money later. Stablecoin settlement IS the money moving. The difference isn't speed. It's architecture.

**MPC custody** solved crypto's key management problem because billions were at risk with no insurance and no reversibility. Fireblocks developed multi-party computation for exchanges. Now BNY Mellon, State Street, and Citibank use it.[^18] Traditional custody works by concentrating trust in a single institution. MPC distributes trust across multiple independent parties, so no single compromise can drain the vault. Banks didn't need this when FDIC backstopped their failures. But MPC is architecturally superior regardless of whether insurance exists, the way a distributed system is more resilient than a mainframe whether or not you have a backup generator.

The ERC-20 standard was proposed in 2015 by Fabian Vogelsteller for creating and transferring digital tokens. It was designed for memecoins. BlackRock launched BUIDL on Ethereum using that standard.[^7] Franklin Templeton runs tokenized money market funds on it. Goldman Sachs, Deutsche Bank, BofA, Santander, BNP Paribas, Citi, and UBS are exploring reserve-backed digital assets on public blockchains using it. Larry Fink put it plainly in his 2025 letter: "If SWIFT is the postal service, tokenization is email itself."[^19]

Then there's zero-knowledge proofs. ZK proofs were theoretical computer science for decades. Crypto's need for privacy-preserving verification drove billions in applied R&D through zkSync, Starknet, Polygon zkEVM.[^20] Financial institutions are now exploring ZK proofs for regulatory compliance: proving adherence without exposing proprietary data.

Ursula K. Le Guin saw this pattern in 1974. _The Dispossessed_ is about a physicist named Shevek on Anarres, a resource-poor anarchist moon colony. No luxury. No abundance. Nothing. But those constraints force Shevek to develop the General Temporal Theory, the physics that enables instantaneous interstellar communication. The wealthy home world couldn't produce this theory. They had no reason to think that differently.

The parallel is precise. SWIFT worked well enough for banks. FDIC insurance made custody a solved problem. Markets closing at 4pm was acceptable. Nobody on Earth needed to invent programmable settlement, trustless custody, tokenized securities, or zero-knowledge compliance. The settlers invented them because the conditions on Mars demanded it. And the solutions turned out to be better than what Earth had, because solving for the harder environment (no trust, no institutions, no safety net) produced more general, more portable infrastructure.

---

## The developing world

Huang cited Argentina, Turkey, and Ukraine. The data three years later is extensive.[^21][^22][^23][^24] Argentina's stablecoin adoption exceeds 40% of the adult population. Nigeria hit $92.1 billion in P2P volume. Latin American stablecoin volume reached $324 billion. Not all of it is utility. Turkey's altcoin trading eclipsed stablecoin hedging. Indonesia tripled on speculation. My estimate: roughly 50 to 60% utility, 40 to 50% speculation across developing markets.

The genuinely interesting data point isn't the adoption numbers. It's what happened when governments tried to compete. Nigeria's CBDC, the eNaira, launched to great fanfare. 98.5% of wallets are inactive.[^28] Private stablecoins grew 30%+ in the same period. Kenya's M-Pesa (91% mobile money penetration) didn't fight stablecoins. It signed an MOU to launch them on its network.[^27] Brazil's PIX integrated with crypto platforms. India's UPI accelerated crypto adoption.

Haseeb Qureshi described what this looks like at street level: "You get off a plane and your taxi driver will say, please pay me in Tether on Tron."[^25] Nic Carter called Nigeria "the first real crypto dollarization event" where people are "actively deserting the naira and going to dollars via stablecoins."[^26] A Castle Island/Visa survey of 2,541 users across five countries found 47% cited dollar savings as their primary stablecoin use. 69% had converted local currency. Nigerian respondents ranked stablecoins most favorably of any country surveyed.[^26]

Stablecoins found product-market fit for dollar savings, remittances, freelancer payments, B2B settlement.

Also true: the most successful mobile money networks aren't competing with crypto. They're integrating it.

---

## What the settlers built

In Robinson's trilogy, the First Hundred don't end up ruling the colony. Many die in the failed revolution of 2061. The survivors scatter. Some live for centuries thanks to the longevity treatment, but they become historical figures, not rulers. New generations take over. The settlers' legacy isn't ownership. It's the fact that Mars exists at all.

Philip K. Dick saw the other side of this in _Martian Time-Slip_ (1964). Arnie Kott, a union boss, tries to use a child's precognition to front-run land speculation on Mars. He thinks the value is in the real estate. He's wrong. In Dick's telling, speculation reveals the structure of reality while the speculators themselves capture almost nothing.

I work in stablecoin payments infrastructure, so I'm not neutral here. But that vantage point gives me a specific view: $318 billion market growing 83% year-over-year.[^3] B2B volumes at $3 billion monthly, up 30x in two years.[^29] Institutional adoption at 13%, with 54% planning within 12 months.[^30]

Marc Andreessen wrote in 2014 that Bitcoin's speculative value wasn't incidental to its function: "The Bitcoin currency had to be worth something before it could bear any amount of real-world payment volume. This is the classic chicken and egg problem with new technology: new technology is not worth much until it's worth a lot."[^31] The same mechanism now applies to stablecoin settlement at a scale Andreessen probably didn't anticipate.

The question I keep thinking about is which of Mars's inventions become permanent infrastructure on Earth. Stablecoin settlement is already there. Tokenized securities look inevitable. ZK proofs for institutional privacy are next. I don't know if that happens cleanly. There's a real risk that the technology gets domesticated in the transfer. BlackRock's BUIDL runs on Ethereum, but settlement still routes through traditional custodians. Banks adopting "tokenization" might strip out the permissionless properties that made it good in the first place. The technology comes home from Mars, and Earth makes it safe, and in making it safe, loses the thing that made it work.

Robinson got the mechanism right. Le Guin explained why it works. Dick warned about mistaking the speculation for the value.

The casino built more than a city. Whether what it built survives contact with Earth is the question that matters now.

---

## Notes & Sources

[^1]: Carlota Perez, _Technological Revolutions and Financial Capital_ (Edward Elgar, 2002). The five revolutions: Industrial Revolution, Age of Steam, Age of Steel/Electricity, Age of Oil/Mass Production, Age of Information/Telecommunications.

[^2]: Matt Huang, "The Casino on Mars," Paradigm, September 2023. [paradigm.xyz/2023/09/casino-on-mars](https://www.paradigm.xyz/2023/09/casino-on-mars)

[^3]: DefiLlama stablecoin dashboard, February 2026. September 2023 baseline from same source. Year-over-year growth calculated from $174B (February 2025) to $318B (February 2026).

[^4]: Visa USDC settlement data. Visa began settling USDC on Ethereum and Solana in 2023; annualized volume reported by Visa Head of Crypto Cuy Sheffield, Q4 2025.

[^6]: Stripe acquired Bridge in October 2024 for $1.1 billion, its largest acquisition. Bridge operates stablecoin orchestration infrastructure across 70+ countries. CNBC, February 5, 2025; Patrick Collison, CoinDesk interview, September 6, 2025.

[^7]: BlackRock BUIDL (USD Institutional Digital Liquidity Fund) AUM as of February 2026. Launched March 2024 on Ethereum. Consortium exploration of reserve-backed digital assets reported by Financial Times, 2025.

[^8]: iShares Bitcoin Trust (IBIT) reached $100 billion AUM faster than any ETF in history. Total crypto ETF AUM includes IBIT, FBTC, GBTC conversion, and spot Ethereum ETFs. Bloomberg ETF data, 2025.

[^9]: Electric Capital Developer Report 2024. Solana fee data from Solana Foundation and DefiLlama. Base transaction costs from Coinbase/Optimism documentation.

[^11]: GENIUS Act (Guiding and Establishing National Innovation for U.S. Stablecoins) signed into law 2025. OCC conditional charter recipients include Anchorage Digital, Paxos, Protego, Figure.

[^12]: Galaxy Digital crypto VC funding reports, 2021-2025. PitchBook crypto venture data, 2025.

[^13]: Messari and Galaxy Digital reports on infrastructure share of crypto VC, 2025. "40% premium" refers to higher average round sizes for infrastructure deals vs. DeFi/application deals.

[^14]: Paradigm investment data from CoinDesk, The Block, and company announcements. Monad: $225M Series A, April 2024; Farcaster: $150M, May 2024; Babylon: $70M, May 2024. Current valuations from secondary market data.

[^15]: Haseeb Qureshi, "Blockchain: the revolution we're not ready for," haseebq.com, July 10, 2017. [haseebq.com/blockchain-the-revolution-were-not-ready-for/](https://haseebq.com/blockchain-the-revolution-were-not-ready-for/)

[^16]: pump.fun fee revenue from on-chain data aggregated by Dune Analytics, 2025. Cumulative launchpad fees from Solana transaction data.

[^17]: Patrick Collison, X post, October 2024. [x.com/patrickc/status/1848393059559502177](https://x.com/patrickc/status/1848393059559502177)

[^18]: BNY Mellon digital asset custody launched September 2022. State Street and Citibank custody partnerships with Fireblocks announced 2023-2024. Fireblocks processes over $6 trillion in digital asset transfers.

[^19]: Larry Fink, 2025 Annual Chairman's Letter to Investors. BlackRock. [blackrock.com/corporate/investor-relations/larry-fink-annual-chairmans-letter](https://www.blackrock.com/corporate/investor-relations/larry-fink-annual-chairmans-letter). Fink and Rob Goldstein expanded on this in The Economist, December 1, 2025: "Ledgers haven't been this exciting since the invention of double-entry bookkeeping."

[^20]: zkSync (Matter Labs), Starknet (StarkWare), Polygon zkEVM. Combined VC funding exceeds $1.5 billion. ZK proof institutional adoption tracked by Ernst & Young's Nightfall protocol and similar enterprise implementations.

[^21]: Argentina stablecoin data: Chainalysis Geography of Cryptocurrency 2025; Triple-A crypto adoption report; Central Bank of Argentina inflation data (43.5% annual CPI, 2025). Bitso Argentina 4x YoY growth from company disclosures. 70% freelancer stablecoin preference from Deel/Remote.com surveys.

[^22]: Chainalysis Global Crypto Adoption Index 2025. Nigeria P2P volume includes centralized and decentralized exchange data. Yellow Card processed $3 billion in stablecoins across 34 countries, serving 30,000 businesses.

[^23]: Philippines data: GCash (Mynt/Globe Fintech) 94 million active users from company filings, 2025. Coins.ph targeting $31 billion remittance market. Fees from roughly 6% to roughly 1%. Gaming traffic from Chainalysis.

[^24]: Chainalysis Latin America Crypto Report 2025. Sub-Saharan Africa 9.3% stablecoin adoption rate from Chainalysis Geography of Cryptocurrency 2025. Latin American stablecoin volume $324 billion, up 89%.

[^25]: Haseeb Qureshi on _Complex Systems_ podcast with Patrick McKenzie, April 10, 2025. [complexsystemspodcast.com/episodes/taking-stablecoins-seriously-with-haseeb-qureshi/](https://www.complexsystemspodcast.com/episodes/taking-stablecoins-seriously-with-haseeb-qureshi/)

[^26]: Nic Carter, Blockworks interview, September 2024. Castle Island Ventures / Visa / Brevan Howard stablecoin survey, May-June 2024, n=2,541 across Brazil, India, Indonesia, Nigeria, Turkey. Full report: [castleisland.vc/writing/stablecoins-the-emerging-market-story/](https://castleisland.vc/writing/stablecoins-the-emerging-market-story/)

[^27]: M-Pesa (Safaricom/Vodacom) mobile money penetration from Communications Authority of Kenya, 2025. Stablecoin MOU reported by CoinDesk Africa, 2025.

[^28]: Central Bank of Nigeria eNaira adoption data. 98.5% wallet inactivity reported by Bloomberg and Reuters, 2025.

[^29]: B2B stablecoin volume from Circle, Fireblocks, and Bridge transaction reports. 30x growth from approximately $100 million monthly (2023) to $3 billion monthly (2025).

[^30]: Fireblocks institutional crypto survey, 2025. 13% current adoption, 54% planning within 12 months. Developer data from Electric Capital Developer Report.

[^31]: Marc Andreessen, "Why Bitcoin Matters," New York Times / a16z, January 21, 2014. [a16z.com/why-bitcoin-matters/](https://a16z.com/why-bitcoin-matters/)
