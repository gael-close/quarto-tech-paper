from pathlib import Path
import os
from invoke import task
import shutil

@task
def test(c, gh=False, format='memo2'):
    shutil.rmtree(Path("~/Downloads/new-repo").expanduser(), ignore_errors=True)
    
    c.run(f'''
        rm -fr new-dir/*  
        cookiecutter -f {'gh:gael-close' if gh else '$B4'}/quarto-tech-paper --no-input
        cd new-dir

        # Render the notebook(s) and the paper
        inv notebook 01-notebook.ipynb --html
        inv render

        open manuscript/manuscript.pdf &
        open reports/01-notebook.html &
        ''')
    
@task
def save(c):
    c.run('''
          cd ~/Downloads/new-repo/reports;
          cp *.pdf $B4/quarto-tech-paper/example
          convert -density 150 *.pdf -quality 90 -background white -alpha remove thumbnail.png; cp thumbnail*.png $B4/quarto-tech-paper/example
          cd ../
          sd new_repo {{cookiecutter.package}} notebooks/01-notebook.ipynb; cp notebooks/01-notebook.ipynb $B4/quarto-tech-paper/"{{cookiecutter.repo_name}}/notebooks"          
          ''')
    

