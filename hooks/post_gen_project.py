import shutil
import os
from copy import copy
from pathlib import Path
from subprocess import run
import shutil

# The tech memo manuscript is available here.
# we just need to install the CLI tool
run("cd reports; uv tool install git+https://github.com/gael-close/quarto-tech-memo", shell=True)



