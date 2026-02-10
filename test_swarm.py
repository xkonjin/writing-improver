#!/usr/bin/env python3
"""Test OpenRouter swarm directly."""

import asyncio
import httpx
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

async def test_openrouter():
    """Test if OpenRouter API works."""
    
    api_key = os.getenv("OPENROUTER_API_KEY")
    
    if not api_key:
        print("❌ OPENROUTER_API_KEY not found in environment variables")
        print("Set it with: export OPENROUTER_API_KEY=sk-or-v1-your-key-here")
        return
    
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