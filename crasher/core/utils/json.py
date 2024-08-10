# Code by @selfkilla666
# https://github.com/witch-software/crasher
# MIT License

from __future__ import annotations

from typing import Any
from pathlib import Path

from json import load, dump


def load_json_file(path: Path) -> dict[Any, Any]:
    """
    Load dictionary from the JSON file.

    :param path: Path to JSON file.
    :return: Dictionary loaded from JSON file.
    """

    with open(path, 'r') as file:
        return load(file)


def save_json_file(dictionary: dict[Any, Any], path: Path) -> None:
    """
    Save dictionary to the JSON file.

    :param dictionary: Dictionary to be saved.
    :param path: Path to JSON file.
    """

    with open(path, 'w') as file:
        dump(dictionary, file, indent=4)