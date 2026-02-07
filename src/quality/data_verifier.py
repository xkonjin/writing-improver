import json
import re
from dataclasses import dataclass, field

from src.agents.base import BaseAgent


@dataclass
class VerificationResult:
    claims_checked: int = 0
    claims_verified: int = 0
    claims_stale: int = 0
    claims_unverified: int = 0
    stale_claims: list[str] = field(default_factory=list)
    unverified_claims: list[str] = field(default_factory=list)
    issues: list[str] = field(default_factory=list)

    @property
    def verification_rate(self) -> float:
        if self.claims_checked == 0:
            return 1.0
        return self.claims_verified / self.claims_checked

    def passes_gate(self) -> bool:
        return self.claims_stale == 0 and self.verification_rate >= 0.8


def extract_claims_regex(text: str) -> list[str]:
    """Extract factual claims using regex patterns."""
    claims = []

    # Numbers with context
    number_claims = re.findall(r"[^.!?]*?\$[\d,.]+\s*(?:billion|million|trillion|B|M|T)[^.!?]*[.!?]", text)
    claims.extend(number_claims)

    # Percentage claims
    pct_claims = re.findall(r"[^.!?]*?\d+(?:\.\d+)?%[^.!?]*[.!?]", text)
    claims.extend(pct_claims)

    # Year-specific claims
    year_claims = re.findall(r"[^.!?]*?(?:in |since |by |as of )\d{4}[^.!?]*[.!?]", text, re.IGNORECASE)
    claims.extend(year_claims)

    # Deduplicate while preserving order
    seen = set()
    unique = []
    for claim in claims:
        cleaned = claim.strip()
        if cleaned not in seen:
            seen.add(cleaned)
            unique.append(cleaned)

    return unique


async def verify_claims(text: str, model: str = "claude-haiku-4-5-20251001") -> VerificationResult:
    """Use LLM to extract and verify factual claims via Chain-of-Verification."""
    result = VerificationResult()

    # First pass: regex extraction
    regex_claims = extract_claims_regex(text)
    result.claims_checked = len(regex_claims)

    if not regex_claims:
        return result

    agent = BaseAgent(model=model)
    system = """You are a fact-checking assistant. For each claim provided, assess:
1. Is this a verifiable factual claim? (not opinion/analysis)
2. Does it have a date or time reference?
3. Could the data be stale (>6 months old without justification)?
4. Does it cite a specific, checkable source?

Respond in JSON:
{
    "claims": [
        {
            "claim": "the claim text",
            "verifiable": true/false,
            "has_date": true/false,
            "potentially_stale": true/false,
            "has_source": true/false
        }
    ]
}"""

    claims_text = "\n".join(f"- {c}" for c in regex_claims[:20])
    response = await agent.call(system, f"Assess these claims:\n{claims_text}")

    try:
        json_match = re.search(r"\{[\s\S]+\}", response)
        if json_match:
            data = json.loads(json_match.group())
            for claim_data in data.get("claims", []):
                if claim_data.get("potentially_stale"):
                    result.claims_stale += 1
                    result.stale_claims.append(claim_data.get("claim", ""))
                elif claim_data.get("verifiable") and claim_data.get("has_source"):
                    result.claims_verified += 1
                else:
                    result.claims_unverified += 1
                    if not claim_data.get("has_date"):
                        result.unverified_claims.append(f"No date: {claim_data.get('claim', '')[:80]}")
    except (json.JSONDecodeError, AttributeError):
        result.issues.append("Failed to parse LLM verification response")

    if result.claims_stale > 0:
        result.issues.append(f"{result.claims_stale} potentially stale claims")
    if result.verification_rate < 0.8:
        result.issues.append(f"Low verification rate: {result.verification_rate:.0%}")

    return result
