
# A Quarto Tech Paper Example


## Introduction

The project structure is based on: https://github.com/gael-close/quarto-tech-paper.

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) 
and [taskfile.dev](https://taskfile.dev/docs/installation) 
as described in their documentation.
This is for Python environment management and task automation, respectively.

The command `task list` shows the available tasks,
and `task <taskname> --dry` shows the commands to be executed.
The tasks are defined in the [Taskfile.yml](Taskfile.yml) file.

## Installation

```bash
task install
```

By default, generic names are used

* The Python package is "my_package",
* The paper filename is "manuscript.pdf". It can be adjusted in `.env`.


## Usage

### Render the manuscript
This command generates the [rendered manuscript.pdf](manuscript/manuscript.pdf) (in 2-column memo format):

```bash
task render (TO=memo2)
```

### Re-run the supplementary computational notebooks

Whenever the data or the code has changed,
re-run the supplementary notebook(s) in the project virtual environment with:

```bash {name=notebook}
# Just execute
task notebook NB=01-notebook.ipynb
task notebook NB=02-notebook.py

# Execute and convert to HTML
task notebook NB=01-notebook.ipynb HTML=true
task notebook NB=02-notebook.py HTML=true
```

Note that the second notebook is the tutorial [marimo notebook](https://marimo.io/).
See also [this article](https://towardsdatascience.com/why-im-making-the-switch-to-marimo-notebooks/)
for the motivation behind this new notebook format.
Install the [vscode extension](https://marketplace.visualstudio.com/items?itemName=marimo-team.vscode-marimo)
to run it in VSCode.

The updated plots will be embedded automatically next time the paper is rendered.
Providing the `HTML=true` named argument generates standalone HTML versions of the notebooks 
in the `supplementary` directory (shared as supplementary materials).


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
uv run jupyter notebook 01-notebook.py
uv run marimo edit 02-notebook.py
# Run unit tests
uv run pytest
```

## To publish

### PDF to Gdrive

You can publish the manuscript PDF to Gdrive
using a Gdrive client like [gdrive](https://github.com/glotlabs/gdrive).
Adjust the file ID and publication name in the `Taskfile.yml` file.
You first need to upload the PDF in the desired Gdrive folder,
to create a file ID.


```shell
task pub-gdrive
```


### Distribute as a website

It is also possible to publish the materials to GitLab/GitHub pages as a mini website,
called a project landing page.
This can includes the paper PDF and the HTML for the supplementary materials.
Collect the material in the dist/ folder, either via symlink or plain copy.
possibly via symlinks.

Either use GitLab or GitHub actions to publish automatically on every commit. 
See in the optional folder for the action file to be used in this case.

Create a proper website page embedding the PDF and the supplementary materials.
Enrich it with a proper abstract, link to videos, and other highlights.
A Quarto example is provided in [site/index.qmd](site/index.qmd).
It can be build into a proper website ready for distribution with:

```shell
task dist
```

Other (non quarto) templates are available at: 
<https://github.com/eliahuhorwitz/Academic-project-page-template>

Instead of a full website, the project can be shared as single HTML file with just the table of contents
with the [contents file](dist/contents.html). Regenerate it needed with:

```bash
cd dist; tree -H '' -T "My Project" --noreport -o contents.html
```