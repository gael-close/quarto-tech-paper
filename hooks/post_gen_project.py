import shutil
import os
from copy import copy
from pathlib import Path
from subprocess import run
import shutil

# Install quarto-tech-memo as a standalone tool
run("cd reports; uv tool install quarto-tech-memo", shell=True)



