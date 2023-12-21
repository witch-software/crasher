# Code by @selfkilla666
# https://github.com/witch-software/crasher
# MIT License

from __future__ import annotations

from pathlib import Path

import os


def get_user_local_directory() -> Path:
    """
    Get the user's local directory for application data.

    This function determines the user's local
    application directory based on the operating system
    and returns a pathlib.Path object pointing to that directory.

    :return: Path to the user's local application directory.
    """

    path: Path

    # Determine the user's local application directory
    if os.name == "posix":
        path = Path(
            os.path.expanduser('~/.witchsoftware/crasher/')
        )
    elif os.name == "nt":
        path = Path(
            os.path.expanduser(
                'C:/Users/{}/AppData/Local/Witch Software/Crasher/'.format(
                    os.getlogin()
                )
            )
        )
    else:
        path = Path("./")

    # Create the log directory if it doesn't exist
    os.makedirs(path, exist_ok=True)

    return path
