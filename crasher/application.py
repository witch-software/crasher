# Code by @selfkilla666
# https://github.com/witch-software/crasher
# MIT License

from __future__ import annotations

import sys
import argparse
import platform

from loguru import logger

from crasher.widgets.application import QCrasherApplication
from crasher.utils.path import get_user_local_directory


def get_run_arguments() -> argparse.Namespace:
    """ Get application startup arguments """

    argument_parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="crasher",
        description="Crasher application with launch arguments"
    )

    argument_parser.add_argument("--windowless", action="store_true", help="run in windowless mode", default=False)
    argument_parser.add_argument("--debug", action="store_true", help="run application in debug mode", default=False)

    return argument_parser.parse_args()


def run_application() -> None:

    args = get_run_arguments()

    # Setup logger
    logger.add(
        str(get_user_local_directory()) + r"\logs\log_{time}.log",
        format="{time:HH:mm:ss.SS} ({file}) [{level}] {message}",
        colorize=True
    )

    logger.info("Application starts")

    # Log debug data about user computer
    logger.debug(f"Platform: {platform.system()} {platform.release()} ({platform.architecture()[0]})")
    if sys.argv[1:]:
        logger.debug(f"Running application with arguments: {sys.argv[1:]}")

    # Setup application
    application: QCrasherApplication = QCrasherApplication(sys.argv, arguments_=args, logger_=logger)

    # Execute application
    application.exec()


if __name__ == "__main__":
    run_application()
