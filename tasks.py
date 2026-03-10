from pathlib import Path
import os
from invoke import task
import shutil

@task
def test(c, gh=False, format='memo2'):
    shutil.rmtree(Path("~/Downloads/new-repo").expanduser(), ignore_errors=True)
    
    c.run(f'''
        rm -fr new-dir/*  
        uvx cookiecutter -f {'gh:gael-close' if gh else '$B4'}/quarto-tech-paper --no-input
        cd new-dir

        # Render the notebooks and the paper
        inv notebook 01-notebook.ipynb --html
        inv notebook 02-notebook.py --html
        
        # And the paper
        inv render

        open manuscript/manuscript.pdf &
        open reports/01-notebook.html &
        open reports/02-notebook.html
            
        ''')
    
@task
def save(c):
    c.run('''
          cp new-dir/manuscript/*.pdf examples/
          cp new-dir/reports/*.html examples/
          (cd examples; convert -density 150 *.pdf -quality 90 -background white -alpha remove thumbnail.png)
          (cd examples; tree -H '.' -I rest > index.html)
          ''')
    

