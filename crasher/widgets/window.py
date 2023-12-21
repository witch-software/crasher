# Code by @selfkilla666
# https://github.com/witch-software/crasher
# MIT License

from __future__ import annotations

from PySide6.QtWidgets import QMainWindow, QApplication, QStatusBar, QMenuBar, QMenu
from PySide6.QtGui import QAction

from crasher.utils.log_handler import StatusBarLogHandler

import loguru


__all__ = ["QCrasherWindow"]


class QCrasherWindow(QMainWindow):
    """ Class of application window for Crasher. """

    # Todo: Make hello central widget
    # Todo: Set geometry for window at initialize_ui()
    # Todo: Add commentaries at code
    # Todo: Add actions to menubar

    menu_bar: QMenuBar
    status_bar: QStatusBar

    def __init__(self, *, application: QApplication) -> None:

        super().__init__()

        self.application: QApplication = application
        self.logger: loguru.Logger = self.application.logger    # type: ignore[attr-defined]
        self.initialize_ui()                                    # TODO: Fix this typehint sometime in future ¯\_(ツ)_/¯

    def initialize_ui(self) -> None:

        self.logger.info("Initializing UI...")

        # Set window info
        self.setWindowTitle(self.application.applicationName())
        self.setWindowIcon(self.application.windowIcon())

        # Initialize status bar
        self.status_bar = QStatusBar(parent=self)
        self.status_bar_log_handler = StatusBarLogHandler(self.status_bar)
        self.logger.add(self.status_bar_log_handler, format="{message}")
        self.setStatusBar(self.status_bar)

        # Initialize menu bar
        self.menu_bar = QMenuBar(parent=self)

        file_menu: QMenu = self.menu_bar.addMenu("File")

        new_project_action: QAction = QAction(text="New project", parent=self)
        open_project_action: QAction = QAction(text="Open project", parent=self)
        open_image_action: QAction = QAction(text="Open image", parent=self)
        open_settings_action: QAction = QAction(text="Settings", parent=self)
        exit_window_action: QAction = QAction(text="Exit", parent=self)

        file_menu.addAction(new_project_action)
        file_menu.addAction(open_project_action)
        file_menu.addAction(open_image_action)
        file_menu.addSeparator()
        file_menu.addAction(open_settings_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_window_action)

        self.setMenuBar(self.menu_bar)
