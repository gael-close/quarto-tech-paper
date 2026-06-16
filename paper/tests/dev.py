#!/usr/bin/env -S uv run python
'''
Development area for Work in Progress (WIP). 
To be moved to modular code once working.

Can be run from VScode
- Double check that Python interpreter (.venv/bin/python) is set for the workspace
- Run as interactive Jupyter script: >Jupyter: Run file in Interactive
- Run as standalone Python file: F5
- Run as cell

Can be run as standalone exec script: tests/dev.py
'''

from my_package.config import *

# Autoreload in Notebook only
try:
    from IPython import get_ipython
    ipython = get_ipython()
    if ipython is not None and 'IPKernelApp' in ipython.config:
        ipython.magic('reload_ext autoreload')
        ipython.magic('autoreload 2')
    logger.info("Autoreload enabled")
except:
    pass

#%% Development area
logger.info("## WIP code##")

from my_package.plots import *
from my_package.data import *
# Optional checks and watermark
my_sineplot();
df = load_data()
