#!/bin/bash
# Download and initialize the Quarto Tech Paper template
# Cross-platform: Bash on Linux/macOS/Git Bash, PowerShell on Windows

set -e

echo "Downloading Quarto Tech Paper template..."

# Clone repository with sparse checkout
git clone --depth 1 --filter=blob:none --sparse https://github.com/gael-close/quarto-tech-paper.git temp-clone
cd temp-clone

# Configure sparse checkout for paper directory only
git sparse-checkout set --no-cone paper

# Move paper contents directly to current directory (avoid nesting)
mv paper/* .
rmdir paper

# Clean up temporary clone
cd ..
rm -rf temp-clone

echo "✓ Template initialized in current directory"
echo "Installing dependencies..."

# Install dependencies
pixi install

echo "✓ Setup complete!"
echo "✓ Next: pixi run render"
