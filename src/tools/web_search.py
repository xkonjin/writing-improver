import os

import httpx


async def perplexity_search(query: str, max_results: int = 5) -> str:
    """Search using Perplexity API for current, sourced information."""
    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if not api_key:
        return f"[No PERPLEXITY_API_KEY set. Query was: {query}]"

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.perplexity.ai/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "model": "sonar",
                "messages": [
                    {
                        "role": "system",
                        "content": "Provide specific, sourced facts. Include dates and numbers.",
                    },
                    {"role": "user", "content": query},
                ],
            },
            timeout=30.0,
        )
        if response.status_code == 200:
            data = response.json()
            content: str = data["choices"][0]["message"]["content"]
            return content
        return f"[Perplexity search failed: {response.status_code}]"
