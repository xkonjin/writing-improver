# Thesis Generation System

A system for producing non-obvious investment theses from real data. Output: sharp commentary that demonstrates you see something others don't.

---

## What This System Produces

A **thesis card**: one non-consensus structural claim, backed by specific data, with a falsifiable prediction and a clear "who wins / who's exposed" conclusion. 400-800 words written up. The kind of thing where a smart investor reads it and thinks "I hadn't connected those two things."

**Not:** explainers, market recaps, "here are 5 trends to watch," thinkpieces, or anything where swapping the company names leaves the argument intact.

---

## The Kolmogorov Test (Applied Throughout)

Every thesis must pass: **can you state this claim in a way that ONLY works for this specific situation?** If you can swap the company/industry names and the argument still holds, it's a template, not an insight. Discard it.

Examples:

- "Regulation creates moats for incumbents" → template (works for any industry)
- "GENIUS Act Section 4 requires T-bill backing with ≤93 day maturity, which codifies $141B of mandatory Treasury demand from stablecoin issuers alone, saving the US ~$15B/year in interest — making enforcement against the largest issuer structurally irrational" → thesis (remove any specific and it weakens)

---

## Step 0: SIGNAL DETECTION

This is the daily habit that feeds the system. You're scanning for **anomalies** — things that don't fit the consensus narrative.

### Data sources (ranked by signal density)

| Source                                           | What to look for                                                                                                                                                        | Frequency                         |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| SEC/state filings (EDGAR, state registrars)      | New registrations, amendments, S-1s, 10-K footnotes, exemption applications                                                                                             | Weekly scan                       |
| Earnings call transcripts                        | Specific numbers that contradict the company's own narrative. Capex commitments. Revenue mix shifts.                                                                    | Quarterly deep, weekly highlights |
| On-chain data (Dune, Artemis, DefiLlama, Nansen) | Flow anomalies: sudden volume shifts between chains/protocols, whale wallet movements, TVL divergences from price                                                       | Daily glance, weekly analysis     |
| Job postings (company career pages, LinkedIn)    | What a company is hiring for tells you what they're building 6-12 months out. A stablecoin company hiring compliance lawyers in 3 new jurisdictions = expansion signal. | Biweekly                          |
| Regulatory text (actual bills, not commentary)   | Read the bill text. Specific sections, thresholds, exemptions. Who benefits from each provision? Who wrote it?                                                          | As published                      |
| Patent filings                                   | What's being patented reveals R&D direction before product announcements                                                                                                | Monthly                           |
| GitHub/open source repos                         | What's being built in public. New repos from known teams. Dependency changes in major projects.                                                                         | Weekly                            |
| Conference talks / podcasts (insider, not media) | What operators say to other operators vs. what they say to press. Contradictions = signal.                                                                              | Selective                         |
| Deal flow data (Crunchbase, PitchBook)           | What's getting funded, at what stage, at what valuation. What's NOT getting funded anymore.                                                                             | Biweekly                          |

### What counts as an anomaly

1. **A number moving in the wrong direction.** Revenue growing while margins compress. Usage up while token price flat. Hiring in area X while announcing pivot away from X.
2. **A gap between public narrative and filed data.** CEO says "AI-first company" but 10-K shows 90% revenue from legacy product. Claims "decentralized" but one entity controls 80% of supply.
3. **Two entities connected that shouldn't be.** Regulator-to-company revolving door. Shared investors across supposedly competing companies. Supply chain dependencies that create hidden exposure.
4. **Consensus belief with thin evidence.** Everyone says "X is the next big thing" but actual adoption data is flat or declining. Or the reverse: everyone ignores Y but adoption data is accelerating.
5. **A structural constraint that money can't solve.** Physical lead times, regulatory timelines, talent bottlenecks, permitting queues. Markets price capital. They underprice time.

**Write anomalies as simple factual statements. Don't interpret yet.**

---

## Step 1: SATURATE (When You Have an Anomaly Worth Pursuing)

Pick one anomaly. Run 3-4 parallel research tracks, each attacking a different dimension of the anomaly. Each track returns **specific facts**: numbers, names, dates, mechanisms. Not narratives.

### The four tracks

| Track                     | Question                                                                                                          | Output                                                                                          |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| 1. Money/value flow       | How does value actually move through this system? Who touches it? What's the plumbing?                            | Dollar amounts, fee structures, settlement mechanisms, intermediary chain                       |
| 2. Power/governance       | Who controls what? Who owns whom? What relationships exist between the decider and the beneficiary?               | Ownership stakes, board seats, regulatory relationships, investor overlap                       |
| 3. Regulatory/legal       | What does the law actually say? What specific provisions apply? Who wrote them? Who benefits from each provision? | Section numbers, thresholds, exemptions, legislative history, lobbying data                     |
| 4. Structural constraints | What physical, temporal, or human constraints govern this system? What can't be changed with capital?             | Lead times, permitting timelines, supply bottlenecks, talent pools, infrastructure dependencies |

