from pathlib import Path
from loguru import logger
from tqdm import tqdm
import typer
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from .myinit import my_sineplot
from {{ cookiecutter.package_name }}.config import FIGURES_DIR, PROCESSED_DATA_DIR

app = typer.Typer()

@app.command()
def plot_joint(df):
    df2=df.copy()
    df2["weight"]=df2["weight"]/1000 # convert to tons
    ax=sns.jointplot(df, x="weight", y="horsepower", height=4) #kind="reg", kwargs={'markersize':5})
    ax.set_axis_labels("Weight [t]", "Horsepower [hp]")

    # Needed to explicitly show the plot when called from CLI
    plt.show()
    return ax


@app.command()
def plot_sine(frequency: float = 1.0):
    """Plot a sine wave with the given frequency."""
    x = np.linspace(0, 10, 100)
    y = np.sin(2 * np.pi * frequency * x)

    plt.figure(figsize=(10, 4))
    plt.plot(x, y)
    plt.title(f"Sine Wave with Frequency {frequency} Hz")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    app()
