#!/bin/bash
# Kolmogorov Compressor - Instant clarity check for any text

if [ $# -eq 0 ]; then
    echo "Usage: ./compress.sh <file> or echo 'text' | ./compress.sh"
    exit 1
fi

# Count metrics
text="${1:-$(cat)}"
words=$(echo "$text" | wc -w)
chars=$(echo "$text" | wc -c)
hedges=$(echo "$text" | grep -oE "(perhaps|maybe|seems|appears|might|possibly|probably)" | wc -l)
fluff=$(echo "$text" | grep -oE "(As you know|It's important to note|In today's world|To be honest|In conclusion)" | wc -l)

echo "=== KOLMOGOROV ANALYSIS ==="
echo "Words: $words"
echo "Characters: $chars"
echo "Hedge words: $hedges"
echo "Fluff phrases: $fluff"
echo ""

# Calculate clarity score
if [ $words -gt 100 ]; then
    echo "❌ TOO LONG: Over 100 words. Compress by 50%+"
elif [ $hedges -gt 2 ]; then
    echo "⚠️  HEDGING: Remove uncertainty. Be direct."
elif [ $fluff -gt 0 ]; then
    echo "⚠️  FLUFF: Delete throat-clearing phrases."
else
    echo "✅ CLEAR: Minimal verbosity detected."
fi