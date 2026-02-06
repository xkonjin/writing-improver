# Dense, High-Signal Technical Writers in Fintech/Crypto/Payments on X

## Complete Research Report

_Research conducted: February 6, 2026_

---

## THE ANTI-CONTENT-CREATOR ARCHETYPE

This document catalogs writers on X/Twitter who represent the opposite pole from "content creators" like Dan Koe, Sahil Bloom, or Alex Hormozi. These are domain experts whose writing reads like compressed internal memos, DMs to smart colleagues, or annotated research notes -- not performances for an audience.

The core distinction: **Content creators optimize for reach. Domain experts optimize for signal.** The writing feels different at a molecular level because the intent is different. One is trying to get you to follow. The other is trying to get the idea across.

---

## PART 1: THE TIER-1 ACCOUNTS (Highest Information Density)

### 1.1 Patrick McKenzie (@patio11) -- Payments Infrastructure

**Background**: Former Stripe advisor, founder of Bits about Money newsletter. Two decades in software, now the preeminent public explainer of financial plumbing.

**What makes his writing dense**:

- He writes about systems nobody else can explain: ACH batch processing, interchange economics, Reg E liability regimes, how money actually moves between banks
- He cites specific numbers: "NACHA charges a per-transaction fee of 1.85 hundredths of a cent, which compares favorably to regulated debit card interchange (21 cents plus five basis points) and extremely favorably to Durbin-exempt debit cards or credit cards (generally about 2.X% plus 20-30 cents)"
- His recent essay "One Regulation E, Two Very Different Regimes" (Jan 2026) dissects how a single consumer protection law creates two completely different operational realities for different payment types

**Characteristic writing moves**:

- Treats the reader as a peer who happens not to know this specific domain
- Uses parenthetical asides that contain as much signal as the main clause
- Follows a "here is how this actually works" structure, where "actually" carries real weight because the common understanding is wrong
- Humor is dry and comes from the absurdity of the system, not from performing jokes
- Casually drops details that reveal he has read the actual regulation, not a summary of it

**Example tweet-style insight** (paraphrased from his work):

> "Rewards programs are primarily funded by interchange fees paid by merchants, not by interest charges. The entire value proposition of premium credit cards is a wealth transfer from merchants and non-rewards-card holders to rewards-card holders."

**Why this does not read like AI**: The parenthetical qualifications. The specific regulatory citations. The "actually, the mechanism is..." framing that requires genuine understanding. AI generates confident declarative statements; patio11 generates conditional, precisely-scoped statements with acknowledged edge cases.

---

### 1.2 Patrick Collison (@patrickc) -- Stripe CEO / Payments

**Background**: CEO of Stripe. Reads more history than business. Tweets infrequently but each tweet carries unusual payload.

**Characteristic writing moves**:

- Analogies that compress entire theses: "Stablecoins are room-temperature superconductors for financial services"
- When announcing Stripe's blockchain Tempo, he wrote that Stripe had been "disappointed with crypto's payments utility for much of the past decade" -- a rare admission of prior skepticism from a CEO now investing heavily
- Lists specifics when making claims: cited five distinct reasons companies prefer stablecoins (near-instant settlement reducing trapped liquidity, lower costs than card payments, greater reliability in cross-border transfers, fewer currency conversions, direct on-chain access to US dollars)
- Compared Tempo to "decentralized, internet-scale SWIFT" -- dense because it requires knowing what SWIFT is and why that comparison is both ambitious and technically precise

**What makes his voice distinct**:

- Prizes "rigour and clarity of thought rather than smoothness"
- Prefers correctness over cohesion
- "At times more history professor than CEO"
- Does not use superlatives. Does not use empty hype language. States what something is and what it does.

**Why this does not read like AI**: The willingness to say "we were disappointed" about crypto for a decade. AI-generated CEO content would never include retrospective skepticism alongside current investment. The analogy itself ("room-temperature superconductors") is weird and specific enough to be human -- AI would default to "game-changer" or "paradigm shift."

---

### 1.3 Nic Carter (@nic\_\_carter) -- Bitcoin Analytics / Proof of Reserves

