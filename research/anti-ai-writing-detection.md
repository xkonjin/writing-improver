# Research Report: Making Writing NOT Sound AI-Generated
## Maximum Information Density + Unmistakably Human Voice

---

## 1. AI WRITING TELLS -- What Patterns Make Text Obviously AI-Generated

### 1.1 The Overused Word List (The "AI Lexicon")

Research from GPTZero's analysis of 3.3 million texts, Wikipedia's Signs of AI Writing page, Pangram Labs, and multiple compiled lists reveals a specific vocabulary fingerprint. These words appear anywhere from 2x to 269x more frequently in AI text than in human text.

**TIER 1: INSTANT RED FLAGS (the words that scream "AI wrote this")**

| Category | Words |
|----------|-------|
| **Verbs** | delve, embark, leverage, utilize, navigate, harness, foster, underscore, elucidate, illuminate, transcend, unveil, resonate, elevate, optimize, streamline, supercharge, unleash |
| **Adjectives** | robust, comprehensive, intricate, pivotal, crucial, vital, seamless, cutting-edge, vibrant, dynamic, innovative, transformative, unprecedented, compelling, nuanced, daunting, remarkable, state-of-the-art |
| **Nouns** | tapestry, landscape, realm, beacon, journey, paradigm, synergy, interplay, testament, intersection, metropolis |
| **Adverbs** | seamlessly, notably, significantly, meticulously, profoundly, arguably |

**TIER 2: PHRASE-LEVEL TELLS (GPTZero frequency data)**

| Phrase | AI/Human Frequency Ratio |
|--------|--------------------------|
| "objective study aimed" | 269x more common in AI |
| "play a significant role in shaping" | 182x |
| "notable works include" | 120x+ |
| "today's fast-paced world" | 107x |
| "aims to explore" | 50x+ |
| "showcasing" | 20x |
| "remarked" | 18x |
| "aligns" | 16x |

