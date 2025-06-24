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


# TODO
# Sub paths for faster looking
# Extension blacklist
# Inclusion extension blacklist
# Inclusion paths specific rules
