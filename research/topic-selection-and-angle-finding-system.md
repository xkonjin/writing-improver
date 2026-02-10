# Topic Selection & Angle-Finding System

## How Elite Newsletter Writers Pick Topics, Find Novel Angles, and Write What's Culturally Resonant

**Context:** Designed for Jin Fernando's stablecoin/payments/fintech/AI newsletter. The goal: write pieces that feel current (about what people are ALREADY thinking about) but with a genuinely novel angle that reframes how they see it.

---

## Table of Contents

1. [How Top Newsletter Writers Pick Topics](#1-how-top-newsletter-writers-pick-topics)
2. [Narrative Economics: How Stories Spread and Stick](#2-narrative-economics-how-stories-spread-and-stick)
3. [Cultural Zeitgeist Tracking: Tools and Methods](#3-cultural-zeitgeist-tracking-tools-and-methods)
4. [The Angle Selection Problem](#4-the-angle-selection-problem)
5. [Timeliness vs. Timelessness: The Thompson Pattern](#5-timeliness-vs-timelessness-the-thompson-pattern)
6. [Tools, APIs, and Systems for Real-Time Topic Identification](#6-tools-apis-and-systems-for-real-time-topic-identification)
7. [The Integrated System: How This All Works Together](#7-the-integrated-system-how-this-all-works-together)

---

## 1. How Top Newsletter Writers Pick Topics

### Ben Thompson (Stratechery)

**The Process, Concretely:**

Thompson wakes up early, scans all the headlines and everything that happened the day before. Running through his head is an outline of what he will probably write about that day. For his weekly articles, he usually knows the topic several days in advance -- for instance, he knew he would write about Zuckerberg's congressional testimony well ahead of time, and when Microsoft reorganized on a Thursday, he immediately knew it would be his topic the following week.

The middle part of his day is spent reading, being on Twitter, and exploring various sources. He lets ideas percolate, thinking about what points he will make and what his angle is. Then in mid-afternoon, "the necessary dose of sheer panic and terror" that his deadline is in 3-4 hours forces him to buckle down and write for publication by 6-7 PM.

**The Selection Filter:**

Thompson identified a gap nobody else was filling: "There's lots of sites writing about the products. Wall Street is writing about the financial results, but there's a big gap in the middle there. What is the strategy that goes into the products?" Every topic he selects is filtered through this lens: does this news event have a strategic implication that nobody else is explaining?

He has said: "I think it's a very distinct skill and capability to come up with interesting things consistently." His system is not random curiosity. He applies known frameworks (Aggregation Theory, the Smiling Curve, platform dynamics) to whatever news surfaces, and the topic becomes interesting when the framework reveals something non-obvious about the news.

**His "strong opinions, weakly held" approach:** He writes with authority but always tests the underlying assumptions. He says having a systematic view of the world is very beneficial because his nature is to challenge assumptions rather than just look at outcomes.

**How We Could Implement This:**

- **Step:** During the daily intelligence scan (see Section 7), filter every news item through a specific question: "What is the structural/strategic implication of this that nobody is explaining?"
- **Tools:** RSS feeds of tech/fintech news, Twitter/X lists of key analysts, Stratechery's own concepts page as a framework library
- **Application for Jin:** The equivalent gap for stablecoins is: "There are people reporting stablecoin news. There are crypto analysts. But nobody is explaining the strategic logic -- why this company made this decision, what second-order effects follow, what structural pattern this fits."

**Example in Practice:** When Stripe acquired Bridge, most coverage was "Stripe buys stablecoin company for $1.1B." Thompson's approach would be: "What does this acquisition tell us about where value is being created in payment infrastructure? Does this represent Aggregation Theory playing out in stablecoins?"

**Limitations:** Requires deep pre-existing frameworks to filter through. Without frameworks, you are just reacting to news like everyone else. The frameworks take years of thinking to develop, but they can be borrowed, adapted, and built upon.

---

### Matt Levine (Money Stuff)

**The Process, Concretely:**

Levine plucks about five financial news headlines each day and analyzes them through hypothetical conversations, thought experiments, footnotes, and snarky asides. He does not originate stories. He takes existing news, explains the context in plain language, and offers interpretations that both insiders and outsiders find meaningful.

He has extremely good contacts in the upper levels of finance. Those people inform his selection of topics. Over 13 years of writing, he has built a network where people leak to him, send him interesting things, and where his recurring themes have gained enough currency that readers "can now do much of the work of sourcing an issue for him."

**The Angle Machine:**

Levine's distinctive value is not being the most knowledgeable person on any given topic. As he puts it: "I'm never going to be the guy who knows the most details about litigation or finance. What I can do is write something that rings true to the specialists and is accurate but that reframes and conceptualizes it in a way where people who do it can be like, 'I didn't think about it that way because I'm in the weeds of it.'"

This is the core insight for angle selection: **the people closest to a topic are too deep in the weeds to see the conceptual pattern. The angle comes from being close enough to understand but far enough to reframe.**

**Recurring Themes as a Structural Technique:**

Levine uses named recurring themes as scaffolding. "Everything is securities fraud" -- where any time something bad happens at a public company, lawyers sue for securities fraud -- is not just a joke. It is a structural lens that reveals how American securities law absorbs all conduct into its framework. He returns to this theme hundreds of times, each time with a new example that reinforces and extends the concept.

Other recurring themes: "proximity to Elon Musk" (the idea that the most important factor in financial markets was closeness to Musk), "private markets are the new public markets," and crypto as "an amazing laboratory for understanding real finance."

His view on crypto as a writing exercise: "Crypto is an incredible writing exercise because it is new enough that he can quickly get readers up to speed but established enough to mimic ancient financial patterns." People rebuild schematic versions of existing financial structures in crypto, often "in a really dumb way," and then you can observe how they break -- which illuminates financial market intuitions.

**The Low-Stakes Iterative Return:**

The daily format allows him to point at interesting subjects without providing one definitive take. He returns to the same topic over time, building on readers' knowledge. This creates a spaced-repetition effect -- readers learn the pattern across many examples, and each new example reinforces the previous ones.

**How We Could Implement This:**

- **Step:** Develop 3-5 named recurring themes for the stablecoin/payments space (analogous to "everything is securities fraud"). See Section 4 for how to identify these.
- **Tools:** Keep a running document of every instance where a new news story maps to a recurring theme. Each time, add to the compounding knowledge.
- **Application for Jin:** Stablecoin equivalents might be: "Everything is a money market fund" (when every new stablecoin product is structurally identical to traditional money market instruments), "The compliance arbitrage" (regulatory asymmetries that determine where stablecoin activity concentrates), or "The reserve question" (every stablecoin crisis ultimately comes back to what's backing it).

**Example in Practice:** When USDC briefly depegged during the SVB collapse, Levine's approach would not be "USDC lost its peg." It would be: "Here is another example of 'the reserve question' -- the thing that matters about stablecoins is what's backing them, and this time the answer was 'a bank that just failed,' which is both terrifying and also kind of funny because the whole point of stablecoins was supposed to be not depending on banks."

**Limitations:** Requires daily frequency to build the compounding effect. Also requires genuinely deep domain knowledge -- Levine worked at Goldman Sachs and as a corporate lawyer before becoming a writer. As Gwern's "Why So Few Matt Levines?" essay argues, the rarity of Levine-like writers is structural: most fields are too slow or ambiguous, and writers with the right combination of expertise, obsession, and persistence are extremely rare. Finance is uniquely suited because events play out publicly and quickly, with legally mandated disclosures.

---

### Packy McCormick (Not Boring)

**The Process, Concretely:**

McCormick started by writing about everything -- links, book summaries, community content. The first 18 months were "all over the place." He found his lane when he came back to business strategy and finance, the things he was personally passionate about, but written in a fun, less serious way. His positioning: "If Ben Thompson and Bill Simmons had a baby, it would look like Not Boring."

His current topic selection is passion-driven with a collaborative twist. He talks to smart people -- founders, researchers, investors -- who are betting their prime years on ideas nobody else understands yet. His two most popular essays ever (_The Electric Slide_ and _Excel Never Dies_) were co-written with founders who had deep domain expertise.

His latest evolution is explicit: "We aim to write down ideas you can't find in an LLM. Our co-authors are figuring out new knowledge in real time, and they share it fresh, before they're even sure it's right, while the hypothesis is still being tested."

**The Selection Filter:**

McCormick advises: get really specific on the topic, and make sure it is something you love. He optimizes for going deep into a world where he can "meet more people, have more knowledgeable conversations, and enjoy it." He spends all his energy on writing great posts and hopes readers share them, rather than spending time on growth marketing.

**How We Could Implement This:**

- **Step:** Build a network of 10-15 "frontier practitioners" -- people actually building stablecoin/payments products, writing regulatory frameworks, or deploying capital -- and have regular conversations with them. The topics emerge from what they are thinking about.
- **Tools:** A structured interview/conversation cadence. Monthly calls with 3-4 practitioners. Record themes, not just quotes.
- **Application for Jin:** The "co-written with a practitioner" format maps directly. A piece co-written with a compliance officer at a stablecoin issuer about what the GENIUS Act actually means for day-to-day operations would have both insider credibility and accessibility.

**Limitations:** Requires network building that takes months to years. Early on, the network is thin. The founder co-writing model only works when you have enough audience that founders want the exposure.

---

### Byrne Hobart (The Diff)

**The Process, Concretely:**

Hobart reads voraciously -- books, news articles, SEC filings, academic papers. He has stated: "You will not learn anything of lasting importance from TV, movies, podcasts. The way serious people learn is by reading. The way they share important information is by writing it down. Read, read, read."

His topic generation methods:

1. **Reader feedback as a growth engine.** His backlog of posts to write is either growing or approaching zero, and "the best way for the backlog to grow is to get ideas and questions from readers." This creates a compounding network effect.

2. **Iterative expansion from past work.** "See an interesting pattern, write about it; find a case study of that pattern, write about that case study; see other interesting patterns in the case study, write about those." He explicitly notes: "This often takes the form of turning a footnote into a full article."

3. **Physical notebook backlog.** He maintains a running list of ideas in a physical notebook. He writes the easier ideas first while items requiring more research accumulate.

4. **Non-partisan, undecided topics.** He deliberately chooses topics where "nobody has picked a side yet." This prevents him from writing predictable takes.

5. **Writing what he wants to read.** "I wanted there to be a good article on the social impact of The Social Network, so I wrote one."

**The Anti-Timeliness Principle:**

This is what makes Hobart distinctive. His newsletter's goal is "not to be topical -- instead, it's to choose topics and framing that will be more relevant a year from now." His guiding question: "In a few centuries, when historians reach a consensus on what was happening today, what will they believe?"

The five links he includes in each piece are "not the five biggest news stories of the day, but five data points that illustrate long-term trends, refute them, or are widely reported but deeply misunderstood."

**The Writing Process:**

He writes drafts on airplane mode at maximum speed. His rule: if anything slows him down during draft one, he writes "TK" followed by a quick note about what he needs to add, then moves on. He finishes 1,000-2,000 words in 45 minutes this way, then goes back to fill in all the TKs.

**How We Could Implement This:**

- **Step:** After publishing each piece, mine it for 2-3 footnotes or asides that could be expanded into full pieces. Maintain a notebook (physical or digital) of these seeds.
- **Step:** For every trending stablecoin/fintech story, ask: "Will this matter in 12 months? If so, why? If not, what deeper pattern does it exemplify that WILL matter?"
- **Tools:** The "TK" drafting method for speed. The "five links" format for the curated intelligence section.
- **Application for Jin:** The "undecided topics" filter is powerful. When Circle's IPO was announced, most coverage was bullish or skeptical. The Hobart approach would be to find the structural question nobody had answered yet -- for example, "What does Circle's IPO filing reveal about the economics of being a regulated stablecoin issuer vs. an unregulated one?"

**Limitations:** The anti-timeliness approach can feel disconnected from what readers urgently care about today. It requires immense trust from readers that the payoff will come later. Also, the heavy-reading information diet (2+ hours/day of books, filings, papers) is a real time investment.

---

### Lenny Rachitsky (Lenny's Newsletter)

**The Process, Concretely:**

Lenny keeps a running list of about 50 topics he wants to write about and has a rough idea of what the next 2-3 posts will be. As each Tuesday approaches, he picks the topic he is most excited to write about that week.

His filtering principle: "I optimize for my own curiosity vs. what people want, because that always leads to the best stuff." He reiterates: "I pick the topic I'm most excited to write about this week (as I optimize for my own curiosity vs. what people want because it ends up being better that way, and I stay sane)."

He frames every post as a question, since it is an advice column. The post always starts with a concrete, simple, direct question from a reader. He regularly asks questions on Twitter to flesh out concepts and generate new ideas.

**How We Could Implement This:**

- **Step:** Maintain a running "topic backlog" of 30-50 ideas at all times. Every week, pick from it based on energy/excitement, not obligation.
- **Step:** Frame each newsletter edition as answering a specific question a reader or practitioner would actually ask. "How do stablecoin issuers actually make money?" not "The economics of stablecoin issuance."
- **Tools:** Reader question pipeline (from LinkedIn comments, DMs, Twitter replies).

**Limitations:** The curiosity-driven approach can produce inconsistent topics week to week. For a niche newsletter (stablecoins), there is less room to wander than Lenny has in the broader product/growth space.

---

### Synthesis: The Five Models Compared

| Writer    | Selection Method                       | Time Horizon                   | Angle Source                           | Frequency |
| --------- | -------------------------------------- | ------------------------------ | -------------------------------------- | --------- |
| Thompson  | Framework application to news          | Structural (weeks-months)      | Strategic gap nobody fills             | Daily     |
| Levine    | News + recurring theme mapping         | Today's events                 | Insider/outsider reframing             | Daily     |
| McCormick | Practitioner conversations + passion   | Deep dives (weeks of research) | Frontier knowledge from builders       | Weekly    |
| Hobart    | Heavy reading + iterative expansion    | 1+ years                       | Non-partisan undecided questions       | 4x/week   |
| Rachitsky | Curiosity-driven from reader questions | Tactical (this week)           | Practitioner answers to real questions | Weekly    |

**For Jin's newsletter, the recommended hybrid:**

- **Thompson's framework application** for the daily/weekly intelligence angle
- **Levine's recurring themes** to build compounding reader knowledge
- **McCormick's practitioner conversations** for frontier knowledge nobody else has
- **Hobart's anti-timeliness filter** to ensure structural depth
- **Rachitsky's reader question framing** for accessibility and engagement

---

## 2. Narrative Economics: How Stories Spread and Stick

### Robert Shiller's Framework, Operationalized

Shiller's core thesis: economic narratives spread like diseases. He adapted the Kermack-McKendrick (1927) epidemiological model -- the same math used to model disease outbreaks -- to explain how economic stories go viral and drive major economic events.

**The Seven Propositions of Narrative Economics:**

1. **Epidemics can be big or small.** Not every narrative becomes a pandemic. Most narrative "infections" stay small. Implication: Don't assume every trend you see will become dominant. Most won't.

2. **Important economic narratives may comprise a very small percentage of popular talk.** A narrative doesn't need to be known by everyone. It only needs to be accepted by a small number of people well positioned to "move" the society. Implication: Track what elite decision-makers (VCs, regulators, bank CEOs) are saying, not just what's trending on Twitter.

3. **Narrative constellations have more impact than any one narrative.** A collection of related narratives is more robust than a singleton. Implication: When you see multiple related narratives converging (e.g., "stablecoins are replacing correspondent banking" + "dollar hegemony is threatened" + "crypto regulation is coming"), the constellation is the real story, not any individual narrative.

4. **The economic impact of narratives may change through time.** The same narrative can be bullish in one era and bearish in another. Implication: Track how the framing of a narrative is shifting, not just whether it exists.

5. **Truth is not enough to stop false narratives.** Once a narrative achieves momentum, facts cannot stop it. Implication: If you are writing to correct a false narrative, pure factual debunking will not work. You need to provide a MORE compelling counter-narrative.

6. **Contagion builds on opportunities for repetition.** Narratives spread when they can be easily retold. Simplicity and repeatability are features, not bugs. Implication: Your framing must be simple enough to repeat. "Everything is securities fraud" works because it is five words.

7. **Narratives thrive on attachment: human interest, identity, and patriotism.** Stories that connect to identity spread faster than stories about abstract systems. Implication: A piece about "dollar hegemony and stablecoins" spreads less than a piece about "why your Uber driver in Lagos uses USDT to save money."

**Narrative Mutation:**

Shiller's most operationally useful insight: narratives mutate. Old narratives can be renewed by mutation, just like viruses. The "labor-saving machines replace jobs" narrative has re-emerged in different forms during every wave of automation -- the Luddite version, the 1960s automation anxiety version, and the current AI version. Each mutation makes an old narrative feel new.

**How To Apply This:**

For stablecoin/fintech content, the question becomes: which narrative constellations are currently active, and which are mutating?

Current active narrative constellations in stablecoins (as of early 2026):

- **"Stablecoins as the new dollar infrastructure"** -- GENIUS Act, bank entry, Stripe/Shopify integration, $33T in 2025 volume
- **"Crypto meets TradFi"** -- banks entering crypto, regulatory frameworks (MiCA, GENIUS), the cooperation-not-confrontation shift
- **"AI + crypto convergence"** -- 40 cents of every crypto VC dollar now goes to companies also building AI, agentic commerce protocols
- **"Dollar hegemony and digital money"** -- CBDCs vs. private stablecoins, BRICS alternatives, Tether's role in dollarizing emerging markets

Narratives that are mutating:

- **"Crypto is for criminals"** is mutating into **"crypto is now regulated but regulation might kill what made it interesting"**
- **"DeFi will replace banks"** is mutating into **"DeFi protocols are becoming banks"** (or "banks are becoming DeFi protocols")
- **"Stablecoins are just crypto trading tools"** has mutated into **"stablecoins are payments infrastructure"** -- this mutation is mostly complete

**How We Could Implement This:**

- **Step:** Maintain a "narrative tracking document" that lists the 5-7 active narrative constellations in the stablecoin space, with sub-narratives under each. Update monthly. Track which are peaking, emerging, mutating, or dying.
- **Tools:** Google Trends for volume signals, Twitter/X advanced search for elite discourse tracking, Reddit/HackerNews for retail sentiment
- **Concrete example:** In Q4 2025, the narrative "stablecoins are replacing correspondent banking" was emerging. By Q1 2026, it was peaking (Stripe/Bridge acquisition, $10T monthly volume in January). A piece written during the emerging phase would feel prescient. A piece written during the peak needs a twist -- perhaps "the thing that's NOT being discussed about stablecoins replacing correspondent banking is [X]."

**Failure Modes:**

- Confusing narrative popularity with narrative truth. A narrative can be viral and wrong.
- Chasing narratives that are already peaking. By the time everyone is talking about something, the angle space is saturated.
- Missing mutation. The most important narrative shifts happen when an old story gets a new frame, and these are easy to miss because the words sound familiar.

---

## 3. Cultural Zeitgeist Tracking: Tools and Methods

### Google Trends Analysis Patterns

**How It Works Concretely:**

Google Trends measures relative search interest over time. It does not show absolute search volume but rather normalized interest on a 0-100 scale. The key signals:

- **Rising queries:** Topics experiencing sudden spikes in search interest. These indicate what just entered public consciousness.
- **Breakout queries:** New terms that have spiked from near-zero. These indicate truly emerging concepts.
- **Comparing terms:** Plotting "stablecoin" vs "CBDC" vs "digital dollar" over time reveals which framing is winning the narrative war.
- **Geographic filtering:** Seeing where searches originate reveals adoption patterns (stablecoin searches from Nigeria, Argentina, Turkey tell a different story than searches from New York).

**For Our System:**

Run weekly Google Trends checks on 10-15 key terms: stablecoin, USDC, USDT, stablecoin regulation, GENIUS Act, crypto payments, digital dollar, CBDC, Circle IPO, Tether, cross-border payments, embedded finance, agentic payments. Track directional movement week-over-week.

**Limitations:** Google Trends is a lagging indicator for B2B topics. Institutional discussions about stablecoin infrastructure happen in Slack channels and boardrooms, not Google searches. It is more useful for retail/mainstream narrative tracking.

---

### Social Listening: What's Actually Being Discussed

**How It Works Concretely:**

Modern social listening goes beyond hashtag tracking. AI-powered tools now detect sentiment, emotional tone, sarcasm, and cultural context. The social listening market is projected to grow from $8.44B (2024) to $16.19B (2029), indicating massive investment in this capability.

**The Hierarchy of Social Platforms as Signals:**

| Platform                             | Signal Type                                | Lead Time                                                  | Reliability                                                                                |
| ------------------------------------ | ------------------------------------------ | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Twitter/X fintech elite              | What sophisticated thinkers are processing | 1-4 weeks ahead of mainstream                              | High for direction, low for timing                                                         |
| Reddit r/CryptoCurrency, r/Fintech   | Retail sentiment and confusion             | Real-time barometer of mass understanding                  | High for sentiment, low for accuracy                                                       |
| HackerNews                           | Technical community reaction               | 1-2 weeks ahead                                            | High for technical assessment, blind to non-technical factors                              |
| LinkedIn fintech influencers         | Professional consensus formation           | Lagging indicator, but shows what's becoming "safe" to say | High for B2B content timing -- when something hits LinkedIn, the mainstream window is open |
| Telegram/Discord channels            | Insider trading sentiment, whale movements | Real-time, but extremely noisy                             | Low reliability without filtering                                                          |
| Substack/newsletter cross-references | What other writers are covering            | Shows topic saturation vs. topic opportunity               | High -- if nobody is writing about X, there is room                                        |

**For Our System:**

- **Morning scan (15 min):** Check Twitter/X lists of 30-50 key fintech/crypto voices. What are they reacting to? What thread got unusually high engagement?
- **Weekly scan (30 min):** Check Reddit frontpages of r/CryptoCurrency, r/Fintech, r/Stablecoins. What questions are people asking? What confusions keep recurring?
- **HackerNews (as needed):** When a major fintech/stablecoin story hits HN, read the top 20 comments. The HN audience is technical and skeptical -- their objections reveal the steel-man case against any narrative.
- **LinkedIn (weekly):** When a stablecoin topic starts appearing on LinkedIn with "thought leader" framing, it has crossed into mainstream acceptability. This is the signal that a topic needs a twist, not a straight take.

---

### Overton Window Shifts

**How It Works Concretely:**

The Overton Window describes the range of ideas considered politically/socially acceptable at any given time. It shifts through a predictable sequence: Unthinkable -> Radical -> Acceptable -> Sensible -> Popular -> Policy.

**For Stablecoins:**

The Overton Window on stablecoins has shifted dramatically in 18 months:

- **2023:** "Stablecoins need strict regulation or banning" (popular/policy)
- **2024:** "Stablecoins could be useful if regulated properly" (acceptable -> sensible)
- **2025:** "Stablecoins are dollar infrastructure the US should encourage" (sensible -> popular)
- **2026:** "Banks should be allowed to issue stablecoins, and maybe they should pay yield" (radical -> acceptable)

**The content opportunity exists at the edges of the window.** Writing about ideas that are currently transitioning from "radical" to "acceptable" positions you as ahead of the curve when they become mainstream.

**For Our System:**

Track the Overton Window position of 5-10 key stablecoin propositions quarterly:

- "Stablecoins should pay yield" (currently: radical/acceptable boundary)
- "Tether is a systemic risk" (currently: acceptable but losing ground)
- "CBDCs are unnecessary because stablecoins do the job" (currently: acceptable/sensible)
- "Stablecoin issuers are the new banks" (currently: acceptable)
- "On-chain identity should replace KYC" (currently: radical)

Writing about propositions at the radical/acceptable boundary is where the highest engagement potential exists -- it feels provocative but not crazy.

---

### Reddit/HackerNews/Twitter as Leading Indicators

**The Key Insight:**

These platforms operate as leading indicators precisely because they capture unfiltered thinking. When a Reddit user asks "Why would I use USDC instead of just keeping dollars in my bank?" they are revealing a genuine gap in the mainstream understanding. When a HackerNews commenter says "The whole stablecoin thing is just recreating fractional reserve banking with extra steps," they are articulating a critique that will eventually reach mainstream financial media -- usually 2-4 weeks later.

**Research confirms this:** LLM-based sentiment analysis of HackerNews posts shows that 65% have negative sentiment and they tend to outperform in engagement. This means HN is a skepticism engine -- it surfaces objections and criticisms faster than any other platform.

**For Our System:**

Build a "question and objection harvester" that extracts:

- The top 5 questions being asked about stablecoins on Reddit each week
- The top 3 objections/criticisms on HackerNews when stablecoin stories surface
- The 2-3 Twitter threads that generated the most quote-tweets (indicating disagreement/debate)

These questions and objections are the raw material for angles. If everyone on Reddit is asking "But what happens to stablecoins if interest rates drop to zero?" -- that is a newsletter topic.

**Failure Modes:**

- Mistaking vocal minorities for consensus. Reddit and HN comments can be dominated by a small number of prolific commenters.
- The "negativity trap" -- HN skews skeptical about everything, which means you need to filter out reflexive negativity from substantive criticism.
- Platform-specific blindness. Twitter/X captures fintech insiders, Reddit captures retail, HN captures engineers. None captures regulators, banking executives, or compliance officers -- the people who actually make stablecoin policy. Those voices must be tracked through other channels (regulatory filings, conference transcripts, industry association publications).

---

## 4. The Angle Selection Problem

### Given a Topic Everyone Is Writing About, How Do You Find a Genuinely Different Perspective?

This is the hardest problem in content creation, and it has several systematic solutions:

---

### Method 1: The Problem/Gap/Hook Framework

**From academic writing, adapted for newsletters:**

1. **Problem:** Identify what people are talking about. (e.g., "Circle is going public")
2. **Gap:** What is everyone assuming but nobody is questioning? (e.g., "Everyone assumes the IPO will succeed because stablecoin adoption is growing, but nobody is examining what Circle's S-1 reveals about the actual unit economics of regulated stablecoin issuance")
3. **Hook:** Why does filling this gap matter? (e.g., "Because if Circle's economics don't work at scale, the entire thesis of 'stablecoins as infrastructure' needs to be revised")

**Concrete Application:**

For any trending stablecoin topic, run through these three questions:

- What is everyone saying about this? (Read the first 10 articles/tweets)
- What are they all assuming without stating? (The unstated premise)
- What happens if that assumption is wrong? (The hook)

The gap is almost always an unstated assumption. When the GENIUS Act passed, most coverage assumed it would accelerate stablecoin adoption. The gap: nobody examined whether the specific reserve requirements (T-bills with maturity less than or equal to 93 days) would create enough Treasury demand to matter for US debt markets. That is the angle.

---

### Method 2: The Levine Reframing

**The technique:** Take the specialized, insider version of a story and explain it in a way that reveals the conceptual pattern to outsiders -- while simultaneously making insiders see their own world differently.

Levine describes this as: writing "something that rings true to the specialists and is accurate but that reframes and conceptualizes it in a way where people who do it can be like, 'I didn't think about it that way because I'm in the weeds of it.'"

**Concrete Application:**

When everyone is writing about "stablecoin regulation is coming," the Levine reframe might be: "Stablecoin regulation is not about stablecoins. It is about which government agencies get to control the on-ramps to the digital dollar system. The GENIUS Act is a turf war disguised as consumer protection."

The technique: identify the second-level system dynamics that insiders are too close to see.

---

### Method 3: The Inversion (What If Everyone Is Wrong?)

**The technique:** State the consensus view explicitly, then systematically examine what would have to be true for it to be wrong.

This is NOT being contrarian for its own sake. The key distinction: contrarianism says "everyone believes X, so I believe not-X." Inversion says "everyone believes X -- let me examine the assumptions that would have to hold for X to be true, and check whether they actually hold."

**Concrete Application:**

Consensus: "Stablecoins will become the dominant form of cross-border payments."

Inversion questions:

- What would have to be true for this? (Low fees, fast settlement, regulatory acceptance globally, merchant willingness to accept, conversion infrastructure in every corridor)
- Which of these assumptions are weakest? (Regulatory acceptance globally -- most countries have not passed stablecoin frameworks. Conversion infrastructure -- the "last mile" problem of converting stablecoins to local currency is unsolved in most markets.)
- What is the strongest version of the counter-argument? ("Cross-border payments will be improved by traditional rails upgrading (FedNow, Pix, UPI) faster than stablecoin infrastructure can be built.")

If the inversion produces a compelling counter-argument, you have found a genuinely novel angle. You don't have to agree with it -- you just have to present it honestly and let readers decide.

**Failure Modes:**

- Being contrarian for its own sake. If your inversion doesn't produce a substantive counter-argument backed by evidence, abandon it. Not every consensus is wrong.
- The "hot take" trap. Inversions that are designed to generate outrage rather than insight damage credibility. The test: would a thoughtful insider nod and say "that's a fair point" even if they disagree?

---

### Method 4: The Time-Shift

**The technique:** Take a current event and map it to a historical precedent that nobody is citing. Then use the historical precedent to predict what happens next.

**Concrete Application:**

Current event: The GENIUS Act requires stablecoin reserves to be held in T-bills.

Historical precedent: Regulation Q in the 1960s capped interest rates US banks could pay on deposits, which drove dollars offshore into the Eurodollar market. The US government eventually decided the Eurodollar market was useful because it kept dollars dominant globally.

The angle: "The GENIUS Act is this generation's Regulation Q. By raising compliance costs for onshore stablecoin issuers, it will drive activity offshore -- and the US government is probably okay with that, because offshore dollar stablecoins (Tether) still buy T-bills and still dollarize emerging markets."

This angle requires Track 4 (comparative/historical data) from the Insight Generation System that already exists in the codebase.

---

### Method 5: The Adjacent Domain Transfer

**The technique:** Take a well-understood principle from an adjacent domain and apply it to the current topic. The novelty comes from the cross-pollination.

**Concrete Application:**

Adjacent domain: Epidemiology (Shiller's approach).

Application: "Stablecoin adoption follows the same S-curve as disease transmission. The 'contagion rate' is driven by network effects -- each new user who accepts USDT makes USDT more useful for every other user. The 'recovery rate' is driven by regulatory action and competing alternatives. The current reproductive rate (R0) of USDT adoption in emerging markets is above 1, meaning adoption will continue accelerating until a critical mass of regulatory intervention raises the recovery rate above the contagion rate."

The adjacent domain gives you a vocabulary and a set of predictions that feel genuinely novel, even though the underlying facts are well-known.

---

### Method 6: The Gap-in-the-Conversation Audit

**The technique:** Systematically map what IS being said about a topic, then identify what is NOT being said.

**Concrete Steps:**

1. Read the 10 most recent articles/takes on the topic
2. List every claim, argument, and assertion made
3. For each assertion, ask: "What would someone who disagrees say? Who would disagree?"
4. Identify which stakeholders are NOT represented in the coverage
5. The missing stakeholders' perspective is your angle

**Concrete Application:**

Topic: "Banks entering crypto."

What's being said: Banks are launching crypto custody, stablecoin issuance, trading desks. Coverage is either bullish ("crypto is finally mainstream") or cautious ("banks face regulatory risk").

Who's NOT being heard: The compliance officers at those banks, who are dealing with the operational reality of integrating crypto into legacy banking infrastructure. The community banks that will be left behind. The crypto-native companies that banks are now competing with.

The angle from the missing voice: "I talked to three compliance officers at banks launching stablecoin products. Here's what the press releases don't tell you about what it actually takes to issue a stablecoin from inside a bank."

---

### Summary: The Angle Selection Checklist

Before writing any piece, run through:

1. **What is the consensus take?** (If you can't articulate it, you haven't done enough reading)
2. **What unstated assumption does the consensus rest on?** (The gap)
3. **What historical precedent does nobody cite?** (The time-shift)
4. **What adjacent domain offers a useful lens?** (The transfer)
5. **Whose voice is missing from the conversation?** (The missing stakeholder)
6. **What recurring theme does this map to?** (The Levine pattern)
7. **Will this framing be more relevant in 12 months?** (The Hobart filter)

If you can answer at least 3 of these with something non-obvious, you have a viable angle.

---

## 5. Timeliness vs. Timelessness: The Thompson Pattern

### The Best Pieces Are Timely AND Timeless

The goal is not to choose between timeliness and timelessness. The goal is to use a timely event as the entry point to a timeless structural insight.

**Ben Thompson's Pattern: News -> Framework -> Structural Implication**

Every Stratechery article follows a recognizable structure:

1. **News hook:** Something happened today or this week (Stripe acquired Bridge, the GENIUS Act passed, Circle filed its S-1)
2. **Framework application:** Thompson applies a known framework to the news (Aggregation Theory, the Smiling Curve, platform dynamics, modular vs. integrated)
3. **Structural implication:** The framework reveals something about the news that is not time-bound. It is a truth about how this type of system works, regardless of the specific companies involved.

**Concrete Example:**

- **News:** "Stripe acquires Bridge for $1.1B"
- **Framework:** Aggregation Theory. "Aggregators win by owning demand (the user relationship), not by owning supply (the technology). Stripe already owns the demand side (merchants). Bridge gives Stripe the supply side (stablecoin infrastructure). This is vertical integration to own the full stack."
- **Structural implication:** "The stablecoin infrastructure layer will be absorbed by existing payment aggregators rather than remaining independent. This means the 'picks and shovels' thesis for stablecoin startups -- that they can sell infrastructure to multiple players -- is weaker than it appears. The aggregators will build or buy."

The news hook makes it timely (people are searching for analysis of the Stripe/Bridge deal right now). The structural implication makes it timeless (the pattern of aggregators absorbing infrastructure will repeat in other contexts).

---

### How to Systematically Connect News to Structure

**Step 1: Identify the news event's "type."**

Every news event is an instance of a broader pattern. Classify it:

- Acquisition? (Aggregator absorbing infrastructure)
- Regulation? (Government reshaping incentive structures)
- Product launch? (Company testing a thesis about where value lives)
- Partnership? (Two entities recognizing complementary strengths)
- Failure/collapse? (A thesis was proven wrong -- what was the thesis?)

**Step 2: Ask "What does this tell us about how [this type of system] works?"**

Not "what happened" but "what does this reveal about the structure?"

**Step 3: Test the structural claim with a counterfactual.**

"If the opposite had happened (if Stripe had NOT acquired Bridge), what would that have told us?" If the structural insight holds regardless, it is robust.

**Step 4: Identify the prediction.**

Every structural insight implies a prediction. "If aggregators absorb stablecoin infrastructure, then standalone stablecoin API companies are in trouble." State the prediction explicitly. This gives readers something to track and gives you something to revisit (building the Levine "return to themes" compounding effect).

---

### Failure Modes:

- **Over-framework-ification:** Not every news event illuminates a structural pattern. Sometimes an acquisition is just an acquisition. The test: does the structural insight hold for 3+ other examples? If not, it may be a one-off.
- **Framework hammer:** When you only have Aggregation Theory, everything looks like aggregation. Maintain a library of 5-10 frameworks and rotate which one you apply.
- **Losing the reader in abstraction:** The news hook exists to keep the reader grounded. Never go more than 2 paragraphs without returning to the specific news event or a concrete example.

---

## 6. Tools, APIs, and Systems for Real-Time Topic Identification

### News APIs

| Tool            | Best For                     | Key Capabilities                                                          | Pricing                       | Stablecoin/Fintech Fit                                                     |
| --------------- | ---------------------------- | ------------------------------------------------------------------------- | ----------------------------- | -------------------------------------------------------------------------- |
| **Perigon**     | AI-enriched trend detection  | Up to 1M articles/day, AI-driven insights, clustering, sentiment analysis | Tiered plans                  | High -- supports custom topic feeds, category filtering for fintech/crypto |
| **NewsAPI.ai**  | Semantic search + historical | 150,000+ publishers, semantic precision, advanced filtering               | Tiered plans                  | High -- good for tracking specific entities (Circle, Tether, GENIUS Act)   |
| **Newsdata.io** | Market trend dashboards      | Live dashboards, sentiment analysis, business monitoring                  | Free tier + paid ($49-499/mo) | Medium -- good for general fintech trends, less crypto-specific            |
| **GNews**       | Lightweight topic tracking   | 80,000+ sources, 6 years historical, JSON API                             | Free tier available           | Low -- basic filters, no sentiment or clustering                           |

**Recommended for our system:** Perigon or NewsAPI.ai for the primary news intelligence feed. Use their clustering feature to identify when multiple outlets are covering the same story (indicating saturation) vs. stories with low coverage (indicating opportunity).

---

### On-Chain Data Tools (Fintech/Crypto Specific)

| Tool               | Best For                       | Key Signals for Content                                                                 | Pricing                      |
| ------------------ | ------------------------------ | --------------------------------------------------------------------------------------- | ---------------------------- |
| **Dune Analytics** | Custom stablecoin queries      | Stablecoin supply changes, active addresses, transfer volume, protocol-specific metrics | Free tier, paid from $420/mo |
| **Artemis**        | Stablecoin fundamental metrics | Supply/adoption/market trends, cross-chain analysis, Excel integration                  | Contact for pricing          |
| **Glassnode**      | On-chain cycle signals         | Exchange flows, whale movements, stablecoin supply on exchanges, liquidity stress       | Free tier, paid from $29/mo  |
| **DeFiLlama**      | DeFi TVL and protocol tracking | Stablecoin TVL across protocols, bridge volumes, yield comparisons                      | Free                         |
| **Nansen**         | Smart money tracking           | Institutional wallet movements, stablecoin flow between protocols                       | Paid                         |

**How on-chain data becomes content signals:**

- **Stablecoin supply hitting new ATH:** Content trigger -- "Why stablecoin supply just hit $300B, and what that money is actually doing"
- **Unusual whale movement:** Content trigger -- "Someone just minted $500M in USDT. Here's what that typically precedes."
- **Exchange stablecoin balance shifts:** Content trigger -- "Stablecoin balances on exchanges are at an all-time high. Is this dry powder about to deploy?"
- **Stablecoin velocity changes:** Content trigger -- "Stablecoin velocity just spiked -- meaning the same dollars are moving faster. This happened before [previous event] too."

---

### Trend Detection Tools

| Tool                 | Best For                     | How It Helps                                                               |
| -------------------- | ---------------------------- | -------------------------------------------------------------------------- |
| **Google Trends**    | Mainstream interest tracking | Shows when stablecoin topics enter public consciousness                    |
| **Exploding Topics** | Early-stage trend detection  | AI-powered identification of topics gaining traction before peak           |
| **SparkToro**        | Audience behavior analysis   | Shows what stablecoin/fintech audiences actually read, follow, and discuss |
| **Similarweb**       | Competitive traffic analysis | Shows which stablecoin/fintech sites are gaining or losing readers         |

---

### Regulatory and Funding Signals (Stablecoin-Specific)

| Signal Type                   | Where to Find It                                    | Content Trigger                                                                            |
| ----------------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **New regulatory proposals**  | Congress.gov, Federal Register, EU Official Journal | "The bill nobody is talking about that could reshape stablecoins"                          |
| **Agency guidance changes**   | OCC, FDIC, Fed bulletins                            | "The OCC just quietly changed its guidance on bank crypto activity"                        |
| **Funding rounds**            | Crunchbase, The Block, Decrypt                      | "Why VCs just put $X into [company] and what it signals about the market"                  |
| **Patent filings**            | USPTO, Google Patents                               | "Circle just filed a patent for [X]. Here's what that tells us about their roadmap."       |
| **Conference agendas**        | Money20/20, Consensus, Token2049                    | "The panels at [conference] reveal what the industry thinks the next 12 months look like"  |
| **Enforcement actions**       | SEC, DOJ, state AG announcements                    | "The enforcement action against [company] just created a new precedent for stablecoins"    |
| **On-chain governance votes** | Snapshot, Tally                                     | "MakerDAO just voted to [X]. This changes the competitive landscape for stablecoin yield." |

---

### The Integrated Intelligence Stack

**Recommended minimum viable toolset:**

1. **News API** (Perigon or NewsAPI.ai) -- automated daily feed of stablecoin/fintech/crypto coverage, clustered by topic
2. **Dune Analytics** (free tier) -- weekly dashboard check of stablecoin supply, active addresses, transfer volumes
3. **Google Trends** -- weekly check of 10-15 key terms
4. **Twitter/X lists** -- curated lists of 30-50 fintech/crypto voices for daily scanning
5. **Reddit/HN** -- weekly scan of r/CryptoCurrency, r/Fintech, and HN stablecoin threads
6. **Regulatory RSS** -- Congress.gov alerts for stablecoin/crypto bills, Federal Register for agency guidance

**Cost:** Free to ~$100/month for the minimum viable stack. $400-500/month for the full stack with paid API tiers.

---

## 7. The Integrated System: How This All Works Together

### The Weekly Topic Selection Workflow

**Monday Morning: Intelligence Scan (45 min)**

1. **News API feed review (15 min):** What stablecoin/fintech stories generated the most coverage this week? What stories are clustered (saturated) vs. standalone (opportunity)?

2. **On-chain signal check (10 min):** Any unusual movements in stablecoin supply, exchange balances, or velocity? Any new ATHs or significant drops?

3. **Social signal scan (15 min):** What are the top 5 questions/objections on Reddit and HN? What threads got the most engagement on Twitter/X? What topics are appearing on LinkedIn for the first time (the "mainstream signal")?

4. **Regulatory signal check (5 min):** Any new bills, guidance, or enforcement actions?

**Monday Midday: Angle Selection (30 min)**

5. **Topic shortlist:** From the intelligence scan, identify 3-5 candidate topics. For each, note:
   - Timeliness (is this in the news now?)
   - Saturation level (how many people are already writing about it?)
   - Structural depth (does this connect to a deeper pattern?)
   - Narrative constellation (which active narrative does this belong to?)

6. **Angle selection checklist:** For the top 2-3 candidates, run through the 7-question angle checklist from Section 4. Pick the topic+angle combination where you have the most non-obvious answers.

7. **The Hobart filter:** "Will this framing be more relevant in 12 months?" If yes, proceed. If no, consider whether the piece is worth writing as a quick reaction vs. a deep dive.

**Monday Afternoon - Wednesday: Research and Writing**

8. **Research using the Insight Generation System** (already in the codebase at `/research/insight-generation-system.md`): Four parallel research tracks, saturate with data, identify anomalies, cross-reference, articulate the mechanism.

9. **Draft using the Thompson pattern:** News hook -> Framework application -> Structural implication -> Explicit prediction.

10. **Quality check:** Does the piece pass the "Levine test"? Would an insider say "I didn't think about it that way"? Would an outsider say "I now understand something I didn't before"?

**Thursday: Publish and observe**

11. **Track engagement signals:** Which parts generated the most responses? What did people push back on? What did they share? These signals feed back into the topic backlog for next week.

12. **Update the narrative tracking document:** Did this piece confirm, challenge, or extend one of the active narrative constellations?

---

### The Topic Backlog System

Maintain a running list (Notion, physical notebook, whatever sticks) with:

| Column                      | Purpose                                                                                         |
| --------------------------- | ----------------------------------------------------------------------------------------------- |
| **Topic**                   | The specific news event or question                                                             |
| **Angle**                   | The non-obvious framing (from the angle checklist)                                              |
| **Narrative constellation** | Which active narrative this belongs to                                                          |
| **Timeliness**              | How time-sensitive (1-5, where 5 is "must publish this week")                                   |
| **Structural depth**        | How deep the structural insight goes (1-5, where 5 is "changes how you see the whole industry") |
| **Research needed**         | What data/sources you'd need to make this work                                                  |
| **Source**                  | Where the idea came from (news, reader question, practitioner conversation, footnote expansion) |

The goal: maintain 30-50 items at all times. Each week, pick from the backlog based on the intersection of timeliness (what's in the news NOW) and structural depth (what has the most lasting insight potential).

**Replenishment sources:**

- Every published piece generates 2-3 footnotes that could become their own pieces (Hobart method)
- Reader responses and questions (Rachitsky method)
- Practitioner conversations (McCormick method)
- News events filtered through frameworks (Thompson method)
- Recurring theme instances (Levine method)

---

### The Recurring Theme Library

Develop and maintain 5-7 named recurring themes, analogous to Levine's "everything is securities fraud." These should be:

1. **Stated in 5-10 words** (repeatable, memetic)
2. **Structurally true** (not just clever -- revealing of actual system dynamics)
3. **Applicable to many specific events** (each new instance reinforces the theme)

**Candidate themes for the stablecoin/payments space:**

- **"Everything is a money market fund"** -- When every new stablecoin product ends up structurally identical to traditional money market instruments
- **"The reserve question"** -- Every stablecoin crisis comes back to what is backing it
- **"Compliance is the moat"** -- In a commoditized infrastructure market, the ability to navigate regulation is the only durable competitive advantage
- **"The last mile problem"** -- Stablecoin technology works, but converting to/from local currency at the point of use remains unsolved
- **"Dollarization by API"** -- Stablecoins are accomplishing what US foreign policy could not -- making the dollar the default currency in emerging markets, delivered through technology infrastructure rather than political pressure

Each time a news event maps to one of these themes, write about it through that lens. Over time, readers learn the theme and begin to see new events through it before you even write about them. This is the compounding knowledge effect Levine has built over 13 years.

---

### What Success Looks Like

**In 30 days:** You have a working intelligence scan routine, a topic backlog of 30+ items, and 3-5 named recurring themes.

**In 90 days:** Readers begin referencing your recurring themes in their own conversations ("as Jin's newsletter puts it, 'everything is a money market fund'"). Your topic selections consistently hit the 48-72 hour window where something is in the news but nobody has published the structural take yet.

**In 6 months:** Practitioners start sending you information because they know you will give it a useful frame. Your backlog is growing faster than you can write (Hobart's signal of a healthy feedback loop). You have become a canonical source on at least one recurring theme.

**In 12 months:** When a major stablecoin event happens, people check whether you have written about it yet before forming their own opinion. This is the Thompson/Levine endgame -- becoming the place people go for the structural take.

---

## Sources

### Newsletter Writer Processes

- [Stratechery About Page](https://stratechery.com/about/)
- [How Ben Thompson Built a Writing Empire (Podcast)](https://deepcast.fm/episode/how-ben-thompson-built-a-writing-empire)
- [Ben Thompson's Daily Information Habits](https://thrivingonoverload.com/stratechery-founder-ben-thompson-daily-information-media-habits/)
- [Lessons from Ben Thompson](https://www.antoinebuteau.com/lessons-from-ben-thompson/)
- [Ben Thompson on Knowledge Project (Farnam Street)](https://fs.blog/knowledge-project-podcast/ben-thompson/)
- [Stratechery on Acquired Podcast](https://www.acquired.fm/episodes/stratechery-with-ben-thompson)
- [Matt Levine on David Perell Podcast](https://perell.com/podcast/matt/)
- [Why So Few Matt Levines? (Gwern)](https://gwern.net/matt-levine)
- [What Matt Levine Writes About (Topic Analysis)](https://blog.vghaisas.com/matt-levine-topics/)
- [Matt Levine: Money Stuff on Bloomberg](https://www.bloomberg.com/account/newsletters/money-stuff)
- [Matt Levine on "Everything Is Securities Fraud"](https://omny.fm/shows/what-goes-up/matt-levine-on-why-everything-is-securities-fraud)
- [Harvard Magazine Profile of Matt Levine](https://www.harvardmagazine.com/2025/07/harvard-bloomberg-column-matt-levine)
- [Packy McCormick on Building Not Boring](https://www.reidtandy.com/p/building-not-boring-a-conversation)
- [Not Boring on Acquired Podcast](https://www.acquired.fm/episodes/not-boring-with-packy-mccormick)
- [Packy McCormick on A Media Operator](https://www.amediaoperator.com/podcast/podcast-packy-mccormick-on-building/)
- [Byrne Hobart on Reading](https://byrnehobart.medium.com/read-2c3d4fba90ab)
- [The Diff Reading List](https://www.thediff.co/archive/the-diff-reading-list/)
- [Byrne Hobart About/FAQ](https://byrnehobart.medium.com/about-best-of-faq-25df97a74467)
- [Byrne Hobart on The Browser](https://thebrowser.com/notes/byrne-hobart/)
- [Byrne Hobart on Nathan Barry Podcast](https://nathanbarry.com/021-byrne-hobart-build-recurring-revenue-newsletter/)
- [Lenny Rachitsky Interview (Compound Manual)](https://manual.compoundplanning.com/chapters/interview-with-lenny-rachitsky-writer-of-lennys-newsletter)

### Narrative Economics

- [Robert Shiller: Narrative Economics (AEA Paper)](https://fairmodel.econ.yale.edu/ec439/shiller1.pdf)
- [Narrative Economics: How Stories Go Viral (Yale Insights)](https://insights.som.yale.edu/insights/narrative-economics-how-stories-go-viral)
- [Narrative Economics (Princeton University Press)](https://press.princeton.edu/books/hardcover/9780691182292/narrative-economics)
- [Narrative Economics (NBER Working Paper)](https://www.nber.org/system/files/working_papers/w23075/w23075.pdf)
- [LSE Review of Narrative Economics](https://blogs.lse.ac.uk/lsereviewofbooks/2020/02/18/book-review-narrative-economics-how-stories-go-viral-and-drive-major-economic-events-by-robert-j-shiller/)
- [Narrative Economics on Coursera](https://www.coursera.org/learn/narrative-economics)

### Cultural Tracking & Signal Analysis

- [Google Year in Search 2025](https://trends.withgoogle.com/year-in-search/2024/)
- [Social Listening Trends 2026 (The CMO)](https://thecmo.com/demand-generation/social-listening-trends/)
- [The Overton Window (Mackinac Center)](https://www.mackinac.org/OvertonWindow)
- [Signal vs. Noise: Navigating Misinformation (Firesight)](https://blog.firesight.ai/signal-vs-noise-navigating-misinformation-in-2025s-digital-overload/)
- [Noise vs Signal Mental Model (FunBlocks)](https://www.funblocks.net/thinking-matters/classic-mental-models/noise-vs-signal)
- [HN Sentiment Analysis vs. FAANG Stocks](https://medium.com/@danthelion/hacker-news-sentiment-analysis-vs-faang-stocks-db40ac23de9d)
- [Reddit Sentiment Analysis (Brand24)](https://brand24.com/blog/reddit-sentiment-analysis/)

### Tools & APIs

- [Best News API 2025 Comparison (NewsAPI.ai)](https://newsapi.ai/blog/best-news-api-comparison-2025/)
- [Perigon Real-Time News API](https://www.perigon.io/products/news-api)
- [Newsdata.io](https://newsdata.io/)
- [SparkToro Audience Research](https://sparktoro.com/)
- [Exploding Topics](https://www.bestprofitsonline.com/myblog/top-10-google-trends-alternatives-in-2025/)
- [Dune Analytics](https://dune.com/home)
- [Artemis Stablecoin Metrics](https://www.artemis.xyz/)
- [Glassnode On-Chain Analytics](https://tronpoolenergy.com/blog/glassnode-onchain-analytics/)
- [Dune + Artemis Stablecoin Report](https://cryptorank.io/news/feed/de166-dune-analytics-and-artemis-stablecoin-report-on-supply-adoption-and-market-trends)

### Stablecoin & Fintech Context

- [2025 Crypto Regulatory Round-Up (Chainalysis)](https://www.chainalysis.com/blog/2025-crypto-regulatory-round-up/)
- [Stablecoin Predictions 2026 (FinTech Weekly)](https://www.fintechweekly.com/news/stablecoin-predictions-2026-payments-infrastructure-regulation)
- [2026 Crypto Outlook (SVB)](https://www.svb.com/industry-insights/fintech/2026-crypto-outlook/)
- [Y Combinator Stablecoin Pivot](https://www.webpronews.com/y-combinators-stablecoin-pivot-signals-cryptos-mainstreaming-in-silicon-valley-funding/)
- [GENIUS Act and Stablecoin Regulation](https://www.fintechweekly.com/magazine/articles/stablecoin-regulation-banks-crypto-cooperation-shift)

### Angle Finding & Writing Technique

- [The Problem/Gap/Hook Heuristic (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4602011/)
- [Content Gap Analysis (HubSpot)](https://blog.hubspot.com/marketing/content-gap-analysis)
- [Contrarian Style Copywriting](https://watkinstben.medium.com/contrarian-style-copywriting-how-to-write-disruptive-messages-ad70365f1e41)
- [Use Your Inner Contrarian (ProBlogger)](https://problogger.com/use-inner-contrarian-generate-endless-content-ideas/)
- [Timely vs Timeless Writing](https://fastforwardjsy.medium.com/timely-vs-timeless-6f0d451ce70a)
- [Stratechery Concepts Page](https://stratechery.com/concepts/)
