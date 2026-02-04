#!/usr/bin/env python3
"""
Fix all site text in index.html
Handles BOTH possible states:
  - Original file: $2M-$50M+ revenue
  - Partially edited: $3M-$15M EBITDA
Run from your Exitplaybook folder: python3 fix-site.py
"""

with open('index.html', 'r', encoding='utf-8') as f:
    t = f.read()

original = t
changes = []

def rep(old, new, label):
    global t
    if old in t:
        t = t.replace(old, new)
        changes.append(f"  \u2713 {label}")

# ============================================================
# 1. HERO TEXT - revenue range
# ============================================================
# From partially edited version ($3M-$15M EBITDA)
rep('$3M\u2013$15M in EBITDA', '$10M\u2013$150M+ in revenue', 'Hero: EBITDA→revenue')
# From original version ($2M-$50M+)
rep('$2M\u2013$50M+ in revenue', '$10M\u2013$150M+ in revenue', 'Hero: $2M→$10M revenue')

# ============================================================
# 2. META DESCRIPTION
# ============================================================
rep('$3M\u2013$15M in EBITDA. We guide', '$10M\u2013$150M+ in revenue. We guide', 'Meta: EBITDA→revenue')
rep('$2M\u2013$50M+ in revenue. We guide', '$10M\u2013$150M+ in revenue. We guide', 'Meta: $2M→$10M')

# ============================================================
# 3. STATS BANNER - number + label
# ============================================================
rep('>$3M\u2013$15M<', '>$10M\u2013$150M+<', 'Stats banner: $3M→$10M')
rep('>$2M\u2013$50M+<', '>$10M\u2013$150M+<', 'Stats banner: $2M→$10M')
rep('>EBITDA Range<', '>Revenue Range<', 'Stats label: EBITDA→Revenue')

# ============================================================
# 4. LMM → Lower Middle Market (with smaller font)
# ============================================================
rep('<div class="st-n">LMM</div>', '<div class="st-n" style="font-size:1.6rem">Lower Middle Market</div>', 'LMM→Lower Middle Market')

# ============================================================
# 5. ABOUT BIO
# ============================================================
rep('the $3M to $15M EBITDA space', 'the $10M to $150M+ revenue space', 'Bio: EBITDA→revenue')
rep('the $2M to $50M+ revenue space', 'the $10M to $150M+ revenue space', 'Bio: $2M→$10M')

# ============================================================
# 6. WHO IT'S FOR CARD
# ============================================================
rep('$3M\u2013$15M in EBITDA and want', '$10M\u2013$150M+ in revenue and want', 'Card: EBITDA→revenue')
rep("You\u2019re doing $2M\u2013$50M+ in revenue", "You\u2019re doing $10M\u2013$150M+ in revenue", 'Card: $2M→$10M (smart quote)')
rep("You're doing $2M\u2013$50M+ in revenue", "You're doing $10M\u2013$150M+ in revenue", 'Card: $2M→$10M')

# ============================================================
# 7. ALL EMAILS
# ============================================================
rep('eddieriva@gmail.com', 'info@theexitplaybook.net', 'Email: gmail→info@')

# Cloudflare-encoded email links in footer/about/contact/CPA
# These are /cdn-cgi/l/email-protection# links - replace with real mailto
rep('href="/cdn-cgi/l/email-protection#90f9fef6ffd0e4f8f5f5e8f9e4e0fcf1e9f2fffffbbefef5e4"', 
    'href="mailto:info@theexitplaybook.net"', 'Footer email link')
rep('href="/cdn-cgi/l/email-protection#83eaede5ecc3f7ebe6e6fbeaf7f3efe2fae1ecece8adede6f7"',
    'href="mailto:info@theexitplaybook.net"', 'About email link')
rep('href="/cdn-cgi/l/email-protection#d0b9beb6bf90a4b8b5b5a8b9a4a0bcb1a9b2bfbfbbfebeb5a4"',
    'href="mailto:info@theexitplaybook.net"', 'Contact email link')
# CPA partnership encoded link
if '/cdn-cgi/l/email-protection#' in t and 'CPA' in t:
    # Find and replace any remaining cloudflare-encoded email links
    import re
    t = re.sub(r'href="/cdn-cgi/l/email-protection#[a-f0-9]+"', 
               'href="mailto:info@theexitplaybook.net?subject=CPA%20Referral%20Partnership"', t, count=0)
    changes.append("  \u2713 All CF-encoded email links→mailto")

