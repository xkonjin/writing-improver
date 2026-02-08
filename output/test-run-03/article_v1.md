# The 7-Gigawatt Problem

Stargate — the OpenAI/Oracle/SoftBank joint venture — needs 7 gigawatts of power capacity across its planned data center network. For scale: that's roughly the output of seven nuclear power plants. The Abilene, Texas flagship alone draws 1.2 gigawatts, with the first two buildings operational since September 2025 and six more under construction.

They're not alone. Amazon's Project Rainier in Indiana: 2.2 gigawatts, 30 buildings, $11 billion. Meta's Prometheus in New Albany, Ohio: the world's first 1-gigawatt single-site data center, online in 2026. xAI's Colossus in Memphis was built in 122 days and is already at 300 megawatts.

Add it up. The Big Four hyperscalers — Microsoft, Google, Amazon, Meta — have committed over $600 billion in combined capex for 2026. That's a 36% increase over 2025. Apple added another $500 billion over four years. The industry issued $108 billion in debt last year alone, with $1.5 trillion expected in total.

I've been trying to understand what this spending actually buys.

### The watt problem

The answer starts with a single number: 1,200 watts. That's the thermal design power of Nvidia's B200 GPU, the Blackwell-generation chip that every hyperscaler is ordering. The previous generation H100 drew 700 watts. That's a 71% increase in power per chip.

The next version — Blackwell Ultra — draws 1,400 watts. A full GB200 NVL72 rack pulls 140 kilowatts. There's a reason liquid cooling is now mandatory. Air cooling physically cannot move enough heat out of these racks.

So when Stargate says it needs 7 gigawatts, that's not an engineering choice. It's arithmetic. You want a certain number of Blackwell GPUs, each draws 1,200 watts minimum, the cooling infrastructure adds another 30-40%, and you arrive at a power number that would have seemed absurd for computing five years ago.

### Where the power comes from

This is where it gets complicated.

Meta signed nuclear deals with TerraPower, Oklo, and Vistra. But nuclear plants take 10-15 years to build. Prometheus runs on gas turbines with behind-the-meter generation — meaning Meta generates its own electricity on-site rather than drawing from the grid. Apple's North Carolina facility runs on 82% solar and 12% wind, with biogas fuel cells filling the gap.

Michigan is offering tax exemptions for data centers through 2050. That's not a typo. Through 2050.

The water problem is less discussed. Large facilities use up to 5 million gallons per day for cooling. In water-stressed regions — Arizona, parts of Texas — this is becoming a genuine constraint. Not a theoretical one.

### The GPU bottleneck

Nvidia shipped 150-200 thousand Blackwell units in Q4 2024. By Q1 2025 that ramped to 750-800 thousand. Full-year 2025: 1.5-2 million units. Google, running its own silicon, shipped 2.5 million TPUs in 2025 — 1.9 million v5 and 600 thousand v6. Anthropic alone signed a deal for up to 1 million TPUs with at least 1 gigawatt of capacity.

SK Hynix — the company that makes the high-bandwidth memory these GPUs require — is sold out through 2026 and hiked HBM3E prices 20%. They overtook Samsung in annual profit for the first time: 47.2 trillion won versus 43.6 trillion. The global HBM market is projected to hit $43 billion by 2027.

Every link in this chain is running at capacity.

And then there's CoreWeave. The GPU cloud provider IPO'd in May 2025 at a $23 billion valuation with $55.6 billion in contracted backlog and $14 billion in debt. Their capex runs at 94% of operating cash flow. That's not a growth-stage metric. That's a capital structure that requires perpetual growth to service.

### What nobody's modeling

The total US data center construction spending was $31.5 billion in 2024. The hyperscalers have committed to multiples of that. But the physical constraints don't scale linearly with dollars.

Power generation has lead times. Nuclear: 10-15 years. Gas peaker plants: 2-3 years. Solar and wind: 12-18 months but intermittent. Grid transmission upgrades: 5-7 years and politically contentious.

Skilled labor for high-voltage electrical work, liquid cooling installation, and GPU rack deployment doesn't double because spending doubled. Neither does the permitting process, the environmental review, or the water allocation rights.

I keep running the numbers and landing on the same conclusion. The $600 billion in committed capex implies a build-out timeline that the physical world can't support at the implied pace. Something has to give — either the timeline stretches, the spending slows, or the competition for scarce resources (power, water, HBM, skilled labor) drives costs substantially above what's currently budgeted.

### The question I can't answer

The hyperscalers are betting that AI revenue will justify this spending. Microsoft's AI revenue run rate crossed $13 billion in early 2025. Google's AI-related cloud revenue was similar. But $600 billion in capex needs $60-100 billion in incremental annual revenue just to hit reasonable returns.

That's not impossible. But it requires AI to generate more revenue in the next three years than the entire cloud computing industry generates today.

Maybe it will. The market seems to think so.

But every one of those gigawatts needs a physical wire connecting it to a physical building filled with physical chips cooled by physical water. And right now, some of those wires don't exist yet.
