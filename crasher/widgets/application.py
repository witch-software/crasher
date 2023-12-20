# Code by @selfkilla666
# https://github.com/witch-software/crasher
# MIT License

from __future__ import annotations

from argparse import Namespace
from loguru._logger import Logger

from pathlib import Path

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon

from crasher.widgets.window import QCrasherWindow


__all__ = ["QCrasherApplication"]


class QCrasherApplication(QApplication):
    """ Custom PySide6.QApplication implementation for Crasher """

    APPLICATION_TITLE: str = "Crasher"
    APPLICATION_VERSION: str = "1.0.0b"
    APPLICATION_ORG_NAME: str = "Witch Software"
    APPLICATION_ORG_DOMAIN: str = "witch-software.com"

    run_arguments: Namespace
    logger: Logger
    window: QMainWindow

    def __init__(self, argv: list[str], *, arguments_: Namespace, logger_: Logger) -> None:
        """
        Initialize the QCrasherApplication.

        :type argv: list[str]
        :type arguments_: argparse.Namespace
        :type logger_: loguru.Logger

        :param argv: Command-line arguments passed to the application.
        :param arguments_: Parsed command-line arguments for configuration.
        :param logger_: An instance of the logger for logging application events.

        :rtype: None
        """

        # Todo: Add settings config

        super(QCrasherApplication, self).__init__(argv)

        self.run_arguments = arguments_
        self.logger = logger_

        self.initialize_application()
        self.initialize_window()

    def initialize_application(self) -> None:
        """
        Method to initialize the application.

        :rtype: None
        """

        # Connect application events
        self.aboutToQuit.connect(self.on_close_event)

        # Set application metadata
        self.setApplicationName(self.APPLICATION_TITLE)
        self.setApplicationVersion(self.APPLICATION_VERSION)
        self.setOrganizationName(self.APPLICATION_ORG_NAME)
        self.setOrganizationDomain(self.APPLICATION_ORG_DOMAIN)

        # Set application icon
        icon = QIcon(str(Path("./static/gui/icons/icon.png")))
        self.setWindowIcon(icon)

    def initialize_window(self) -> None:

        if not self.run_arguments.windowless:
            self.window: QCrasherWindow = QCrasherWindow(application=self)
            self.window.show()
        else:
            self.logger.info("Application is running in windowless mode")

    def set_window(self, window: QMainWindow) -> None:
        self.window = window

    def on_close_event(self) -> None:
        """
        Event called when closing the application.

        :rtype: None
        """

        # Todo: Add saving settings config

        self.logger.success("Application was successfully closed.")
