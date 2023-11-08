from __future__ import annotations

import sys
import argparse
import platform

from loguru import logger

from crasher.widgets.application import QCrasherApplication
from crasher.widgets.window import QCrasherWindow
from crasher.utils.path import get_user_local_directory


def run_application() -> None:
    """  """

    argument_parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="crasher",
        description="Crasher application with launch arguments"
    )

    argument_parser.add_argument("--windowless", action="store_true", help="run in windowless mode", default=False)

    args = argument_parser.parse_args()

    # Setup logger
    logger.add(str(get_user_local_directory()) + r"\logs\log_{time}.log",
               format="{time:HH:mm:ss.SS} ({file}) [{level}] {message}",
               colorize=True)

    logger.info("Application starts")

    # Log debug data about user computer
    logger.debug(f"Platform: {platform.system()} {platform.release()} ({platform.architecture()[0]})")
    if sys.argv[1:]:
        logger.debug(f"Running application with arguments: {sys.argv[1:]}")

    # Setup Qt application
    application: QCrasherApplication = QCrasherApplication(sys.argv, arguments_=args, logger_=logger)

    if not application.run_arguments.windowless:

        # Initialize application window
        window: QCrasherWindow = QCrasherWindow(application=application)

        # Show application window
        window.show()

    else:

        logger.info("Application is running in windowless mode")

    # Execute application
    application.exec()


if __name__ == "__main__":
    run_application()
