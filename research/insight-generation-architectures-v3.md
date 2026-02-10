# Deep Research: Systematic Generation of Genuinely Novel Insights

## The Core Problem with Your Current System

Your Insight Generation System v2 is strong at **data-driven pattern recognition** -- the SATURATE-to-VALIDATE pipeline is genuinely good at producing high-Kolmogorov-complexity observations by forcing data-first, framework-second thinking. But as you correctly diagnose, it tends toward "smart framework application." The reason is structural: the system starts with a topic, gathers data about that topic, and finds connections within that data. It never forces the thinker **out of the topic's own conceptual space**. Every step operates within the domain. The anomalies are domain anomalies. The cross-references are cross-track within the same domain. The mechanism is a domain mechanism.

Genuinely novel insights require at least one moment where the thinker is forced to operate **between domains** or **outside the existing conceptual space entirely**. The research below provides specific mechanisms for doing this.

---

## 1. Arthur Koestler's Bisociation

**Source:** _The Act of Creation_ (1964)

### Core Mechanism

Koestler distinguishes **association** (linking ideas within a single frame of reference, which is what your current system does) from **bisociation** (perceiving a situation simultaneously in two previously unrelated frames of reference). He represents this spatially: two "matrices of thought" (M1 and M2) as orthogonal planes, with the creative act occurring at the intersection point where both matrices apply simultaneously.

The critical insight: bisociation is not blending or averaging two ideas. It is perceiving the **same event, idea, or data point** as belonging to two entirely different rule-systems at once. A joke works because the punchline makes you suddenly reinterpret the setup through a second, incompatible frame. A scientific breakthrough works identically -- the emotional charge is different (eureka instead of laughter), but the cognitive mechanism is the same.

Koestler argues that all creative breakthroughs across humor, science, and art share this identical structure. The three differ only in the emotional response: laughter (humor), insight (science), or aesthetic experience (art).

### How It Improves Your System

Your Step 3 (CROSS-REFERENCE) currently looks for connections between data tracks within the same domain. Bisociation would add a **mandatory cross-domain step** where the system must identify a second matrix of thought that is NOT the topic domain and perceive the anomalies through that foreign frame.

### What Step It Modifies

**Modify Step 3: CROSS-REFERENCE** -- Add a sub-step 3B: "Forced Bisociation."

### Specific Implementation

After completing intra-domain cross-referencing (Step 3A, which is your current Step 3), add:

**Step 3B: BISOCIATE**

1. Take the 3-5 strongest anomalies from Step 2
2. For each anomaly, the system must identify a completely unrelated domain where a structurally identical dynamic exists. Not "stablecoins are like banking" (same domain) but "stablecoins are like the East India Company" or "stablecoin reserve dynamics follow the same logic as biological mutualism"
3. The foreign domain must have its own internal logic (its own "matrix of thought" with its own rules)
4. The insight candidate is the statement that is true when you read it through BOTH matrices simultaneously
5. Test: if removing the second matrix doesn't weaken the insight, the bisociation was decorative, not generative

In practice, this means the AI needs to be prompted with something like: _"Take anomaly X. Now forget stablecoins entirely. What other system in biology, physics, military strategy, ecology, game theory, or any non-financial domain exhibits this exact dynamic? Describe the dynamic in the foreign domain first. Then describe how the stablecoin anomaly maps onto it. Then ask: what does the foreign domain predict should happen next that we haven't considered?"_

The last question is where the novel insight lives -- the foreign domain may predict a consequence that is invisible from within the original domain.

### Key Sources

