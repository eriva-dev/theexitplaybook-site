#!/bin/bash
FILE="index.html"
echo "Updating $FILE..."

# 1. Hero text
sed -i '' 's/\$3M–\$15M in EBITDA/\$10M–\$150M+ in revenue/g' "$FILE"

# 2. Stats banner number
sed -i '' 's/>\$3M–\$15M</>\$10M–\$150M+</g' "$FILE"

# 3. Stats banner label EBITDA Range → Revenue Range
sed -i '' 's/>EBITDA Range</>Revenue Range</g' "$FILE"

# 4. Stats banner LMM → Lower Middle Market
sed -i '' 's/<div class="st-n">LMM</<div class="st-n" style="font-size:1.6rem">Lower Middle Market</g' "$FILE"

# 5. About bio
sed -i '' 's/the \$3M to \$15M EBITDA space/the \$10M to \$150M+ revenue space/g' "$FILE"

# 6. Who Its For card
sed -i '' "s/\$3M–\$15M in EBITDA and want/\$10M–\$150M+ in revenue and want/g" "$FILE"

# 7. Meta description
sed -i '' 's/\$3M–\$15M in EBITDA. We guide/\$10M–\$150M+ in revenue. We guide/g' "$FILE"

# 8. All email addresses
sed -i '' 's/eddieriva@gmail.com/info@theexitplaybook.net/g' "$FILE"

# 9. Book home section: "Learn More & Get a Free Chapter"
sed -i '' 's/Learn More \&amp; Get a Free Chapter/Download the Free Book/g' "$FILE"
sed -i '' 's/Learn More & Get a Free Chapter/Download the Free Book/g' "$FILE"

# 10. Book page: "Get a Free Chapter →"
sed -i '' 's/Get a Free Chapter →/Download Free Book (PDF) →/g' "$FILE"

# 11. "Request Your Free Chapter"
sed -i '' 's/Request Your Free Chapter/Download the Full Book Free/g' "$FILE"

# 12. Chapter description text
sed -i '' "s/Drop your info and we'll send a sample chapter plus updates on the full release./20 chapters of straight-talking M\&A guidance. Download your free copy today./g" "$FILE"

# 13. "Get Your Free Chapter →"
sed -i '' 's/Get Your Free Chapter →/Download Free PDF →/g' "$FILE"

# 14. "Buy on Amazon"
sed -i '' 's/Buy on Amazon/View on Amazon/g' "$FILE"

# 15. Contact form EBITDA label → Annual Revenue
sed -i '' 's/>EBITDA Range<\/label>/>Annual Revenue<\/label>/g' "$FILE"

# 16. Fix dropdown - replace old EBITDA ranges with revenue ranges
sed -i '' 's/>Under \$3M</>Under \$10M</g' "$FILE"
sed -i '' 's/>\$3M – \$5M</>$10M – $25M</g' "$FILE"
sed -i '' 's/>\$5M – \$10M</>\$25M – \$50M</g' "$FILE"  
sed -i '' 's/>\$10M – \$15M</>\$50M – \$100M</g' "$FILE"
sed -i '' 's/>\$15M+</>\$100M – \$150M</g' "$FILE"
# Add $150M+ option before Prefer not to say
sed -i '' 's/\$100M – \$150M<\/option><option>Prefer/\$100M – \$150M<\/option><option>\$150M+<\/option><option>Prefer/g' "$FILE"

echo "✅ All updates applied!"
echo "Run: git add . && git commit -m 'Fix all site text updates' && git push"
