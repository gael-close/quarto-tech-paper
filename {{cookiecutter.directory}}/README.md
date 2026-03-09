
# {{cookiecutter.directory}}

## Installation

The project structure is based on: https://github.com/gael-close/quarto-tech-paper.
Please refer to that repository for installation and usage instructions 

## Usage

ℹ️ First time any `uv ...` command run, it will install 
the needed dependencies in a virtual env.

> The `uv run ...` prefix ensures that the command is executed in the project virtual environment,
> and this is considered the best practice.
> Alternatively, you can activate the virtual environment once for all with 
> `.\venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Linux/Mac) 
> and run the commands without the prefix.

### Render the manuscript

This command generates the [rendered manuscript.pdf](manuscript/manuscript.pdf) (in 2-column memo format):

```bash
uv run invoke render (--format memo2)
```

You can edit the [source manuscript.md](manuscript/manuscript.md)
directly in your favorite editor,
and preview the compiled version updated automatically in your browser with:

```bash
uv run invoke render --preview
```

### Re-run the supplementary computational notebooks

Whenever the data or the code has changed,
re-run the supplementary notebook(s) in the project virtual environment with:

```bash
uv run invoke notebook 01-notebook.ipynb --html
uv run invoke notebook 02-notebook.py --html
```

Note that the second notebook is the tutorial [marimo notebook](https://marimo.io/).
See also [this article](https://towardsdatascience.com/why-im-making-the-switch-to-marimo-notebooks/)
for the motivation behind this new notebook format.
Install the [vscode extension](https://marketplace.visualstudio.com/items?itemName=marimo-team.vscode-marimo)
to run it in VSCode or via the CLI:

```bash
uv run marimo edit notebooks/02-notebook.py
```

The updated plots will be embedded automatically next time the paper is rendered.
The optional `--html` flag generates standalone HTML versions of the notebooks 
in the `reports` directory. 
These files can be shared as supplementary materials:
* [HTML version 01-notebook.html](reports/01-notebook.html)
* [HTML version 02-notebook.html](reports/02-notebook.html)


### Run CLI scripts

Some scripts are available as CLI commands as defined in pyproject.toml. Example:

```bash
uv run plots --frequency 1
```

