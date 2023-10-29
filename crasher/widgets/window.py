from __future__ import annotations

from PySide6.QtWidgets import QApplication, QMainWindow
from loguru import Logger


__all__ = ["QCrasherWindow"]


class QCrasherWindow(QMainWindow):
    """ Class of application window for Crasher """

    # Todo: Add menu- & statusbar
    # Todo: Make hello central widget
    # Todo: Set icon and geometry for window at initialize_ui()
    # Todo: Add to statusbar handler of logger messages
    # Todo: Add onClose event handler
    # Todo: Add commentaries at code

    def __init__(self, *, application: QApplication, logger: Logger) -> None:
        super().__init__()

        self.application: QApplication = application
        self.logger: Logger = logger

        self.initialize_ui()
        self.logger.success("Window initialized!")

    def initialize_ui(self) -> None:

        self.logger.info("Initializing UI...")

        self.setWindowTitle(self.application.applicationName())