Source: [GPTZero - Top 10 Most Common Words Used by AI](https://gptzero.me/news/most-common-ai-vocabulary/)

**TIER 3: FORMULAIC OPENINGS AND CONNECTORS**

- "In today's digital age..."
- "It's important to note..."
- "It's worth mentioning..."
- "When it comes to..."
- "In the world of..."
- "No discussion would be complete without..."
- "Dive into..."
- "Delving into the intricacies of..."
- "Navigating the complexities of..."
- "A testament to..."
- "Pave the way for..."
- "At the forefront of..."
- "Unlock the potential of..."

**TIER 4: TRANSITION WORD ABUSE**

AI paragraphs disproportionately begin with: "Furthermore," "Moreover," "Additionally," "Consequently," "Subsequently," "Notably," "Indeed," "However," "In contrast," "On the other hand," "That being said."

A key finding: AI-generated essays are far more likely than human-written essays to begin paragraphs with "Furthermore," "Moreover," and "Overall" (Source: [Inside Higher Ed](https://www.insidehighered.com/opinion/career-advice/teaching/2024/07/02/ways-distinguish-ai-composed-essays-human-composed-ones)).

### 1.2 Sentence Structure Patterns

**The Trailing Present Participle** -- This is one of the most distinctive AI tells. AI ends sentences with dangling "-ing" clauses that make vague claims about significance:

- "...emphasizing the importance of diversity"
- "...highlighting the need for continued innovation"
- "...reflecting the continued relevance of traditional approaches"
- "...ensuring that all stakeholders benefit"
- "...showcasing the potential for transformative change"

This structure follows the formula: `subject + verb + object, present participle + additional detail`. Human writers rarely end sentences this way consistently. Source: [Wikipedia: Signs of AI Writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)

**Uniform Sentence Length / Low Burstiness.** AI produces sentences of remarkably consistent length (typically 10-15 words). Human writing has high standard deviation in sentence length per paragraph -- mixing 3-word punches with 30-word elaborations. AI text has flat, regular rhythm. Human text has bursts and lulls. Source: [Originality.ai - Perplexity and Burstiness](https://originality.ai/blog/perplexity-and-burstiness-in-writing)

**The "Subject + Is + Adjective" Default.** AI defaults to simple declarative structures: "This approach is innovative." "The framework is comprehensive." "The results are significant." Human writers use more varied syntactic constructions.

### 1.3 Rhetorical Patterns AI Defaults To

Colin Gorrie's rhetorical analysis ([Why ChatGPT Writes Like That](https://www.deadlanguagesociety.com/p/rhetorical-analysis-ai)) identifies three rhetorical devices LLMs abuse compulsively:

**1. Contrastive Parallelism with Identity Reframing**
This is identified as THE signature AI pattern. The structure: "You are not just X, you are Y."

Examples:
- "You're not just surviving -- you're mastering"
- "It's not about problem-solving -- it's about reshaping possibilities"
- "Not just following trends, but setting them"
- "Failure isn't the end -- it's the foundation"

The pattern flatters the reader while repositioning them in an "empowering light." Humans vary their rhetorical approaches organically; AI deploys this in nearly every other paragraph. Source: [Contrastive Parallelism as AI Signature](https://www.layng.ai/contrastive-parallelism-with-identity-reframing-a-signature-of-ai-writing/)

**2. Antithesis Overuse ("It's Not X, It's Y")**
JFK's "Ask not what your country can do for you -- ask what you can do for your country" works because it's deployed once, at the climax. AI deploys explicit negation antithesis (`not...but`) in every section. Human writers use implicit contrast more often -- trusting the reader to see the opposition without spelling it out. LLMs always spell it out with "not" or "isn't."

**3. The Ascending Tricolon (Rule of Threes)**
"Life, liberty, and the pursuit of happiness" is powerful because it's rare. AI arranges concepts in threes compulsively: "efficiency, innovation, and growth." The constant application eliminates its special character.

Gorrie's core diagnosis: **"What the LLM lacks is not technical ability, but taste."** These devices work when deployed selectively. LLMs saturate text with them indiscriminately.

**4. The Motivational Closer.** AI defaults to ending paragraphs, sections, and posts with uplifting, forward-looking statements. "The future is bright." "Together, we can achieve more." "This is just the beginning." Human writers end with ambiguity, questions, discomfort, or nothing at all.

**5. The "Challenges" Section Pattern (from Wikipedia analysis).** AI articles frequently include a section that begins: "Despite its [positive words], [subject] faces challenges..." and ends with either vague optimism or speculation. This is structural filler that sounds balanced but says nothing.

### 1.4 Formatting Patterns

- **Too-perfect structure.** AI produces evenly balanced sections with uniform paragraph lengths. Human writing is asymmetric -- some sections are long, some are two sentences.
- **Excessive bold text.** AI bolds key terms predictably. Often the bolded word is then repeated verbatim in the following sentence.
- **Bullet points with bold headers.** The format of `**Bold Title:** Description that repeats the bold title` is a near-certain AI marker.
- **Em-dash overuse.** ChatGPT and some models use em dashes where humans would use commas, parentheses, or just restructure the sentence. Source: [Plagiarism Today - Em Dashes and AI](https://www.plagiarismtoday.com/2025/06/26/em-dashes-hyphens-and-spotting-ai-writing/)
- **Curly quotation marks.** ChatGPT and DeepSeek use curly/"smart" quotes where straight quotes would be more typical in casual writing.
- **Perfect grammar always.** AI never starts a sentence with "And" or "But." It never uses fragments. It never breaks grammatical rules for effect. Human writing breaks rules constantly and deliberately.

### 1.5 The "LinkedIn AI Slop" Aesthetic

Sean Goedecke's analysis ([Why Does AI Slop Feel So Bad to Read?](https://www.seangoedecke.com/on-slop/)) identifies the core mechanism:

**AI slop feels terrible because it creates an unpleasant mental shift from human-to-human interaction to human-to-machine interaction.** The reader invested effort in engaging at a human level with something that isn't human.

Specific markers of LinkedIn slop:
- Too many emojis used as bullet points
- Markdown formatting that doesn't render (literal asterisks, hash marks)
- The "motivational post" formula: short line, short line, short line, then a "kicker"
- Fragmented sentences presented as profound
- Every post ends with "Agree?" or "Thoughts?" or "Curious what others think"
- Excessive use of "Here's the kicker" / "And honestly? That's rare" / "You're not imagining it"

The deeper problem: **AI gives the median response.** It produces the most down-the-line, uncontroversial, safe answer. Real human writing has an intellectual edge -- a perspective, a bias, an angle. AI writing is deliberately neutral, which paradoxically makes it immediately recognizable.

**No consistent model-of-the-author.** When you read a human writer repeatedly, you build a mental model of them -- their expertise areas, what they disagree about, their voice quirks. AI content comes from different parts of a massive latent space with no guarantee of consistency. There's no "person" behind it.

Source: [LinkedIn is Drowning in AI Generated Content Slop](https://www.trevorlasn.com/blog/linkedin-is-drowning-in-ai-generated-content-slop), [How LinkedIn Opened the Door to AI Slop - Fast Company](https://www.fastcompany.com/91237998/how-linkedin-opened-the-door-to-ai-slop)

---

## 2. WHAT HUMAN WRITING ACTUALLY LOOKS LIKE vs AI

### 2.1 Sentence Structure and Rhythm Differences

A 2025 University College Cork study confirmed: AI writing follows a "narrow and uniform pattern." Human texts show "far greater variation and individuality." The key metrics:

**Perplexity** (how predictable each word is in context):
- AI writing: low perplexity. The model chooses safe, high-probability words.
- Human writing: spikes in perplexity when choosing an unusual verb, inserting a metaphor, bringing in a surprising example.

**Burstiness** (variation in sentence length and structure):
- AI: flat. Sentences are consistently 10-15 words. Paragraph lengths are uniform.
- Human: irregular. A 4-word sentence followed by a 35-word sentence. Short paragraphs then long ones.

Source: [University College Cork Study](https://www.ucc.ie/en/news/2025/new-study-reveals-that-ai-cannot-fully-write-like-a-human.html)

### 2.2 How Real Experts Write vs How AI Writes

Analysis of specific expert writers reveals patterns AI cannot replicate:

**Paul Graham** -- Analysis by Sasha Chapin ([Paul Graham Isn't a Simple Writer](https://sashachapin.substack.com/p/paul-graham-isnt-a-simple-writer)) reveals three key techniques:

1. **Self-riffing.** Graham introduces a word, then calls attention to it, then builds the next argument from that anchor. This creates "buttery-smooth" pivots between ideas. AI doesn't reference its own earlier word choices to build momentum.

2. **Occasional fancy language amid simplicity.** The phrase "spectral signature" works precisely because it's rare -- a single poetic term in otherwise plain prose. AI either stays uniformly simple or uniformly ornate. Graham deploys complexity strategically.

3. **Chattiness that isn't sloppy.** Inconsistent contractions ("I'm" alongside "they are"), padding language like "very specific," double questions. This is elevated everyday speech -- familiar yet impossible in actual conversation. AI text is either formal or informal, not both simultaneously.

**Matt Levine (Bloomberg's "Money Stuff")** -- His prose "reads like a hurried bar conversation mixed with a caring high school lecture." Key characteristics:
- Deadpan humor mixed with technical elucidation (no AI does this)
- Hypothetical conversations mid-analysis ("Imagine you're a banker and...")
- Neologisms, footnotes, snarky asides
- Assumes the audience may know more than he does
- Background in Goldman Sachs email culture -- comical explanations of derivative trades
- Source: [Harvard Magazine - Matt Levine](https://www.harvardmagazine.com/2025/07/harvard-bloomberg-column-matt-levine)

**Patrick McKenzie (@patio11, "Bits about Money")** -- His style:
- Self-described as "quite indirect and elliptical"
- Comparative advantage at the intersection of marketing and engineering
- Makes financial infrastructure wonkery accessible
- Uses real systems-level examples rather than abstractions
- Has noted that writing can either "sound natural by writing in quick natural form" or "put in crazy amounts of work to make it happen" -- anything in between won't work
- Source: [Conversations with Tyler - Patrick McKenzie](https://conversationswithtyler.com/episodes/patrick-mckenzie/)

**Byrne Hobart ("The Diff")** -- "Reads like an industrial vacuum and synthesizes like a minimoog." Fuses economics, technology, and sociology into financial analysis. Each piece includes long-form analysis plus five curated news links with commentary -- not the five biggest stories, but five data points illustrating long-term trends. Source: [The Browser - Byrne Hobart](https://thebrowser.com/notes/byrne-hobart/)

### 2.3 What Makes Writing Feel "Lived-In" vs "Generated"

| "Lived-In" (Human) | "Generated" (AI) |
|---------------------|-------------------|
| Specific details only someone who was there would know | Generic details that could apply to any similar topic |
| Opinions stated without hedging | "Some argue X, while others suggest Y" |
| References to particular failures, mistakes, embarrassments | Always positive or diplomatically balanced |
| Inconsistent formatting (some sections longer, some shorter) | Perfectly balanced section lengths |
| Sentence fragments, run-ons, rule-breaking for effect | Perfect grammar throughout |
| Inside references, domain jargon used naturally | Jargon defined immediately or avoided |
| Emotional texture -- frustration, excitement, boredom | Uniformly professional tone |
| Digressions that end up being the point | Stays on a clean outline |
| Contractions mixed inconsistently | Either all contractions or none |
| Starting sentences with "And," "But," "So" | Never starts sentences with conjunctions |
| Parenthetical asides that reveal personality | Clean, linear prose |

### 2.4 The Role of Imperfection, Asymmetry, and Messiness

Human writing has **texture**. This manifests as:

- **Rhythm variation:** Short. Then a longer sentence that lets you breathe. Then another short one. (AI keeps a metronomic beat.)
- **Structural asymmetry:** One section of a blog post might be 800 words; the next might be 50. The length matches the complexity of the idea, not a template.
- **Tonal shifts:** A serious analysis suddenly becomes wry. A joke lands in the middle of dense argument. AI maintains consistent tone throughout.
- **Deliberate imperfection:** Starting a sentence with "Look." Using fragments. Ending a paragraph with an ellipsis. Using "like" or "basically" or "honestly" -- verbal tics that signal a real person thinking.
- **Specific over general:** Not "many companies face challenges" but "Stripe ate the lunch of legacy payment processors because they made onboarding take 7 lines of code instead of a 3-week procurement cycle."

---

## 3. KOLMOGOROV COMPLEXITY IN PRACTICE FOR SOCIAL MEDIA

### 3.1 Maximum Information Per Word -- How To Achieve This

The concept maps directly from algorithmic information theory: the Kolmogorov complexity of a message is the length of the shortest program that produces it. Applied to writing, it means: **what is the shortest string of words that transmits the full insight?**

Lexical density is the measurable proxy. It's the ratio of content words (nouns, verbs, adjectives, adverbs) to total words. Written English typically scores 40-60% lexical density. High-density writing pushes above 60% by:

1. **Eliminating function words.** "The implementation of the system" becomes "the system" or better yet, just naming it.
2. **Using active voice.** "Revenues were increased by the new strategy" (9 words) becomes "The new strategy grew revenue" (6 words).
3. **Cutting hedges.** "It could potentially be argued that" --> delete entirely and state the claim.
4. **One thought per sentence, then compress.** Not two half-thoughts in one sentence.
5. **Specific nouns and verbs carry the load.** "Went quickly" becomes "sprinted." "Very big problem" becomes "crisis."

Source: [Lexical Density analysis](https://www.analyzemywriting.com/lexical_density.html), [IUP - Clear and Concise Writing](https://www.iup.edu/scholarlycommunication/our-writing-resources/clarity-and-conciseness.html)

### 3.2 The Difference Between "Compressed Insight" and "Aphoristic Platitude"

This is the critical distinction. Both are short. Both sound confident. But they are fundamentally different:

**Aphoristic platitude (low Kolmogorov complexity -- easily generated from a simple template):**
- "Success isn't a destination, it's a journey"
- "The future belongs to those who prepare for it"
- "Your network is your net worth"

These can be generated from the template: `[Abstract positive noun] + [reframing verb] + [aspirational abstraction]`. They contain near-zero information because they apply to everything and predict nothing.

**Compressed insight (high Kolmogorov complexity -- cannot be derived from a simple pattern):**
- "Stripe won because developer experience is a moat" (specific subject, specific mechanism, specific claim)
- "Stablecoins are the first crypto product where the primary user doesn't know they're using crypto" (specific domain, counterintuitive observation, testable)
- "The ACH system settles in 1-3 business days not for technical reasons but because banks earn float on the delay" (specific system, specific timeframe, specific economic incentive, challenges assumption)

The test: **Can you derive this from a general template, or does it require domain-specific knowledge to produce?** If the former, it's a platitude. If the latter, it's a compressed insight.

As one LessWrong analysis puts it: making a statement particular is what transforms a platitude into an insight. "He would have wanted you to live on" is generic. "He would have wanted you to keep kayaking" requires knowing the person. The particulars function as evidence that a generic thought lacks. Source: [LessWrong - On Platitudes](https://www.lesswrong.com/posts/R7ZBSLjJfkpTWkWRj/on-platitudes)

### 3.3 Techniques for Increasing Information Density

Drawn from William Sloane's craft analysis and lexical density research:

1. **Layer multiple meanings within sentences.** Real density is achieved "when the optimum number of things is going on at once" -- not single-progression writing where each sentence makes only one point. Source: [Theodora Goss - Writing with Density](https://theodoragoss.com/2016/05/07/writing-with-density/)

2. **Use concrete nouns instead of abstract ones.** "Financial infrastructure" is abstract. "The Rails file that tells Stripe which bank account to debit" is concrete and actually more information-dense because it specifies the mechanism.

3. **Replace adverb + weak verb with strong verb.** "Moved quickly through the market" --> "Ripped through the market." One word carries the speed and violence both.

4. **Cut meta-commentary.** "In this post, I'm going to explore..." is zero-information. Just explore it.

5. **Make the reader do work.** Don't explain the implication -- state the fact and let the reader derive the implication. This is how experts write on Twitter: they drop the data point and trust the audience to connect it. This is the opposite of AI writing, which explains everything.

6. **Specificity as compression.** Paradoxically, being more specific is often shorter. "A large technology company" = 4 words, vague. "Apple" = 1 word, precise. Specific proper nouns, exact numbers, and named mechanisms compress information.

### 3.4 How Technical Writers and Domain Experts Write on Social Media

The pattern among high-signal accounts:
- **Lead with the conclusion, not the setup.** No "In today's world of..." -- just the claim.
- **Use numbers and names.** "Visa processes 65k transactions/second" not "payment networks handle enormous volumes."
- **Take a position.** Not "some believe X while others argue Y" but "X is wrong and here's why."
- **Reference specifics only insiders know.** This signals domain authority and is impossible to fake with AI.
- **Use technical shorthand.** "ACH" not "automated clearing house." "BPS" not "basis points." The jargon itself is information-dense.
- **Thread structure mirrors argument structure.** Not formulaic listicles but genuine argument progression where each tweet builds on the last.

---

## 4. ANTI-AI FILTERS / CHECKLISTS

### 4.1 Word-Level Checks

Run every piece of text through these filters:

**THE BAN LIST -- Words that trigger instant "AI suspicion":**

Verbs: delve, embark, leverage, utilize, navigate, harness, foster, underscore, elucidate, illuminate, transcend, unveil, resonate, elevate, optimize, streamline, unleash, showcase, align, explore (when used abstractly)

Adjectives: robust, comprehensive, intricate, pivotal, crucial, vital, seamless, cutting-edge, vibrant, dynamic, innovative, transformative, unprecedented, compelling, nuanced, daunting, remarkable, ever-evolving, state-of-the-art, groundbreaking

Nouns: tapestry, landscape, realm, beacon, journey (metaphorical), paradigm, synergy, interplay, testament, intersection, metropolis, fabric, mosaic, cornerstone

Adverbs: seamlessly, notably, significantly, meticulously, profoundly, arguably, undeniably

**REPLACEMENT PRINCIPLE:** For every banned word, ask: "What would I actually say out loud to a colleague?" Use that word instead. "Robust" becomes "strong" or "works well." "Leverage" becomes "use." "Navigate" becomes "figure out" or "deal with."

### 4.2 Sentence-Level Checks

- [ ] Does every sentence have a different length than the one before it?
- [ ] Are there any trailing present participles? ("...highlighting the importance of...")
- [ ] Does the sentence start with "Furthermore," "Moreover," "Additionally," "It's important to note," or "In today's..."?
- [ ] Is there an "It's not X, it's Y" construction? (One per piece maximum, not per paragraph.)
- [ ] Does the sentence use "not only... but also..."?
- [ ] Is there a Rule of Three that could be a Rule of One or Two?
- [ ] Would you actually say this sentence out loud?
- [ ] Does the sentence contain information the reader doesn't already know?
- [ ] Is the sentence hedged with "could potentially," "it's worth noting," or "it may be argued"?

### 4.3 Paragraph-Level Checks

- [ ] Are all paragraphs roughly the same length? (Bad -- vary them.)
- [ ] Does the paragraph begin with a formulaic transition?
- [ ] Does the paragraph end with a motivational/uplifting sentence?
- [ ] Does the paragraph contain a "Challenges" structure ("Despite X, Y faces challenges...")?
- [ ] Could this paragraph apply to a different topic with minimal changes? (If yes, it's too generic.)
- [ ] Does the paragraph contain at least one specific fact, number, name, or example?

### 4.4 Structure-Level Checks

- [ ] Are sections/headers evenly balanced in length? (Human writing is asymmetric.)
- [ ] Is the conclusion just repeating earlier points? (Human conclusions add something new or end abruptly.)
- [ ] Is there excessive bold formatting?
- [ ] Are there bullet points with bold headers followed by sentences that repeat the header?
- [ ] Is the overall tone perfectly consistent throughout? (Human tone shifts.)
- [ ] Does the piece have any digressions, asides, or personality? (If not, it reads as generated.)

### 4.5 The "Median Response" Test

Ask: **Is this what the average, safe, non-committal answer to this prompt would be?** If yes, it fails. Human writing has a point of view. It takes a side. It says something specific that could be wrong. AI writing hedges, presents "both sides," and arrives at a safe non-conclusion.

The strongest anti-AI signal: **making a specific, falsifiable claim that requires domain expertise to produce.** "Visa's interchange economics make it impossible for anyone to build a cheaper card network without regulatory intervention" -- this is either right or wrong, and it takes knowledge to write. AI would say "there are challenges and opportunities in the payments space."

### 4.6 The Read-Aloud Test

Read the text aloud. If you sound like a corporate press release, a motivational poster, or a conference keynote, it sounds AI-generated. If you sound like yourself explaining something to a smart friend over coffee, it sounds human.

---

## 5. EXAMPLES OF HIGH-SIGNAL, NON-AI WRITING ON X

### 5.1 Writers Whose Voice Is Unmistakable

**Patrick McKenzie (@patio11)** -- Fintech/Payments
- Writes about financial infrastructure with genuine insider knowledge
- Style: indirect, elliptical, systems-thinking approach
- What makes it unmistakable: casual authority. He explains how ACH settlement works or why debanking happens with the tone of someone who has personally dealt with these systems, not someone summarizing Wikipedia. Uses specific case studies, regulatory references, and named counterparties.
- "Bits about Money" is "accurate, incisive, and balanced" per experts including a crypto VC and a former federal banking regulator.
- Source: [Bits About Money](https://www.bitsaboutmoney.com/)

**Matt Levine (@matt_levine)** -- Finance
- Bloomberg's "Money Stuff" newsletter
- Style: deadpan humor interwoven with technical analysis. Hypothetical dialogues mid-argument. Footnotes that are funnier than the main text.
- What makes it unmistakable: the consistent personality. You can predict what Levine would find funny about a given financial situation. He has preferences, biases, running jokes. AI has none of these.
- Source: [Harvard Magazine](https://www.harvardmagazine.com/2025/07/harvard-bloomberg-column-matt-levine)

**Byrne Hobart (@ByrneHobart)** -- Finance/Tech
- "The Diff" newsletter
- Style: synthesis machine. Draws connections between disparate domains (sociology + economics + tech). Chooses stories based on long-term relevance, not recency.
- What makes it unmistakable: the connections between ideas that no one else is making. AI can summarize known connections; Hobart creates new ones.
- Source: [The Browser - Byrne Hobart](https://thebrowser.com/notes/byrne-hobart/)

**Nassim Taleb (@nntaleb)** -- Risk/Finance
- Style: provocative, contrarian, short and punchy. Insults people by name. References specific mathematical concepts alongside street-level wisdom.
- What makes it unmistakable: the aggression, the willingness to alienate, the specific intellectual enemies. AI is designed to be agreeable. Taleb is designed to be disagreeable. You could never mistake his writing for AI because AI would never insult someone's statistical literacy in a tweet.
- Source: [Nassim Taleb's Twitter Archive](https://nassimtaleb.org/tag/twitter/)

**Paul Graham (@paulg)** -- Tech/Startups
- Style: plain vocabulary, complex structure. Self-riffing (referencing his own word choices to pivot). Chatty but precise. Occasional poetic phrases ("spectral signature") in otherwise plain prose.
- What makes it unmistakable: the structural sophistication hidden under simple words. His essays feel like they're thinking in real-time. AI produces finished thoughts; Graham produces thinking-in-progress.
- Source: [Paul Graham Isn't a Simple Writer](https://sashachapin.substack.com/p/paul-graham-isnt-a-simple-writer)

### 5.2 What Makes These Writers Unmistakable (Common Patterns)

1. **Domain-specific knowledge that can't be faked.** They reference specific systems, specific numbers, specific failures. Not "the financial system" but "FedWire's cutoff time" or "Regulation E's liability rules."

2. **Consistent personality across posts.** You can identify the author without a byline. They have recurring interests, pet peeves, running jokes, and signature rhetorical moves that are theirs.

3. **Willingness to be wrong.** They make specific claims. They take sides. They have enemies. AI hedges; humans commit.

4. **Asymmetric emphasis.** They spend 80% of a piece on the one thing that matters and skip what's "expected." AI gives equal weight to all sections.

5. **Earned authority signals.** They use insider shorthand naturally. They reference meetings they attended, systems they built, mistakes they made. This is not achievable by summarizing training data.

6. **Humor that serves the argument.** Levine's jokes illuminate his point. Taleb's insults clarify his framework. The humor is functional, not decorative. AI humor is decorative at best.

### 5.3 How They Achieve Density Without Templates

- **They cut the setup.** No "In the complex world of payments..." Just start with the insight.
- **They trust the reader.** They don't explain what ACH is or what a basis point is. The assumed shared knowledge compresses enormously.
- **They use proper nouns.** "Stripe" not "a leading payment technology company." "Dodd-Frank" not "post-financial-crisis regulatory framework."
- **They state the mechanism, not the outcome.** Not "the company grew" but "the company grew because their API handled idempotency keys natively, which meant developers didn't have to build retry logic."
- **They pick one angle.** A thread about stablecoins doesn't try to cover "everything about stablecoins." It covers one specific mechanism -- how Tether's reserve composition creates systemic risk, or how USDC's banking relationships affect settlement speed. One angle, fully explored, is infinitely denser than a survey.

---

## KEY SYNTHESIS: The Anti-AI Writing Principles

The research converges on these principles for writing that is maximally information-dense and unmistakably human:

1. **Be specific or be quiet.** Every sentence should contain at least one proper noun, number, or mechanism that requires domain knowledge to produce.

2. **Vary everything.** Sentence length, paragraph length, section length, tone. Asymmetry is the fingerprint of a human mind.

3. **Take a position.** Make falsifiable claims. Have opinions. AI gives the median; you give your actual assessment.

4. **Cut the ceremony.** No openings that "set the stage." No conclusions that "summarize key points." No transitions that signal transitions. Just the content.

5. **Write like you talk to a smart colleague.** Not like you're presenting at a conference. Not like you're writing a press release. Like you're explaining something interesting to someone who will call you out if you're wrong.

6. **Trust your reader.** Don't explain the implication. State the fact; let them derive it. This respects their intelligence and compresses your text.

7. **Break rules on purpose.** Start with "And." Use fragments. End sentences with prepositions. Drop articles. Use contractions inconsistently. Perfect grammar is an AI tell.

8. **Kill the banned words.** If it's on the list above, find the word you'd actually use. "Robust" is never the word you'd use.

9. **One insight, fully compressed, beats ten points surveyed.** Kolmogorov complexity means finding the shortest program that produces the truth. One deep insight is a shorter "program" than a list of surface observations.

10. **The personality test.** If you removed the byline, could someone identify the author? If not, the writing has no voice. Voice is the anti-AI signal.

---

## Sources

- [University College Cork - AI Cannot Fully Write Like a Human (2025)](https://www.ucc.ie/en/news/2025/new-study-reveals-that-ai-cannot-fully-write-like-a-human.html)
- [Wikipedia: Signs of AI Writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- [GPTZero - Top 10 Most Common Words Used by AI](https://gptzero.me/news/most-common-ai-vocabulary/)
- [Plus AI - Most Overused ChatGPT Words](https://plusai.com/blog/the-most-overused-chatgpt-words)
- [God of Prompt - 500 ChatGPT Overused Words](https://www.godofprompt.ai/blog/500-chatgpt-overused-words-heres-how-to-avoid-them)
- [Colin Gorrie - Why ChatGPT Writes Like That (Rhetorical Analysis)](https://www.deadlanguagesociety.com/p/rhetorical-analysis-ai)
- [Contrastive Parallelism with Identity Reframing as AI Signature](https://www.layng.ai/contrastive-parallelism-with-identity-reframing-a-signature-of-ai-writing/)
- [Blake Stockton - Don't Write Like AI: Red Flag Words](https://www.blakestockton.com/red-flag-words/)
- [Blake Stockton - 10 Takeaways from Wikipedia's Signs of AI Writing](https://www.blakestockton.com/takeaways-from-wikipedias-signs-of-ai-writing-2/)
- [Sean Goedecke - Why Does AI Slop Feel So Bad to Read?](https://www.seangoedecke.com/on-slop/)
- [Trevor Lasn - LinkedIn is Drowning in AI Generated Content Slop](https://www.trevorlasn.com/blog/linkedin-is-drowning-in-ai-generated-content-slop)
- [Fast Company - How LinkedIn Opened the Door to AI Slop](https://www.fastcompany.com/91237998/how-linkedin-opened-the-door-to-ai-slop)
- [Originality.ai - Perplexity and Burstiness in Writing](https://originality.ai/blog/perplexity-and-burstiness-in-writing)
- [Pangram Labs - Comprehensive Guide to Spotting AI Writing Patterns](https://www.pangram.com/blog/comprehensive-guide-to-spotting-ai-writing-patterns)
- [Pangram Labs - Most Common AI Phrases](https://www.pangram.com/resources/most-common-ai-phrases)
- [Sasha Chapin - Paul Graham Isn't a Simple Writer](https://sashachapin.substack.com/p/paul-graham-isnt-a-simple-writer)
- [Harvard Magazine - Matt Levine's Bloomberg Finance Column](https://www.harvardmagazine.com/2025/07/harvard-bloomberg-column-matt-levine)
- [Conversations with Tyler - Patrick McKenzie](https://conversationswithtyler.com/episodes/patrick-mckenzie/)
- [The Browser - Byrne Hobart](https://thebrowser.com/notes/byrne-hobart/)
- [Bits About Money - Patrick McKenzie](https://www.bitsaboutmoney.com/)
- [Inside Higher Ed - Distinguishing AI from Human Essays](https://www.insidehighered.com/opinion/career-advice/teaching/2024/07/02/ways-distinguish-ai-composed-essays-human-composed-ones)
- [Plagiarism Today - Em Dashes, Hyphens and AI Writing](https://www.plagiarismtoday.com/2025/06/26/em-dashes-hyphens-and-spotting-ai-writing/)
- [LessWrong - On Platitudes](https://www.lesswrong.com/posts/R7ZBSLjJfkpTWkWRj/on-platitudes)
- [Theodora Goss - Writing with Density](https://theodoragoss.com/2016/05/07/writing-with-density/)
- [IUP - Clear, Precise, and Concise Writing](https://www.iup.edu/scholarlycommunication/our-writing-resources/clarity-and-conciseness.html)
- [Lexical Density Analysis Tool](https://www.analyzemywriting.com/lexical_density.html)
- [TechCrunch - The Best Guide to Spotting AI Writing Comes from Wikipedia](https://techcrunch.com/2025/11/20/the-best-guide-to-spotting-ai-writing-comes-from-wikipedia/)
- [Grammarly - Decoding AI Language: Common Words and Phrases](https://www.grammarly.com/blog/ai/common-ai-words/)
- [Nassim Taleb - Twitter Archives](https://nassimtaleb.org/tag/twitter/)