# Support script for notebooks


# %% Test fixtures: live reload, environment, arguments
# Generic init code
from {{cookiecutter.package}}.myinit import *
from {{cookiecutter.package}}.dataset import *

# Load the data and everything else when run as a script
# Invoke from notebook with 
# n=10; 
# %run -i support.py
df=load_data(n=n)
plot_joint(df)