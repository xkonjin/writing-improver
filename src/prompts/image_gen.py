"""Prompts for content classification and image prompt generation."""

CLASSIFY_CONTENT_SYSTEM = """You classify thesis card articles into exactly ONE content type.

Content types:
- BULLISH: Growth thesis, optimistic prediction, value creation
- BEARISH: Breakdown thesis, systemic risk, value destruction
- REGULATORY: Law, regulation, compliance, institutional analysis
- CONTRARIAN: Against-consensus take, surprising reversal
- PARADOX: Two opposing forces in tension, dual thesis
- TECHNICAL: Deep system analysis, infrastructure, mechanism
- PARADIGM_SHIFT: Fundamental change in how something works

Respond with ONLY the content type label (e.g. BULLISH). Nothing else."""

# ──────────────────────────────────────────────────────────────────────
# VISUAL IDENTITY: Isometric Tilt-Shift Miniature Diorama
#
# Consistent constraints across ALL content types:
#   - Isometric camera angle, tilt-shift shallow depth of field
#   - Wes Anderson symmetrical framing
#   - Dollhouse / miniature scale with tiny figurines
#   - 35mm film grain
#   - Soft pastel palette (pink, mint, cream, dusty blue, terracotta)
#
# What varies per content type:
#   - Scene composition and metaphor
#   - Palette emphasis (warmer vs cooler pastels)
#   - Mood (calm vs tension vs decay)
# ──────────────────────────────────────────────────────────────────────

VISUAL_IDENTITY = (
    "Isometric tilt-shift miniature diorama, Wes Anderson symmetrical framing, "
    "dollhouse scale with tiny figurines, 35mm film grain, "
    "shallow depth of field blurring the edges"
)

STYLE_MAP = {
    "BULLISH": {
        "primary": "Isometric diorama — expansion",
        "prompt": (
            f"{VISUAL_IDENTITY}, scene suggesting growth and construction, "
            "new structures being built, scaffolding, figurines carrying materials upward"
        ),
        "palette": "soft pink, mint green, warm cream, touches of gold",
    },
    "BEARISH": {
        "primary": "Isometric diorama — decay",
        "prompt": (
            f"{VISUAL_IDENTITY}, scene suggesting quiet decline, "
            "structures partially dismantled or boarded up, figurines packing or leaving, "
            "muted and desaturated"
        ),
        "palette": "dusty rose, faded mint, concrete gray, muted terracotta",
    },
    "REGULATORY": {
        "primary": "Isometric diorama — institutional",
        "prompt": (
            f"{VISUAL_IDENTITY}, scene with imposing symmetrical architecture, "
            "orderly pathways, figurines in queues or at desks, "
            "institutional but miniature"
        ),
        "palette": "cream, dusty blue, soft gold, marble white",
    },
    "CONTRARIAN": {
        "primary": "Isometric diorama — inversion",
        "prompt": (
            f"{VISUAL_IDENTITY}, scene where something is upside-down or reversed, "
            "figurines walking on ceilings or buildings inverted, "
            "playful visual contradiction"
        ),
        "palette": "soft pink, electric mint, cream, unexpected coral",
    },
    "PARADOX": {
        "primary": "Isometric diorama — split scene",
        "prompt": (
            f"{VISUAL_IDENTITY}, scene split into two contrasting halves "
            "connected by a single bridge or doorway, "
            "each half a different miniature world in tension"
        ),
        "palette": "warm pastels on one side, cool pastels on the other",
    },
    "TECHNICAL": {
        "primary": "Isometric diorama — cutaway",
        "prompt": (
            f"{VISUAL_IDENTITY}, architectural cutaway revealing internal layers, "
            "rooms within rooms, figurines operating machinery or climbing between floors, "
            "visible plumbing and wiring"
        ),
        "palette": "cream, dusty blue, soft terracotta, steel accents",
    },
    "PARADIGM_SHIFT": {
        "primary": "Isometric diorama — transformation",
        "prompt": (
            f"{VISUAL_IDENTITY}, scene where small structures are being dwarfed or replaced "
            "by larger ones arriving from the edges, figurines caught between old and new, "
            "a frontier being overtaken"
        ),
        "palette": "dusty rose, mint, cream, warm terracotta",
    },
}

IMAGE_PROMPT_SYSTEM = (
    "You write image generation prompts for thesis card header images.\n\n"
    "VISUAL IDENTITY (NEVER deviate from this):\n"
    "- Isometric tilt-shift miniature diorama\n"
    "- Wes Anderson symmetrical framing\n"
    "- Dollhouse scale with tiny figurines\n"
    "- 35mm film grain, shallow depth of field blurring the edges\n"
    "- Soft pastel palette: pink, mint, cream, dusty blue, terracotta\n\n"
    "Given:\n"
    "- Article title and summary\n"
    "- Scene composition directive and palette emphasis\n"
    "- Content type\n\n"
    "Generate a single image prompt (2-3 sentences) that:\n"
    "1. ALWAYS uses the isometric tilt-shift diorama style — every image must look "
    "like a miniature architectural model photographed from above at an angle\n"
    "2. Translates the article's core concept into a PHYSICAL SCENE with tiny "
    "figurines doing something allegorical. Not literal — find the metaphor. "
    "An article about regulation becomes figurines queuing at an imposing miniature "
    "customs office. An article about value capture becomes figurines on a conveyor belt.\n"
    "3. NEVER reference: coins, tokens, blockchain, crypto symbols, dollar signs, "
    "stock charts, computer screens, logos, brand names, or any finance/tech iconography\n"
    "4. Include specific details: what the buildings look like, what the figurines are "
    "doing, what connects different parts of the scene\n"
    "5. End with \"no text, no words, no letters, no UI elements, no symbols, no logos\"\n\n"
    "Respond with ONLY the image prompt. Nothing else."
)
