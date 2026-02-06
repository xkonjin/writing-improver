# LinkedIn Posts — Jin Fernando

---

## POST 1: The Stablecoin Issuer Stack

### Format: Text + diagram (Excalidraw at 3x). Newsletter link in first comment.

---

Working in stablecoin infrastructure, the thing that keeps coming up in conversations with payments companies: everyone asks about the technology. Which chain, what smart contracts, how do reserves work.

Those are the straightforward parts. Bridge made issuance an API call. Stripe paid $1B+ for them. Any funded team builds token minting and reserve management in a quarter. Circle's S-1 showed their reserve setup: 75% Treasuries (BlackRock), 25% cash at BNY Mellon/JPMorgan/Goldman. Nothing proprietary there.

The hard questions are different.

𝗕𝗮𝗻𝗸𝗶𝗻𝗴 𝗮𝗰𝗰𝗲𝘀𝘀: You need banks that will receive and send fiat in every jurisdiction you serve. US banking doesn't help Singapore customers. EU EMI doesn't give ACH access. The list of banks willing to handle stablecoin flows is shorter than people think, and those banks set the terms.

𝗟𝗶𝗰𝗲𝗻𝘀𝗶𝗻𝗴: GENIUS Act (effective Jan 2027) requires stablecoin issuers to be "permitted payment stablecoin issuers." Bank charter, OCC nonbank approval, or qualifying state license. 2-3 year queue. Circle and Paxos already cleared it.

𝗣𝗮𝘆𝗺𝗲𝗻𝘁 𝗿𝗼𝘂𝘁𝗶𝗻𝗴: $50K cross-border payment — which stablecoin, which chain, which pool, which off-ramp, what FX rate. Good routing = 50bps. No routing = 5%. Same payment. This barely exists as a product category yet.

New stablecoin launches I've been tracking — when you ask about banking partners or licensing timelines, the conversations get less specific. The token is the part they have figured out.

What differentiates Circle isn't their reserves. It's their banking relationships, their CCTP cross-chain protocol, their regulatory approvals — things that took years, not quarters.

Wrote a longer breakdown with specific companies and economics at each layer — link in comments.

---

## POST 2: The Volume Problem

### Format: Text post.

---

Something I keep seeing in stablecoin infrastructure conversations:

Payments volume on a chain is not a business.

At single-digit bips on transaction fees, a chain needs hundreds of billions in annual volume for meaningful revenue. Switching costs are near-zero — a payment processor migrates chains in a weekend if the incentive program ends.

I've watched chains celebrate $1B+ in weekly stablecoin volume while their token goes nowhere. The math doesn't work and institutional investors have figured this out. Incentivized volume isn't organic demand.

The question I'd ask instead of "what's your volume": what products are built on the rails that make it hard for customers to leave? Orchestration, compliance tooling, merchant settlement. Not the cheapest pipes — the pipes you can't easily replace.

---

## POST 3: The Banking Bottleneck

### Format: Text post.

---

The part of the stablecoin stack I keep underestimating: banking access.

Every stablecoin issuer needs bank accounts that send and receive fiat in each market they serve. US banking doesn't cover Singapore. EU EMI doesn't give ACH access. You need relationships everywhere.

The list of banks willing to handle stablecoin flows is short and getting shorter as compliance pressure increases. The banks that remain have pricing power and they're using it. Every new issuer that launched in Q4 2025 is competing for the same limited pool.

This gets more complicated with the EMI vs. banking license question. An EMI (months to get, low capital) can't hold deposits, can't lend, and doesn't cross borders. A full banking license (2-5 years, much more capital) gives direct central bank settlement — no intermediary. The intermediary the EMI needs adds cost, latency, and a failure point.

Under GENIUS Act, issuers must be "permitted payment stablecoin issuers" — bank, OCC-approved nonbank, or qualifying state license. Circle and Paxos already cleared this. Everyone else is 2-3 years behind.

When I'm evaluating stablecoin infrastructure, the first question isn't "which chain" — it's "which banks process your fiat flows, and in which jurisdictions." If the answer is vague, everything else is secondary.

---

## POSTING ORDER

1. **Post 1** — pairs with diagram, starts the series
2. **Post 2** — contrarian take, generates debate from chain maximalists
3. **Post 3** — banking deep dive, positions Jin as someone who understands the plumbing

## NOTES

- Newsletter link always in first comment, never post body
- Plasma company account reshares selectively
- Team (Bamlak, Adam) adds perspective in comments
