from pathlib import Path
from loguru import logger
from pyprojroot import here
import sys
from pydantic_settings import BaseSettings, SettingsConfigDict

# Paths
PROJ_ROOT = here()
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")

DATA_DIR = PROJ_ROOT / "data"
SUPP_DIR = PROJ_ROOT / "dist" / "supplementary"

# Venv
logger.info(f"Python executable: {sys.executable}")

# Settings
class Settings(BaseSettings):
    GOOGLE_FID: str | None = None
    SHORT_TITLE: str = "paper"

    # Modern Pydantic V2 Configuration
    model_config = SettingsConfigDict(
        env_file=PROJ_ROOT / '.env',
        extra="ignore"  # <-- Silently discards any other keys found in your .env
    )
settings = Settings()


