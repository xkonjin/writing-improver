import json
import re
from dataclasses import dataclass, field

from src.agents.base import BaseAgent

SIGNPOSTING_PATTERNS = [
    re.compile(
        r"(?:In this (?:article|section|piece)"
        r"|Let(?:'s| us) (?:explore|examine|look at|dive into))",
        re.IGNORECASE,
    ),
    re.compile(r"(?:We(?:'ll| will) (?:explore|examine|look at|discuss))", re.IGNORECASE),
    re.compile(r"(?:This (?:article|section|piece) (?:will|explores|examines))", re.IGNORECASE),
    re.compile(
        r"(?:First, (?:let's|we'll|I'll) |Second(?:ly)?, |Third(?:ly)?, |Finally, )",
        re.IGNORECASE,
    ),
    re.compile(r"(?:As (?:we'll|we will) see)", re.IGNORECASE),
]

SUMMARIZING_CONCLUSION_PATTERNS = [
    re.compile(r"(?:In (?:conclusion|summary)|To (?:summarize|sum up|conclude))", re.IGNORECASE),
    re.compile(
        r"(?:(?:The )?(?:key|main|critical) (?:takeaway|point|lesson|insight)s? (?:is|are|here))",
        re.IGNORECASE,
    ),
    re.compile(r"(?:What (?:this|we've|I've) (?:means|learned|shown|demonstrated))", re.IGNORECASE),
]

PERFORMATIVE_INTROSPECTION = [
    re.compile(
        r"(?:I(?:'ve| have) been (?:thinking|sitting with|reflecting on|wrestling with|pondering))",
        re.IGNORECASE,
    ),
    re.compile(r"(?:This (?:has been|keeps) (?:on my mind|weighing on me|haunting me))", re.IGNORECASE),
    re.compile(r"(?:I find myself (?:wondering|thinking|asking|questioning))", re.IGNORECASE),
]


@dataclass
class AITellResult:
    signposting_count: int = 0
    signposting_examples: list[str] = field(default_factory=list)
    parallelism_detected: bool = False
    parallelism_examples: list[str] = field(default_factory=list)
    summarizing_conclusion: bool = False
    performative_introspection_count: int = 0
    data_density_issues: list[str] = field(default_factory=list)
    llm_issues: list[str] = field(default_factory=list)
    issues: list[str] = field(default_factory=list)

    def score(self) -> float:
        """Score 0-10, higher = more human-sounding."""
        deductions = 0.0
        deductions += min(self.signposting_count * 1.5, 4)
        deductions += 3.0 if self.parallelism_detected else 0
        deductions += 2.0 if self.summarizing_conclusion else 0
        deductions += min(self.performative_introspection_count * 1.5, 3)
        return max(0, 10 - deductions)


def detect_ai_tells_regex(text: str) -> AITellResult:
    """Detect AI tells using pure regex — no LLM needed."""
    result = AITellResult()

    # Signposting
    for pattern in SIGNPOSTING_PATTERNS:
        matches = pattern.findall(text)
        result.signposting_count += len(matches)
        result.signposting_examples.extend(matches[:2])

    # Summarizing conclusion — check last 500 chars
    last_chunk = text[-500:]
    for pattern in SUMMARIZING_CONCLUSION_PATTERNS:
        if pattern.search(last_chunk):
            result.summarizing_conclusion = True
            break

    # Performative introspection
    for pattern in PERFORMATIVE_INTROSPECTION:
        matches = pattern.findall(text)
        result.performative_introspection_count += len(matches)

    # Parallelism: detect 3+ consecutive paragraphs with same opening structure
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip() and not p.strip().startswith("#")]
    if len(paragraphs) >= 3:
        for i in range(len(paragraphs) - 2):
            chunk = paragraphs[i : i + 3]
            # Check if they start with the same structural pattern
            starts = [re.match(r"^(\*\*[^*]+\*\*)", p) for p in chunk]
            if all(starts):
                result.parallelism_detected = True
                result.parallelism_examples = [s.group(0) for s in starts if s]
                break

    # Build issues
    if result.signposting_count > 1:
        result.issues.append(f"Signposting detected ({result.signposting_count} instances)")
    if result.parallelism_detected:
        result.issues.append("Structural parallelism detected (3+ same-pattern paragraphs)")
    if result.summarizing_conclusion:
        result.issues.append("Summarizing conclusion detected")
    if result.performative_introspection_count > 0:
        result.issues.append(f"Performative introspection ({result.performative_introspection_count} instances)")

    return result


async def detect_ai_tells_llm(text: str, model: str = "claude-haiku-4-5-20251001") -> AITellResult:
    """Detect AI tells using LLM for nuanced detection."""
    regex_result = detect_ai_tells_regex(text)

    agent = BaseAgent(model=model)
    system = (
        "You are an AI writing detection expert. Analyze the text for these AI tells:\n\n"
        '1. SIGNPOSTING: Announcing what text will do before doing it ("Let\'s explore...")\n'
        "2. PARALLELISM: 3+ consecutive sections with identical structural templates\n"
        "3. SUMMARIZING CONCLUSION: Article ends by restating what was already said\n"
        "4. PERFORMATIVE INTROSPECTION: Writer tells you about feelings, not insight\n"
        "5. DATA DENSITY: Paragraphs with 3+ data points, no interpretation\n\n"
        "Respond in JSON: "
        '{"signposting": {"count": N, "examples": []}, '
        '"parallelism": {"detected": bool, "examples": []}, '
        '"summarizing_conclusion": bool, '
        '"performative_introspection": {"count": N, "examples": []}, '
        '"data_density_issues": []}'
    )

    response = await agent.call(system, f"Analyze this text for AI tells:\n\n{text[:8000]}")

    try:
        # Extract JSON from response
        json_match = re.search(r"\{[\s\S]+\}", response)
        if json_match:
            data = json.loads(json_match.group())
            llm_signposting = data.get("signposting", {}).get("count", 0)
            regex_result.signposting_count = max(regex_result.signposting_count, llm_signposting)
            if data.get("parallelism", {}).get("detected", False):
                regex_result.parallelism_detected = True
            if data.get("summarizing_conclusion", False):
                regex_result.summarizing_conclusion = True
            llm_intro = data.get("performative_introspection", {}).get("count", 0)
            regex_result.performative_introspection_count = max(
                regex_result.performative_introspection_count, llm_intro
            )
            regex_result.data_density_issues = data.get("data_density_issues", [])
    except (json.JSONDecodeError, AttributeError):
        regex_result.llm_issues.append("Failed to parse LLM response")

    return regex_result
