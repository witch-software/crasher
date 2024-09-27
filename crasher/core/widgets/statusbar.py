
from typing import Optional, TYPE_CHECKING

from PySide6.QtWidgets import QStatusBar

import loguru

if TYPE_CHECKING:
    from crasher.core.widgets.window import QCrasherWindow


class QCrasherStatusBar(QStatusBar):
    """ Custom PySide6.QtWidgets.QStatusBar implementation for Crasher """

    class StatusBarLogHandler:
        """ Crasher status bar handler for logs messages """

        status_bar: QStatusBar

        def __init__(self, status_bar: QStatusBar) -> None:
            self.status_bar = status_bar

        def write(self, message: str) -> None:
            self.status_bar.showMessage(message)

    logger: loguru.Logger
    logger_handler: StatusBarLogHandler

    def __init__(self, parent: Optional[QCrasherWindow] = None, *, logger: Optional[loguru.Logger] = None) -> None:

        super(QCrasherStatusBar, self).__init__(parent=parent)

        if logger:
            self.logger = logger
            self.logger_handler = self.StatusBarLogHandler(self)
            self.logger.add(self.logger_handler, format="{message}")