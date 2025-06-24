import configparser
from pathlib import Path


class ConfigManager:
    SECTION = "settings"

    def __init__(self):
        self.path = Path.home() / "appdata" / "local" / "Star-Files" / "config.ini"

        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self.path.write_text("")

        self._parser = configparser.ConfigParser()
        self._parser.read(self.path)

        if not self._parser.has_section(self.SECTION):
            self._parser.add_section(self.SECTION)
            self._save()

    def get(self, key: str, default: str | None = None) -> str | None:
        return self._parser.get(self.SECTION, key, fallback=default)

    def set(self, key: str, value: str) -> None:
        self._parser.set(self.SECTION, key, value)
        self._save()

    def _save(self) -> None:
        with self.path.open("w") as f:
            self._parser.write(f)