**Background**: Partner at Castle Island Ventures, co-founder of Coin Metrics. Former first crypto analyst at Fidelity Digital Assets. ~350K followers.

**What makes his writing dense**:

- Created the field of exchange proof-of-reserves scoring: rated exchanges on parameters like third-party auditor involvement, disclosure of liabilities alongside assets, commitment to ongoing attestation
- Scored Binance's first proof-of-reserves attempt as failing because "it only covers Bitcoin, which only represents 16.5% of their client assets"
- On Bitcoin mining: parsed all coinbase outputs across Bitcoin's 600K+ blocks to identify miner prevalence at the most granular level, showing that ~71% of mining was in China (4Q19-2Q20) concentrated in four provinces
- Tracked Bitcoin electricity consumption to specific numbers: "peaked at around 92 terawatt hours on an annualized basis in March 2021, then drew down because China's mining ban took 50% of Bitcoin's hash rate offline"

**Characteristic writing moves**:

- Leads with data, not opinion
- Names specific exchanges, specific percentages, specific time periods
- When critiquing a position, cites the exact methodology he disagrees with and explains why
- Long-form blog posts on Medium read like research papers but written in conversational tone
- Defends positions with data when challenged, not with rhetoric

**Why this does not read like AI**: The specificity is impossible to fake. "16.5% of their client assets" -- that requires having run the numbers on Binance's actual asset distribution. "Four provinces -- Xinjiang, Sichuan, Inner Mongolia, and Yunnan -- produced 63% of the global Bitcoin hashrate" -- AI would say "most mining was concentrated in China," not name the provinces and give the percentage.

---

### 1.4 Austin Campbell (@CampbellJAustin) -- Stablecoin Regulation

**Background**: Adjunct professor at Columbia Business School and NYU Stern. Former stable value trading at JP Morgan, co-head of Digital Assets Rates Trading at Citi, head of Portfolio Management at Paxos. Now Head of Strategy at WSPN. Two decades trading catastrophe bonds, mortality swaps, and BOLI wraps before crypto.

**What makes his writing dense**:

- Wrote a viral thread (April 2025) titled "INTEREST BEARING STABLECOINS (or Old Banker Yells at Cloud)" dissecting the GENIUS Act and Stable Act implications for yield-bearing stablecoins
- Positions himself as someone who has actually read the proposed legislation and compares it against how banking regulation actually works
- His framing: banks say interest-bearing stablecoins are "bad" -- he asks "bad for whom?" and then unpacks the competitive dynamics
- Specific technical knowledge: the difference between stablecoin issuers earning yield on reserves vs. passing yield to holders, and why banks lobby against the latter
- Explains that under the GENIUS Act, stablecoin issuers "can't outright [pay interest] directly, they can on exchanges" -- a level of regulatory nuance that requires reading the actual bill text

**Characteristic writing moves**:

- Self-deprecating headers ("Old Banker Yells at Cloud")
- Frames arguments as questions first ("bad for whom?") before presenting analysis
- Draws on TradFi background to contextualize crypto regulation -- compares stablecoin reserves to money market fund mechanics
- Uses professional jargon naturally: "stable value," "BOLI wraps," "cat bonds" -- these are not explained because his audience knows what they are
- States opinions with conviction but acknowledges where reasonable people disagree

**Why this does not read like AI**: The biographical specificity. AI cannot credibly claim to have traded mortality swaps at JP Morgan. The regulatory analysis requires having read the GENIUS Act, not a summary. The phrase "Old Banker Yells at Cloud" signals self-awareness that AI does not generate.

---

### 1.5 Vitalik Buterin (@VitalikButerin) -- Ethereum Protocol Design

**Background**: Ethereum co-founder. Posts long technical threads and blog posts on protocol design, mechanism economics, and scaling.

**What makes his writing dense**:

- Specific calculations embedded in explanations: "With EIP-4844, we now have 3 blobs per slot, or a data bandwidth of 384 kB per slot. Quick napkin math suggests that this is 32 kB per second, and each transaction takes about 150 bytes onchain, so we get ~210 tx/sec."
- February 2026 post on state scaling: "Current state grows at 100 GB annually, and a 20x increase would create 2 TB yearly growth. After four years, this results in 8 TB total state size that builders must maintain."
- Blunt technical assertions: "If you create a 10000 TPS EVM where its connection to L1 is mediated by a multisig bridge, then you are not scaling Ethereum."
- Proposes concrete solutions: "The most practical path for Ethereum may actually be to scale existing state only a medium amount, and at the same time introduce newer forms of state" -- temporary storage that resets monthly and UTXO-based systems

