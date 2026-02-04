#!/bin/bash
# Run this from your Exitplaybook project folder where index.html lives
# Usage: bash update-site.sh

FILE="index.html"

echo "Updating $FILE..."

# 1. Hero text: revenue range $2M-$50M+ → $10M-$150M+
sed -i '' 's/\$2M–\$50M+ in revenue/\$10M–\$150M+ in revenue/g' "$FILE"

# 2. Stats banner: $2M-$50M+ Revenue Range → $10M-$150M+ Revenue Range
sed -i '' 's/>\$2M–\$50M+</>$10M–$150M+</g' "$FILE"

# 3. Stats banner: LMM → Lower Middle Market (with smaller font)
sed -i '' 's/<div class="st-n">LMM</<div class="st-n" style="font-size:1.6rem">Lower Middle Market</g' "$FILE"

# 4. About bio: $2M to $50M+ revenue → $10M to $150M+ revenue
sed -i '' 's/the \$2M to \$50M+ revenue space/the \$10M to \$150M+ revenue space/g' "$FILE"

# 5. Who It's For card: $2M-$50M+ → $10M-$150M+
sed -i '' "s/You're doing \$2M–\$50M+ in revenue/You're doing \$10M–\$150M+ in revenue/g" "$FILE"

# 6. Meta description update
sed -i '' 's/\$2M–\$50M+ in revenue/\$10M–\$150M+ in revenue/g' "$FILE"

# 7. All email addresses: eddieriva@gmail.com → info@theexitplaybook.net
sed -i '' 's/eddieriva@gmail.com/info@theexitplaybook.net/g' "$FILE"

# 8. Book section: "Learn More & Get a Free Chapter" → "Download the Free Book"
sed -i '' 's/Learn More \&amp; Get a Free Chapter/Download the Free Book/g' "$FILE"
sed -i '' 's/Learn More & Get a Free Chapter/Download the Free Book/g' "$FILE"

# 9. Book page: "Get a Free Chapter" → "Download Free Book (PDF)"
sed -i '' 's/Get a Free Chapter →/Download Free Book (PDF) →/g' "$FILE"

# 10. Book page CTA: "Request Your Free Chapter" → "Download the Full Book Free"
sed -i '' 's/Request Your Free Chapter/Download the Full Book Free/g' "$FILE"

# 11. Book page subtitle: "Drop your info and we'll send a sample chapter plus updates on the full release."
sed -i '' "s/Drop your info and we'll send a sample chapter plus updates on the full release./20 chapters of straight-talking M\&A guidance. Download your free copy today./g" "$FILE"

# 12. "Get Your Free Chapter" button → "Download Free PDF"
sed -i '' 's/Get Your Free Chapter →/Download Free PDF →/g' "$FILE"

# 13. "Buy on Amazon" → "View on Amazon"
sed -i '' 's/Buy on Amazon/View on Amazon/g' "$FILE"

# 14. Annual Revenue dropdown: update ranges to $10M-$150M+
sed -i '' 's/Under \$1M/Under \$10M/g' "$FILE"
sed -i '' 's/\$1M – \$5M/\$10M – \$25M/g' "$FILE"
sed -i '' 's/\$5M – \$10M/\$25M – \$50M/g' "$FILE"
sed -i '' 's/\$10M – \$25M/\$50M – \$100M/g' "$FILE"
sed -i '' 's/\$25M+/\$100M – \$150M/g' "$FILE"
# Add $150M+ option
sed -i '' 's/\$100M – \$150M<\/option><option>Prefer/\$100M – \$150M<\/option><option>\$150M+<\/option><option>Prefer/g' "$FILE"

echo "✅ All updates applied! Review changes then:"
echo "   git add . && git commit -m 'Update revenue ranges, emails, book download text' && git push"
