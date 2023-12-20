# Code by @selfkilla666
# https://github.com/witch-software/crasher
# MIT License

from __future__ import annotations

from PySide6.QtWidgets import QStatusBar


class StatusBarLogHandler:
    """ Crasher window status bar handler for logs messages """

    status_bar: QStatusBar

    def __init__(self, status_bar: QStatusBar) -> None:
        self.status_bar = status_bar

    def write(self, message: str) -> None:
        self.status_bar.showMessage(message)