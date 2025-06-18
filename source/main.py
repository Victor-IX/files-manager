from pathlib import Path

from config import REPO_PATH, FILE_KEY


def find_files_by_name(directory, target_filename):
    base_path = Path(directory)
    matching_files = []

    for file_path in base_path.rglob(f"*{target_filename}*"):
        if file_path.is_file():
            matching_files.append(file_path)

    return matching_files


if __name__ == "__main__":
    results = find_files_by_name(REPO_PATH, FILE_KEY)

    print(f"Found {len(results)} matching files:")
    for path in results:
        print(f"  {path}")
