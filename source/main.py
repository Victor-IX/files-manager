from pathlib import Path
from typing import List

try:
    from n_config import (
        REPO_PATH,
        FILE_KEY,
        PATHS_FILTER,
        INCLUSION_PATHS_BLACKLIST,
        INCLUSION_FILTER,
        IS_INCLUSION,
        OUTPUT_PATH,
        EXTENSION_BLACKLIST,
    )
except ImportError:
    from config import (
        REPO_PATH,
        FILE_KEY,
        PATHS_FILTER,
        INCLUSION_PATHS_BLACKLIST,
        INCLUSION_FILTER,
        IS_INCLUSION,
        OUTPUT_PATH,
        EXTENSION_BLACKLIST,
    )


FILES: List[Path] = []


def find_files_by_name(directory):
    for file_path in directory.rglob(f"*{FILE_KEY}*"):
        if file_path.is_file():
            if IS_INCLUSION:
                if any(flag in str(file_path) for flag in INCLUSION_PATHS_BLACKLIST):
                    continue
                for path, extensions in INCLUSION_FILTER.items():
                    if str(file_path) in (str(path)) and file_path.suffix in extensions:
                        continue
            if file_path.suffix in EXTENSION_BLACKLIST:
                continue
            file_path: Path = file_path.relative_to(REPO_PATH)
            FILES.append(file_path)

    return FILES


def write_files_to_file():
    try:
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(OUTPUT_PATH, "w") as f:
            for file in FILES:
                f.write(f"{file}\n")
    except Exception as e:
        print(f"Error writing to file {OUTPUT_PATH}: {e}")


def config_check():
    if not FILE_KEY:
        print("Please set the FILE_KEY in the configuration file.")
        exit(1)
    if REPO_PATH == Path(""):
        print("Please set the REPO_PATH in the configuration file.")
        exit(1)
    if not REPO_PATH.exists():
        print(f"Repository path {REPO_PATH} does not exist.")
        exit(1)
    if IS_INCLUSION:
        print("Inclusion filter is enabled")


if __name__ == "__main__":
    for path in PATHS_FILTER:
        directory = REPO_PATH / path

        if not directory.exists():
            print(f"Path {directory} does not exist, skipping...")
            continue

        find_files_by_name(directory)
        write_files_to_file()

    print(f"Found {len(FILES)} matching files")
