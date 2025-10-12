from pathlib import Path
import os
from invoke import task
import shutil

@task
def test(c, gh=False, format='memo2'):
    shutil.rmtree(Path("~/Downloads/new-repo").expanduser(), ignore_errors=True)
    
    c.run(f'''
        cd ~/Downloads;
        cookiecutter -f {'gh:gael-close' if gh else '$B4'}/quarto-tech-paper --no-input;
        cd new-repo

        inv render
        inv notebook 01-notebook.ipynb --html
        
        open reports/paper.pdf
        open notebooks/_build/01-notebook.html
        ''')
    