# Also fix the [email protected] display text
rep('<span class="__cf_email__" data-cfemail="31585f575e7145595454495845415d5048535e5e5a1f5f5445">[email\xa0protected]</span>',
    'info@theexitplaybook.net', 'Contact email display text')

# ============================================================
# 8. BOOK BUTTONS - "Free Chapter" → "Download Book"
# ============================================================
rep('Learn More &amp; Get a Free Chapter', 'Download the Free Book', 'Home book btn (encoded)')
rep('Learn More & Get a Free Chapter', 'Download the Free Book', 'Home book btn')
rep('Download the Free Book \u2192', 'Download the Free Book \u2192', 'Home book (already done)')
rep('Get a Free Chapter \u2192', 'Download Free Book (PDF) \u2192', 'Book page main btn')
rep('Request Your Free Chapter', 'Download the Full Book Free', 'Book page CTA heading')
rep("Drop your info and we\u2019ll send a sample chapter plus updates on the full release.",
    "20 chapters of straight-talking M&A guidance. Download your free copy today.", 'Book subtitle (smart quote)')
rep("Drop your info and we'll send a sample chapter plus updates on the full release.",
    "20 chapters of straight-talking M&A guidance. Download your free copy today.", 'Book subtitle')
rep('Get Your Free Chapter \u2192', 'Download Free PDF \u2192', 'Book download btn')

# ============================================================
# 9. AMAZON BUTTON
# ============================================================
rep('Buy on Amazon', 'View on Amazon', 'Amazon btn')

# ============================================================
# 10. CONTACT FORM DROPDOWN
# ============================================================
# From partially edited (EBITDA ranges)
rep('<label class="fl">EBITDA Range</label>', '<label class="fl">Annual Revenue</label>', 'Dropdown label: EBITDA→Revenue')
rep('>Under $3M<', '>Under $10M<', 'Dropdown: Under $3M')
rep('>$3M \u2013 $5M<', '>$10M \u2013 $25M<', 'Dropdown: $3M-$5M')
rep('>$5M \u2013 $10M<', '>$25M \u2013 $50M<', 'Dropdown: $5M-$10M')
rep('>$10M \u2013 $15M<', '>$50M \u2013 $100M<', 'Dropdown: $10M-$15M')
rep('>$15M+<', '>$100M \u2013 $150M<', 'Dropdown: $15M+')

# From original (revenue ranges)  
rep('>Under $1M<', '>Under $10M<', 'Dropdown: Under $1M')
rep('>$1M \u2013 $5M<', '>$10M \u2013 $25M<', 'Dropdown: $1M-$5M')
rep('>$5M \u2013 $10M<', '>$25M \u2013 $50M<', 'Dropdown: $5M-$10M orig')
rep('>$10M \u2013 $25M<', '>$50M \u2013 $100M<', 'Dropdown: $10M-$25M')
rep('>$25M+<', '>$100M \u2013 $150M<', 'Dropdown: $25M+')

# Add $150M+ option (works for both states)
rep('$100M \u2013 $150M</option><option>Prefer', 
    '$100M \u2013 $150M</option><option>$150M+</option><option>Prefer', 'Dropdown: add $150M+')

# ============================================================
# RESULTS
# ============================================================
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(t)

if original != t:
    print("\u2705 Updates applied successfully!")
    print(f"   {len(changes)} changes made:")
    for c in changes:
        print(c)
    print()
    # Verify key terms exist
    print("Verification:")
    checks = [
        ('$10M\u2013$150M+', 'revenue range'),
        ('info@theexitplaybook.net', 'email updated'),
        ('Lower Middle Market</div>', 'LMM spelled out'),
        ('Download the Free Book', 'book button text'),
        ('View on Amazon', 'amazon button'),
        ('Annual Revenue', 'dropdown label'),
        ('$150M+', '$150M+ option'),
    ]
    for term, label in checks:
        status = "\u2713" if term in t else "\u2717 MISSING"
        print(f"  {status} {label}")
    
    # Check for leftover old values
    print("\nLeftover check (should be empty):")
    for bad in ['eddieriva@gmail.com', 'Free Chapter', '>LMM<', '$2M\u2013$50M', '$3M\u2013$15M']:
        if bad in t:
            print(f"  \u26a0\ufe0f  Still found: {bad}")
    print()
    print("Next steps:")
    print("  git add . && git commit -m 'Update all site content' && git push")
else:
    print("\u274c No changes made! The patterns didn't match your file.")
    print("Run this to check what's in your file:")
    print("  grep -n '\\$[0-9]M' index.html | head -20")
