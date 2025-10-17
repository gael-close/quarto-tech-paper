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
from {{cookiecutter.package_name}}.myinit import *
# Optional checks and watermark
my_sineplot();

from {{cookiecutter.package_name}}.dataset import *

# %%
df = load_data()