**Characteristic writing moves**:

- "Quick napkin math" framing -- shows the work, invites verification
- Uses specific EIP numbers (EIP-4844, EIP-7999, EIP-4444) without explanation because his audience tracks them
- Conditional language when uncertain: "may actually be" rather than "is"
- Critiques his own ecosystem directly: L2s "no longer make sense" in current form
- Blog posts at vitalik.eth.limo are 3000-5000 words of dense technical argument

**Why this does not read like AI**: The self-critique. The conditional uncertainty. The napkin math that shows work. AI generates confident assertions; Vitalik generates proposals with explicit uncertainty ranges and invitations to challenge.

---

## PART 2: TIER-2 ACCOUNTS (High Density, Different Styles)

### 2.1 Adam Cochran (@adamscochran) -- "The Threadooor"

**Background**: Managing partner at Cinneamhain Ventures. Known as the "notorious threadooor" for viral long-form tweet threads.

**Why he matters for voice study**:

- Writes threads structured like research memos: thesis, evidence, counter-evidence, conclusion
- Focus on how systems fail in practice -- incentive misalignment, governance failures, disclosure gaps
- His FTX thread used on-chain analysis to trace specific wallet movements and expose lies before the story fully broke
- Frames risk as outcome of incentives rather than purely technical design
- The Defiant literally calls him "The Everything Expert" -- the breadth of his analysis (centralized exchange risk, market structure, leverage, stablecoins, settlement rails, governance) is the signal

**Density indicator**: Publishes threads that other analysts spend days unpacking.

---

### 2.2 Dave White (@_Dave\_\_White_) -- Paradigm Research

**Background**: Research partner at Paradigm. Former quantitative trader at Headlands, Two Sigma, and Cutler Group. Three credits shy of a Harvard math A.B.

**Why he matters for voice study**:

- Invents financial primitives and announces them on Twitter: power perpetuals, TWAMM (time-weighted average market maker), squeeth
- His power perpetuals tweet: "If the price of ETH doubles, the ETH^2 power perp 4Xs, the ETH^3 power perp 8Xs, and the ETH^5 power perp 32Xs."
- "Power perpetuals provide global options-like exposure without the need for either strikes or expiries" -- this is a one-sentence description of a genuinely novel financial product
- Names products with personality: "squeeth" (squared ETH) -- shows a human behind the math
- TWAMM: "enables the on-chain equivalent of the TWAP order by breaking long-term orders into infinitely many infinitely small pieces and executing them smoothly against its embedded AMM over time"

**Density indicator**: Each tweet thread announces research that would be a paper at a traditional institution. The information-per-word ratio is probably the highest of anyone on this list.

---

### 2.3 Haseeb Qureshi (@hosseeb) -- Dragonfly Capital

**Background**: Managing partner at Dragonfly, a global crypto investment fund. Former software engineer. Published crypto security vulnerability in Bancor (early DeFi protocol).

**Why he matters for voice study**:

- His 2025 crypto predictions thread opens: "I'm either going to look like a prophet or an idiot over these predictions, but one thing is for sure: I'm going to piss off a lot of people with bags"
- This opening is dense with voice: self-deprecation, stakes-setting, acknowledgment that predictions are fundamentally about conviction under uncertainty
- Describes his own analysis as "the fuzziest blockchain valuation" -- without "fancy metrics or charts"
- Argues against prevailing CT sentiment frequently -- contrarianism as methodology, not personality
- On Monad launch (2026): "I used to tell founders, the reaction you are going to get to your launch is not hate, it's indifference. By default, nobody cares about your new chain. I have to stop telling them that now."

**Density indicator**: The Monad observation packs three insights into three sentences: (1) the historical default was indifference to new chains, (2) something changed, (3) the meta-observation that his own advice is now outdated.

---

