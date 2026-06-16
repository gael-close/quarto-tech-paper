# AGENTS.md: Development Guidelines for Agentic Coding

This guide provides instructions for agentic coding systems working in this repository.

## Project Overview

This is a Python research/data science project built with `uv` for dependency management and `task` (Taskfile) for task automation. The project generates technical papers/memos with supplementary computational notebooks and modular Python packages.

**Key Technologies:** Python 3.10+, Quarto, Jupyter/Marimo notebooks, Taskfile, Pytest

## Build, Lint & Test Commands

### Setup & Dependencies

```bash
# Install project and dependencies in virtual environment
uv sync

# Activate virtual environment (alternative to uv run prefix)
source .venv/bin/activate  # macOS/Linux
.\venv\Scripts\activate     # Windows
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run single test file
uv run pytest tests/tests.py

# Run single test function
uv run pytest tests/tests.py::test_load_data

# Run tests matching keyword pattern
uv run pytest -k "test_dummy"

# Run tests with verbose output and print statements
uv run pytest -s tests/tests.py

# Run with interactive debugger on failure
uv run pytest --pdb tests/tests.py

# Collect tests without running
uv run pytest --co
```

### Build/Render

```bash
# Render manuscript to PDF (memo2 format default)
task render

# Render with specific format
task render TO=memo2

# Execute and optionally convert supplementary notebooks to HTML
task notebook NOTEBOOK=01-notebook.ipynb
task notebook NOTEBOOK=01-notebook.ipynb HTML=true
task notebook NOTEBOOK=02-notebook.py
task notebook NOTEBOOK=02-notebook.py HTML=true
```

### Running CLI Scripts

```bash
# Run CLI app defined in pyproject.toml
uv run plots --frequency 1

# Direct Python invocation
uv run python -m new_dir.plots --frequency 0.5
```

## Code Style Guidelines

### Imports

- **Organization**: Standard library → third-party → local imports, each group separated by blank lines
- **Format**: Use full module imports; avoid `from module import *` (except in test scratchpads)
- **Example**:
  ```python
  from pathlib import Path
  from loguru import logger
  import pandas as pd
  import numpy as np
  from .config import DATA_DIR
  ```

### Naming Conventions

- **Modules/Files**: `snake_case` (e.g., `plots.py`, `config.py`)
- **Functions/Variables**: `snake_case` (e.g., `plot_joint()`, `load_data()`)
- **Classes**: `PascalCase` (e.g., `DataProcessor`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `DATA_DIR`, `PROJ_ROOT`)
- **Private members**: Leading underscore (e.g., `_internal_helper()`)

### Type Annotations

- Use type hints for function signatures: `def load_data(path: Path) -> pd.DataFrame:`
- Annotate return types explicitly, especially for public APIs
- Use `Optional[Type]` from `typing` for nullable values
- Type hints are encouraged but not strictly required for exploratory code

### Formatting & Structure

- **Line length**: Aim for 88 characters (common Python standard)
- **Docstrings**: Use triple quotes with brief description; add parameter/return docs for public functions
  ```python
  def plot_joint(df) -> None:
      """Plot joint distribution of weight vs horsepower from auto-mpg data."""
  ```
- **Blank lines**: Two between top-level functions/classes, one within function sections

### Error Handling

- **Logging**: Use `loguru.logger` for all logging (configured in `config.py`)
  ```python
  from loguru import logger
  logger.info("Processing started")
  logger.error("Failed to load data", exc_info=True)
  ```
- **Exceptions**: Raise meaningful exceptions with descriptive messages; avoid bare `except:` clauses
- **Validation**: Check inputs early in functions; raise `ValueError` or `TypeError` with context

### Package Structure

- **Modular design**: Organize code into reusable functions in `src/new_dir/`
- **Separation of concerns**: Data loading → analysis → plotting (distinct modules/functions)
- **Configuration**: Use `src/new_dir/config.py` for paths, environment variables, logger setup
- **CLI apps**: Use `typer` for command-line interfaces (see `plots.py` for example)

### Testing

- **Test location**: Place tests in `tests/` directory
- **Test naming**: `test_*.py` files with `test_*()` functions
- **Fixtures**: Use `@pytest.fixture` for reusable test data
- **Parametrization**: Use `@pytest.mark.parametrize()` for multiple test cases
- **Assertions**: Use clear assertions; leverage `pytest.approx()` for floating-point comparisons

### Notebook Development

- **Percent format**: Notebooks use `jupytext` with percent-format (`.py` files with `# %%` cells)
- **Interactive development**: Test in Jupyter/VSCode interactive mode first, then refactor into modules
- **Integration**: After stable, extract core functions into `src/new_dir/` package for reuse

## Configuration Files

- **pyproject.toml**: Project metadata, dependencies, build config, CLI scripts
- **pytest.ini**: Pytest configuration (ignores `*dev.py`, runs from `tests/`)
- **Taskfile.yml**: Taskfile task definitions (render, notebook, etc.)
- **.python-version**: Specifies Python version (3.10+)

## Project Architecture

```
src/new_dir/           # Main package
├── __init__.py
├── config.py          # Paths, logger, env vars
├── dataset.py         # Data loading
├── features.py        # Feature engineering
├── plots.py           # Plotting functions & CLI
├── modeling/          # Modeling subpackage
tests/                 # Test directory
notebooks/            # Jupyter/Marimo notebooks
manuscript/           # Quarto manuscript source
```

## Dependencies Management

- **Primary tool**: `uv` (fast Python package installer/resolver)
- **Adding packages**: Edit `pyproject.toml` [project.dependencies], then `uv sync`
- **Virtual environment**: Automatically created in `.venv/`
- **Editable install**: Package installs in editable mode automatically via `uv run`
