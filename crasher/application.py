# Code by @selfkilla666
# https://github.com/witch-software/crasher
# MIT License

from __future__ import annotations

from crasher.widgets.application import QCrasherApplication

import sys
import argparse


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

    # Setup application
    application: QCrasherApplication = QCrasherApplication(sys.argv, arguments_=args)

    # Set the global exception handler
    sys.excepthook = application.handle_exception

    # Execute application
    application.exec()


if __name__ == "__main__":
    run_application()
