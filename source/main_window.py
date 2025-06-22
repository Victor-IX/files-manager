import sys
import logging

from PySide6.QtWidgets import QApplication, QMainWindow

logger = logging.getLogger(__name__)


def run_gui():
    logger.info("Running GUI mode...")

    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("Star-Files")
    window.resize(640, 480)

    window.show()

    sys.exit(app.exec())
