# Code by @selfkilla666
# https://github.com/witch-software/crasher
# MIT License

from __future__ import annotations

from path import Path
from hashlib import new as new_algorithm


__all__ = ["generate_checksum"]


def generate_checksum(file_path: Path, *, algorithm: str = "md5", buffer_size: int = 8192) -> str:
    """
    Generate a checksum (hash value) for a file.

    :param file_path: Path to the file for which the checksum is to be generated.
    :param algorithm: The hashing algorithm to be used (default is 'md5').
    :param buffer_size: Size of the buffer for reading the file in chunks (default is 8192).
    :return: The checksum of the file.
    """

    hash_algorithm = new_algorithm(algorithm)

    with open(file_path, 'rb') as file:
        while chunk := file.read(buffer_size):
            hash_algorithm.update(chunk)

    return hash_algorithm.hexdigest()