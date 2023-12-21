# Code by @selfkilla666
# https://github.com/witch-software/crasher
# MIT License

from __future__ import annotations

from typing import Any


def are_keys_present(dictionary_to_check: dict[Any, Any], dictionary_pattern: dict[Any, Any]) -> bool:
    """
    Check if all keys and their corresponding values in the `dictionary_pattern` are present
    in the `dictionary_to_check`. If a value in `dictionary_pattern` is not `None`, the function
    recursively checks the presence of keys and values in nested dictionaries.

    :param dictionary_to_check: Dictionary to check for the presence of keys and values.
    :param dictionary_pattern: Dictionary containing keys and values to be checked for presence.
    :return: True if all keys and values (if not None) in `dictionary_pattern` are present
             in `dictionary_to_check`, False otherwise.
    """

    for key, value in dictionary_pattern.items():
        if key not in dictionary_to_check or not are_keys_present(dictionary_to_check[key], value):
            return False

    return True

def add_missing_values(dictionary_to_check: dict[Any, Any], dictionary_pattern: dict[Any, Any]) -> dict[Any, Any]:
    """
    Add missing keys and their corresponding values from `dictionary_pattern` to
    `dictionary_to_check`. If a key is already present in `dictionary_to_check`, and both the
    value in `dictionary_pattern` and the corresponding value in `dictionary_to_check` are
    dictionaries, the function recursively adds missing keys in the nested dictionaries.

    :param dictionary_to_check: Dictionary to which missing keys and values will be added.
    :param dictionary_pattern: Dictionary containing keys and values to be added if missing.
    :return: A new dictionary containing all keys and values from `dictionary_to_check`,
             with missing keys and values added from `dictionary_pattern`
    """

    result = dictionary_to_check.copy()

    for key, value in dictionary_pattern.items():
        if key not in result:
            result[key] = value
        elif isinstance(value, dict) and isinstance(result[key], dict):
            result[key] = add_missing_values(result[key], value)

    return result