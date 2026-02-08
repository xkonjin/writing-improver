# Tether Is Building an AI Company

Tether made $13 billion in profit last year. Most people assume that money goes into T-bills and Bitcoin. And it does — $113 billion in T-bills, $2 billion in mining infrastructure across 15 sites. But there's a $4 billion line item that doesn't get enough attention.

Tether has quietly deployed $4 billion into AI.

### The Northern Data deal

The anchor investment is Northern Data AG, a German data center operator. Tether's exposure: roughly €1.1 billion across debt and equity, including a $610 million unsecured loan maturing in 2030.

Northern Data runs three business units. Taiga Cloud operates 22,400 GPUs — 20,480 H100s and 2,048 H200s — generating €120-150 million in revenue last year. Ardent Data Centers is building out ~250 megawatts across eight facilities, with a 180-megawatt flagship in Maysville, Georgia. And there was a mining unit called Peak Mining, which Tether sold for $200 million to companies controlled by Tether's own CFO and CEO.

That last part is worth pausing on. Related-party transaction. $200 million. The corporate governance implications are... notable. But it tells you something about where Tether's management thinks value is going: away from mining, toward AI compute.

Then in December 2024, Tether invested $775 million in Rumble — the video platform — plus $150 million in GPU services and $100 million in advertising. A month later, Rumble announced it was acquiring Northern Data for ~$767 million. Since Tether owns 54% of Northern Data, this makes Tether the largest shareholder of Rumble.

Follow the money: Tether funds Rumble, Rumble buys Northern Data, Tether controls both. The AI compute, the content platform, the distribution — all consolidated under one capital allocator spending from $13 billion in annual profit. And unlike the hyperscalers burning 94% of operating cash flow on capex (CoreWeave) or issuing $108 billion in debt (the hyperscaler industry in 2025 alone), Tether funds this entirely from retained earnings. No dilution. No debt covenants. No quarterly earnings calls where analysts ask about return on invested capital.

### Why the economics make sense

The conversion math is straightforward. AI compute generates roughly 25x higher revenue per megawatt than Bitcoin mining. A 10-megawatt GPU cluster produces the revenue equivalent of a 100-megawatt mining operation. The annualized revenue is approximately $9.1 million per megawatt at 80% utilization.

Supply side math.

The demand side is where Tether gets specific.

### QVAC and the edge-first bet

In October 2025, Tether released Genesis I — a 41-billion-token synthetic STEM dataset. By December, Genesis II brought the total to 148 billion tokens across 19 domains. These aren't academic exercises. They feed into QVAC Fabric, which Tether describes as the world's first edge-first LLM inference runtime.

What "edge-first" means in practice: QVAC runs on smartphones. iOS, Android, Windows, macOS, Linux, across Nvidia, AMD, Intel, Apple Silicon, Qualcomm, and ARM Mali hardware. It's the first framework that enables LLM training on smartphone-class hardware. Apache 2.0 license.

I don't know if "first" is technically accurate. But the intent is clear. Most AI infrastructure is built for the cloud — for data centers, for enterprise API access, for markets where connectivity is reliable and latency is low. Tether is building for the opposite environment: developing markets where 534.5 million people already hold USDT, mostly on Tron, mostly through OTC desks, mostly in countries where the banking infrastructure is limited.

### The wallet in the AI

This is where it gets interesting.

Tether's other product is WDK — a Wallet Development Kit. Open-source, self-custodial, multi-chain. Bitcoin, Lightning, Ethereum, Arbitrum, Polygon, TON, Solana. Free at wallet.tether.io.

CEO Paolo Ardoino demonstrated AI agents autonomously sending Bitcoin without human intervention at a conference last year. His claim: "Every single AI agent will have a wallet" within 15 years. One trillion agents.

That sounds absurd. But here's what isn't absurd: QVAC (edge AI runtime) + WDK (embedded wallet) = an AI agent running on a phone that can spend money autonomously. No cloud. No bank. No API billing through Stripe. Just a local model with access to a USDT wallet.

And this isn't just Tether's thesis. Coinbase launched AgentKit and a Payments MCP — toolkits for giving AI agents crypto wallets with compliance controls. Coinbase and Cloudflare are building the x402 Foundation to revive the HTTP 402 "Payment Required" status code. 200-millisecond stablecoin confirmation on Base, compared to 2-3 day ACH.

Fetch.ai ran the first AI-to-AI payment in December 2025 — two personal AIs coordinated a dinner reservation and payment while their users were offline. Google Cloud launched the Agent Payments Protocol for autonomous B2B procurement in September. This isn't speculative. It's in production.

### The bifurcation

So there are two AI-agent-payments stacks emerging. One is built for US enterprise: Coinbase/Circle, regulated, on Base, designed for API-level micropayments between cloud services. The other is built for emerging markets: Tether, edge-first, on Tron and local networks, designed for smartphone-native agents that work offline.

The interesting part isn't which wins. Both probably will, in different markets.

The interesting part is that Tether — which everyone thinks of as a stablecoin company — is spending $4 billion to become an AI infrastructure company. And they can afford to do it because the stablecoin business generates $13 billion a year in near-riskless profit from T-bill interest that they don't share with USDT holders.

Which raises a question nobody's asking. If the AI agent economy does arrive — hundreds of millions of autonomous agents needing wallets, needing inference, needing payment rails — and Tether has already built the edge runtime, the wallet SDK, and the AI training data, how much is that worth?

More than the stablecoin business?

I don't know. Ask me again in 18 months.
