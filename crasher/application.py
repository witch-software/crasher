
import sys
import argparse

from crasher.core.widgets.application import QCrasherApplication


DEFAULT_WINDOWLESS: bool = False
DEFAULT_DEBUG: bool = False


def get_run_arguments() -> argparse.Namespace:
    """
    Parse command line arguments for the application.

    :return: argparse.Namespace: The parsed command line arguments.
    """

    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="crasher",
        description="Crasher application with launch arguments."
    )

    # General Options
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Run application in debug mode",
        default=DEFAULT_DEBUG
    )
    parser.add_argument(
        "--windowless",
        action="store_true",
        help="Run in windowless mode",
        default=DEFAULT_WINDOWLESS
    )

    # Project Options
    parser.add_argument(
        "-r", "--render",
        action="store_true",
        help="Render the current project",
        default=False
    )
    parser.add_argument(
        "-o", "--open",
        dest="filename",
        type=argparse.FileType("r", encoding="UTF-8"),
        help="Open a specific project file",
        metavar="PATH",
        default=None
    )
    parser.add_argument(
        "-f", "--file",
        dest="filename",
        type=argparse.FileType("r", encoding="UTF-8"),
        help="Output rendered image to specific file",
        metavar="PATH",
        default=None
    )

    return parser.parse_args()


def run_application() -> None:
    """ Set up and run the application. """

    # Get run arguments for application
    args = get_run_arguments()

    # Setup application
    application: QCrasherApplication = QCrasherApplication(sys.argv, arguments_=args)

    # Execute application
    application.exec()


if __name__ == "__main__":
    run_application()
