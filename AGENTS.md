# AGENTS.md - Coding Guidelines for Agentic Development

This guide helps AI agents and developers work effectively in the quarto-tech-paper repository.

## Project Overview

This is a **Quarto-based scientific paper template** integrating:
- Python data analysis and visualization (modular packages in `src/`)
- Computational notebooks (Jupyter with Jupytext sync)
- Manuscript in Quarto/Markdown (rendered to PDF via Typst)
- Modern tooling: `uv` (package management), `invoke` (task automation), `pytest` (testing)

## Build, Lint, and Test Commands

### Install & Setup
```bash
# One-time: install uv, invoke, quarto-tech-memo
pip install uv invoke quarto-tech-memo

# Create new project
cookiecutter gh:gael-close/quarto-tech-paper
cd new-dir
```

### Run Tests
```bash
# All tests
uv run pytest

# Single test by name
uv run pytest -k "test_load_data"

# Specific file
uv run pytest tests/tests.py

# Verbose + print statements
uv run pytest -v -s

# Debug mode (pdb on failure)
uv run pytest --pdb

# Collect only (no execution)
uv run pytest --co
```

### Render Manuscript
```bash
# Render to PDF (memo2 format default)
invoke render

# With live browser preview
invoke render --preview

# Different format (memo1, slides, poster, ieee)
invoke render --to ieee
```

### Run Notebooks & Scripts
```bash
# Execute notebook in-place
invoke notebook 01-notebook.ipynb

# Execute + generate HTML report
invoke notebook 01-notebook.ipynb --html

# CLI entry points (defined in pyproject.toml)
uv run plots plot-sine --frequency 0.5

# Start Jupyter lab for development
uv run jupyter lab notebooks
```

## Code Style Guidelines

### Python Imports
- Order: standard library → third-party → local imports
- One import per line (preferred)
- Absolute imports from package root: `from new_dir.config import DATA_DIR`

```python
from pathlib import Path
import numpy as np
import pandas as pd
from loguru import logger
from new_dir.config import DATA_DIR
from new_dir.dataset import load_data
```

### Formatting & Structure
- **Line length**: ~100 characters
- **Indentation**: 4 spaces (never tabs)
- **Blank lines**: 2 between functions/classes, 1 within
- **String formatting**: f-strings only: `f"Value: {x:.2f}"`
- **Trailing commas**: In multi-line lists/dicts

### Type Hints
- **Required** on all function signatures
- Use `Optional[T]` not `Union[T, None]`
- Use `pathlib.Path` not strings for file paths

```python
def load_data(path: Path, remove_outliers: bool = True) -> pd.DataFrame:
    """Load CSV with optional outlier removal."""
    pass
```

### Naming Conventions
- Variables/functions: `snake_case`
- Constants: `UPPER_SNAKE_CASE` (e.g., `DATA_DIR`, `RAW_DATA_DIR`)
- Classes: `PascalCase`
- Private methods: Leading underscore `_private_method`
- Descriptive names: full words (abbreviations OK: `df` for DataFrame)

### Error Handling
- Catch **specific** exceptions, never bare `except:`
- Include helpful error messages with context
- Log errors via `loguru.logger`
- Re-raise after logging if needed

```python
try:
    df = pd.read_csv(path)
except FileNotFoundError as e:
    logger.error(f"Data file missing: {path}")
    raise
```

### Docstrings (Google Style)
```python
def analyze_data(df: pd.DataFrame, threshold: float = 0.5) -> dict:
    """Analyze dataframe with given threshold.
    
    Args:
        df: Input dataframe to analyze.
        threshold: Cutoff value for filtering.
        
    Returns:
        Dictionary with analysis results.
        
    Raises:
        ValueError: If threshold is negative.
    """
    pass
```

### Logging
- **Tool**: `loguru` (import as `from loguru import logger`)
- Avoid `print()` in library code
- Use: `logger.debug()`, `logger.info()`, `logger.warning()`, `logger.error()`
- Configured in `src/new_dir/config.py` (integrates with tqdm)

```python
logger.info(f"Processing: {path}")
logger.warning(f"Missing column: {col}")
logger.error(f"Failed to analyze: {error}")
```

### Paths & Configuration
- Use `pyprojroot` + `pathlib.Path` for all file operations
- Import from config: `from new_dir.config import DATA_DIR, REPORTS_DIR`
- Never hardcode paths or use relative paths

```python
from pathlib import Path
from new_dir.config import DATA_DIR, REPORTS_DIR

df = pd.read_csv(DATA_DIR / "raw" / "file.csv")
fig.savefig(REPORTS_DIR / "plot.png")
```

### Project Structure
- **Source code**: `src/new_dir/` (main package)
- **Data**: `data/raw/`, `data/processed/`
- **Tests**: `tests/` (pytest ignores `*dev.py` per pytest.ini)
- **Notebooks**: `notebooks/` (sync'd to `.py` via Jupytext)
- **Manuscript**: `manuscript/manuscript.md` (Quarto)
- **Reports**: `reports/` (generated HTML, PDFs)

### Testing with pytest
- **Framework**: pytest
- **Fixtures**: Use `@pytest.fixture` for test data
- **Parametrization**: Use `@pytest.mark.parametrize` for multiple cases
- **Assertions**: Standard `assert`, not unittest-style

```python
@pytest.fixture
def sample_data():
    return pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})

@pytest.mark.parametrize("x,expected", [(1, 2), (2, 4)])
def test_double(x, expected):
    assert x * 2 == expected
```

### CLI Scripts (Typer)
- Define in `src/new_dir/plots.py` or similar
- Register entry points in `pyproject.toml` under `[project.scripts]`
- Use `typer.Typer()` for commands

```python
import typer

app = typer.Typer()

@app.command()
def process(file: Path, verbose: bool = False) -> None:
    """Process a file."""
    pass

if __name__ == "__main__":
    app()
```

## Dependencies

- **Manager**: `uv` (modern, fast)
- **Lock file**: `uv.lock` (commit to git)
- **Definition**: `pyproject.toml` under `[project] dependencies`
- **Virtual env**: Auto-created in `.venv/`

```bash
uv run <command>   # Runs in isolated environment
uv pip install pkg # Add new packages
```

## Key Packages
pandas, numpy, matplotlib, seaborn, holoviews/hvplot, jupyterlab, jupytext, pytest, loguru, typer, python-dotenv, pyprojroot

## Common Pitfalls

1. **Don't use print()** → Use `logger` instead
2. **Don't hardcode paths** → Use config module + `Path`
3. **Don't skip type hints** → Add to all functions
4. **Don't catch broad exceptions** → Catch specific types, re-raise
5. **Don't edit `.ipynb` directly** → Edit `.py` files (Jupytext syncs)
6. **Don't skip docstrings** → Document all public functions
7. **Don't ignore dependencies** → Update `pyproject.toml`, run `uv lock`

## Notes

- No `.cursorrules` or GitHub Copilot instructions found
- Follow PEP 8 for Python code style
- Commit `uv.lock` for reproducibility
- Use invoke tasks for automation (`invoke --help` to see all tasks)
