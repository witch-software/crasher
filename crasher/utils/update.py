# Code by @selfkilla666
# https://github.com/witch-software/crasher
# MIT License

from __future__ import annotations

import urllib.request
import json


def get_latest_version(owner: str = "witch-software", repo: str = "crasher") -> str | None:
    """
    Retrieves the latest version number of a program from a GitHub repository.

    :param owner: The username or organization name that owns the GitHub repository.
    :param repo: The name of the GitHub repository.
    :return: The latest version number if successful, or None if there was an error.
    """

    url: str = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"

    with urllib.request.urlopen(url) as response:
        data = response.read()
        encoding = response.info().get_content_charset('utf-8')
        json_data = json.loads(data.decode(encoding))

    return json_data["tag_name"] or None