**3,000+ words of facts per track. Primary sources over summaries. Filing data over analyst takes.**

### Model assignment

Research agents: **Sonnet**. This is fact compilation, not reasoning. Save Opus for cross-referencing.

---

## Step 2: CROSS-REFERENCE (Where the Thesis Emerges)

This is the only step that requires deep reasoning. Look for connections BETWEEN tracks that produce a non-obvious structural claim.

### The productive intersections

- **Money flow + Power structure** = who benefits from the plumbing being structured this way? Is someone capturing rent from a structural position they designed?
- **Regulation + Structural constraints** = does the regulation create a moat by exploiting a constraint that can't be arbitraged? Does it lock in an advantage that would otherwise be temporary?
- **Money flow + Regulation** = does the law create a closed loop in the value chain? Does it mandate demand for a specific asset/service?
- **Power structure + Structural constraints** = who already controls the scarce resource? Can they be displaced, or have they locked in position?

### The mechanism test

Can you trace value from origin to destination, naming every entity and what they gain at each step? If yes, you understand the mechanism. If you can only describe the pattern ("value is shifting from X to Y"), you're still at the surface.

### Model assignment

**Opus.** This is where the insight lives. The difference between "smart framework application" and "genuine thesis" happens here.

---

## Step 3: CONSTRUCT THE THESIS CARD

| Field             | Requirement                                                                      | Example                                                                                                                                                                                                                                                                            |
| ----------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Claim**         | One sentence. Non-consensus. Specific.                                           | "Power companies, not chip companies, will capture the majority of AI infrastructure margin by 2028."                                                                                                                                                                              |
| **Mechanism**     | The causal chain. Each step leads to the next. Name every entity.                | GPU power draw doubled per generation → electricity cost exceeds chip cost over useful life → hyperscalers vertically integrating into power → companies with locked-in generation capacity (behind-the-meter, nuclear PPAs) have structural advantage over those buying from grid |
| **Key evidence**  | 3-5 specific data points. Each load-bearing (remove one and the thesis weakens). | B200: 1,200W TDP. GB200 NVL72 rack: 140kW. 3-year power cost > chip cost at industrial rates. Meta Prometheus: on-site gas turbines. Amazon Susquehanna: direct nuclear PPA. CoreWeave: no own generation, power as fastest-growing cost line.                                     |
| **Who wins**      | Specific companies/categories positioned to benefit.                             | Vertically integrated hyperscalers (Meta, Amazon, Apple). Independent power producers with data center proximity. Companies with existing nuclear/gas assets and land.                                                                                                             |
| **Who's exposed** | Specific companies/categories at risk.                                           | Pure-play GPU cloud (CoreWeave, Lambda). Utilities that assumed stable demand growth. Data center REITs without power generation assets.                                                                                                                                           |
| **Prediction**    | Specific, falsifiable, timebound.                                                | "CoreWeave's power cost as % of revenue exceeds 35% by Q4 2026, compressing margins below debt service requirements."                                                                                                                                                              |
| **Falsification** | What data would prove this wrong?                                                | Grid capacity additions accelerate faster than expected. Nuclear SMRs hit commercial deployment by 2027. GPU efficiency gains outpace power draw increases (Rubin architecture).                                                                                                   |
| **Edge**          | Why you see this and others don't.                                               | Inside stablecoin infrastructure — you see the same "who controls the scarce input" dynamic playing out in payments, where the constraint is banking relationships, not power. Structural pattern recognition across domains.                                                      |

---

## Step 4: STRESS-TEST

### The four kills

Run each against the thesis. If any kills it, discard or revise.

1. **Template kill.** Swap the company/industry names. Does the argument still work? If yes → it's a framework, not a thesis. Discard.

2. **Consensus kill.** State the claim to a knowledgeable person in the space. If they say "obviously" → the thesis isn't non-consensus. It might be correct but it's not a trade. Discard.

3. **Pre-mortem kill.** It's 2028 and you were wrong. Write three specific scenarios explaining why. Each reveals an assumption. Test each assumption against current data. If any assumption is shaky, the thesis needs qualification.

4. **Data kill.** Remove each evidence point one at a time. If the thesis still stands without one → that data point is decoration, cut it. If removing ANY point breaks the thesis → high Kolmogorov complexity. Keep.

### User stress-test (most important)

Present the thesis card to a smart person and let them attack it. The best refinements come from someone breaking your analogy or finding the assumption you didn't know you were making.

From experience: the highest-quality insight in the stablecoin project came from the user breaking the Visa/orchestration analogy. Sequential falsification > clever framing.

---

## Step 5: WRITE-UP

### Format: 400-800 words

Not a newsletter essay. Not discovery-order. This audience knows the basics. The write-up structure:

