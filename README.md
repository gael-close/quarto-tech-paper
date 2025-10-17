# Quarto Tech Paper

> See [the companion medium article](https://medium.com/data-science-collective/turning-your-notes-into-pdf-technical-memos-or-data-science-reports-ddd150273cc6) for more background.

This repository contains the skeleton for a technical paper built
from computational Python notebooks, Python modular code, and markdown manuscript.
The manuscript is rendered in a well-formatted PDF by [Quarto](https://quarto.org/).
It is built upon two previous projects:

* [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/)
for the project structure and best practices for data science and scientific computing.
* [Quarto Tech Memo](https://github.com/gael-close/quarto-tech-memo)
for the report rendering as a well-formatted PDF tech memo or pre-print paper.

It is intended for technical papers (reports, preprints, ...) in engineering and science,
where data analysis and visualization is done in Python.

The skeleton contains:

* Data and code and supplementary computational notebooks
* The needed dependencies to re-run in a proper python environment.
* The manuscript in simple Markdown syntax.
* The data-intensive figures, which can be re-generated on demand. 
* Simple automation command(s) to render the paper and re-run the supplementary computational notebooks
(e.g. to update the figures when data or code has changed).


## PDF 2-column paper

The rendered paper is, by default, a 2-column PDF document.
The formats provided by the [Quarto Tech Memo](https://github.com/gael-close/quarto-tech-memo) 
are also available, including single-column tech memo, poster, slides.

Here is the [formatted PDF paper](https://github.com/gael-close/quarto-tech-paper/blob/master/example/paper.pdf)
generated from the template.

<img width=800 src="https://raw.githubusercontent.com/gael-close/quarto-tech-paper/master/example/thumbnail.png">


## Features 

* Directories organized similarly to [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/) that incorporate best practices for scientific computing.

* Proper git setup (git LFS, git ignore, ...)
* Paper manuscript in Quarto markdown with the ability to mix code, illustrations and narrative story in a lean syntax.
* Under the hood, the final formatting is handled by [Typst](https://typst.app/), 
a modern typesetting engine that is much easier and faster than Latex---this is [fully integrated in Quarto](https://quarto.org/docs/output-formats/typst.html).
* The Python dependencies are managed with [uv](https://docs.astral.sh/uv/) another modern and fast tool, which install dependencies on the fly in isolated reproducible environment
with one command.
* A `tasks.py` to invoke common operations with [invoke](https://docs.pyinvoke.org/en/stable/index.html)

Generally speaking, the project is designed to be as lean and simple as possible
while following best practices for scientific computing and reproducible research.
The tools used are modern and fast. They work on all major platforms (Linux, MacOS, Windows).
[VS code](https://code.visualstudio.com/) extensions are available for Quarto/Typst/Markdown
for a smooth writing experience (auto-completion, live & sync preview, spell checking, AI assistance...).

| Legacy tool        | Modern tool     |
| ------------------ | --------------- |
| Latex syntax       | Markdown syntax |
| PdfLatex rendering | Typst           |
| venv, pip          | uv              |
| Makefile           | invoke          |

## Installation (one-time only)

* Install [Conda](https://www.anaconda.com/download/success) or another equivalent python installation
* And a few python utilities (with `pip` or better `pipx` for full isolation)

```bash
pip install cookiecutter uv invoke
```

## Usage

Create a new project from this skeleton with cookiecutter.

```bash
cookiecutter gh:gael-close/quarto-tech-paper
cd new-repo
```

### Render the paper
To render a working copy of the paper (in 2-column memo format):

```bash
invoke render (--format memo2)
```

The rendered working copy should be available [there](reports/paper.pdf).
You can edit the source file `docs/paper.md` directly in your favorite editor,
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
The optional `--html` flag generates a standalone HTML version of the notebook,
in case it should be shared as supplementary materials to a broad audience.

## Python development recommendations

All code for generating the paper plots including data loading/analysis/visualization
should be in **modular Python code: functions inside re-usable installable package**.
While monolithic long scripts are OK, and even desirable, during development and tinkering,
the code should be refactored once stable for reusability and clarity.
A pipeline approach is recommended, with separate functions for data loading, analysis and plotting.
With this approach, the paper notebook is just a thin wrapper calling these functions.
They can be tested independently, 
reused in different notebooks or scripts residing in other directories,
or even invoked from other projects using the package once installed
(`pip install <path/to/my-project>` or the equivalent [`uv` command](https://docs.astral.sh/uv/pip/packages/)).

```python
from <package_name>.dataset import load_data1
from <package_name>.analysis import run_analysis1
from <package_name>.plot import plot_result1
from <package_name>.config import RAW_DATA_DIR
df=load_data1(RAW_DATA_DIR/"dataset.csv", remove_outliers=True)
results=run_analysis1(df)
plot_result1(results)
```
where `<package_name>` is the Python package name for this project (replace with your own).

In the present template, the package is automatically installed (with `uv run`), 
along with its dependencies, 
in editable mode so that changes to the functions are immediately available 
without re-installation or manual path manipulations.
Support notebooks in the `notebooks` directory can be used
for interactive development and tinkering.
Once the package is installed with `uv run`,
the package functions can be readily called from there.
The same hold for scripts, test cases, the paper quarto notebook itself,
or another python project.


Examples of Python development tasks:

```bash
# Start a jupyter notebook server in the notebooks directory
uv run jupyter notebook notebooks

# Optionally, sync the .ipynb and .py versions of the notebooks
# For easier code review and version control
uv run jupytext --sync notebooks/*.ipynb

# Run unit tests
uv run pytest

# Run a CLI script by wrapping a function in the package with Typer
## If the script is defined in pyproject.toml under [project.scripts]
uv run plots plot-sine --frequency 0.5
## Otherwise, call the function in the module with full path
uv run python -m new_repo.plots plot-sine --frequency 0.5
```

## Optional files

A few optional git config files are available in the `optional/` folder.
To enable them move them in the root folder.

## Development

To run a complete test suite to check that everything is working as expected:

```bash
invoke test
```

This should generate the skeleton project with cookiecutter,
render the paper and re-run the first notebook,
and open the generated files for visual inspection.


