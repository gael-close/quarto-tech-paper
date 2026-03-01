# Basics
import sys
import os
import numpy as np
import pandas as pd
from box import Box
from pathlib import Path
from contextlib import contextmanager
from subprocess import PIPE, Popen
from pyprojroot import here
from icecream import install
install()
try:
    pd.options.mode.copy_on_write = True
except:
    pass

# Units
import forallpeople as si
import sigfig
si.environment("default", top_level=False)


# Plots
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import hvplot.pandas
import holoviews as hv  # Load w/ hv.extensions('bokeh') in notebook
plt.rcParams.update({'font.size': 9})

# Display
from IPython.display import IFrame, HTML, Image, Markdown, display


# Magic (use plain python syntax)
import builtins
from IPython import get_ipython

if get_ipython() is not None:
    mgc = get_ipython().run_line_magic
    mgc("matplotlib", "inline")
    mgc("config", "InlineBackend.figure_format='retina'")

# Ignore warnings
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)
import logging

logging.getLogger("param").setLevel(logging.ERROR)

# Styles
mpl.rcParams.update(
    {
        "grid.color": "darkgrey",
        # "grid.linestyle": ":",
        "axes.grid": False,  # only enable grid line in a few plots
        "font.family": "sans-serif",
        "mathtext.default": "it",
        "mathtext.fontset": "dejavusans",
        "axes.facecolor": "white",
        "svg.hashsalt": "",  # reproducable SVG
    }
)
sns.set_palette("tab10")
my_table_class = 'class="table table-striped table-bordered table-sm"'


MLX_COLORS= pd.Series({
    'blue':  '#00354C',
    'red'  : '#db4140',
    'green': '#65bba9',
    'orange': '#eea320',
    'grey':   '#b2c4cb',
    'brown3': '#ccb28f',
    'red2': '#cc7a7a',
    'black':  '#3e4242',
    'blue2': '#2d6c7f',
    'blue3': '#599db2',
    'blue4': '#8fc1cc',
    'green2':'#8fccbc',
    'green3':'#59b29d',
    'green4': '#53a5a1',
    'green5': '#597f7c',
    'green6': '#c0cc8f',
    'brown2': '#d8cfc3',
    'red3':'#a35471'})


# Test plot
# from http://seaborn.pydata.org/tutorial/aesthetics.html?highlight=sine%20plot
def my_sineplot():
    fig, ax = plt.subplots(figsize=(6, 4))
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * 0.5) * (7 - i))
    plt.xlabel(r"Angle $\theta$ [rad]")  # raw string to rende latex
    plt.ylabel(r"Voltage $V_\mathrm{ADC}$ [V]")
    plt.title("Test Plot")
    return fig, ax


# Helper functions
def my_savefig(fig, fname, dpi=200, formats=[]):
    """Save figure to file. Arguments:

    Args:
      fig: figure instance
      fname: file name w/ extension
      formats: list of extra formats ['png', 'svg', 'pdf']
      dpi: 200
    """

    fig.savefig(
        fname,
        format=os.path.splitext(fname)[1][1:],
        dpi=dpi,
        bbox_inches="tight",
        metadata={"Date": None},
    )
    for ext in formats:
        fig.savefig(
            fname.replace(".png", ".%s" % ext),
            format=ext,
            dpi=dpi,
            bbox_inches="tight",
            metadata={"Date": None},
        )


def annotate_sl(ax, sl=[], color="gray", orient="h", linestyle=":"):
    """Annotate axes with speciation limit"""
    import itertools

    if type(ax) not in [list, np.ndarray]:
        ax = [ax]
    for a in itertools.chain(*ax):
        for s in sl:
            if orient == "h":
                a.hlines(s, *a.get_xlim(), linestyle=linestyle, color=color)
            else:
                a.vlines(s, *a.get_ylim(), linestyle=linestyle, color=color)


def apply_func_df(func):
    def wrapper(df, dd, **kwargs):
        Y = df.apply(func, dd=dd, **kwargs, axis=1, result_type="expand")
        return df.drop(columns=Y.columns, errors="ignore").join(Y)

    wrapper.__wrapped__ = func
    return wrapper


def display_dd(dd):
    display(
        pd.DataFrame.from_dict(dd, orient="index")
        .stack()
        .rename_axis(["component", "parameter"])
        .to_frame("value")
    )


def nest_columns(df, split="."):
    """Nest columns hierarchically"""
    df.columns = pd.MultiIndex.from_tuples(
        list(map(lambda x: x.split(split), df.columns.values))
    )
    return df


def nest_index(df, split="."):
    """Nest columns hierarchically"""
    df.index = pd.MultiIndex.from_tuples(
        list(map(lambda x: x.split(split), df.index.values))
    )
    return df


def my_stack(
    df,
    level="parameter",
    value="value",
):
    """Stack a dataframe. The column keys are stacked under a new level.
    The values are retained in the column named value."""
    df_2 = df.copy()
    df_2.columns.name = level
    df_2 = df_2.stack(dropna=False).to_frame(value)
    return df_2


def print_git_version():
    from git import Repo

    repo = Repo(".", search_parent_directories=True)
    version = repo.git.describe("--tags", "--always", "--dirty")
    return Markdown(f"Git version\n: `{version}`.")


def sf(x, n=3):
    """
    Return a string representation of x with n significant numbers
    """
    if isinstance(x, si.Physical):
        m, u = str(x).split()
        return sigfig.round(m, n) + " " + u
    else:
        return str(sigfig.round(x, n))


def sf_(x, n=3):
    """
    Same as sf_ but for a numpy array
    """
    return np.frompyfunc(sf, 2, 1)(x, n)



# https://stackoverflow.com/a/75049113
@contextmanager
def set_directory(path):
    _oldCWD = os.getcwd()
    os.chdir(os.path.abspath(path))

    try:
        yield
    finally:
        os.chdir(_oldCWD)

def cmdline(command):
    process = Popen(args=command, stdout=PIPE, shell=True)
    return process.communicate()[0]