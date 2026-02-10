# Compression Substitution

## Insight V3

---

Last issue I wrote about the two timescales of AI disruption — the fast clock of capability improvements and the slow clock of institutional adaptation. I spent all that time looking at what AI does to industries and jobs. I should have been looking at what it does to the people.

### The 39-point gap

METR recruited 16 experienced open-source developers in mid-2025. Not juniors — people with 5+ years of contributions to the specific repositories they were tested on. Real tasks in their own codebases, randomized into AI-assisted and unassisted conditions.

Before each task, they predicted they'd be about 24% faster with AI. Afterward, they estimated 20% faster.

The objective measurement: 19% slower.

Not a rounding error. A 39-point gap between what they perceived and what actually happened. And 69% kept using Cursor after the study ended.

That second number is the one I keep coming back to. It's not just that the tool made them slower. The feeling of productivity completely decoupled from actual productivity, and they couldn't tell. The metacognitive channel — the part of your mind that monitors how well you're doing — was compromised.

### Across domains

People who wrote with ChatGPT couldn't recall their own essays afterward. 83% couldn't quote a single passage from work they'd just submitted. Brain activity associated with memory encoding was significantly weaker than in people who wrote by hand.

Same pattern in code. GitClear analyzed 211 million lines of changed code and found that Copilot-assisted code was 5% more likely to pass individual review. Looks great at the pull request level. But across the whole codebase, refactoring collapsed — from 24% to under 10% of changed lines. Copy-paste code nearly doubled. Each PR looked fine. The architecture was rotting.

Divergent thinking scores among college students dropped 42% over five years. Raters judging AI-assisted creative writing scored it 15-26% higher on "creativity."

Every metric we optimize for is improving. Every metric we don't measure is degrading.

### The pipeline

The individual effects worry me. The structural ones worry me more.

Brynjolfsson studied 5,179 customer service agents. AI boosted novice performance by 34%. Experts barely moved. Same in a study of Japanese taxi drivers — 7% for low-skilled, near-zero for high-skilled.

Then look at hiring. Entry-level tech jobs dropped 50% between 2019 and 2024. Junior developer roles went from 43% of postings to 28%. Bootcamps started shutting down.

If AI performs at the level of a junior with two years of experience, an actual junior with zero years has negative marginal value. Companies stop hiring them. But those junior years were where people built the mental models that eventually made them experts. The middle rungs of the ladder are being removed while people are still climbing it.

When I wrote about the handloom weavers last issue, I was looking at wage effects. I should have been looking at skill formation. The weavers' skills didn't atrophy — a machine made them irrelevant. What's happening now is subtler: the pathway to acquiring skills is being closed.

### Where it converges

At the population level, something different is happening. Wharton ran an experiment where individuals using ChatGPT for brainstorming produced ideas rated more creative and more original. But across participants, the AI-assisted ideas were more similar to each other. Individual creativity up. Collective diversity down.

This follows from how LLMs work. RLHF pushes outputs toward the mode of the training distribution — the average of human preferences. Temperature sampling, which everyone recommends for "more creative" outputs, increases surface variation (different words) without increasing structural variation (different frameworks). One study found temperature had zero effect on typicality, the measure that actually captures novelty.

And there's a feedback loop. 74% of newly published web pages contain AI-generated content. LLMs train on LLM output. Model collapse research shows that by the ninth generation of AI training on AI outputs, the model produces gibberish. We're not at nine. But we're past one.

Juergen Schmidhuber published a theory of curiosity in 2009 that keeps surfacing as I work through this data. Learning IS compression, he argued. When you encounter something confusing — a messy codebase, a regulatory framework, a market you don't understand — your brain compresses that mess into a mental model. The drive to compress is what we experience as curiosity. The satisfaction when it works is understanding.

There's a formal version. Kolmogorov complexity defines the complexity of something as the length of the shortest program that can reproduce it. Your mental model of a domain is a compression program. When an experienced developer looks at an unfamiliar codebase and "gets it" in twenty minutes, that's their compressor — built over years of struggling with other codebases — running on new input.

LLMs hand you the compressed output directly. You get the product of compression without doing the compressing. And the compressing — the struggle to find the pattern — is what builds the compressor. The product of cognitive compression is being substituted for the process. The process is where expertise, memory, creativity, and judgment actually form.

Which explains the METR result. The developers got answers faster but completed tasks slower — they'd imported a model of the code they didn't build, and it didn't integrate with the mental models they'd spent years constructing.

People will say we've heard this before. Calculators, Google, spell-checkers. Socrates warning that writing would destroy memory. And yes, he was wrong. But calculators offload arithmetic — the conceptual work stays with you. GPS offloads navigation — you still decide where to go. Google offloads retrieval — you still formulate the question. LLMs offload the structuring of thought itself. The deeper the offload, the worse the cognitive effect — which is probably why the "Google Effect" on memory failed to replicate in a 2018 study, while GPS effects on spatial memory have held up consistently across labs.

And with calculators, you could tell when you needed to go back to manual. The METR data shows a 39-point perception-reality gap. You can't choose unassisted thinking if you can't perceive that assisted thinking is making you worse.

Air France 447. The captain logged 346 hours over six months, about 4 hours manually. When autopilot switched to a degraded mode — not a full failure, partial — the pilots stalled the airplane. They knew what to do. Their certifications said so. Knowledge without fluency, under stress, killed 228 people. No calculator ever did that. No previous tool corrupted the channel that tells you your skills have degraded.

### What I'm trying

Honestly, I don't know what the right response looks like. The most concrete thing I've found is Robert Bjork's work on "desirable difficulties" — tasks that feel harder produce better long-term retention. The difficulty IS the learning mechanism.

I've been experimenting with a system prompt that forces Claude into Socratic mode in domains where I'm building expertise. No answers, just questions back. It's annoying. It also noticeably changes what I remember afterward. I'll share a version with subscribers next issue.

Whether any of this is enough, I don't know.

### How to check if I'm wrong

The perception-reality gap should widen with usage duration, not narrow. If people "calibrate" to the tool over time — if the gap shrinks — I'm wrong about the most alarming part.

Fields with high LLM adoption for ideation should show declining variance in published novelty scores within three years. This follows directly from how RLHF works.

The one I'd bet most on: companies that cut 30%+ of junior roles between 2023 and 2025 will underperform on innovation by 2028-2030. Slowest to resolve. But if the pipeline argument holds, it shows up within five years.

---

— Jin Fernando
