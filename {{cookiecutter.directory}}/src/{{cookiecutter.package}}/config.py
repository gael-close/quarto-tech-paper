from pathlib import Path
from loguru import logger
from pyprojroot import here
from tqdm import tqdm
import sys
import yaml
import socket
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

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
    ESP32S3_USB_VID: int
    ESP32S3_USB_PID: int
    BAUD_RATE: int
    
    class Config:
        env_file = '.env'

# Load settings from YAML file
settings_path = PROJ_ROOT / 'settings.yml'
with open(settings_path) as f:
    settings_dict = yaml.safe_load(f)

settings = Settings.model_validate(settings_dict)
