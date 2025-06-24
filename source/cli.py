import typer

from rich import print
from pathlib import Path
from typing import Optional

from query import query

cli = typer.Typer(name="StarFiles", help="Query files")


def cli_commands(
    key: Optional[str] = typer.Argument(None, help="Key to query files"),
    all: bool = typer.Option(False, "-a", "-all", "--all", help="Show all files disabling inclusion filters"),
    config: bool = typer.Option(False, "-c", "-config", "--config", help="Print the path to the config file and exit."),
):
    if config:
        config_path = Path.home() / "AppData" / "Local" / "Star-Files" / "config.ini"
        typer.echo(f"Config path: {config_path}")
        raise typer.Exit()

    if key is not None:
        query(key, all)
        raise typer.Exit()
