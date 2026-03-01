from pathlib import Path
from dotenv import load_dotenv
from loguru import logger
from pyprojroot import here


# Load environment variables from .env file if it exists
load_dotenv()

# Paths
PROJ_ROOT = here()
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")

DATA_DIR = PROJ_ROOT / "data"
REPORTS_DIR = PROJ_ROOT / "reports"

# If tqdm is installed, configure loguru with tqdm.write
# https://github.com/Delgan/loguru/issues/135
try:
    from tqdm import tqdm

    logger.remove(0)
    logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)
except ModuleNotFoundError:
    pass
