# OpenRouter API Setup

## Quick Start

1. **Get an API Key**
   - Visit https://openrouter.ai/keys
   - Create a new API key
   - Keep it secure - never commit to git!

2. **Configure Environment**

   ```bash
   # Copy the example file
   cp .env.example .env

   # Edit .env and replace placeholder with your actual key
   # OPENROUTER_API_KEY=sk-or-v1-your-actual-key-here
   ```

3. **Load Environment Variables**

   ```bash
   # Option 1: Use python-dotenv (automatic)
   pip install python-dotenv

   # Option 2: Export manually
   export OPENROUTER_API_KEY=sk-or-v1-your-key-here

   # Option 3: Source the .env file
   source .env
   ```

## Security Best Practices

✅ **DO:**

- Store API key in `.env` file (already in .gitignore)
- Use environment variables: `os.getenv("OPENROUTER_API_KEY")`
- Rotate keys if accidentally exposed
- Use different keys for dev/prod

❌ **DON'T:**

- Hardcode keys in source files
- Commit `.env` to git (only `.env.example`)
- Share keys in documentation
- Use the same key across multiple projects

## Testing Your Setup

```bash
# Test the API key
python test_swarm.py

# Run the full swarm
python run_bottom_up_swarm.py
```

## Troubleshooting

- **"API key not found"**: Make sure `.env` exists and contains `OPENROUTER_API_KEY=...`
- **"User not found" (401)**: Your API key may be invalid or deactivated
- **"Rate limit exceeded"**: Check your OpenRouter dashboard for usage limits

## Key Rotation

If your key gets exposed on GitHub:

1. It will be automatically deactivated by OpenRouter
2. Generate a new key at https://openrouter.ai/keys
3. Update your local `.env` file
4. Never commit the actual key to git!
