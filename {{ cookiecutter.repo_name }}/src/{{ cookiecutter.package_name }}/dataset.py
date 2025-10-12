from pathlib import Path
from loguru import logger
from tqdm import tqdm
import pandas as pd
import typer
from {{ cookiecutter.package_name }}.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()

# For configuration data files, better to have them inside the package: src/<package>/data
# In that case use: PACKAGE_DATA_DIR = resources.files(__package__) / "data"

# Data Preparation
def load_data(file=RAW_DATA_DIR/"auto-mpg.csv", n=None):    
    df = pd.read_csv(file)

    if n is not None:
        ic("Sampling ", n)
        df= df.sample(n=n, random_state=42)

    return df

@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Processing dataset...")
    for i in tqdm(range(10), total=10):
        if i == 5:
            logger.info("Something happened for iteration 5.")
    logger.success("Processing dataset complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()


