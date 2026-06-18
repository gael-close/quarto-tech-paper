<# :
@echo off
# This section is read by Bash, but treated as a block comment by PowerShell

set -e

DEST="paper"

if [ -d "$DEST" ]; then
    echo "✗ Directory '$DEST' already exists. Please remove it or run from a different location."
    exit 1
fi

echo "Downloading Quarto Tech Paper template to: $DEST"

# Clone with sparse checkout
git clone --depth 1 --filter=blob:none --sparse https://github.com/gael-close/quarto-tech-paper.git temp-clone
cd temp-clone

# Configure sparse checkout for paper directory only
git sparse-checkout set --no-cone "paper/**"

# Move paper directory to current working directory
mv paper ../"$DEST"

# Clean up temporary clone
cd ..
rm -rf temp-clone

echo "✓ Template downloaded to: $(pwd)/$DEST"
echo "✓ Next: cd paper && pixi install"

# Exit Bash cleanly so it never reads the PowerShell code below
exit
#>

# --- PowerShell Section Starts Here ---
$DEST = "paper"

if (Test-Path $DEST) {
    Write-Host "✗ Directory '$DEST' already exists. Please remove it or run from a different location."
    exit 1
}

Write-Host "Downloading Quarto Tech Paper template to: $DEST"

git clone --depth 1 --filter=blob:none --sparse https://github.com/gael-close/quarto-tech-paper.git temp-clone
cd temp-clone

git sparse-checkout set --no-cone "paper/**"

Move-Item paper ../$DEST

cd ..
Remove-Item -Recurse -Force temp-clone

Write-Host "✓ Template downloaded to: $(Get-Location)\$DEST"
Write-Host "✓ Next: cd paper && pixi install"
