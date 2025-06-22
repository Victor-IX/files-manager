import sys
import ctypes
import winreg
import logging

from pathlib import Path

logger = logging.getLogger(__name__)


def register_app():
    hwnd_broadcast = 0xFFFF
    wm_settingchange = 0x1A
    app_path = Path(sys.executable).parent if hasattr(sys, "frozen") else Path(__file__).parent.resolve() / "main.py"
    print(f"Registering Star-Files at {app_path}")

    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_READ) as key:
        current_path, _ = winreg.QueryValueEx(key, "Path")

    if str(app_path) not in current_path.split(";"):
        new_path = current_path + ";" + str(app_path)
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)

        # Notify other apps (so new cmd/powershell sessions pick it up)
        ctypes.windll.user32.SendMessageW(hwnd_broadcast, wm_settingchange, 0, "Environment")
        logger.info("Star-Files registered in the system PATH.")
    else:
        logger.info("Star-Files is already registered in the system PATH.")
