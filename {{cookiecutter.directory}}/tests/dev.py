# ===================================
# WIP
# ===================================
# Check env
import sys
print(f'Python executable: {sys.executable}')
# Autoreload
%reload_ext autoreload
%autoreload 2
# Generic init code
from {{cookiecutter.package}}.myinit import *
# Optional checks and watermark
my_sineplot();

from {{cookiecutter.package}}.dataset import *

# %%
df = load_data()

