from config_manager import ConfigManager

cfg = ConfigManager()


def set_enable_inclusion_filter(enable: bool) -> None:
    cfg.set("inclusion", enable)


def get_enable_inclusion_filter() -> bool:
    return cfg.get("inclusion", default=True)
