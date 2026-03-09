from pathlib import Path
from invoke import task, Context

@task
def render(c, to='memo2', preview=False):
    print(f"Rendering the paper")
    c.run(f"cd manuscript; quarto-tech-memo manuscript.md --to {to} {'--preview' if preview else ''}")    
    
@task
def notebook(c, notebook, html=False):
    if html:
        print(f"Converting the supplementary notebook {notebook} to HTML")
    else:
        print(f"Executing the supplementary notebook {notebook}")

    if notebook.endswith(".ipynb"):
        c.run(f"uv run jupyter nbconvert --to notebook --inplace --execute notebooks/{notebook}")
    elif notebook.endswith(".py") and not html:
        # Skip if exportin to HTML, as it will be executed during the export
        c.run(f"uv run python notebooks/{notebook}")

    if html:
        src=Path("notebooks")/notebook
        Path("reports").mkdir(parents=True, exist_ok=True)
        dst=Path("reports")/(src.stem+".html")

        if notebook.endswith(".ipynb"):
            c.run(f"quarto render {src} --self-contained --toc; mv {src.with_suffix('.html')} {dst}")
        elif notebook.endswith(".py"):
            c.run(f"uv run marimo export html {src} -o {dst}")
            