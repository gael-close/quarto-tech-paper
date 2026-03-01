
# {{cookiecutter.directory}}

## Installation

The project structure is based on: https://github.com/gael-close/quarto-tech-paper.
Please refer to that repository for installation and usage instructions 

## Usage

ℹ️ First time any `uv ...` command run, it will install 
the needed dependencies in a virtual env.


### Render the manuscript

This command generates the [rendered manuscript.pdf](manuscript/manuscript.pdf) (in 2-column memo format):

```bash
invoke render (--format memo2)
```

You can edit the [source manuscript.md](manuscript/manuscript.md)
directly in your favorite editor,
and preview the compiled version updated automatically in your browser with:

```bash
invoke render --preview
```

### Re-run the supplementary computational notebooks

Whenever the data or the code has changed,
re-run the supplementary notebook(s) in the project virtual environment with:

```bash
invoke notebook 01-notebook.ipynb (--html)
```

The updated plots will be embedded automatically next time the paper is rendered.
The optional `--html` flag generates a standalone
[HTML version 01-notebook.html](reports/01-notebook.html)
in case it should be shared as supplementary materials to a broad audience.

### Run CLI scripts

Some scripts are available as CLI commands as defined in pyproject.toml. Example:

```bash
uv run plots --frequency 1
```

