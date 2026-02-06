# What Actually Differentiates a Stablecoin Business

## Newsletter — Issue #1

---

Bridge shipped stablecoin issuance APIs last month. Stripe paid over $1 billion to acquire them. Which means any developer can now mint a stablecoin — the token part is a solved problem.

So what separates a stablecoin business from a stablecoin token?

I've spent the past year at a stablecoin infrastructure company having this conversation with payments teams. The pattern: everyone starts by asking about the technology. Which chain, what smart contracts, how do the reserves work. Those are reasonable questions. They're also the straightforward parts. The parts that trip people up are different, and they're mostly not engineering problems.

---

### The easy parts: reserves and minting

Circle's S-1 showed their reserve breakdown: roughly 75% in Treasuries (managed by BlackRock) and 25% in cash deposits across BNY Mellon, JPMorgan, and Goldman Sachs. Monthly attestation reports are now mandatory under the GENIUS Act. This is the part Tether got all its scrutiny over and where Terra/UST blew up.

But holding T-bills in a custodial account is something any well-capitalized team sets up in a quarter. Same with minting — Circle operates USDC on 16+ chains, but multi-chain smart contract deployment is a known engineering problem with known solutions. Bridge just turned it into an API call.

The metric worth knowing: mint speed = settlement speed. Circle does near-instant minting with same-day fiat redemption for requests before 3 PM ET. If your issuer takes 2-3 business days to redeem, you've built ACH with more counterparty risk. That's a product differentiator. The reserve structure is not.

---

### Banking access: where it becomes a different problem

This is the part I keep underestimating.

To let customers move between dollars and stablecoins, you need bank accounts that can receive wires and send them — in every jurisdiction you serve. A US banking partner doesn't help your customers in Singapore. A European EMI doesn't give you ACH access. Every new market means a new banking relationship.

The thing people outside the industry don't appreciate: the list of banks willing to handle stablecoin-related flows is genuinely short. As regulatory scrutiny has increased, some banks that were crypto-adjacent have pulled back. The ones that remain have pricing power, and they use it. Every new stablecoin issuer that launched in Q4 2025 is now competing for the same limited pool of willing banking partners.

The EMI vs. full banking license distinction matters here because the economics are completely different. An EMI lets you issue e-money and process payments — you can get one in the EU in months. But you can't hold deposits, can't lend, and the license doesn't cross borders. A full banking license takes 2-5 years and far more capital, but gives you direct access to central bank settlement. No intermediary between you and the clearing system. The intermediary that the EMI needs adds cost, latency, and a failure point.

This isn't a technical detail. It flows straight to margin. Companies building on direct banking relationships and companies going through intermediaries are running fundamentally different economics.

---

### Licensing: the GENIUS Act queue

GENIUS Act was enacted July 2025, effective January 2027. Stablecoin issuers in the US must be "permitted payment stablecoin issuers" — federally licensed bank, OCC-approved nonbank, or state-licensed entity meeting federal standards.

This is a 2-3 year process requiring dedicated legal teams, compliance infrastructure, and ongoing regulatory engagement. Circle and Paxos already have the necessary approvals. Everyone else is in the queue.

Europe has MiCA adding its own requirements — capital adequacy, reserve composition rules, transaction limits for non-euro stablecoins. Every new jurisdiction means another licensing process.

KYC/AML infrastructure sits on top of all of this. Every fiat entry and exit point needs identity verification, transaction monitoring, sanctions screening. The tooling (Chainalysis, Elliptic, Sardine) is mature but not cheap, and the bar keeps going up.

New stablecoin launches I've been tracking — when you ask about licensing timelines, the conversations get less specific. The token is the part they have figured out.

---

### Orchestration: the layer nobody talks about

This is the part I find most interesting, partly because it barely exists as a defined product category.

When a payment goes from a sender in the US to a recipient in the Philippines, something needs to decide: Which stablecoin? On which chain? Through which liquidity pool? Via which off-ramp partner? At what FX rate? What happens when the primary route fails?

These routing decisions happen in real-time and directly determine cost. A good orchestration layer routes a $50,000 cross-border payment in under a minute at 50bps. Without one, the same payment costs 3-5% in slippage and fees. Sometimes it just gets stuck.

The engineering isn't smart contract deployment — it's real-time routing optimization across chains, liquidity sources, and fiat off-ramps. Closer to building a payment network's routing engine than building a token.

It also creates real switching costs. Once a payments company integrates with an orchestrator and the routing is optimized for their specific corridors, migrating means re-optimizing everything.

I think this is where the most interesting competition plays out over the next few years. But the market structure hasn't settled. It's early.

---

### What differentiates Circle

Not their reserves — any funded team replicates that. What differentiates them: banking relationships in multiple jurisdictions, CCTP cross-chain protocol for native interoperability, near-instant settlement with same-day redemption, and regulatory approvals that took years to accumulate.

Those are the things that are hard to replicate. Not because of engineering complexity, but because they require time, relationships, and regulatory patience. Different skill sets than building smart contracts.

---

### What I'd ask if I were evaluating stablecoin infrastructure

Not "which chain are you on" — that's the most commoditized decision in the stack.

Instead: Which banks process your fiat flows, and in which jurisdictions? What licenses do you hold? How does your payment routing work? What's your redemption speed?

If the answers get vague after the first question, you're talking to a token project, not an infrastructure business.

Going deeper on the banking access problem next issue — who the willing banks are, how the economics actually work, and why this is the chokepoint most people are underestimating.

— Jin Fernando
