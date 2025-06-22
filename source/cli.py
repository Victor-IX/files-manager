import argparse
import logging
from pathlib import Path
from venv import logger

logger = logging.getLogger(__name__)


def run_cli(args):
    if args.test:
        print("Test")
    else:
        print("No test argument provided")
    logger.info("Running CLI mode...")


def cli_commands():
    parser = argparse.ArgumentParser(prog="StarFiles", description="Query files")
    parser.add_argument("-d", "-debug", "--debug", action="store_true", help="Enable debug logging")
    parser.add_argument("-t", "-test", "--test", action="store_true", help="Show this help message and exit")

    return parser.parse_args()

    # if args.register:
