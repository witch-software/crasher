# Code by @selfkilla666
# https://github.com/witch-software/crasher
# MIT License

from __future__ import annotations

from pathlib import Path

import os


DEFAULT_PATHS: dict[str, dict[str, str]] = {
    "nt": {
        "org": "Witch Software",
        "application": "Crasher"
    },
    "posix": {
        "org": "witchsoftware",
        "application": "crasher"
    }
}


def get_user_local_directory(paths: dict[str, dict[str, str]] = DEFAULT_PATHS) -> Path:
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
        path = Path(os.path.expanduser(f"~/.{paths[os.name]['org']}/{paths[os.name]['application']}/"))
    elif os.name == "nt":
        path = Path(
            os.path.expanduser(
                f"C:/Users/{os.getlogin()}/AppData/Local/{paths[os.name]['org']}/{paths[os.name]['application']}/"
            )
        )
    else:
        path = Path("./")

    # Create the log directory if it doesn't exist
    os.makedirs(path, exist_ok=True)

    return path