### 2.4 Jon Wu (@jonwu\_) -- Aztec Network / Privacy + DeFi

**Background**: Head of growth at Aztec, a privacy-preserving Layer 2 for Ethereum. Known for "consistently cogent content on everything from encryption and privacy to DeFi and finance to civil liberties."

**Why he matters for voice study**:

- Guest post explaining the Terra/UST/Luna collapse was widely cited as one of the clearest breakdowns
- Describes Aztec Connect as "a VPN for Ethereum" -- compresses a complex zero-knowledge proof bridge into one phrase that a technical reader can unpack
- Specific savings metrics: "Users save 80-90% on gas fees with privacy thrown in for free"
- Thread on privacy coins (March 2022): "I'm clearly very biased but I'm long privacy networks like @aztecnetwork over privacy coins like $XHR and $ZEC and mixers like @tornadocash" -- declares bias, then makes the case anyway
- Frames privacy technology through civil liberties lens, not just tech capability

**Density indicator**: The "VPN for Ethereum" compression -- one metaphor that communicates: it's a layer between you and the public chain, it obscures your identity, it's a tunnel. Four concepts in three words.

---

### 2.5 Hasu (@hasufl) -- Flashbots / Paradigm

**Background**: Strategy lead at Flashbots, research collaborator at Paradigm, general editor at Deribit Insights. Co-hosted Uncommon Core podcast with Su Zhu.

**Why he matters for voice study**:

- Known for "crystallizing crypto ideas, tying things back to traditional finance, and generally being very articulate"
- Explores crypto "from first principles" -- Uncommon Core tagline
- Bridges MEV (maximal extractable value) research with practical market structure implications
- Writing style is the "smart colleague explaining over coffee" archetype: informal register, precise content
- Treats complex topics like MEV as worth sustained attention, not one-off hot takes

---

### 2.6 Lyn Alden (@LynAldenContact) -- Macro + Stablecoin Analysis

**Background**: Founder of Lyn Alden Investment Strategy. Engineering and finance background. 695K followers.

**Why she matters for voice study**:

- Combines macro analysis (fiscal deficits, monetary policy, credit cycles) with specific crypto implications
- Warned about Luna/UST before collapse by distinguishing between fiat-backed and algorithmic stablecoins -- a technical distinction most commentators missed
- Tracks stablecoins as "dollar rails outside the traditional banking stack" -- frames them as monetary infrastructure, not speculative assets
- Explains complex financial concepts "in an accessible manner" without dumbing down -- the rare skill of removing jargon while preserving mechanism
- First-principles reasoning from engineering background: treats financial systems as systems to be analyzed, not narratives to be promoted

---

### 2.7 Matt Levine (@matt_levine) -- Bloomberg Money Stuff

**Background**: Bloomberg Opinion columnist. Former Goldman Sachs investment banker and mergers lawyer. Harvard math.

**Why he matters for voice study**:

- "No specific jokes, but the whole text reads humorously" -- humor emerges from the absurdity of the facts, not from crafted punchlines
- "I'm never going to be the guy who knows the most details about litigation or finance. What I can do is write something that rings true to the specialists and is accurate but that reframes and conceptualizes it in a way where people who do it can be like, 'I didn't think about it that way because I'm in the weeds of it.'"
- Returns to the same topic over time, "building on readers' knowledge, as though they are learning a new language"
- Approaches ideas "in a low-stakes manner" -- can point to interesting subjects without providing one definitive take
- "Distills complex phenomena into simpler explanations" while "hunting down minute details, posing questions few other people would consider"

**The Levine voice formula**: Take a complex financial/legal situation. Describe what happened factually. Point out the absurd implication that everyone in the industry already knows but nobody has articulated this way. Move to the next item.

---

### 2.8 Byrne Hobart (@ByrneHobart) -- The Diff Newsletter

**Background**: Writer and consultant. CFA. Former crypto and fintech analyst for hedge funds. Publishes The Diff five days a week.

**Why he matters for voice study**:

