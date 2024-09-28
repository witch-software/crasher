
from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Any

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QImage, QWheelEvent, QMouseEvent, QPen, QColor
from PySide6.QtCore import Qt, QRectF, QPointF

from PIL import Image
import io

import loguru

if TYPE_CHECKING:
    from crasher.core.widgets.workspace.workspace import QCrasherWorkspace
    from crasher.core.widgets.application import QCrasherApplication


class QCrasherViewport(QWidget):
    """
    A QWidget subclass for displaying and interacting with an image.

    :param parent: Parent widget, if any.
    """

    application: QCrasherApplication
    workspace: QCrasherWorkspace

    logger: loguru.Logger

    image: Optional[Any]

    def __init__(self,
                 parent: Optional[QWidget] = None,
                 *,
                 workspace: Optional[QCrasherWorkspace] = None,
                 application: Optional[QCrasherApplication] = None,
                 logger: Optional[loguru.Logger] = None,
                 image: Optional[Image.Image] = None
                ) -> None:

        super().__init__(parent)

        self.workspace = workspace
        self.application = application
        self.logger = logger or application.logger

        # Initialize interaction parameters
        self.scale = 1.0
        self.offset = QPointF(0, 0)
        self.last_mouse_position = None
        self.min_scale = 0.1
        self.max_scale = 10.0

    def _load_image(self, image_path: str) -> QImage:
        """
        Loads an image from the given path, converts it to QImage.

        :param image_path: Path to the image file.
        :return: QImage object.
        """

        pil_image = Image.open(image_path).convert("RGBA")
        buffer = io.BytesIO()
        pil_image.save(buffer, format="PNG")
        buffer.seek(0)
        return QImage.fromData(buffer.read())

    def _draw_image(self, painter: QPainter):
        """
        Draws the image on the widget with applied transformations such as scaling and offset.

        :param painter: QPainter object used for rendering.
        """
        target_rect = QRectF(self.offset.x(), self.offset.y(),
                             self.image.width() * self.scale,
                             self.image.height() * self.scale)
        source_rect = QRectF(0, 0, self.image.width(), self.image.height())

        painter.drawImage(target_rect, self.image, source_rect)

    def _draw_border(self, painter: QPainter, target_rect: QRectF):
        """
        Draws a white border around the image.

        :param painter: QPainter object used for rendering.
        :param target_rect: QRectF defining the target rectangle of the image.
        """
        pen = QPen(Qt.white, 1)
        painter.setPen(pen)
        border_rect = QRectF(target_rect.left() - 1, target_rect.top() - 1,
                             target_rect.width() + 2, target_rect.height() + 2)
        painter.drawRect(border_rect)

    def _draw_grid(self, painter: QPainter, target_rect: QRectF):
        """
        Draws a semi-transparent grid when zoomed in.

        :param painter: QPainter object used for rendering.
        :param target_rect: QRectF defining the target rectangle of the image.
        """
        if self.scale > 9:
            grid_color = QColor(255, 255, 255, 25)
            grid_pen = QPen(grid_color, 0.5)
            painter.setPen(grid_pen)
            step = 100 / self.scale
            for x in range(0, int(target_rect.width() / step)):
                painter.drawLine(target_rect.left() + x * step, target_rect.top(),
                                 target_rect.left() + x * step, target_rect.bottom())
            for y in range(0, int(target_rect.height() / step)):
                painter.drawLine(target_rect.left(), target_rect.top() + y * step,
                                 target_rect.right(), target_rect.top() + y * step)

    def paintEvent(self, event):
        """
        Handles the widget's paint event to render the image and the grid.

        :param event: QPaintEvent object.
        """
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(50, 50, 50))  # Fill the background with dark gray.

        target_rect = QRectF(self.offset.x(), self.offset.y(),
                             self.image.width() * self.scale,
                             self.image.height() * self.scale)

        # Draw image, border, and grid
        self._draw_image(painter)
        self._draw_border(painter, target_rect)
        self._draw_grid(painter, target_rect)

    def wheelEvent(self, event: QWheelEvent):
        """
        Handles zooming of the image based on the mouse wheel event.

        :param event: QWheelEvent object containing wheel event data.
        """
        zoom_factor = 1.25 if event.angleDelta().y() > 0 else 0.8

        new_scale = max(self.min_scale, min(self.max_scale, self.scale * zoom_factor))
        cursor_pos = event.position()

        # Adjust offset for zoom to focus around the cursor position
        self.offset = cursor_pos - ((cursor_pos - self.offset) * new_scale / self.scale)
        self.scale = new_scale
        self.update()

    def mousePressEvent(self, event: QMouseEvent):
        """
        Handles the event when the mouse button is pressed.

        :param event: QMouseEvent object containing mouse event data.
        """
        if event.button() == Qt.LeftButton:
            self.last_mouse_position = event.position()

    def mouseMoveEvent(self, event: QMouseEvent):
        """
        Handles the event when the mouse is moved while a button is pressed.

        :param event: QMouseEvent object containing mouse event data.
        """
        if event.buttons() & Qt.LeftButton and self.last_mouse_position:
            delta = event.position() - self.last_mouse_position
            self.offset += delta
            self.last_mouse_position = event.position()
            self.update()

    def mouseReleaseEvent(self, event: QMouseEvent):
        """
        Handles the event when the mouse button is released.

        :param event: QMouseEvent object containing mouse event data.
        """
        if event.button() == Qt.LeftButton:
            self.last_mouse_position = None
