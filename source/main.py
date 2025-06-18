from pathlib import Path
from typing import List

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


if __name__ == "__main__":
    for path in PATHS_FILTER:
        directory = REPO_PATH / path
        find_files_by_name(directory)
        write_files_to_file()

    print(f"Found {len(FILES)} matching files:")
    for file in FILES:
        print(f"{file}")
