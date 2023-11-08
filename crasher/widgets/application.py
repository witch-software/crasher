from __future__ import annotations

from typing import TypeAlias
from argparse import Namespace
from loguru import logger

from PySide6.QtWidgets import QApplication

__all__ = ["QCrasherApplication"]


class QCrasherApplication(QApplication):
    """ Custom PySide6.QApplication implementation for Crasher """

    APPLICATION_TITLE: str = "Crasher"
    APPLICATION_VERSION: str = "1.0.0b"
    APPLICATION_ORG_NAME: str = "Witch Software"
    APPLICATION_ORG_DOMAIN: str = "witch-software.com"

    def __init__(self, argv: list[str], *, arguments_: Namespace, logger_: TypeAlias[logger]) -> None:
        """
        Initialize the QCrasherApplication.

        :type argv: list[str]
        :type arguments_: argparse.Namespace
        :type logger_: TypeAlias[loguru.logger]

        :param argv: Command-line arguments passed to the application.
        :param arguments_: Parsed command-line arguments for configuration.
        :param logger_: An instance of the logger for logging application events.

        :rtype: None
        """

        # Todo: Add settings config

        super(QCrasherApplication, self).__init__(argv)

        self.run_arguments: Namespace = arguments_
        self.logger: TypeAlias[logger] = logger_

        self.initialize_application()

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

    def on_close_event(self) -> None:
        """
        Event called when closing the application.

        :rtype: None
        """

        # Todo: Add saving settings config

        self.logger.success("Application was successfully closed.")
