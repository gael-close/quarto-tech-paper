#!/bin/bash
# Download and initialize the Quarto Tech Paper template

set -e

# Default destination, or use first argument
DEST="${1:-.}/quarto-tech-paper"

echo "Downloading Quarto Tech Paper template to: $DEST"

# Clone with sparse checkout
git clone --depth 1 --filter=blob:none --sparse https://github.com/gael-close/quarto-tech-paper.git "$DEST"
cd "$DEST"

# Configure sparse checkout for paper directory only
git sparse-checkout set --no-cone "paper/**"

# Navigate to paper and extract .env
cd paper
git show HEAD:paper/.env.example > .env

echo "✓ Template downloaded to: $(pwd)"
echo "✓ Next: pixi install"
