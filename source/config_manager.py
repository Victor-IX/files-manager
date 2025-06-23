import configparser

from pathlib import Path


class ConfigManager:
    def __init__(self):
        self.path = Path(Path.home(), "appdata", "local", "Star-Files", "config.ini")
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self.path.write_text("")
        self._parser = configparser.ConfigParser()
        self._parser.read(self.path)

    def get(self, key: str, default: str | None = None) -> str | None:
        if not self._parser.has_key(key):
            return default
        return self._parser.get(key, default)

    def set(self, key: str, value: str) -> None:
        if not self._parser.has_key(key):
            self._parser.add_key(key)
        self._parser.set(key, value)
        self._save()

    def _save(self) -> None:
        with self.path.open("w") as f:
            self._parser.write(f)
