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
#%% Generic init code
from {{cookiecutter.package}}.config import *
from {{cookiecutter.package}}.myinit import *


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
my_sineplot()
from {{cookiecutter.package}}.dataset import *
df = load_data()
