
# A Quarto Tech Paper Example


## Introduction

The project structure is based on: https://github.com/gael-close/quarto-tech-paper.

**Prerequisites:**
- Install [pixi](https://pixi.sh/latest/#installation) for cross-platform task automation and environment management

## Quick Start

**Download the template:**
```bash
# Option 1: Download just the paper folder (recommended)
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/gael-close/quarto-tech-paper.git
cd quarto-tech-paper
git sparse-checkout set paper
mv paper ../my-project
cd ../my-project

# Option 2: Clone entire repository
git clone https://github.com/gael-close/quarto-tech-paper.git
cd quarto-tech-paper/paper
```

**Install dependencies:**
```bash
# Install ALL dependencies (conda packages + Python packages + local package)
pixi install
```

That's it! Pixi installs everything: uv, Quarto, Python packages, and the local `my_package` in editable mode.

**Note:** The `quarto-tech-memo` extension will be installed automatically on first render if not already present.

**Configuration** (`.env` file):
- `SHORT_TITLE` - Paper filename (default: "manuscript.pdf")
- `GOOGLE_FID` - Google Drive file ID for publishing

Run `pixi list`
 
## Usage

**Discover available tasks:**
```bash
pixi task list        # List all available tasks
pixi task info <task> # Show details for a specific task
```

**Common workflows:**
```bash
# Render manuscript to PDF
pixi run render

# Execute and convert notebooks to HTML
NB=01-notebook.ipynb pixi run notebook 
NB=02-notebook.py pixi run notebook-marimo
# on Windows: env:NB="01-notebook.ipynb"; pixi run notebook

# Build distribution website
pixi run dist

# Publish to Google Drive (see Publishing section)
pixi run pub-gdrive
```

**Run CLI scripts:**
```bash
pixi run plots --frequency 1
# or: pixi run python -m my_package.plots --frequency 0.5
```

**Python development:**
```bash
pixi run pytest -s        # Run tests
pixi run jupyter lab      # Open Jupyter
```

## Python Development

Organize code into **modular, reusable packages** for maintainability:

```python
from my_package.dataset import load_data
from my_package.analysis import run_analysis
from my_package.plots import plot_results
from my_package.config import RAW_DATA_DIR

df = load_data(RAW_DATA_DIR / "dataset.csv")
results = run_analysis(df)
plot_results(results)
```

The package (`my_package`) is installed in editable mode, so changes take effect immediately.

**Note:** All Python commands should be prefixed with `pixi run` to use the environment managed by pixi.

**Advanced:** If you modify `pyproject.toml` dependencies directly, run:
```bash
pixi run uv sync --extra dev
```

## Publishing

### Google Drive

Publish the manuscript PDF to Google Drive using PyDrive2:

1. **First-time setup:**
   - Create Google Drive API credentials ([instructions](https://console.cloud.google.com/))
   - Place `client_secrets.json` in `~/.config/pixi_gdrive/`
   - Run `pixi run pub-gdrive` - browser auth will open once

2. **Set file ID in `.env`:**
   ```
   GOOGLE_FID=your_google_drive_file_id
   ```

3. **Publish:**
   ```bash
   pixi run pub-gdrive
   ```

See [scripts/README.md](scripts/README.md) for detailed setup instructions.

### Website Distribution

Build a landing page with embedded PDF and supplementary materials:

```bash
pixi run dist
```

The output in `dist/` can be deployed to GitHub/GitLab Pages. Example workflow files are in `optional/`.

Customize the landing page in [site/index.qmd](site/index.qmd).