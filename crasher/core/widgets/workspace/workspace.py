
from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtWidgets import QWidget

import loguru

if TYPE_CHECKING:
    from crasher.core.widgets.application import QCrasherApplication
    from crasher.core.widgets.window import QCrasherWindow


class QCrasherWorkspace(QWidget):

    application: QCrasherApplication
    window: QCrasherWindow
    logger: loguru.Logger

    project: None

    def __init__(self, window: QCrasherWindow, application: QCrasherApplication, *args, **kwargs) -> None:
        super().__init__(window, *args, **kwargs)

        self.application = application
        self.window = window

        self.initialize_ui()

    def initialize_ui(self) -> None:
        pass

    def render_viewport(self) -> None:
        pass