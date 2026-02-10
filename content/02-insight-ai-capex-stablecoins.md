# Velocity vs. Float

## Insight V2

---

Last issue I argued that $600 billion in AI capex was bifurcating the stablecoin market — USDC capturing enterprise AI payments, USDT capturing edge AI through Tether's smartphone inference runtime and wallet toolkit. I spent the week stress-testing that thesis.

Most of it fell apart.

The x402 protocol, which I'd highlighted as the foundation of USDC's AI payment channel, has processed $1.2 million through Coinbase's flagship Shopify integration. Total. Enterprise GPU procurement still settles by wire and ACH because procurement teams already have vendor relationships and accounting systems. On the Tether side, QVAC Fabric has zero measurable independent adoption. No third-party deployments. No meaningful GitHub activity outside Tether's own repos. And there's a circular logic problem I missed: if QVAC runs entirely on-device with no cloud dependency, where does the USDT payment demand actually come from?

The AI-specific predictions were premature. But the split itself is real, and it's driven by something I should have looked at first: distribution costs.

### The number that matters

In 2024, Circle paid Coinbase $908 million in distribution fees. That was 54% of Circle's total revenue.

Tether paid $0 in distribution fees. USDT distributes through crypto exchanges, OTC desks, and informal networks. 51% of volume runs on Tron. Nobody takes a cut.

This sounds like a minor business model detail. It isn't. It determines the entire strategic logic of both companies, and it explains why USDT's market cap ($187 billion) is three times USDC's despite processing less transaction volume.

### Two models

Circle operates on velocity. Revenue comes from yield on reserves, same as Tether. But after paying Coinbase 54%, the margins are thin. And the dependency is self-reinforcing: more USDC in circulation means more distribution, which means more Coinbase dependency, which means Coinbase keeps its leverage on the revenue share. Circle's 2025 revenue was $1.68 billion. After the Coinbase payment, they kept roughly $770 million. So the rational strategy is to maximize throughput. More transactions, more integrations, faster settlement. Which is exactly what x402 does.

Tether operates on float. They take in dollar deposits ($192 billion in reserves, mostly T-bills), earn yield, and keep all of it. $10 billion in profit in 2025 with 235 employees. $42.5 million per employee. The business doesn't need to maximize transaction velocity. It needs to maximize how long people hold USDT.

The comparison that keeps coming to mind is Berkshire Hathaway. Berkshire collects insurance premiums, holds the float, invests it, keeps the returns. The insurance business doesn't need to be spectacularly profitable. It needs to keep float growing. Tether collects dollar deposits, holds the reserves, earns yield, keeps everything. Both companies use float to fund acquisitions in unrelated industries. Neither needs a distribution partner taking half their revenue.

### What the $4 billion in AI actually is

This is where V1 went wrong. I argued Tether's AI investments (Northern Data's 22,400 GPUs, Rumble, QVAC, WDK) were strategic demand creation for USDT. The stress test pointed out that Tether also invests in gold (140 tons), humanoid robots, brain-computer interfaces, and farmland. None of which create USDT demand. When a company earns $10 billion a year and deploys capital across 120+ companies in "AI, biotechnology, education, and digital media," the simpler explanation is that they're a holding company deploying profits.

Honestly, most of it is probably just a holding company deploying profits. The wallet toolkit and AI agent integration are at least plausibly demand-creating for USDT. But GPU compute at 25x the revenue per megawatt of Bitcoin mining? That's just a good investment. The structural point is what matters: Tether CAN put $4 billion into speculative AI infrastructure because nobody takes half their revenue. Circle can't. Their capital goes to integrations, compliance certifications, and payment rails.

And yes, the Northern Data self-dealing is concerning. Executives buying the mining arm through shell companies, second attempt at a lower price, undisclosed related-party transactions. If you hold USDT you should care about this. But it doesn't change the structural argument. Loosely governed holding company deploying float earnings in opaque ways. That's been Tether's pattern since the beginning.

### So what about AI payments

AI agent payments are coming. The infrastructure exists (x402, AgentKit, Payments MCP, WDK). The first AI-to-AI transaction happened in December 2025 via Fetch.ai. But we're at the $1.2-million-via-Shopify stage, not the $600-billion-enterprise-settlement stage.

When AI payments reach meaningful scale, they won't split neatly between USDC and USDT the way I predicted. PYUSD is targeting GPU financing with 4.5% yield. Solana flipped Base in x402 volume by late 2025. NEAR Protocol was designed from the ground up for AI agents. The payment layer will fragment across multiple stablecoins and chains in ways nobody can predict from 2026.

What won't fragment is the structural difference underneath. Velocity stablecoins (Circle, PYUSD, bank-issued) will compete on integration speed and compliance. Float stablecoins (Tether, and eventually others who figure out the model) will compete on creating reasons to hold. AI capex is one arena where this plays out. The cause is older than that.

### Two predictions

First: Circle's Coinbase revenue share stays above 40% through 2027. Circle can't renegotiate because Coinbase controls distribution and has no incentive to give back margin. This constrains Circle's strategic flexibility as long as it lasts.

Second: Tether's non-stablecoin investment portfolio exceeds $25 billion by end of 2027, funded entirely by seigniorage. At that point, Tether looks less like a stablecoin company and more like a sovereign wealth fund that happens to issue a stablecoin.

The way to check: Tether's quarterly attestation reports for investment portfolio growth, and Circle's SEC filings for changes to the Coinbase agreement. If Tether's portfolio stagnates or Circle renegotiates to below 30%, the structural divergence thesis weakens.

### For Plasma

The routing question I raised in V1 is real, but the framing needed fixing. The question isn't which chain. It's whether a given payment needs a velocity rail or a float rail. Enterprise procurement, API billing, real-time settlement: velocity. Payroll in developing markets, agent wallets holding working capital, store of value: float. Building routing that understands this difference is what we're working on at Plasma.

---

— Jin Fernando
