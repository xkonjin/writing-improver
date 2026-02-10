# The Real AI Bottleneck Isn't Chips

Nvidia's H100 draws 700 watts. The B200 Blackwell draws 1,200 watts. Blackwell Ultra: 1,400 watts. A full GB200 NVL72 rack pulls 140 kilowatts. In two GPU generations, power consumption per chip doubled.

I kept staring at that progression and something clicked.

Every GPU generation makes the silicon more capable but also more power-hungry. The compute gets cheaper per FLOP, but the electricity gets more expensive per rack. At some point — and I think we might already be there — the cost of powering a GPU over its useful life exceeds the cost of buying it.

When that happens, the bottleneck monopolist shifts. It stops being the chip company. It starts being whoever controls the electricity.

### Follow the power contracts

Meta signed nuclear deals with TerraPower, Oklo, and Vistra. But nuclear plants take 10-15 years to build. So for their Prometheus data center in New Albany, Ohio — the world's first 1-gigawatt single site — Meta went a different route: gas turbines, behind-the-meter generation. They generate their own electricity on-site.

That's not a sustainability decision.

That's vertical integration. Meta doesn't want to depend on a utility for the most critical input to their AI infrastructure. The same way Apple built its own chips to stop depending on Intel, Meta is building its own power to stop depending on Duke Energy. And it's not just Meta. Amazon's Project Rainier in Indiana — 2.2 gigawatts, $11 billion, 30 buildings — uses direct power purchase agreements with solar and wind operators, bypassing the utility entirely. In March 2024, Amazon signed a deal to buy power directly from Talen Energy's Susquehanna nuclear plant. Apple's North Carolina facility: 82% solar, 12% wind, biogas fuel cells, built to Apple's specifications and owned by Apple. Michigan is offering data center tax exemptions through 2050 — not a typo — because states understand that whoever hosts the data centers controls the thirty-year economic relationship. The pattern is the same everywhere: the hyperscalers are vertically integrating into power generation, treating electricity as a strategic input the way they already treat silicon.

And here's what makes this harder to replicate than anyone admits. Grid transmission upgrades take 5-7 years and are politically contentious. New gas plants: 2-3 years. Nuclear: 10-15 years. Solar and wind: 12-18 months but intermittent. Water for cooling: up to 5 million gallons per day per facility, in regions increasingly fighting over water rights. The Big Four hyperscalers committed over $600 billion in capex for 2026, issued $108 billion in debt last year, but dollars don't compress these lead times.

Once the permits are filed, the turbines ordered, and the water rights secured — that's the moat. A physical one.

### Where the value shifts

In 2020, the AI value chain was clear: Nvidia makes chips, cloud providers buy chips, software companies rent compute. The scarce resource was silicon. Nvidia captured the margin. But the B200's 1,200-watt TDP means a rack of GPUs at 80% utilization for a year consumes roughly $100,000-150,000 in electricity at industrial rates. The GPU itself costs $30,000-40,000. Over a three-year useful life, the power cost exceeds the chip cost.

CoreWeave tells you where this is heading.

They IPO'd at $23 billion with $14 billion in debt and 94% of operating cash flow going to capex. Their filings show power costs as the fastest-growing line item — not GPU depreciation. And CoreWeave doesn't generate its own electricity. Which means their margins are permanently exposed to utility pricing.

### What I think this means

The AI compute market bifurcates. Meta, Amazon, and Apple build integrated power-and-compute stacks. Everyone else rents both. The companies most valuable in AI infrastructure five years from now might not be the ones building the best models. They might be the ones that locked up 2 gigawatts of behind-the-meter power before everyone else noticed that was the scarce resource.