1. **Open with the specific data point that makes the claim surprising.** Not a framing device. The data IS the hook. (50-100 words)
2. **The mechanism.** Trace the causal chain. Name entities, name numbers. Each step follows logically from the last. (150-300 words)
3. **The implication nobody's pricing in.** Who wins, who's exposed. Specific names. (100-200 words)
4. **What falsifies this.** Show intellectual honesty. Name the specific data that would prove you wrong. (50-100 words)

### Voice

- Confident but intellectually honest
- Specific numbers, company names, regulatory references
- State what you think, not what "one might argue"
- No hedging unless genuinely uncertain (and then be specific about WHAT is uncertain)
- Matt Levine's "smart friend explaining over drinks" energy
- No signposting, no "in this piece I'll argue," no motivational closers

### What NOT to do

- Don't explain basics the audience already knows
- Don't frame things as "contrarian" (if you have to say it's contrarian, it isn't)
- Don't use ascending reveal structure (save the best for last = theatrical, not analytical)
- Don't write "implications" sections that just restate the mechanism in softer language
- Don't end with a question (lazy closer)

---

## Distribution Strategy

| Channel        | Format                                                                                                                                                | Purpose                                            |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| X/Twitter      | Thread: thesis claim + 3-4 key evidence points + prediction. 5-7 tweets max.                                                                          | Credential building. Demonstrates you see things.  |
| Substack/blog  | Full 400-800 word write-up with the complete thesis card.                                                                                             | Permanent record. Searchable. Linkable.            |
| Telegram group | Share the X thread + a conversation starter question. "I think [claim]. The thing I'm least sure about is [specific uncertainty]. What am I missing?" | The real product. Thesis as conversation catalyst. |

### Frequency

- 2 thesis cards per week (Tuesday/Thursday)
- 1-2 quick takes per week (anomaly observations that aren't fully developed, shared in Telegram for group discussion)
- Monthly: review predictions. Which were right? Which were wrong? Why? Share the scorecard publicly.

The monthly scorecard is the strongest credential builder. Anyone can make predictions. Almost nobody tracks and publishes their accuracy.

---

## Weekly Workflow

| Day          | Activity                                                                                                                           | Time    |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------- | ------- |
| Mon          | Signal scan: review data sources, log anomalies, pick 1-2 to develop                                                               | 1-2 hrs |
| Tue          | SATURATE + CROSS-REFERENCE on thesis #1. Write up. Publish.                                                                        | 2-3 hrs |
| Wed          | Quick takes for Telegram. Signal scan. Start research on thesis #2.                                                                | 1 hr    |
| Thu          | Finish thesis #2. Write up. Publish.                                                                                               | 2-3 hrs |
| Fri          | Telegram engagement. Review the week's discussion threads. Note which theses generated the most debate (= highest value to group). | 1 hr    |
| End of month | Prediction scorecard. Review all theses from the month. Which predictions can be checked? Were you right? Share results.           | 2 hrs   |

---

## Model Usage

| Step                        | Model          | Why                                                                                       |
| --------------------------- | -------------- | ----------------------------------------------------------------------------------------- |
| Signal detection            | Human (you)    | No AI can reliably detect what's anomalous in YOUR domain. This requires insider context. |
| Research / SATURATE         | Sonnet         | Fact compilation. Structured search. Doesn't need reasoning.                              |
| Cross-reference / mechanism | Opus           | Where the thesis emerges. Don't cheap out.                                                |
| Stress-testing              | Sonnet + Human | Sonnet runs the four kills mechanically. Human provides the real stress-test.             |
| Write-up                    | Opus           | Voice and precision matter for credential content.                                        |
| AI tell cleanup             | Haiku          | Mechanical checklist.                                                                     |

Estimated cost per thesis: $3-5 (vs. $15-20 all-Opus).

---

## The Telegram Group Strategy

The content is the filter. The group is the product.

### Admission criteria for the 10-15 H1 2026 slots

- Must be a mutual (you know them, they know you)
- OR: demonstrated engagement with your public theses (thoughtful replies, not "great thread!")
- Investors or founders actively deploying capital
- Bias toward people who will ADD signal to the group, not just consume it

### Group rules (keep it simple)

1. No price talk. No "when moon." No chart analysis.
2. Share theses, not tips. If you think something, show your work.
3. Chatham House Rule on anything shared in the group.
4. Be specific. "I'm bullish on X" is useless. "I think X will do Y by Z because of [specific mechanism]" is valuable.

### How to announce

Don't announce broadly. Share a thesis thread on X. At the bottom: "I run a small group of investors and founders where we discuss theses like this. Opening 10-15 spots for H1 2026. If you're actively deploying capital and want in, DM me."

The scarcity + quality signal from the thesis itself does the filtering. People who DM after reading a sharp thesis are pre-qualified. People who DM after seeing "join my group" are not.
