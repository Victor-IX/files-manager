from settings import get_enable_inclusion_filter


def query(key):
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
