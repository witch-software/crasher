
from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtCore import Slot as qtSlot
from PySide6.QtWidgets import QMainWindow

from crasher.core.widgets.statusbar import QCrasherStatusBar
from crasher.core.widgets.menubar import QCrasherMenuBar
from crasher.core.widgets.workspace.workspace import QCrasherWorkspace

import loguru

if TYPE_CHECKING:
    from crasher.core.widgets.application import QCrasherApplication


class QCrasherWindow(QMainWindow):
    """ Class of application window for Crasher. """

    # TODO: Set geometry for window at initialize_ui()

    logger: loguru.Logger

    application: QCrasherApplication

    status_bar: QCrasherStatusBar
    menu_bar: QCrasherMenuBar
    workspace: QCrasherWorkspace

    def __init__(self, *, application: QCrasherApplication) -> None:

        super().__init__()

        self.application: QCrasherApplication = application

        self.logger: loguru.Logger = self.application.logger

        self.initialize_ui()

    def initialize_ui(self) -> None:

        self.logger.info("Initializing UI...")

        # Set window info
        self.setWindowTitle(self.application.applicationName())
        self.setWindowIcon(self.application.windowIcon())

        self.logger.success("Window info successfully initialized!")

        # Initialize statusbar
        self.status_bar = QCrasherStatusBar(self, logger=self.logger)
        self.setStatusBar(self.status_bar)

        self.logger.success("Application statusbar successfully initialized!")

        # Initialize menubar
        self.menu_bar = QCrasherMenuBar(self, connect_signals=True)
        self.setMenuBar(self.menu_bar)

        self.logger.success("Application menubar successfully initialized!")

        # Initialize workspace
        self.logger.info("Start initialize application workspace...")
        self.workspace = QCrasherWorkspace(self, application=self.application)
        self.setCentralWidget(self.workspace)

        self.logger.success("Application workspace successfully initialized!")

        self.translate_ui()

    def translate_ui(self) -> None:
        pass

    @qtSlot()
    def exit(self):
        self.close()