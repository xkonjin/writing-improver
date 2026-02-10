#!/usr/bin/env python3
"""Test OpenRouter swarm directly."""

import asyncio
import httpx

async def test_openrouter():
    """Test if OpenRouter API works."""
    
    api_key = "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"
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "anthropic/claude-3.5-sonnet",
                "messages": [
                    {"role": "system", "content": "You are a mechanism hunter."},
                    {"role": "user", "content": "In 20 words: Why did Coinbase Super Bowl ad fail?"}
                ],
                "temperature": 0.7,
                "max_tokens": 100
            }
        )
        
        print("Status:", response.status_code)
        result = response.json()
        print("Response:", result)
        
        if "choices" in result:
            print("\nContent:", result["choices"][0]["message"]["content"])
        else:
            print("\nError:", result)

if __name__ == "__main__":
    asyncio.run(test_openrouter())