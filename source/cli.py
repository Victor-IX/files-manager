import argparse
from pathlib import Path

import winreg


APP_NAME = "StarFiles"


def cli_commands():
    parser = argparse.ArgumentParser(prog=APP_NAME, description="Query files")
    parser.add_argument("--register", action="store_true", help="Register StarFiles in the system PATH")
    parser.add_argument("-d", "-debug", "--debug", action="store_true", help="Enable debug logging")

    return parser.parse_args()

    # if args.register:
