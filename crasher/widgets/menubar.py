# Code by @selfkilla666
# https://github.com/witch-software/crasher
# MIT License

from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from PySide6.QtWidgets import QMenuBar, QMenu
from PySide6.QtGui import QAction, QKeySequence

if TYPE_CHECKING:
    from crasher.widgets.window import QCrasherWindow


class QCrasherMenuBar(QMenuBar):
    """ Custom PySide6.QtWidgets.QMenuBar implementation for Crasher """

    # TODO: Add comments to code
    # TODO: Add all actions to menubar
    # TODO: Add recent files to file menu
    # TODO: Add icons (?)
    # TODO: Add shortcuts for actions
    # TODO: Connect signals to functions

    """ General """

    application: QCrasherWindow
    connect_signals: bool = False

    """ Menus """

    fileMenu: QMenu
    editMenu: QMenu
    imageMenu: QMenu
    layersMenu: QMenu
    adjustmentsMenu: QMenu
    effectsMenu: QMenu
    viewMenu: QMenu
    helpMenu: QMenu

    """ Actions """

    # File menu
    newAction: QAction
    openAction: QAction
    saveAction: QAction
    saveAsAction: QAction
    settingsAction: QAction
    exitAction: QAction

    # Edit menu
    undoAction: QAction
    redoAction: QAction
    cutAction: QAction
    copyAction: QAction
    pasteAction: QAction
    pasteSameLayerAction: QAction

    def __init__(self, parent: Optional[QCrasherWindow] = None, *, connect_signals: bool = False) -> None:

        super(QCrasherMenuBar, self).__init__(parent=parent)

        self.application = parent                       # type: ignore[assignment]
        self.connect_signals = connect_signals or False

        self.initialize_ui()
        if self.connect_signals:
            self.connect_signals_to_actions()

    def initialize_ui(self) -> None:
        """ Initialize all actions in menubar """

        self.fileMenu: QMenu = self.addMenu("&File")
        self.editMenu: QMenu = self.addMenu("&Edit")
        self.imageMenu: QMenu = self.addMenu("&Image")
        self.layersMenu: QMenu = self.addMenu("&Layers")
        self.adjustmentsMenu: QMenu = self.addMenu("&Adjustments")
        self.effectsMenu: QMenu = self.addMenu("Effect&s")
        self.viewMenu: QMenu = self.addMenu("&View")
        self.helpMenu: QMenu = self.addMenu("&Help")

        self.initialize_file_menu(self.fileMenu)
        self.initialize_edit_menu(self.editMenu)
        self.initialize_image_menu(self.imageMenu)
        self.initialize_layers_menu(self.layersMenu)
        self.initialize_adjustments_menu(self.adjustmentsMenu)
        self.initialize_effects_menu(self.effectsMenu)
        self.initialize_view_menu(self.viewMenu)
        self.initialize_help_menu(self.helpMenu)

        self.translate_ui()

    def translate_ui(self) -> None:
        pass

    def connect_signals_to_actions(self) -> None:

        self.exitAction.triggered.connect(self.application.exit)

    def initialize_file_menu(self, menu: QMenu) -> None:

        self.newAction: QAction = QAction(text="New...", parent=self.parent())
        self.openAction: QAction = QAction(text="Open...", parent=self.parent())
        self.saveAction: QAction = QAction(text="Save", parent=self.parent())
        self.saveAsAction: QAction = QAction(text="Save as...", parent=self.parent())
        self.settingsAction: QAction = QAction(text="Settings", parent=self.parent())
        self.exitAction: QAction = QAction(text="Exit", parent=self.parent())

        self.newAction.setShortcut(QKeySequence("Ctrl+N"))
        self.openAction.setShortcut(QKeySequence("Ctrl+O"))
        self.saveAction.setShortcut(QKeySequence("Ctrl+S"))
        self.saveAsAction.setShortcut(QKeySequence("Ctrl+Shift+S"))

        menu.addAction(self.newAction)
        menu.addAction(self.openAction)
        menu.addSeparator()
        menu.addAction(self.saveAction)
        menu.addAction(self.saveAsAction)
        menu.addSeparator()
        menu.addAction(self.settingsAction)
        menu.addSeparator()
        menu.addAction(self.exitAction)

    def initialize_edit_menu(self, menu: QMenu) -> None:

        self.undoAction: QAction = QAction(text="Undo", parent=self.parent())
        self.redoAction: QAction = QAction(text="Redo", parent=self.parent())
        self.cutAction: QAction = QAction(text="Cut", parent=self.parent())
        self.copyAction: QAction = QAction(text="Copy", parent=self.parent())
        self.pasteAction: QAction = QAction(text="Paste", parent=self.parent())
        self.pasteSameLayerAction: QAction = QAction(text="Paste into same layer", parent=self.parent())

        self.undoAction.setShortcut(QKeySequence("Ctrl+Z"))
        self.redoAction.setShortcut(QKeySequence("Ctrl+Y"))
        self.cutAction.setShortcut(QKeySequence("Ctrl+X"))
        self.copyAction.setShortcut(QKeySequence("Ctrl+C"))
        self.pasteAction.setShortcut(QKeySequence("Ctrl+V"))
        self.pasteSameLayerAction.setShortcut(QKeySequence("Ctrl+Shift+V"))

        menu.addAction(self.undoAction)
        menu.addAction(self.redoAction)
        menu.addSeparator()
        menu.addAction(self.cutAction)
        menu.addAction(self.copyAction)
        menu.addAction(self.pasteAction)
        menu.addAction(self.pasteSameLayerAction)

    def initialize_image_menu(self, menu: QMenu) -> None:
        pass

    def initialize_layers_menu(self, menu: QMenu) -> None:
        pass

    def initialize_adjustments_menu(self, menu: QMenu) -> None:
        pass

    def initialize_effects_menu(self, menu: QMenu) -> None:
        pass

    def initialize_view_menu(self, menu: QMenu) -> None:
        pass

    def initialize_help_menu(self, menu: QMenu) -> None:
        pass