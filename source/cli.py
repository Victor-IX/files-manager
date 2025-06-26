import typer

from rich import print
from pathlib import Path
from typing import Optional, List

from query import query
from settings import (
    set_enable_inclusion_filter,
    set_extension_blacklist,
    set_inclusion_extension_blacklist,
    set_repo_path,
    set_sub_paths,
    get_repo_path,
)

cli = typer.Typer(name="StarFiles", help="Query files")


def cli_commands(
    key: Optional[str] = typer.Argument(None, help="Key to query files"),
    all: bool = typer.Option(False, "-a", "-all", "--all", help="Show all files disabling inclusion filters"),
    config: bool = typer.Option(False, "-c", "-config", "--config", help="Print the path to the config file and exit."),
    init: bool = typer.Option(False, "-i", "-init", "--init", help="Initialize the config file if it does not exist."),
):
    if config:
        config_path = Path.home() / "AppData" / "Local" / "Star-Files" / "config.ini"
        typer.echo(f"Config path: {config_path}")
        raise typer.Exit()
    if init:
        init_config()

    if key is not None:
        query(key, all)
        raise typer.Exit()


def init_config():
    print("[bold green]Initializing config...[/bold green]")
    print("[bold green]You can change the config later by editing the config file.[/bold green]\n")
    cli_set_extension_blacklist()
    cli_set_inclusion_extension_blacklist()

    # set_repo_path()
    # set_sub_paths()


def cli_set_repo_path():
    while True:
        repo_path = typer.prompt(
            "Enter the repository path",
            default=str(Path.home() / "Documents" / "Star-Files"),
            show_default=True,
        )
        repo_path = Path(repo_path).expanduser().resolve()
        if repo_path.is_dir():
            set_repo_path(repo_path)
            print(f"[bold green]Repository path set to: {repo_path}[/bold green]")
            break
        else:
            print("[bold red]Invalid path. Please enter a valid directory path.[/bold red]")


def cli_set_sub_paths():
    while True:
        sub_paths = typer.prompt(
            "Enter the sub-paths (comma separated, e.g. src,docs)",
            default="src,docs",
            show_default=True,
        )
        sub_paths_list = [path.strip() for path in sub_paths.split(",") if path.strip()]
        if all((get_repo_path() / Path(path)).is_dir() for path in sub_paths_list):
            set_sub_paths(sub_paths_list)
            print(f"[bold green]Sub-paths set to: {', '.join(sub_paths_list)}[/bold green]")
            break
        else:
            print("[bold red]Invalid paths. Please enter valid directory paths.[/bold red]")


def cli_set_extension_blacklist():
    while True:
        extensions = typer.prompt(
            "Enter the extensions to blacklist (comma separated, e.g. .txt,.md)",
            default="",
            show_default=False,
        )
        extensions_list = [ext.strip() for ext in extensions.split(",") if ext.strip()]
        valid, extensions_list = validate_extension(extensions_list)
        if valid:
            break
        else:
            print("[bold red]Invalid extensions. Please try again.[/bold red]")

    set_extension_blacklist(extensions_list)


def cli_set_inclusion_extension_blacklist():
    while True:
        extensions = typer.prompt(
            "Enter the extensions to include (comma separated, e.g. .txt,.md)",
            default="",
            show_default=False,
        )
        extensions_list = [ext.strip() for ext in extensions.split(",") if ext.strip()]
        valid, extensions_list = validate_extension(extensions_list)
        if valid:
            break
        else:
            print("[bold red]Invalid extensions. Please try again.[/bold red]")

    set_inclusion_extension_blacklist(extensions_list)


def validate_extension(extensions: list[str]) -> bool:
    cleaned: List[str] = []
    for ext in extensions:
        # Auto-add leading dot
        if not ext.startswith("."):
            typer.echo(
                f"Warning: '{ext}' → '.{ext}'. Extensions should start with a dot.",
                err=True,
            )
            ext = "." + ext

        # Remove accidental double-dot
        if ext.startswith(".."):
            new_ext = "." + ext.lstrip(".")
            typer.echo(
                f"Warning: '{ext}' → '{new_ext}'. Removed extra dot.",
                err=True,
            )
            ext = new_ext

        # Space check
        if " " in ext:
            typer.echo(f"Error: '{ext}'. Extensions must not contain spaces.", err=True)
            return False, []

        # Dot in the middle check
        if len(ext) < 2 or ext.count(".") != 1:
            typer.echo(
                f"Error: '{ext}'. Bad format; should be like '.txt' or '.md'.",
                err=True,
            )
            return False, []

        cleaned.append(ext)

    return True, cleaned
