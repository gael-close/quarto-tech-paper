from pathlib import Path
from loguru import logger
from pyprojroot import here
from tqdm import tqdm
import sys
from pydantic_settings import BaseSettings

# Configure loguru with tqdm.write
logger.remove()
logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)

# Paths
PROJ_ROOT = here()
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")

DATA_DIR = PROJ_ROOT / "data"
SUPP_DIR = PROJ_ROOT / "supplementary"

# Venv
logger.info(f"Python executable: {sys.executable}")

# Settings
class Settings(BaseSettings):
    GOOGLE_FID: str
    SHORT_TITLE: str
    ESP32S3_USB_VID: str
    ESP32S3_USB_PID: str
    BAUD_RATE: int
    
    class Config:
        env_file = PROJ_ROOT / '.env'

settings = Settings()


