
from argparse import Namespace

from pathlib import Path

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from crasher.core.widgets.window import QCrasherWindow
from crasher.core.classes.settings import QCrasherApplicationSettings
from crasher.core.utils.path import get_user_local_directory

import loguru
import platform


__all__ = ["QCrasherApplication"]


class QCrasherApplication(QApplication):
    """ Custom PySide6.QApplication implementation for Crasher """
    class Metadata:
        APPLICATION_NAME: str = "Crasher"
        APPLICATION_VERSION: str = "1.0.0b"
        APPLICATION_ORG_NAME: str = "Witch Software"
        APPLICATION_ORG_DOMAIN: str = "witch-software.com"

    run_arguments: Namespace
    logger: loguru.Logger
    settings: QCrasherApplicationSettings
    window: QCrasherWindow

    debug: bool = True

    def __init__(self, argv: list[str], *, arguments_: Namespace) -> None:
        """
        Initialize the QCrasherApplication.

        :param argv: Command-line arguments passed to the application.
        :param arguments_: Parsed command-line arguments for configuration.
        """

        self.initialize_logger()
        self.logger.info("Application starts")

        super(QCrasherApplication, self).__init__(argv)

        self.run_arguments = arguments_
        self.debug = self.run_arguments.debug or True

        self.log_debug_info(argv)

        self.logger.info("Start application initialization...")

        # Initialize application parts
        self.initialize_application_information()
        self.initialize_settings()
        self.initialize_window()

        self.logger.success("Application is fully initialized!")

    def initialize_logger(self) -> None:
        """ Method to initialize application logger """

        self.logger: loguru.Logger = loguru.logger

        # Setup logger
        self.logger.add(
            str(get_user_local_directory()) + r"\logs\log_{time}.log",
            format="{time:HH:mm:ss.SS} ({file}) [{level}] {message} {exception}",
            colorize=True, catch=True, backtrace=True
        )

    def initialize_application_information(self) -> None:
        """ Method to initialize application information """

        # Connect application events
        self.aboutToQuit.connect(self.on_close_event)

        # Set application metadata
        self.setApplicationName(self.Metadata.APPLICATION_NAME)
        self.setApplicationVersion(self.Metadata.APPLICATION_VERSION)
        self.setOrganizationName(self.Metadata.APPLICATION_ORG_NAME)
        self.setOrganizationDomain(self.Metadata.APPLICATION_ORG_DOMAIN)

        # Set application icon
        icon = QIcon(str(Path("./crasher/static/application_icon.png")))
        self.setWindowIcon(icon)

    def initialize_settings(self) -> None:
        """ Method to initialize application settings """

        self.logger.info("Initialize application settings...")

        self.settings: QCrasherApplicationSettings = QCrasherApplicationSettings(
            Path(f"{get_user_local_directory()}\\settings.toml"),
            logger=self.logger
        )
        self.settings.load_settings()

    def initialize_window(self) -> None:
        """ Method to initialize application window """

        self.logger.info("Initialize application window...")

        if not self.run_arguments.windowless:

            self.window: QCrasherWindow = QCrasherWindow(application=self)
            self.window.show()

            self.logger.success("Window initialized!")

        else:
            self.logger.info("Application is running in windowless mode")

    def log_debug_info(self, argv: list[str]):
        """ Logging some values that might help for debugging """

        if self.debug:
            self.logger.debug("Application running in debug mode.")

        self.logger.debug(f"Application version: {self.Metadata.APPLICATION_VERSION}")

        # Debug data about user system
        self.logger.debug(f"Platform: {platform.system()} {platform.release()} ({platform.architecture()[0]})")

        if len(argv) > 1:
            self.logger.debug(f"Running application with arguments: {' '.join(argv[1:])}")

    def on_close_event(self) -> None:
        """ Event called when closing the application """

        self.logger.info("Saving application settings...")

        self.settings.save_settings()

        self.logger.success("Application was successfully closed!")