- "One of Silicon Valley's most popular newsletters, read by basically the who's who of Silicon Valley"
- "Insights-to-words ratio is off the charts"
- "Masterfully fuses domains as diverse as economics, technology and sociology into each of his financial analyses"
- Equity research approach: uses complex datasets to understand company fundamentals
- The density comes from cross-domain synthesis -- a single paragraph might reference an economics paper, a code library, and a historical parallel

---

### 2.9 Marc Rubinstein (@MarcRuby) -- Net Interest Newsletter

**Background**: Former hedge fund partner (25+ years analyzing financial services). Launched Net Interest after retiring from Lansdowne Partners.

**Why he matters for voice study**:

- "A master of making the complex world of finance legible and interesting"
- Cited in UK Parliamentary hearings and by global banking regulators -- the audience is literally policymakers
- Covers fintech, macrofinance, financial crisis retrospectives, credit cycles
- Angel investor in Revolut, iwoca -- has skin in the game, which informs the analysis
- Weekly cadence, deep research, academic rigor but narrative accessibility

---

### 2.10 Gabor Gurbacs (@gaborgurbacs) -- VanEck Digital Assets

**Background**: Director of Digital Assets Strategy at VanEck. Built the first industry-standard digital asset indices. Filed for the first futures-based Bitcoin ETF.

**Why he matters for voice study**:

- Straddles institutional finance and crypto -- tweets about regulatory filings, ETF mechanics, index construction
- "Conversations around stablecoins and how money market instruments will be reformed"
- Tracked stablecoin market cap growth "from $0 to $34 billion in five years" (at time of earlier analysis)
- Speaks the language of both SEC filings and protocol design

---

## PART 3: ADDITIONAL HIGH-SIGNAL ACCOUNTS

### Infrastructure / Payments

| Handle                      | Name                        | Signal Type                                                                                                                                     |
| --------------------------- | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| @saboripay (Simon Taylor)   | Fintech Brainfood           | Weekly newsletter, 45K+ readers at banks/fintechs/VCs. Former Barclays blockchain R&D lead. Two decades in payments. Dense operational insight. |
| @AlexH_Johnson              | Alex Johnson, Fintech Takes | Former credit expert, 50K+ fintech professionals. Intersection of financial services, technology, and public policy. Twice-weekly analysis.     |
| @immaborishi (Immad Akhund) | Mercury CEO                 | Founder of Mercury banking platform. Cambridge CS. 350+ angel investments. Tweets about banking infrastructure from the builder's perspective.  |

### Crypto / Protocol

| Handle         | Name                          | Signal Type                                                                                                                                      |
| -------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| @DoveyWan      | Dovey Wan, Primitive Ventures | Founding partner. Deep analytical perspective on Asian crypto markets. Portfolio includes Dfinity, Kyber, Cosmos, StarkWare.                     |
| @0xHamz        | Anonymous                     | Former Goldman. Breaks down leverage structures, market microstructure, and exchange risk in detailed threads.                                   |
| @zackvoell     | Zack Voell                    | Weekend Editor at The Block. Former Messari and Blockstream. Bitcoin mining expertise. Self-describes as "mercenary wordcel and market taker."   |
| @samkazemian   | Sam Kazemian                  | Frax founder. Tweets about DeFi governance, protocol economics, stablecoin design from the builder's seat.                                       |
| @JasonYanowitz | Jason Yanowitz, Blockworks    | Co-founded Blockworks. Goes "very deep and niche" -- entire podcast seasons on MEV.                                                              |
| @molly0xFFF    | Molly White                   | Software engineer and crypto skeptic. Web3 Is Going Just Great. Advises policymakers and regulators. Technical criticism with specific evidence. |

---

## PART 4: WHAT MAKES THEIR WRITING FEEL DIFFERENT FROM AI/CONTENT CREATORS

### 4.1 The Vocabulary Signature

**Content creator vocabulary**:

- "game-changer," "unlock," "level up," "mindset shift," "10x," "powerful," "crushing it"
- Abstract nouns: "growth," "value," "purpose," "impact," "freedom"
- Verbs: "master," "dominate," "scale," "leverage"

**Domain expert vocabulary**:

