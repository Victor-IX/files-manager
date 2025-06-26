import ast
from settings_manager import ConfigManager
from pathlib import Path


cfg = ConfigManager()


def set_enable_inclusion_filter(enable: bool) -> None:
    cfg.set("inclusion", enable)


def get_enable_inclusion_filter() -> bool:
    return cfg.get("inclusion", default=True)


def set_repo_path(path: Path) -> None:
    cfg.set("repo_path", str(path))


def get_repo_path() -> Path:
    return Path(cfg.get("repo_path", default="./"))


def set_sub_paths(sub_paths: list[str]) -> None:
    cfg.set("sub_paths", ",".join(sub_paths))


def get_sub_paths() -> list[str]:
    sub_paths = cfg.get("sub_paths", default="")
    return sub_paths.split(",") if sub_paths else []


def set_extension_blacklist(extensions: list[str]) -> None:
    ext = get_extension_blacklist()
    ext.extend(extensions)
    cfg.set("extension_blacklist", list(set(ext)))


def get_extension_blacklist() -> list[str]:
    extensions = cfg.get("extension_blacklist", default="[]")
    extensions = ast.literal_eval(extensions)
    return extensions


def set_inclusion_extension_blacklist(extensions: list[str]) -> None:
    cfg.set("inclusion_extension_blacklist", ",".join(extensions))


def get_inclusion_extension_blacklist() -> list[str]:
    extensions = cfg.get("inclusion_extension_blacklist", default="")
    return extensions.split(",") if extensions else []


# TODO
# Sub paths for faster looking
# Extension blacklist
# Inclusion extension blacklist
# Inclusion paths specific rules
