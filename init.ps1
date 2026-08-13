# Download and initialize the Quarto Tech Paper template
# PowerShell version for Windows

$ErrorActionPreference = "Stop"

Write-Host "Downloading Quarto Tech Paper template..."

# Clone repository with sparse checkout
git clone --depth 1 --filter=blob:none --sparse https://github.com/gael-close/quarto-tech-paper.git temp-clone
cd temp-clone

# Configure sparse checkout for paper directory only
git sparse-checkout set --no-cone paper

# Move paper contents directly to current directory (avoid nesting)
Get-ChildItem -Path "paper" -Force | Move-Item -Destination ".."
Remove-Item -Path "paper" -Force

cd ..
Remove-Item -Recurse -Force temp-clone

Write-Host "✓ Template initialized in current directory"
Write-Host "Installing dependencies..."

# Install dependencies
pixi install

Write-Host "✓ Setup complete!"
Write-Host "✓ Next: pixi run render"
