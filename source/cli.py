import argparse
import logging
from pathlib import Path

from query import query

logger = logging.getLogger(__name__)


def cli_commands():
    parser = argparse.ArgumentParser(prog="StarFiles", description="Query files")
    parser.add_argument("key", nargs="?", default=None, help="Key to query files")
    parser.add_argument("-a", "-all", "--all", action="store_true", help="Show all files disabling inclusion filters")
    parser.add_argument("-config", "--config", action="store_true", help="Get the config path")
    parser.add_argument("-d", "-debug", "--debug", action="store_true", help="Enable debug logging")

    args = parser.parse_args()

    validate(args)
    config(args)

    if args.key:
        query(args.key)

    return args


def validate(args):
    if args.config and args.key:
        raise ValueError("-config|--config cannot be used with a key, please use only one of them")

    if not args.key and args.all:
        raise ValueError("-a|-all|--all cannot be used without a key, please provide a key to query files")


def config(args):
    if args.config:
        config_path = Path.home() / "AppData" / "Local" / "Star-Files" / "config.ini"
        print(f"Config path: {config_path}")
        return config_path