- Specific regulatory references: "Reg E," "GENIUS Act Section 4(b)," "Durbin amendment," "EIP-4844"
- Precise financial terms used without definition: "interchange," "basis points," "perpetuals," "gamma," "attestation"
- System-level language: "settlement," "batch processing," "hashrate," "coinbase outputs," "Merkle branches"
- Qualifiers that signal precision: "on an annualized basis," "net of fees," "in the 4Q19-2Q20 period"

**The difference**: Content creators use words that make feelings. Domain experts use words that point to specific things in the world.

### 4.2 Argument Structure

**Content creator structure**:

1. Bold claim (hook)
2. Personal anecdote proving the claim
3. 3-5 bullet points elaborating
4. Call to action / restate claim

**Domain expert structure**:

1. Observation about a specific situation (often: "people misunderstand X")
2. Explanation of how the mechanism actually works
3. Evidence -- specific data, specific filing, specific code, specific on-chain activity
4. Implications that follow from the mechanism, not from the author's feelings
5. Acknowledged uncertainty or limitations
6. (Optional) What to watch for next

**The difference**: Content creators argue from assertion to evidence. Domain experts argue from evidence to implication.

### 4.3 Tone Calibration

**Content creator tone**: Certain. Motivational. Slightly performative urgency. "You need to understand this." "Most people don't know..." "This will change everything."

**Domain expert tone**: Curious. Analytical. Professionally opinionated but self-aware about limitations.

- "I think X, but I could be wrong about Y"
- "This is how it works, which is weird because..."
- "The data suggests X, though the sample is limited"
- "I'm clearly very biased but..." (Jon Wu)
- "I'm either going to look like a prophet or an idiot" (Haseeb)

**The difference**: Content creators never express genuine uncertainty because it weakens the hook. Domain experts express uncertainty because it strengthens their credibility.

### 4.4 Handling Complexity

**Content creator approach**: Simplify aggressively. Remove nuance. Make it "accessible." The reader should feel smart after reading.

**Domain expert approach**: Compress without simplifying. Use precise jargon that serves as lossy compression for shared knowledge. Trust the reader to either know the term or look it up. The reader should know more after reading, whether or not they feel smart.

**Example comparison on the same topic -- stablecoins**:

Content creator version:

> "Stablecoins are going to revolutionize payments. Here's why this matters for your money. Most people don't realize that every time you send money internationally, you're losing 3-5% to hidden fees. Stablecoins fix this. They're instant. They're cheap. They're the future. Save this post."

Domain expert version (Austin Campbell style):

> "The GENIUS Act prohibits direct interest payments on stablecoins but permits exchanges to offer yield on stablecoin balances. This creates a structural arbitrage: issuers earn treasury yield on reserves but can't share it directly with holders, so the yield accrues through intermediaries. Banks lobbied hard for this provision because pass-through yield would compete directly with demand deposits. The question is whether synthetic yield via exchanges achieves the same economic result the prohibition intended to prevent."

The content creator version has ~100 words and zero specific claims that could be verified or falsified. The domain expert version has ~80 words and contains at least five specific, falsifiable assertions: the GENIUS Act prohibition, the exchange yield exception, the treasury yield mechanism, the bank lobbying claim, and the demand deposit competition analysis.

### 4.5 The "Smart Colleague" Voice -- Specific Signatures

What distinguishes the "DM to a smart friend" voice from a "LinkedIn post":

1. **Mid-sentence qualifications**: "which, to be fair, is exactly what you'd expect given..." -- shows real-time thinking
2. **Jargon used as shorthand, not as signaling**: When patio11 says "interchange" he means the specific fee structure, not a buzzword
3. **Incomplete thoughts acknowledged**: "I haven't fully worked this out, but..." or "Quick napkin math suggests..."
4. **In-group references without explanation**: "the Durbin exemption," "EIP-4844," "squeeth" -- if you know, you know; if you don't, that's not the target audience
5. **Opinions stated as personal positions, not universal truths**: "I think the most practical path..." vs. "The future is..."
6. **Self-deprecation that's genuine, not strategic**: "Old Banker Yells at Cloud" (Campbell), "the fuzziest blockchain valuation" (Haseeb), "I used to tell founders... I have to stop telling them that now" (Haseeb)
7. **Willingness to be wrong in public**: Vitalik: "the rollup-centric roadmap no longer makes sense" -- publicly revising his own prior framework
8. **The parenthetical aside**: "(which only represents 16.5% of their client assets)" -- the information in parentheses often carries the most weight

---

## PART 5: SYNTHESIZED WRITING PRINCIPLES FROM THESE ACCOUNTS

### Principle 1: Lead with Mechanism, Not Outcome

Bad: "Stablecoins will transform payments"
Good: "Stablecoins reduce settlement from T+2 to T+0, which means 48 hours of trapped liquidity per transaction is freed"

### Principle 2: Specificity Is Credibility

Bad: "Most exchanges lack proper reserves"
Good: "Binance's first proof-of-reserves only covered Bitcoin, which represents 16.5% of their client assets, and used no third-party auditor"

### Principle 3: Acknowledge Your Position

Bad: "Here's the objective truth about privacy coins"
Good: "I'm clearly very biased but I'm long privacy networks over privacy coins -- here's the tradeoff analysis"

### Principle 4: Compress, Don't Simplify

Bad: "Think of it like a VPN but for money" (loses precision)
Good: "Aztec Connect is a VPN for Ethereum -- users bring privacy-shielded zk-assets on Aztec to public DeFi protocols on Ethereum" (compressed but technically complete)

### Principle 5: Show Your Work

Bad: "Ethereum can handle about 200 transactions per second"
Good: "With EIP-4844, we have 3 blobs per slot, 384 kB per slot, ~32 kB/sec, ~150 bytes per transaction on-chain, so ~210 tx/sec"

### Principle 6: Let the Absurdity Speak

Matt Levine's approach: describe what happened factually, and the absurdity emerges without editorializing. The humor is in the system, not in the commentary.

### Principle 7: Use Conditional Language for Genuine Uncertainty

Bad: "Ethereum WILL scale to 100K TPS"
Good: "The most practical path may actually be to scale existing state only a medium amount, and at the same time introduce newer forms of state"

### Principle 8: Time-Stamp Your Knowledge

"At time of writing," "in the 4Q19-2Q20 period," "peaked at ~92 TWh annualized in March 2021" -- domain experts anchor claims to specific moments because they know data changes.

---

## PART 6: THE AI DETECTION HEURISTIC

How readers subconsciously distinguish human domain experts from AI-generated content:

### Signals of Human Expert Writing

1. **Asymmetric sentence structure**: "A short sentence pulls focus. A longer one spills a memory and lets it breathe." -- controlled roughness
2. **Concrete specificity**: Names, places, numbers, regulatory filing numbers, EIP numbers, specific exchange names
3. **Intentional imperfection**: One clause longer than the other. Strategic gaps. Thoughts that trail off with "but I haven't fully worked this out"
4. **Emotional judgment over efficiency**: The writer "pauses for tone or empathy, even when it slows the flow"
5. **Biographical anchoring**: "I ran stable value trading at JP Morgan" -- a claim that positions the analysis within lived experience
6. **Retrospective self-correction**: "I used to tell founders X. I have to stop telling them that now" -- shows evolving thought
7. **The weird analogy**: "Room-temperature superconductors for financial services" -- too strange and specific for AI default generation

### Signals of AI-Generated Content

1. **Steady, predictable rhythm**: Every sentence roughly the same length
2. **Generality where specificity would prove the point**: "Many exchanges" instead of "Binance"
3. **No genuine uncertainty**: Everything stated with uniform confidence
4. **No biographical positioning**: No "when I was at..." or "in my experience..."
5. **Absence of self-correction**: Never revises a prior position
6. **Conventional metaphors**: "Game-changer," "paradigm shift," "unlock"
7. **Smooth completion over honest gaps**: AI fills every gap; humans leave acknowledged holes

As the research on AI vs. human writing authenticity puts it: "Machines can assemble tidy sentences and fill space with confidence. Humans share judgment and experience." Readers detect presence -- the sense of a person weighing decisions -- which machines struggle to convincingly fake.

---

## PART 7: PRACTICAL TAXONOMY -- WHICH VOICE FOR WHICH CONTENT