- [The Act of Creation - Wikipedia](https://en.wikipedia.org/wiki/The_Act_of_Creation)
- [How Creativity in Humor, Art, and Science Works - The Marginalian](https://www.themarginalian.org/2013/05/20/arthur-koestler-creativity-bisociation/)
- [Towards Creative Information Exploration Based on Koestler's Concept of Bisociation - Springer](https://link.springer.com/chapter/10.1007/978-3-642-31830-6_2)

---

## 2. The Geneplore Model (Finke, Ward, Smith)

**Source:** _Creative Cognition_ (1992)

### Core Mechanism

The Geneplore model splits creative thinking into two distinct phases that cycle iteratively:

1. **Generative phase**: Produce "preinventive structures" -- loose, incomplete, ambiguous forms that are NOT solutions but have properties that make them promising raw material for solutions. Generated through knowledge retrieval, mental synthesis, analogical transfer, and especially **categorical reduction** (stripping an idea down to its abstract structural skeleton).

2. **Exploratory phase**: Interpret the preinventive structures, test them against constraints, find meaning in them. Processes include hypothesis testing, attribute finding, functional inference, and **contextual shifting** (reinterpreting the structure in a different context).

The critical insight is Finke's "**function follows form**" principle: instead of starting with a goal and searching for solutions (form follows function), you start by generating interesting abstract structures with minimal constraints, THEN look for what they might be useful for. This inverts the normal creative process and is the opposite of what your current system does.

Your current system is goal-directed: "find an insight about stablecoins." Geneplore would say: generate abstract structural patterns first (with minimal domain constraints), then explore whether any of them map onto stablecoins in interesting ways.

### How It Improves Your System

Your system is entirely **function-follows-form**: you start with the topic, gather data about it, and search for insights within it. The Geneplore model suggests adding a **form-follows-function inversion** where you first generate abstract structural patterns (preinventive structures) without any domain constraint, then explore whether they apply.

### What Step It Would Add

**Add a new Step 0: GENERATE PREINVENTIVE STRUCTURES** before SATURATE.

### Specific Implementation

**Step 0: GENERATE PREINVENTIVE STRUCTURES**

Before diving into the topic, generate 10-15 abstract structural patterns. These are domain-agnostic templates of interesting dynamics:

- "A system where the users finance an asset that benefits a third party, and none of the three parties has incentive to change this"
- "A resource that becomes more valuable the more it is given away for free"
- "A middleman who is retained not because they add value but because removing them is more expensive than keeping them"
- "A system where the regulation designed to constrain an actor actually entrenches their position"
- "An entity that hedges against the collapse of the very asset that makes it powerful"

These are **not** insights. They are preinventive structures -- abstract patterns with interesting properties. Generate them by:

1. Abstracting from known examples in completely unrelated domains
2. Inverting known patterns (if X normally leads to Y, what if Y led to X?)
3. Combining two simple dynamics into a compound one
4. Taking a constraint and asking "what if this constraint were the feature, not the bug?"

THEN proceed to SATURATE. During the cross-referencing step, check each preinventive structure against the data. If a preinventive structure maps onto the data in a way that wasn't obvious from the data alone, you have a candidate insight that couldn't have been found by the data-first approach alone.

The key Geneplore principle: **relax constraints during generation, reintroduce them during exploration.** During Step 0, don't worry about whether the structures apply to stablecoins. During Step 3, check rigorously.

### Key Sources

- [Geneplore Model - ScienceDirect](https://www.sciencedirect.com/topics/psychology/geneplore-model)
- [CQ20: Geneplore: theory ready for practical use](https://www.creativityn.com/publication/cq20-geneplore-theory-ready-for-practical-use/)
- [AI-enhanced creative cognition - Gabriele Mirra](https://www.gabrielemirra.com/ai-enhanced-creative-cognition/)

---

## 3. TRIZ (Theory of Inventive Problem Solving)

**Source:** Genrich Altshuller, developed 1946-1985

### Core Mechanism

Altshuller analyzed 400,000+ patents and discovered that inventive breakthroughs share common patterns. His key insight: **most problems that feel unique have already been solved in a different domain.** The difficulty is not in the solution but in recognizing that your problem matches a known pattern.

TRIZ is built on three findings:

1. Problems and solutions repeat across industries
2. Patterns of evolution repeat across industries
3. Innovations use scientific effects from outside their field

The practical tool is the **contradiction matrix**: inventive problems arise when improving one parameter worsens another (a "technical contradiction"). Altshuller's 40 Inventive Principles are generic solution strategies that resolve specific types of contradictions. The matrix maps contradictions to the most likely useful principles.

### How It Applies to Insight Generation in Writing

Several TRIZ principles translate directly to knowledge work:

**Principle 1 (Segmentation):** Break a monolithic concept into independent parts. Instead of "stablecoins are a business," segment into: the reserve function, the minting function, the distribution function, the compliance function, the yield function. Analyze each independently before recombining. Your system already does this with research tracks, but TRIZ would push for finer segmentation.

**Principle 13 (Inversion):** Do the opposite. If everyone analyzes stablecoins as a payments business, analyze them as a sovereign debt distribution mechanism. This is structurally identical to Thiel's "what important truth do very few people agree with you on?"

**Principle 17 (Another Dimension):** Move to a different dimension of analysis. If all commentary operates at the business layer, shift to the geopolitical layer, the sociological layer, or the thermodynamic layer. This is the TRIZ equivalent of bisociation.

**Principle 25 (Self-Service):** Ask what the system can do for itself. What if the insight writes itself? What if the data, properly arranged, makes the conclusion unavoidable without any framework application? This is essentially what your V3 stablecoin insight achieved -- the data points were so specific that arranged together they pointed to only one conclusion.

**Principle 35 (Parameter Change):** Change the state or form of the object of analysis. Instead of analyzing stablecoins as a financial product, analyze them as a protocol, or as a political instrument, or as a demographic phenomenon.

### What Step It Would Modify

**Modify Step 2: FIND ANOMALIES** -- Add a TRIZ contradiction analysis.

### Specific Implementation

After listing anomalies, add a **contradiction identification step**:

For each major player or system in your analysis, ask: "What contradiction does this entity face? What are they trying to improve, and what does improving it necessarily worsen?"

Example: Tether wants regulatory legitimacy (improves trust) but regulatory legitimacy means transparency (worsens their operational flexibility and competitive advantage from opacity). This is a TRIZ-style contradiction. The 40 Principles suggest resolution strategies. Principle 35 (Parameter Change) might suggest: change the form of legitimacy from regulatory compliance to market legitimacy (534.5M users IS legitimacy, regardless of S&P ratings). This reframe was present in your V3 output but arrived accidentally through data examination; TRIZ would make it systematic.

### Key Sources

- [TRIZ - Wikipedia](https://en.wikipedia.org/wiki/TRIZ)
- [40 Principles of Invention - Wikipedia](https://en.wikipedia.org/wiki/40_principles_of_invention)
- [TRIZ in Non-Technical Settings - AITRIZ](https://www.aitriz.org/triz-articles/triz-features/627-non-tech-triz)
- [AutoTRIZ: Artificial Ideation with TRIZ and LLMs](https://arxiv.org/html/2403.13002v2)

---

## 4. Abductive Reasoning (Peirce)

**Source:** Charles Sanders Peirce, 1865-1914

### Core Mechanism

Peirce identified three modes of inference:

- **Deduction:** Given a rule and a case, derive a result (if all A are B, and X is A, then X is B)
- **Induction:** Given many cases and results, derive a rule (X1, X2, X3 are A and are B, therefore all A are probably B)
- **Abduction:** Given a surprising result, infer a case and rule that would explain it (we observe B in a surprising context; if rule R were true and case C held, then B would follow; therefore R and C are worth investigating)

Peirce's canonical formulation: _"The surprising fact C is observed. But if A were true, C would be a matter of course. Hence, there is reason to suspect that A is true."_

The crucial properties of abduction:

1. It is the **only** form of inference that generates new ideas (Peirce: "the only logical operation which introduces any new idea")
2. It is triggered by **surprise** -- an observation that violates expectations
3. It is **ampliative** -- the conclusion goes beyond the premises
4. It is **fallible** -- the hypothesis might be wrong, and that is fine because the purpose is to generate candidates for testing, not to prove truth

Your current system uses abduction implicitly (anomalies are surprising facts, and you look for explanations). But it does not use abduction **deliberately** or **systematically**. The difference matters.

### How It Improves Your System

Your Step 2 (FIND ANOMALIES) identifies surprising facts. Your Step 4 (ARTICULATE MECHANISM) explains them. But the gap between Steps 2 and 4 is where abduction lives, and your system doesn't formalize what happens there. Specifically:

- Your system jumps from "here is a surprising fact" to "here is the mechanism." Abduction says you should first generate **multiple competing hypothetical explanations** for each surprising fact, then test which one explains the most anomalies simultaneously.
- Your system generates one mechanism. Abduction says you should generate 3-5 candidate mechanisms (hypotheses), then use the data to select among them.

### What Step It Would Add/Modify

**Modify Step 4: ARTICULATE MECHANISM** -- Replace with a formal abductive reasoning step.

### Specific Implementation

**Step 4 (revised): ABDUCTIVE HYPOTHESIS GENERATION**

For each anomaly cluster from Step 3:

1. **State the surprise explicitly:** "It is surprising that X, because under the standard model we would expect Y."
2. **Generate 3-5 hypothetical explanations (abductions):** "If hypothesis H1 were true, X would be expected. If H2 were true, X would also be expected. If H3 were true..." Each hypothesis must be a different TYPE of explanation: one structural, one political, one economic, one sociological, one historical.
3. **For each hypothesis, derive what ELSE should be true if this hypothesis is correct.** This is the key move. If the "dollar hegemony" hypothesis is correct, then we should also see [specific prediction]. If the "regulatory capture" hypothesis is correct, we should also see [different specific prediction].
4. **Check the derived predictions against your data from Step 1.** The hypothesis that correctly predicts the most additional data points (especially ones you hadn't flagged as anomalies) is the strongest candidate.
5. **The winning hypothesis IS your mechanism.** It was selected not because it was the first one you thought of, but because it explained the most data with the fewest assumptions.

This is more rigorous than your current process because it prevents the common failure mode of "first explanation that comes to mind is treated as the mechanism." It also naturally produces higher-Kolmogorov-complexity insights because the winning hypothesis must explain MULTIPLE anomalies, not just one.

### Key Sources

- [Abduction - Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/abduction/)
- [Abductive Reasoning - Wikipedia](https://en.wikipedia.org/wiki/Abductive_reasoning)
- [Peirce on Abduction - Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/abduction/peirce.html)
- [Abductive Computational Systems: Creative Abduction and Future Directions](https://arxiv.org/html/2507.08264)

---

## 5. Computational Creativity Research (Boden, ICCC)

**Source:** Margaret Boden, _The Creative Mind_ (1990/2004); ICCC conference series (2010-present)

### Core Mechanism

Boden defines three types of creativity:

1. **Combinational creativity:** Novel combinations of familiar ideas. This is what most brainstorming produces, and what your system currently does well. Combining data points from different research tracks is combinational creativity.

2. **Exploratory creativity:** Systematically exploring a "conceptual space" -- a style, paradigm, or framework -- to discover possibilities within it that nobody has found yet. This is what happens when a jazz musician pushes the boundaries of a musical form without breaking its rules. Your system does this when it exhaustively explores the stablecoin domain.

3. **Transformational creativity:** Changing the rules that define the conceptual space itself, making possible ideas that were literally inconceivable within the old space. This is the rarest and most powerful form. The invention of imaginary numbers (the square root of -1) required transforming the rules of what counts as a "number." Einstein's relativity required transforming the assumption of absolute time.

The critical insight for your system: **your system is currently limited to combinational and exploratory creativity. It never performs transformational creativity because it never questions the rules of its own conceptual space.**

The "rules" your system operates within include:

- The domain is defined by the topic (stablecoins)
- Insights are about the topic
- Data is gathered about the topic
- Frameworks are applied to the topic

Transformational creativity would question these rules themselves: What if the insight is not about stablecoins at all, but about something stablecoins are a symptom of? What if the most important data is data that has nothing to do with stablecoins? What if the right framework hasn't been invented yet?

### What Step It Would Add

**Add a new Step 3C: TRANSFORM THE SPACE** after cross-referencing and bisociation.

### Specific Implementation

**Step 3C: TRANSFORM THE SPACE**

After completing Steps 3A (intra-domain cross-reference) and 3B (bisociation), ask:

1. **What assumptions define the space I've been exploring?** List them. For stablecoins: "This is a financial technology story. The relevant actors are companies. The relevant dynamics are economic. The relevant time scale is years."
2. **What happens if I drop one of these assumptions?**
   - Drop "this is a financial technology story" -- maybe it's actually a geopolitical story, or a demographic story, or a sociological story about trust
   - Drop "the relevant actors are companies" -- maybe the relevant actors are nation-states, or demographics, or protocols
   - Drop "the relevant dynamics are economic" -- maybe the relevant dynamics are political, or cultural, or biological
3. **Does the data look different from inside the transformed space?** If yes, you have a candidate for transformational insight. The Tether-as-dollar-hegemony-instrument insight was partially transformational because it shifted the conceptual space from "fintech company analysis" to "geopolitical analysis."

The test for transformational creativity: Can you point to a specific assumption you dropped that made the insight visible? If yes, it is transformational. If the insight could have been found without dropping any assumptions, it is exploratory or combinational (still valuable, but not the most powerful form).

### LLM-Specific Research Findings

The 2024 Stanford study by [Chenglei Si et al.](https://arxiv.org/abs/2409.04109) (presented at ICLR 2025) found that LLM-generated research ideas were judged **more novel (p<0.05) than human expert ideas** by blind reviewers, but **slightly weaker on feasibility**. This maps directly onto Boden's framework: LLMs are good at combinational creativity (novel combinations at scale and speed) and moderate at exploratory creativity, but they do not naturally perform transformational creativity because they cannot question their own conceptual space without explicit prompting.

The key implication for your system: the novelty-feasibility tradeoff that Si et al. found can be managed by using LLMs for the generative/combinational phases and human judgment for the evaluative/transformational phases. Your model assignment table already captures this intuitively (Opus for Steps 3-4, Sonnet for everything else), but the Boden framework makes explicit WHY: the critical steps require transformational reasoning, and that requires the strongest model operating under the right prompts.

Google's [AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/) (2025) uses self-play debate between agents to generate hypotheses, ranking tournaments to compare them, and evolutionary processes to refine them. Three out of five drug repurposing hypotheses tested in the lab actually worked. Their approach validates the multi-hypothesis abductive approach described in section 4 above.

DeepMind's [FunSearch](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/) combines an LLM with an automated evaluator, using an evolutionary method that promotes and develops the highest-scoring ideas expressed as computer programs. It achieved a genuine mathematical discovery (new solutions to the cap set problem). The key design principle: the evaluator guards against hallucinations while the generator is free to explore broadly. This maps to the Geneplore model's generate-then-explore cycle.

### Key Sources

- [Creativity in a Nutshell - Margaret Boden](https://www.interaliamag.org/articles/margaret-boden-creativity-in-a-nutshell/)
- [Which of the three forms of creativity is GAI capable of?](https://markcarrigan.net/2024/01/22/which-of-the-three-forms-of-creativity-is-gai-capable-of/)
- [Can LLMs Generate Novel Research Ideas?](https://arxiv.org/abs/2409.04109)
- [Accelerating Scientific Breakthroughs with an AI Co-Scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/)
- [FunSearch - Google DeepMind](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/)
- [ICCC'25 Conference](https://computationalcreativity.net/iccc25/)
- [A Survey on LLMs in Scientific Discovery - EMNLP 2025](https://github.com/HKUST-KnowComp/Awesome-LLM-Scientific-Discovery)

---

## 6. Cedric Chin / Commoncog: Tacit Knowledge Extraction

**Source:** [The Tacit Knowledge Series](https://commoncog.com/the-tacit-knowledge-series/), Commoncog

### Core Mechanism

Chin's central argument: genuine expertise is **tacit** -- experts cannot articulate what they actually do. When experts are asked to explain their reasoning, they give post-hoc rationalizations that are systematically different from their actual cognitive processes. This means that **studying what experts say they do is unreliable**; you must study what they **actually** do through specialized extraction techniques.

The key extraction method is **ACTA (Applied Cognitive Task Analysis)**, a simplified version of the full Cognitive Task Analysis used by NDM (Naturalistic Decision Making) researchers:

1. **Task Diagram:** Have the expert decompose the task into 3-6 major steps. Identify which steps are cognitively demanding.
2. **Knowledge Audit:** For each cognitively demanding step, probe using specific questions: What cues do you notice first? What do you expect to happen next? What priorities do you set? What courses of action immediately come to mind?
3. **Simulation Interview:** Present a concrete scenario and walk through the expert's real-time cognitive process as they work through it.
4. **Cognitive Demands Table:** Synthesize the extracted knowledge into a structured table of cues, expectations, goals, and actions.

The four by-products of expert cognition that ACTA extracts are:

- **Cues:** What information does the expert notice that novices miss?
- **Expectancies:** What does the expert expect to happen next?
- **Goals:** What priorities does the expert set in the moment?
- **Courses of action:** What options immediately come to mind?

### How It Improves Your System

Your system currently has no mechanism for extracting the tacit knowledge of domain experts. Step 1 (SATURATE) gathers published data -- facts, numbers, filings. But the most valuable insights often live in the heads of practitioners who cannot articulate them directly. A stablecoin compliance officer knows things about how the system actually works that will never appear in any SEC filing.

The Dreyfus model (which Chin uses) shows that experts operate through pattern recognition and intuition, not through conscious framework application. This means the best insights about a domain are held by people who **cannot explain their reasoning** and would give you frameworks or rationalizations if asked directly.

### What Step It Would Modify

**Modify Step 1: SATURATE** -- Add an expert extraction track.

### Specific Implementation

**Step 1, Track 5: EXPERT TACIT KNOWLEDGE EXTRACTION**

Add a fifth research track that uses ACTA-style probing. In an AI-assisted system, this could work as:

1. **Identify 2-3 tough cases from the domain.** Not routine operations, but moments where an expert had to make a judgment call. For stablecoins: a moment when a compliance officer had to decide whether to flag a transaction. A moment when a treasury manager had to decide how to rebalance reserves. A moment when a product manager had to decide between two integration architectures.

2. **For each tough case, generate the ACTA probes:**
   - What cues would an expert notice that a novice would miss?
   - What would an expert expect to happen next?
   - What priorities would an expert set?
   - What course of action would an expert take, and why?

3. **If you don't have direct access to experts, simulate this through research:** Look for interviews, podcasts, and conference talks where domain experts describe specific incidents (not general principles). Practitioners on podcasts sometimes reveal tacit knowledge when describing what they actually did in a specific situation, even though they can't articulate the general principle.

4. **The output is a Cognitive Demands Table:** for each tough case, a structured record of cues, expectancies, goals, and actions that an expert would produce.

The insight value: tacit knowledge often reveals dynamics that are invisible in published data. An expert might mention offhandedly that "we always check X before Y" -- and that sequencing reveals a causal dependency that no published source mentions.

### Key Sources

- [The Tacit Knowledge Series - Commoncog](https://commoncog.com/the-tacit-knowledge-series/)
- [An Easier Method for Extracting Tacit Knowledge - Commoncog](https://commoncog.com/an-easier-method-for-extracting-tacit-knowledge/)
- [Copying Better: How To Acquire The Tacit Knowledge of Experts](https://commoncog.com/how-to-learn-tacit-knowledge/)
- [Cedric Chin interview - Todd Nief](https://toddnief.com/cedric-chin-interview/)

---

## 7. Gary Klein: Triple Path Model of Insight

**Source:** _Seeing What Others Don't: The Remarkable Ways We Gain Insights_ (2013)

### Core Mechanism

Klein collected 120 real-world cases of insight and discovered that insights arrive through three distinct paths, each with a different cognitive mechanism:

**Path 1: Connections.** You encounter a new piece of information that serves as a "new anchor" -- you connect it to existing knowledge and the implications cascade. Trigger: noticing a coincidence, curiosity, or unexpected connection. Mechanism: adding a new anchor to your belief structure and working out implications. Your current system's Step 3 (CROSS-REFERENCE) is primarily a Connection Path process.

**Path 2: Contradictions.** You notice an inconsistency in the accepted story. Something doesn't fit. You take a "weak anchor" (a minor detail that was previously dismissed) and use it to rebuild the entire narrative. Trigger: spotting an inconsistency. Mechanism: elevating a previously minor data point to a central role in a reconstructed story. Your current system's Step 2 (FIND ANOMALIES) partially uses the Contradiction Path, but it doesn't formalize the crucial move of **elevating** the contradiction to a new central anchor.

**Path 3: Creative Desperation.** You are stuck at an impasse. The existing approach cannot work. In desperation, you discard a foundational assumption (a "weak anchor") and the problem restructures itself. Trigger: an impasse that forces reframing. Mechanism: discarding a constraint that had been assumed to be inviolable. This path is almost entirely absent from your current system.

The key insight: these three paths require **different mindsets**:

- Connection requires an **open, inquiring** stance
- Contradiction requires a **critical, skeptical** stance
- Creative Desperation requires a **highly focused** stance under pressure

Your system currently optimizes for the Connection mindset (open, gathering, cross-referencing). It partially uses the Contradiction mindset (anomaly detection). It never uses the Creative Desperation mindset.

### What Step It Would Add

**Add Step 2.5: FORCED IMPASSE** between FIND ANOMALIES and CROSS-REFERENCE.

### Specific Implementation

**Step 2.5: FORCED IMPASSE (Creative Desperation Path)**

After identifying anomalies but before cross-referencing:

1. **State the best explanation you currently have for the domain.** Write it out as a complete narrative.
2. **Deliberately construct an impasse:** Identify the ONE assumption in your narrative that, if false, would make the entire narrative collapse. Not a peripheral assumption -- the load-bearing one.
3. **Remove that assumption.** Pretend it is false.
4. **Attempt to explain all the data WITHOUT that assumption.** This is the impasse. You are stuck because your primary explanation no longer works.
5. **The insight, if one comes, arrives as a restructuring of the entire problem.** The data hasn't changed; the frame has.

Example from the stablecoin case: The load-bearing assumption in most stablecoin analysis is "stablecoins are a financial product." Remove it. Pretend stablecoins are NOT a financial product. What are they? If you are forced to explain all the data (the user numbers, the T-bill holdings, the political connections, the geographic distribution) without the assumption that this is a financial product, you might arrive at: "stablecoins are a dollarization instrument" -- which is a fundamentally different framing that opens new insight space.

Klein also found that **four factors block insight**: flawed core beliefs, lack of experience, passive stance, and concrete reasoning style. Your system can address the first (by explicitly identifying and challenging core beliefs), the third (by requiring active hypothesis generation), and the fourth (by explicitly prompting for speculative, hypothetical reasoning).

### Key Sources

- [Gary Klein's Triple Path Model of Insight - Farnam Street](https://fs.blog/the-remarkable-ways-we-gain-insights/)
- [Insight - garyklein.com](https://www.gary-klein.com/insight)
- [Adopting the Klein Triple Path Model - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10887486/)
- [3 Paths Revolutionary Thinkers Take - The Emotion Machine](https://www.theemotionmachine.com/the-triple-path-model-of-insight-how-revolutionary-thinkers-arrive-at-insights/)

---

## 8. Edward de Bono: Lateral Thinking

**Source:** _Lateral Thinking: A Textbook of Creativity_ (1970), _PO: Beyond Yes and No_ (1972)

### Core Mechanism

De Bono argues that the mind is a self-organizing pattern-recognition system. Once a pattern is established, the mind follows it automatically. This is efficient for routine thought but fatal for creative thought, because the mind cannot escape its own patterns without deliberate intervention.

Lateral thinking is a set of **systematic techniques** for disrupting established patterns. The key techniques:

**Provocation (PO):** Deliberately create an absurd or illogical statement, prefixed with "PO" (Provocative Operation), which signals to suspend judgment. The statement is not a proposal -- it is a stepping stone. Methods for creating provocations:

- **Escape:** Remove a feature everyone takes for granted ("PO: stablecoins without a reserve")
- **Reversal:** Invert a normal relationship ("PO: the users pay the stablecoin issuer to take their money")
- **Exaggeration:** Push a dimension to an extreme ("PO: a stablecoin backed by $10 trillion in reserves")
- **Distortion:** Change a normal sequence or relationship ("PO: the reserve yield goes to the users instead of the issuer")
- **Wishful thinking:** State an impossible ideal ("PO: every person in the developing world has a dollar-denominated savings account")

**Movement:** After creating a provocation, use "movement" techniques to extract useful ideas from the absurd statement:

- Extract a principle
- Focus on the difference from current reality
- Examine the moment-to-moment implications
- Find positive aspects

De Bono's famous example: "PO: the factory is downstream of itself." This absurd provocation (a factory cannot be both upstream and downstream of itself) led to the insight that factories should be required to take their water input from downstream of their waste output, forcing them to clean their own waste. This became actual law in some countries.

### How It Improves Your System

Your system has no mechanism for **deliberate absurdity**. Every step is rational and data-driven. This is a strength for producing high-Kolmogorov-complexity insights but a weakness for producing genuinely surprising reframes. De Bono's provocation technique adds systematic absurdity as a tool.

### What Step It Would Add

**Add Step 3D: PROVOCATION** after bisociation and before mechanism articulation.

### Specific Implementation

**Step 3D: PROVOCATION (PO)**

After cross-referencing and bisociation, generate 5 provocations using de Bono's methods:

1. **Escape:** "PO: [remove the thing everyone takes for granted about the domain]"
2. **Reversal:** "PO: [invert the primary relationship in the domain]"
3. **Exaggeration:** "PO: [push the dominant trend to 100x its current level]"
4. **Distortion:** "PO: [change who benefits from the primary mechanism]"
5. **Wishful thinking:** "PO: [state the impossible ideal outcome]"

For each provocation, apply movement:

- What principle can be extracted from this absurd statement?
- What is different about the world the provocation describes vs. the real world?
- Is there a version of this provocation that is actually achievable?

Example: "PO: Tether pays 5% yield to all 534.5M users." This is currently impossible (GENIUS Act prohibits it, and the yield is Tether's primary profit source). But the movement from this provocation might lead to: "What if someone else could pay yield on stablecoins that the issuer won't? DeFi protocols already do this. The insight: the yield gap between what issuers earn and what holders receive is a $10B+ annual opportunity that DeFi is already capturing, which means stablecoin issuers are losing economic value to the application layer, which strengthens the 'user relationship > reserves' thesis."

The provocation didn't produce the insight directly. It created a **stepping stone** that directed attention to a dynamic (the yield gap) that might not have been salient otherwise.

### Key Sources

- [Lateral Thinking - De Bono Group](https://www.debonogroup.com/services/core-programs/lateral-thinking/)
- [Lateral Thinking - Wikipedia](https://en.wikipedia.org/wiki/Lateral_thinking)
- [How can Lateral Thinking help you? - Edward de Bono](https://www.edwddebono.com/lateral-thinking)
- [Lateral Thinking: A Textbook of Creativity - Internet Archive](<https://ia802901.us.archive.org/10/items/teachyourchildhowtothink.byedwarddebono/Lateral%20Thinking%20A%20Textbook%20of%20Creativity%20by%20Edward%20de%20Bono(1990).pdf>)

---

## 9. Recent LLM Research on Insight/Hypothesis Generation (2024-2026)

### Key Findings

**Finding 1: LLMs are genuinely novel but less feasible.** The [Si et al. ICLR 2025 study](https://arxiv.org/abs/2409.04109) with 100+ NLP researchers found LLM ideas statistically more novel than human expert ideas (p<0.05) but slightly weaker on feasibility. The correlation between overall score and novelty was r=0.725, while correlation with feasibility was r<0.1 -- meaning reviewers valued novelty far more than feasibility when rating overall quality.

**Finding 2: LLM "hallucinations" may be useful as hypotheses.** A [2025 study in the Journal of the Royal Society Interface](https://royalsocietypublishing.org/rsif/article/22/227/20240674/235871/Scientific-hypothesis-generation-by-large-language) tested GPT-4-generated drug combination hypotheses in actual lab experiments. Three out of twelve first-round hypotheses showed synergy above positive controls. The authors concluded that "LLM hallucinations, which are harmful in many applications, may in science be useful as novel hypotheses whose validity can be tested by laboratory experiments."

**Finding 3: Knowledge graphs improve hypothesis grounding.** The KG-CoI (Knowledge-Grounded Chain-of-Idea) approach combines knowledge graphs with LLMs to ground hypothesis generation in established knowledge while still allowing novel connections. This addresses the feasibility gap.

**Finding 4: Multi-agent debate improves hypothesis quality.** Google's [AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/) uses self-play debate between specialized agents, with 3 of 5 drug repurposing hypotheses validated in the lab. The architecture uses a Supervisor agent, specialized worker agents, ranking tournaments, and evolutionary refinement.

**Finding 5: Evolutionary search over programs works.** DeepMind's [FunSearch](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/) achieved genuine mathematical discovery by combining LLM generation with automated evaluation in an evolutionary loop. The key: expressing ideas as evaluable programs rather than natural language allows automated quality filtering.

**Finding 6: LLMs can retrieve the right "inspiration knowledge."** The MOOSE-Chem project showed that LLMs trained on pre-2023 papers could retrieve the correct inspiration sources for 2024 chemistry discoveries at a very high rate, suggesting that the knowledge for novel discoveries is often already in the model's training data and the challenge is retrieval and recombination, not creation of new knowledge.

### How This Improves Your System

**Implication 1: Add multi-agent debate.** Instead of a single cross-referencing step, have multiple AI agents each generate a competing hypothesis and debate each other. The debate process itself generates novel angles that a single pass misses. This is compatible with your existing multi-agent architecture.

**Implication 2: Treat hallucinations as hypothesis candidates.** During the generative phase, explicitly allow the system to generate "what if" explanations that may not be grounded in verified data. Then subject them to rigorous verification in the validation phase. Currently, your system's research agents are instructed to return facts, not speculation. Adding a "speculative hypothesis" agent that is explicitly licensed to speculate (and labeled as such) could expand the hypothesis space.

**Implication 3: Express insights as evaluable claims.** FunSearch's key insight is that expressing ideas in a form that can be automatically evaluated enables evolutionary refinement. For your system, this means expressing insight candidates as specific, falsifiable predictions (which you already do in Step 5) and then automatically checking those predictions against data.

### What Step It Would Modify

**Modify Step 3: CROSS-REFERENCE** -- Add multi-agent debate architecture.

### Specific Implementation

**Step 3 (enhanced): MULTI-AGENT CROSS-REFERENCE**

1. Agent A receives all research data and generates Hypothesis 1 with supporting argument
2. Agent B receives the same data and is prompted to find the STRONGEST alternative to Hypothesis 1
3. Agent C acts as judge, identifying which pieces of evidence each hypothesis explains and fails to explain
4. The "winner" is not the hypothesis with the most support, but the one with the least disconfirming evidence (following ACH logic from your existing framework)
5. A fourth "speculative" agent is licensed to generate a hypothesis that is NOT well-supported by current data but would, if true, explain all the anomalies simultaneously. This agent's output is explicitly labeled as speculative and subjected to extra scrutiny in validation.

### Key Sources

- [Can LLMs Generate Novel Research Ideas?](https://arxiv.org/abs/2409.04109)
- [Scientific hypothesis generation by LLMs - Royal Society Interface](https://royalsocietypublishing.org/rsif/article/22/227/20240674/235871/Scientific-hypothesis-generation-by-large-language)
- [Exploring the role of LLMs in the scientific method - npj AI](https://www.nature.com/articles/s44387-025-00019-5)
- [Google AI Co-Scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/)
- [FunSearch - DeepMind](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/)
- [LLM Scientific Discovery Survey - EMNLP 2025](https://github.com/HKUST-KnowComp/Awesome-LLM-Scientific-Discovery)
- [AI co-scientist - deeplearning.ai summary](https://www.deeplearning.ai/the-batch/ai-co-scientist-an-agent-that-generates-research-hypotheses-aiding-drug-discovery/)

---

## Synthesis: The Upgraded System

Here is how all nine research areas integrate into an upgraded Insight Generation System v3:

### INSIGHT GENERATION SYSTEM v3

**Step 0: GENERATE PREINVENTIVE STRUCTURES** (NEW -- from Geneplore)

- Generate 10-15 domain-agnostic abstract structural patterns
- Relax all constraints; do not think about the topic yet
- Use categorical reduction, inversion, combination of simple dynamics
- Model: Sonnet (this is generative, not evaluative)

**Step 1: SATURATE** (MODIFIED -- add Track 5 from Chin/ACTA)

- Tracks 1-4: same as v2 (money flow, power structure, regulation, comparative)
- Track 5 (NEW): Expert tacit knowledge extraction -- find practitioner accounts of specific tough cases, extract cues/expectancies/goals/actions
- Model: Sonnet for all tracks

**Step 2: FIND ANOMALIES** (MODIFIED -- add TRIZ contradiction analysis)

- Same anomaly detection as v2
- NEW: For each major player/system, identify the TRIZ contradiction (improving X worsens Y)
- NEW: Apply TRIZ inventive principles to suggest resolution strategies
- Model: Sonnet

**Step 2.5: FORCED IMPASSE** (NEW -- from Klein's Creative Desperation Path)

- State the best current explanation as a complete narrative
- Identify the ONE load-bearing assumption
- Remove that assumption and attempt to explain all data without it
- If a restructured explanation emerges, it is a candidate insight
- Model: Opus (this requires strong reasoning)

**Step 3A: CROSS-REFERENCE** (same as v2)

- Find intersections between research tracks
- Model: Opus

**Step 3B: BISOCIATE** (NEW -- from Koestler)

- Take top anomalies and find structurally identical dynamics in completely unrelated domains
- Ask: what does the foreign domain predict should happen next?
- Model: Opus

**Step 3C: TRANSFORM THE SPACE** (NEW -- from Boden)

- List the assumptions that define your current conceptual space
- Drop one assumption at a time
- Check if the data looks different from inside the transformed space
- Model: Opus

**Step 3D: PROVOCATION** (NEW -- from de Bono)

- Generate 5 provocations (escape, reversal, exaggeration, distortion, wishful thinking)
- Apply movement techniques to extract usable principles
- Model: Sonnet (generation), Opus (movement/evaluation)

**Step 3E: MULTI-AGENT DEBATE** (NEW -- from computational creativity research)

- Agent A generates Hypothesis 1
- Agent B generates the strongest alternative
- Agent C judges based on evidence explained/not explained
- Agent D (speculative) generates an unsupported but comprehensive hypothesis
- Model: Opus for all agents

**Step 4: ABDUCTIVE HYPOTHESIS SELECTION** (MODIFIED -- from Peirce)

- For each candidate insight from Steps 3A-3E, generate 3-5 candidate mechanisms
- For each mechanism, derive what ELSE should be true
- Select the mechanism that correctly predicts the most additional data points
- Model: Opus

**Step 4.5: CHECK PREINVENTIVE STRUCTURES** (NEW -- from Geneplore)

- Revisit Step 0's abstract patterns
- Does any preinventive structure map onto the data in a way that adds to the insight?
- If yes, this is a "function follows form" discovery -- the abstract pattern preceded the data
- Model: Sonnet

**Step 5: PREDICT** (same as v2)

- Model: Sonnet

**Step 6: VALIDATE** (MODIFIED -- add Klein's four blockers check)

- Same validation as v2 (Kolmogorov, template, pre-mortem, "wait that means...")
- NEW: Check for Klein's four insight blockers: Are we gripped by a flawed core belief? Are we lacking relevant experience? Are we being passive? Are we reasoning too concretely?
- Model: Haiku for mechanical checks, Sonnet for pre-mortem and blocker analysis

### Cost and Complexity Tradeoff

The full v3 system is substantially more complex than v2. Not every analysis needs every step. The recommendation:

**Tier 1 (Quick analysis, 30 min, ~$5-7):** Steps 1-2, 3A, 4, 5, 6. This is essentially v2. Use for time-sensitive or lower-stakes pieces.

**Tier 2 (Deep analysis, 60-90 min, ~$10-15):** Add Steps 2.5 (Forced Impasse), 3B (Bisociation), and 4 (Abductive Hypothesis Selection). These three additions produce the highest marginal return on insight quality.

**Tier 3 (Maximum insight, 2-3 hours, ~$20-30):** Full v3 pipeline. Use for flagship content, annual predictions, or any piece where genuinely novel thinking is the primary goal.

The highest-ROI additions are:

1. **Forced Impasse (Step 2.5)** -- forces restructuring of the problem
2. **Bisociation (Step 3B)** -- forces cross-domain thinking
3. **Abductive Hypothesis Selection (Step 4)** -- forces multiple competing explanations

These three changes address the specific weakness you identified ("smart framework application rather than genuinely novel thinking") because each one introduces a mechanism that **cannot produce framework application as output.** Forced Impasse requires discarding frameworks. Bisociation requires importing a foreign frame. Abductive selection requires generating multiple competing explanations rather than accepting the first one.

---

## Summary Table

| Research Area                    | Core Mechanism                                                                                              | Step Modified/Added                       | Key Implementation Idea                                                                                              |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Koestler (Bisociation)           | Perceive data through two unrelated frames simultaneously                                                   | Add Step 3B: BISOCIATE                    | For each anomaly, find a structurally identical dynamic in an unrelated domain; ask what the foreign domain predicts |
| Geneplore (Finke et al.)         | Generate abstract structures first, find applications second                                                | Add Step 0: PREINVENTIVE STRUCTURES       | Generate domain-agnostic patterns before research; check them against data later                                     |
| TRIZ (Altshuller)                | Inventive problems are contradictions; contradictions have known resolution patterns                        | Modify Step 2: add contradiction analysis | For each player, identify what improving X worsens Y; apply inventive principles                                     |
| Peirce (Abduction)               | Surprise triggers hypothesis generation; select hypothesis that explains most data                          | Modify Step 4: formal abductive selection | Generate 3-5 competing mechanisms; derive additional predictions from each; select by evidence fit                   |
| Boden (Computational Creativity) | Three types: combinational, exploratory, transformational; the last changes the rules of the space          | Add Step 3C: TRANSFORM THE SPACE          | List assumptions defining the conceptual space; drop one at a time; check if data looks different                    |
| Chin/Commoncog (Tacit Knowledge) | Expert knowledge is tacit and must be extracted through specialized techniques                              | Modify Step 1: add Track 5                | Use ACTA probes to extract cues/expectancies/goals/actions from practitioner accounts                                |
| Klein (Triple Path Model)        | Insights come through connections, contradictions, or creative desperation; each requires different mindset | Add Step 2.5: FORCED IMPASSE              | Identify load-bearing assumption; remove it; attempt to explain data without it                                      |
| De Bono (Lateral Thinking)       | Systematic provocation disrupts established patterns                                                        | Add Step 3D: PROVOCATION                  | Generate 5 provocations using escape/reversal/exaggeration/distortion/wishful thinking; apply movement               |
| LLM Research (2024-2026)         | Multi-agent debate; hallucinations as hypotheses; evolutionary selection                                    | Add Step 3E: MULTI-AGENT DEBATE           | Competing agents generate hypotheses; judge selects by evidence; speculative agent expands search space              |
