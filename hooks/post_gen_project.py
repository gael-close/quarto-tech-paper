import shutil
import os
from copy import copy
from pathlib import Path
from subprocess import run
import shutil

# Inject a quarto-tech-memo template
run("""cookiecutter -f gh:gael-close/quarto-tech-memo --no-input \
    directory='manuscript' filename='manuscript' """, shell=True)



