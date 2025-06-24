import argparse
import logging
import typer

from rich import print
from pathlib import Path

from settings import get_repo_path, get_enable_inclusion_filter

logger = logging.getLogger(__name__)
cli = typer.Typer(name="StarFiles", help="Query files")
repo_path = get_repo_path()


def query(key: str, all: bool = False):
    files = []
    for file_path in repo_path.rglob(f"*{key}*"):
        if file_path.is_file():
            file_path: Path = file_path.relative_to(repo_path)
            files.append(file_path)
            print(f"[bold green]{file_path}[/bold green]")
    return files