| Content Type                                      | Best Model Voice               | Why                                                                         |
| ------------------------------------------------- | ------------------------------ | --------------------------------------------------------------------------- |
| Stablecoin regulation analysis                    | Austin Campbell                | Regulatory precision + TradFi context + irreverent tone                     |
| Payments infrastructure explainer                 | patio11 (Patrick McKenzie)     | Systems thinking + specific numbers + "how it actually works" framing       |
| Protocol mechanism design                         | Vitalik / Dave White           | Mathematical precision + napkin math + conditional proposals                |
| Market structure / risk analysis                  | Adam Cochran / Nic Carter      | On-chain evidence + incentive analysis + data-driven conclusions            |
| Cross-domain synthesis (finance + tech + culture) | Byrne Hobart / Matt Levine     | Domain-fusion + absurdist factual humor + reframing                         |
| Macro + crypto intersection                       | Lyn Alden                      | Engineering-first-principles + macro context + stablecoin as infrastructure |
| Privacy / ZK technology                           | Jon Wu / Hasu                  | Metaphor compression + civil liberties framing + first-principles reasoning |
| Crypto skepticism / accountability                | Molly White                    | Evidence-based criticism + technical credibility + regulatory advisory      |
| Fintech business analysis                         | Marc Rubinstein / Alex Johnson | Institutional perspective + investment insight + weekly depth               |

---

## SOURCES

- [ConsenSys: 40 Crypto Twitter Accounts That Really Matter](https://consensys.io/blog/i-read-crypto-twitter-for-hours-daily-here-are-the-40-accounts-that-really-matter)
- [Bits about Money by Patrick McKenzie](https://www.bitsaboutmoney.com/)
- [Nic Carter - Blogs](https://niccarter.info/blogs/)
- [Austin Campbell on CoinDesk](https://www.coindesk.com/author/austin-campbell)
- [Austin Campbell: Interest Bearing Stablecoins Thread](https://x.com/CampbellJAustin/status/1917581563598102830)
- [Patrick Collison: Stablecoins Tweet](https://x.com/patrickc/status/1848393059559502177)
- [Dave White - Paradigm Team](https://www.paradigm.xyz/team/dave-white)
- [Dave White Power Perpetuals Thread](https://threadreaderapp.com/thread/1427652305009004545.html)
- [Haseeb Qureshi 2025 Crypto Predictions](https://x.com/hosseeb/status/1874288532686295058)
- [Adam Cochran - CryptoSlate Profile](https://cryptoslate.com/people/adam-cochran/)
- [Lyn Alden Investment Strategy](https://www.lynalden.com/)
- [Marc Rubinstein - Net Interest](https://www.netinterest.co/)
- [Byrne Hobart - The Diff](https://www.thediff.co/)
- [Matt Levine - Bloomberg](https://www.bloomberg.com/opinion/authors/ARbTQlRLRjE/matthew-s-levine)
- [Harvard Magazine on Matt Levine](https://www.harvardmagazine.com/2025/07/harvard-bloomberg-column-matt-levine)
- [Alex Johnson - Fintech Takes](https://fintechtakes.com/)
- [Simon Taylor - Fintech Brainfood](https://ffnews.com/people/simon-taylor/)
- [Gabor Gurbacs - VanEck](https://vaneck.com/us/en/news-and-insights/thought-leaders/gabor-gurbacs/)
- [Jon Wu on Privacy Coins](https://x.com/jonwu_/status/1501383868351279107)
- [Molly White](https://www.mollywhite.net/)
- [Vitalik Buterin - Scaling Ethereum L1 and L2s](https://vitalik.eth.limo/general/2025/01/23/l1l2future.html)
- [AI Writing vs Human Writing: Signals of Authenticity](https://thedatascientist.com/ai-writing-vs-human-writing-authenticity/)
- [The Defiant: Adam Cochran - The Everything Expert](https://blockspace.media/podcast/adam-cochran-the-everything-expert/)
- [Zack Voell - Muck Rack](https://muckrack.com/zack-voell)
- [Uncommon Core Podcast](https://uncommoncore.co/)
- [Patrick Collison on Stripe Tempo](https://x.com/patrickc/status/1963638753752420407)
- [Ledn: Top 16 Crypto X Accounts](https://www.ledn.io/post/best-crypto-x-accounts)
