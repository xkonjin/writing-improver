# Kolmogorov Clarity LLM Prompts

## Master Prompt: The Clarity Enforcer

```
You are a Kolmogorov Compressor. Your job: find the shortest accurate expression of any idea.

RULES:
1. Start with the conclusion/answer in ONE sentence (max 30 words)
2. Support with 3 bullet points maximum
3. Include context ONLY if it changes the decision
4. Delete ALL hedge words (perhaps, maybe, seems, appears)
5. Delete ALL throat-clearing (As we know, It's important to note)
6. Use specific numbers, not vague descriptions
7. Every word must be necessary - if removed, meaning breaks

FORBIDDEN:
- Starting with background
- Explaining obvious things
- Using more than one example
- Metaphors unless they're shorter than literal description
- Any sentence that doesn't advance understanding

OUTPUT FORMAT:
ANSWER: [Core message]
BECAUSE: [3 reasons max]
CONTEXT: [Only if critical]

Now respond to: [YOUR QUESTION HERE]
```

## Task-Specific Prompts

### Email Compressor

```
Rewrite this email using Kolmogorov Clarity:

1. Subject line: Action needed + deadline (5 words max)
2. First line: The ask or decision needed
3. Next 3 lines: Why (one reason per line)
4. Optional last line: Critical context only

Delete all pleasantries except "Thanks"
Delete all hedging
Delete all redundancy

Original email: [PASTE EMAIL]
```

### Document Summarizer

```
Compress this document to its Kolmogorov minimum:

STEP 1: Find the ONE decision/action this document wants
STEP 2: Find the THREE most important supporting facts
STEP 3: Delete everything else

Format:
KEY POINT: [One sentence]
EVIDENCE:
• [Fact 1]
• [Fact 2]
• [Fact 3]
ACTION REQUIRED: [What reader must do]

Document: [PASTE DOCUMENT]
```

### Meeting Notes Compressor

```
Convert these meeting notes to Kolmogorov Clarity:

FORMAT:
DECIDED: [What was decided]
ACTIONS:
- [Person]: [Task] by [Date]
- [Person]: [Task] by [Date]
BLOCKERS: [Only if unresolved]

Delete all discussion that didn't lead to decisions
Delete all options that weren't chosen
Delete all context that doesn't affect next steps

Notes: [PASTE NOTES]
```

### Proposal Clarifier

```
Rewrite this proposal using First Principles Clarity:

1. THE ASK: What do you want? (one sentence)
2. THE PROBLEM: What breaks if we don't? (one sentence)
3. THE SOLUTION: What specifically will you do? (three bullets max)
4. THE COST: Time and money (specific numbers)
5. THE RESULT: What changes? (one sentence)

Delete all other content.

Proposal: [PASTE PROPOSAL]
```

### Slop Detector

```
Analyze this text for AI slop and verbosity:

Check for:
- Unnecessary hedging (perhaps, maybe, it seems)
- Redundant transitions (furthermore, moreover, in addition)
- Obvious statements (As we all know)
- Vague language (various, multiple, numerous)
- Repetition disguised as emphasis
- Generic examples that could apply anywhere
- Conclusions that repeat the introduction

For each issue found:
ISSUE: [What's wrong]
EXAMPLE: [Quote from text]
FIX: [Shorter version or DELETE]

Text: [PASTE TEXT]
```

### Story-to-Core Extractor

```
Extract the core message from this narrative:

FIND:
1. What changed?
2. Why does it matter?
3. What should happen next?

OUTPUT (max 50 words total):
WHAT: [The change]
WHY: [The impact]
NEXT: [The action]

Strip all storytelling, context, and color. Just facts and implications.

Story: [PASTE NARRATIVE]
```

### Technical Doc Compressor

```
Compress this technical documentation:

RULES:
- Assume reader knows the basics
- One example maximum per concept
- No explanations of why, just what and how
- Commands/code only, no description
- Prerequisites in one line
- Steps numbered, one line each

FORMAT:
DOES: [What it accomplishes - one line]
REQUIRES: [Prerequisites - one line]
STEPS:
1. [Command or action]
2. [Command or action]
3. [Command or action]
ERROR?: [Most common issue + fix]

Documentation: [PASTE DOCS]
```

## Meta-Prompt: The Clarity Coach

```
I'm going to write something. After I write, do this:

1. Score my Kolmogorov Ratio: (final words / minimum possible words)
   - 1.0-1.2 = Perfect
   - 1.3-1.5 = Good
   - 1.6-2.0 = Needs work
   - 2.0+ = Slop

2. Show me the compressed version

3. List every deleted word/phrase and why it was unnecessary

4. Highlight any remaining words that could still be cut

This will train me to write with clarity first time.

My text: [PASTE TEXT]
```

## Emergency Prompts

### The One-Liner

```
Express this in ONE sentence, maximum 30 words: [PASTE IDEA]
```

### The Binary

```
Answer only YES or NO with one supporting fact: [PASTE QUESTION]
```

### The Number

```
Give me only the number that matters: [PASTE SITUATION]
```

## Integration Instructions

### For ChatGPT/Claude:

1. Save the Master Prompt as a custom instruction
2. Prefix other prompts with: "Using Kolmogorov Clarity principles:"

### For Development Teams:

```python
# Add to your AI wrapper
CLARITY_PREFIX = """
Respond with maximum compression. Start with conclusion.
No hedging. No fluff. Every word necessary.
"""

def query_ai(prompt):
    return ai.query(CLARITY_PREFIX + prompt)
```

### For Email Clients:

Create keyboard shortcut that runs selected text through Email Compressor prompt

### For Documentation:

Add pre-commit hook that scores Kolmogorov Ratio, warns if >2.0

## Remember

The goal isn't to be terse. It's to achieve maximum information transfer with minimum cognitive load.

Every prompt should produce output where removing ANY word would break meaning.
