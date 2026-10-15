"""Unified notebook processing script for Jupyter and Marimo notebooks."""

import subprocess
import sys
from pathlib import Path
from typing import List

import typer

app = typer.Typer()


def process_jupyter(notebook_path: Path, execute: bool = False, output_dir: str = "dist/supplementary") -> None:
    """Process Jupyter notebook (.ipynb)."""
    typer.echo(f"Processing Jupyter notebook: {notebook_path}")
    
    # Resolve output directory to absolute path
    output_path = Path(output_dir).resolve()
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Render to HTML with Quarto (optionally execute)
    html_cmd = [
        "quarto",
        "render",
        str(notebook_path),
        "--to",
        "html",
        "--output-dir",
        str(output_path),
        "--embed-resources",
        "--toc",
    ]
    
    if execute:
        html_cmd.insert(2, "--execute")
    
    subprocess.run(html_cmd, check=True)
    typer.echo(f"✓ Rendered to {output_path}/{notebook_path.stem}.html")


def process_marimo(notebook_path: Path, execute: bool = True, output_dir: str = "dist/supplementary") -> None:
    """Process Marimo notebook (.py).
    
    Marimo notebooks always execute on export (execute flag is ignored).
    """
    typer.echo(f"Processing Marimo notebook: {notebook_path}")
    
    # Resolve output directory to absolute path
    output_path = (Path(output_dir) / f"{notebook_path.stem}.html").resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Marimo notebooks execute by default on export
    cmd = [
        "marimo",
        "export",
        "html",
        str(notebook_path),
        "-o",
        str(output_path),
    ]
    
    subprocess.run(cmd, check=True)
    typer.echo(f"✓ Exported and executed to {output_path}")


@app.command()
def main(
    notebooks: List[str] = typer.Argument(
        ...,
        help="Notebook file(s) to process (*.ipynb or *.py)",
    ),
    exec: bool = typer.Option(
        False,
        "--exec",
        help="Execute notebook code (for Jupyter only)",
    ),
    output_dir: str = typer.Option(
        "dist/supplementary",
        "-o",
        "--output-dir",
        help="Output directory for HTML files",
    ),
) -> None:
    """Process Jupyter (.ipynb) or Marimo (.py) notebooks.
    
    Examples:
        python scripts/notebook.py notebooks/01-notebook.ipynb
        python scripts/notebook.py notebooks/02-notebook.py
        python scripts/notebook.py notebooks/01-notebook.ipynb notebooks/02-notebook.py --exec
        python scripts/notebook.py notebooks/01-notebook.ipynb -o ./output
    """
    if not notebooks:
        typer.echo("Error: At least one notebook file required", err=True)
        sys.exit(1)
    
    for notebook_name in notebooks:
        notebook_path = Path(notebook_name)
        
        if not notebook_path.exists():
            typer.echo(f"Error: {notebook_path} not found", err=True)
            sys.exit(1)
        
        if notebook_path.suffix == ".ipynb":
            process_jupyter(notebook_path, execute=exec, output_dir=output_dir)
        elif notebook_path.suffix == ".py":
            process_marimo(notebook_path, execute=exec, output_dir=output_dir)
        else:
            typer.echo(
                f"Error: Unsupported file type {notebook_path.suffix}. "
                "Use .ipynb or .py",
                err=True,
            )
            sys.exit(1)
    
    typer.echo("✓ All notebooks processed successfully!")


if __name__ == "__main__":
    app()
