import sys
import typer
import logging
import logging.handlers

from pathlib import Path

from register import register_app
from main_window import run_gui
from cli import cli_commands
from rich import print

print("Welcome to [bold green]Star-Files[/bold green]")

# Run CLI version if arguments are provided
if len(sys.argv) > 1:
    typer.run(cli_commands)

# This will only run if no arguments are provided
print("Running GUI")

log_colors = {
    "DEBUG": "\033[36m",  # Cyan
    "INFO": "\033[37m",  # White
    "WARNING": "\033[33m",  # Yellow
    "ERROR": "\033[31m",  # Red
    "CRITICAL": "\033[41m",  # Red background
}
reset_color = "\033[0m"  # Reset to default color


class ColoredFormatter(logging.Formatter):
    def format(self, record):
        log_color = log_colors.get(record.levelname, reset_color)
        message = super().format(record)
        return f"{log_color}{message}{reset_color}"


# Setup logging config
_format = "[%(asctime)s:%(levelname)s] %(message)s"
log_path = Path.home() / "AppData" / "Local" / "Star-Files"
log_path.mkdir(parents=True, exist_ok=True)
color_formatter = ColoredFormatter(_format)

try:
    file_handler = logging.handlers.RotatingFileHandler(
        log_path / "Star-Files.log",
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=2,
    )
    file_handler.setFormatter(logging.Formatter(_format))
except PermissionError:
    file_handler = logging.FileHandler(log_path / "Star-Files.log")

stream_handler = logging.StreamHandler(stream=sys.stdout)
stream_handler.setFormatter(color_formatter)

logging.basicConfig(
    format=_format,
    handlers=[file_handler, stream_handler],
    level=logging.DEBUG,
)

logger = logging.getLogger(__name__)
logger.info("Registering Star-Files")
register_app()
logger.info("Starting Star-Files...")


run_gui()
