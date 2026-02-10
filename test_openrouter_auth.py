#!/usr/bin/env python3
"""
Test OpenRouter API authentication to diagnose the root cause.
Tests different header combinations and API key formats.
"""

import asyncio
import httpx
import os
import json

# API Key from CLAUDE.md
API_KEY = "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"

async def test_openrouter_auth():
    """Test different authentication approaches for OpenRouter."""
    
    print("🔐 OpenRouter Authentication Diagnosis")
    print("=" * 50)
    print(f"API Key: {API_KEY[:20]}...{API_KEY[-10:]}")
    print(f"Key Length: {len(API_KEY)} characters")
    print("=" * 50)
    
    test_payload = {
        "model": "anthropic/claude-3.5-sonnet",
        "messages": [{"role": "user", "content": "Hello"}],
        "max_tokens": 50
    }
    
    # Test cases with different header combinations
    test_cases = [
        {
            "name": "Basic Headers Only",
            "headers": {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }
        },
        {
            "name": "With HTTP-Referer",
            "headers": {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/writing-improver"
            }
        },
        {
            "name": "With X-Title",
            "headers": {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "X-Title": "Writing Improver Test"
            }
        },
        {
            "name": "Full Headers (Referer + Title)",
            "headers": {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/writing-improver",
                "X-Title": "Writing Improver Test"
            }
        },
        {
            "name": "Alternative Referer Format",
            "headers": {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "Referer": "https://github.com/writing-improver",
                "X-Title": "Writing Improver Test"
            }
        }
    ]
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        for i, test_case in enumerate(test_cases, 1):
            print(f"\n{i}. Testing: {test_case['name']}")
            print("-" * 30)
            
            try:
                response = await client.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers=test_case["headers"],
                    json=test_payload
                )
                
                print(f"Status Code: {response.status_code}")
                
                try:
                    result = response.json()
                    print(f"Response: {json.dumps(result, indent=2)}")
                    
                    if "choices" in result:
                        print("✅ SUCCESS! Authentication works with this header combination.")
                        return test_case["headers"]
                    elif "error" in result:
                        error_code = result["error"].get("code", "unknown")
                        error_message = result["error"].get("message", "unknown")
                        print(f"❌ Error {error_code}: {error_message}")
                    
                except json.JSONDecodeError:
                    print(f"❌ Invalid JSON response: {response.text}")
                    
            except Exception as e:
                print(f"❌ Request failed: {str(e)}")
    
    print("\n" + "=" * 50)
    print("🔍 DIAGNOSIS RESULTS:")
    print("=" * 50)
    print("❌ No header combination worked.")
    print("📋 Possible causes:")
    print("   1. API key is invalid/expired")
    print("   2. Account not found or suspended") 
    print("   3. OpenRouter API endpoint changed")
    print("   4. Rate limiting or IP restrictions")
    print("   5. Payment/billing issues with account")
    print("\n💡 RECOMMENDATIONS:")
    print("   1. Get a new API key from https://openrouter.ai/keys")
    print("   2. Check OpenRouter account status")
    print("   3. Verify billing/payment status")
    print("   4. Check API documentation for changes")
    
    return None

async def test_models_endpoint():
    """Test if we can access the models endpoint (usually works without auth)."""
    print("\n🔍 Testing Models Endpoint (no auth required)")
    print("-" * 40)
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.get("https://openrouter.ai/api/v1/models")
            print(f"Status: {response.status_code}")
            
            if response.status_code == 200:
                models = response.json()
                print(f"✅ Models endpoint works. Found {len(models.get('data', []))} models")
                print("📋 Sample models:")
                for model in models.get('data', [])[:5]:
                    print(f"   - {model.get('id', 'unknown')}")
            else:
                print(f"❌ Models endpoint failed: {response.text}")
                
        except Exception as e:
            print(f"❌ Models endpoint error: {str(e)}")

async def main():
    """Main test function."""
    working_headers = await test_openrouter_auth()
    await test_models_endpoint()
    
    if working_headers:
        print(f"\n✅ Use these headers for authentication:")
        for key, value in working_headers.items():
            print(f"   {key}: {value}")
    else:
        print(f"\n❌ Authentication failed. Need to resolve API key issue.")

if __name__ == "__main__":
    asyncio.run(main())