from pathlib import Path
from invoke import task, Context

@task
def render(c, to='memo2', preview=False):
    print(f"Rendering the paper")
    c.run(f"cd manuscript; quarto-tech-memo manuscript.md --to {to} {'--preview' if preview else ''}")    
    
@task
def notebook(c, notebook, html=False):
    print(f"Execute the supplementary notebook {notebook}")
    c.run(f"uv run jupyter nbconvert --to notebook --inplace --execute notebooks/{notebook}")

    if html:
        src=Path("notebooks")/notebook
        Path("reports").mkdir(parents=True, exist_ok=True)
        dst=Path("reports")/(src.stem+".html")
        c.run(f"quarto render {src} --self-contained --toc; mv {src.with_suffix('.html')} {dst}")