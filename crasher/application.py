from __future__ import annotations

import sys
from PySide6.QtWidgets import QApplication

from loguru import logger

from crasher.widgets.window import QCrasherWindow
from crasher.utils.path import get_user_local_directory

APPLICATION_TITLE: str = "Crasher"
APPLICATION_VERSION: str = "1.0.0b"
APPLICATION_ORG_NAME: str = "Witch Software"
APPLICATION_ORG_DOMAIN: str = "witch-software.com"


def run_application() -> None:

    # Setup logger
    logger.add(str(get_user_local_directory()) + "logs/log_{time}.log",
               format="{time:HH:mm:ss.SS} | {file} | {level} | {message}",
               colorize=True)

    logger.info("Application starts")

    # Setup Qt application
    application: QApplication = QApplication(sys.argv)

    # Set application metadata
    application.setApplicationName(APPLICATION_TITLE)
    application.setApplicationVersion(APPLICATION_VERSION)
    application.setOrganizationName(APPLICATION_ORG_NAME)
    application.setOrganizationDomain(APPLICATION_ORG_DOMAIN)

    logger.info("Initialize application window...")

    # Initialize application window
    window: QCrasherWindow = QCrasherWindow(
        application=application,
        logger=logger
    )

    # Start application
    window.show()
    application.exec()

    logger.success("Application was successfully closed.")


if __name__ == "__main__":
    run_application()
