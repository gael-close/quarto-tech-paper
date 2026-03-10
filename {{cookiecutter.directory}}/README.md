
# {{cookiecutter.directory}}

## Installation

The project structure is based on: https://github.com/gael-close/quarto-tech-paper.

Install the quarto and the quarto-tech-memo tool 
with [uv](https://docs.astral.sh/uv/getting-started/installation/),

```bash { name=install }
uv tool install quarto-cli
uv tool install quarto-tech-memo
```

## Usage

ℹ️ First time any `uv ...` command run, it will install 
the needed dependencies in a virtual env.

> The `uv run` prefix ensures that the command is executed in the project virtual environment.
> Alternatively, you can create and activate the virtual environment once for all,
> and run the commands *without* the `uv run` prefix.
> This can be automated whenever you enter the directory with [direnv](https://direnv.net/)

```bash
uv sync
.\venv\Scripts\activate #Windows
source .venv/bin/activate #(Linux/Mac)
```

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

```bash {name=notebook}
uv run invoke notebook 01-notebook.ipynb --html
uv run invoke notebook 02-notebook.py --html
```

Note that the second notebook is the tutorial [marimo notebook](https://marimo.io/).
See also [this article](https://towardsdatascience.com/why-im-making-the-switch-to-marimo-notebooks/)
for the motivation behind this new notebook format.
Install the [vscode extension](https://marketplace.visualstudio.com/items?itemName=marimo-team.vscode-marimo)
to run it in VSCode.

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
# Alternative: direct invokation
# uv run python -m new_dir.plots --frequency 0.5
```


## Python development recommendations

All code for generating the paper plots including data loading/analysis/visualization
should be in **modular Python code: functions inside re-usable installable package**.
While monolithic long scripts are OK, and even desirable, during development and tinkering,
the code should be refactored once stable for reusability and clarity.
A pipeline approach is recommended, with separate functions for data loading, analysis and plotting.
With this approach, the paper notebook is just a thin wrapper calling these functions.
They can be tested independently, 
reused in different notebooks or scripts residing in other directories,
or even invoked from other projects using the package once installed.

```python
from <package>.dataset import load_data1
from <package>.analysis import run_analysis1
from <package>.plot import plot_result1
from <package>.config import RAW_DATA_DIR
df=load_data1(RAW_DATA_DIR/"dataset.csv", remove_outliers=True)
results=run_analysis1(df)
plot_result1(results)
```

where `<package>` is the Python package name for this project (replace with your own).

The package is automatically installed (with `uv run`), 
along with its dependencies, 
in editable mode so that changes to the functions are immediately available 
without re-installation or manual path manipulations.


Examples of Python development tasks:

```bash
# Edit notebooks
uv run jupyter notebook notebooks
uv run marimo edit notebooks

# Run unit tests
uv run pytest
```