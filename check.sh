#!/usr/bin/env bash
# Consistency checker for render-all task
# Verifies that titles and filenames match across dist/ artifacts

set -euo pipefail

# Check the dist/ directory in the root of the project
DIST_DIR="${DIST_DIR:-dist}"

if [ ! -d "$DIST_DIR" ]; then
    echo "❌ Error: dist/ directory not found at: $DIST_DIR"
    echo "   Make sure to run this script from the project root."
    exit 1
fi

ERRORS=0

echo "🔍 Checking dist/ consistency..."
echo ""

# Extract HTML title and strip subtitle (everything after " - " or " – " em dash)
HTML_TITLE_FULL=$(grep -o '<title>[^<]*</title>' "$DIST_DIR/index.html" | sed 's/<title>\(.*\)<\/title>/\1/')
HTML_TITLE=$(echo "$HTML_TITLE_FULL" | sed -E 's/ [–-] .*//')
echo "📄 HTML title: $HTML_TITLE"
if [ "$HTML_TITLE_FULL" != "$HTML_TITLE" ]; then
    echo "   (stripped subtitle from: $HTML_TITLE_FULL)"
fi

# Extract manuscript title from markdown file
MANUSCRIPT_FILE="paper/manuscript/manuscript.md"
if [ -f "$MANUSCRIPT_FILE" ]; then
    MANUSCRIPT_TITLE=$(grep -E "^title:" "$MANUSCRIPT_FILE" | head -1 | sed 's/^title:[[:space:]]*//')
    echo "📝 Manuscript title: $MANUSCRIPT_TITLE"
else
    echo "⚠️  Warning: Could not find $MANUSCRIPT_FILE"
    MANUSCRIPT_TITLE=""
fi

# Find PDF file (should be exactly one)
PDF_COUNT=$(find "$DIST_DIR" -maxdepth 1 -name "*.pdf" | wc -l | tr -d ' ')
if [ "$PDF_COUNT" -ne 1 ]; then
    echo "❌ Error: Expected exactly 1 PDF file in dist/, found $PDF_COUNT"
    ERRORS=$((ERRORS + 1))
else
    PDF_FILE=$(find "$DIST_DIR" -maxdepth 1 -name "*.pdf" -print -quit)
    PDF_BASENAME=$(basename "$PDF_FILE" .pdf)
    echo "📦 PDF filename: $PDF_BASENAME"
    
    # Extract iframe src
    IFRAME_SRC=$(grep -o '<iframe[^>]*src="[^"]*"' "$DIST_DIR/index.html" | sed 's/.*src="\([^"]*\)".*/\1/' || echo "")
    if [ -n "$IFRAME_SRC" ]; then
        # Strip .pdf extension for comparison
        IFRAME_TITLE=$(basename "$IFRAME_SRC" .pdf)
        echo "🖼️  iframe src: $IFRAME_SRC"
    else
        echo "❌ Error: No iframe found in index.html"
        ERRORS=$((ERRORS + 1))
    fi
fi

echo ""
echo "═══════════════════════════════════════"

# Consistency checks
if [ "$PDF_COUNT" -eq 1 ]; then
    # Check 1: HTML title vs Manuscript title
    if [ -n "$MANUSCRIPT_TITLE" ]; then
        if [ "$HTML_TITLE" != "$MANUSCRIPT_TITLE" ]; then
            echo "❌ MISMATCH: HTML title ≠ Manuscript title"
            echo "   HTML:       '$HTML_TITLE'"
            echo "   Manuscript: '$MANUSCRIPT_TITLE'"
            ERRORS=$((ERRORS + 1))
        else
            echo "✅ HTML title = Manuscript title"
        fi
    fi
    
    # Check 2: Manuscript title vs PDF filename
    if [ -n "$MANUSCRIPT_TITLE" ]; then
        if [ "$MANUSCRIPT_TITLE" != "$PDF_BASENAME" ]; then
            echo "❌ MISMATCH: Manuscript title ≠ PDF filename"
            echo "   Manuscript: '$MANUSCRIPT_TITLE'"
            echo "   PDF:        '$PDF_BASENAME'"
            ERRORS=$((ERRORS + 1))
        else
            echo "✅ Manuscript title = PDF filename"
        fi
    fi
    
    # Check 3: iframe src vs PDF filename
    if [ -n "$IFRAME_SRC" ]; then
        if [ "$IFRAME_TITLE" != "$PDF_BASENAME" ]; then
            echo "❌ MISMATCH: iframe src ≠ PDF filename"
            echo "   iframe: '$IFRAME_TITLE'"
            echo "   PDF:    '$PDF_BASENAME'"
            ERRORS=$((ERRORS + 1))
        else
            echo "✅ iframe src = PDF filename"
        fi
    fi
    
    # Check 4: All three should match
    if [ -n "$MANUSCRIPT_TITLE" ] && [ -n "$IFRAME_SRC" ]; then
        if [ "$HTML_TITLE" = "$MANUSCRIPT_TITLE" ] && [ "$MANUSCRIPT_TITLE" = "$PDF_BASENAME" ] && [ "$IFRAME_TITLE" = "$PDF_BASENAME" ]; then
            echo "✅ All titles match: HTML = Manuscript = PDF filename = iframe"
        fi
    fi
fi

echo "═══════════════════════════════════════"

if [ $ERRORS -eq 0 ]; then
    echo "✅ All consistency checks passed!"
    exit 0
else
    echo "❌ Found $ERRORS error(s)"
    exit 1
fi
