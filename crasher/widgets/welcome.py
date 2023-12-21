# Code by @selfkilla666
# https://github.com/witch-software/crasher
# MIT License

from __future__ import annotations

from typing import Optional

from PySide6.QtCore import QSize, Qt, QObject
from PySide6.QtGui import QFont
from PySide6 import QtWidgets


class QCrasherWelcomeWidget(QtWidgets.QWidget):

    # TODO: Optimize imports
    # TODO: Connect buttons signals
    # TODO: Make documentation
    # TODO: Lint code & add typehints
    # TODO: Think about styles/themes (?)
    # TODO: Make another layouts for recent files (grid, list)
    # TODO: Enhance design

    def __init__(self, parent: Optional[QObject] = None):

        super(QCrasherWelcomeWidget, self).__init__(parent=parent)
        self.setObjectName(u"QCrasherWelcomeWidget")

        self.setup_ui()
        self.translate_ui()

    def setup_ui(self):

        """ Layouts """

        # Setup widget layout
        self.WidgetLayout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout(self)
        self.WidgetLayout.setSpacing(6)
        self.WidgetLayout.setContentsMargins(60, 20, 60, 20)
        self.WidgetLayout.setObjectName(u"WidgetLayout")

        # Setup bottom bar layout
        self.BottomBarLayout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout()
        self.BottomBarLayout.setObjectName(u"BottomBarLayout")

        # Setup central layout (for sidebar and recent files)
        self.CentralLayout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout()
        self.CentralLayout.setSpacing(12)
        self.CentralLayout.setObjectName(u"CentralLayout")

        # Setup sidebar layout
        self.SidebarLayout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()
        self.SidebarLayout.setObjectName(u"SidebarLayout")
        self.SidebarButtonsLayout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()
        self.SidebarButtonsLayout.setObjectName(u"SidebarButtonsLayout")

        # Setup recent files layout
        self.RecentFilesLayout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()
        self.RecentFilesLayout.setObjectName(u"RecentFilesLayout")
        self.RecentFilesBarLayout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()
        self.RecentFilesBarLayout.setObjectName(u"RecentFilesBarLayout")
        self.RecentFilesBarTopLayout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout()
        self.RecentFilesBarTopLayout.setObjectName(u"RecentFilesBarTopLayout")
        self.RecentFilesBarBottomLayout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout()
        self.RecentFilesBarBottomLayout.setObjectName(u"RecentFilesBarBottomLayout")

        # Setup recent files scroll area
        self.RecentFilesScrollArea: QtWidgets.QScrollArea = QtWidgets.QScrollArea(self)
        self.RecentFilesScrollArea.setObjectName(u"RecentFilesScrollArea")
        self.RecentFilesScrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.RecentFilesScrollArea.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.RecentFilesScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.RecentFilesScrollArea.setWidgetResizable(True)

        self.RecentFilesScrollAreaWidget: QtWidgets.QWidget = QtWidgets.QWidget()
        self.RecentFilesScrollAreaWidget.setObjectName(u"RecentFilesScrollAreaWidget")
        self.RecentFilesScrollAreaWidget.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum))

        self.RecentFilesScrollAreaWidgetLayout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout(self.RecentFilesScrollAreaWidget)
        self.RecentFilesScrollAreaWidgetLayout.setObjectName(u"RecentFilesScrollAreaWidgetLayout")

        self.RecentFilesNoRecentFilesLayout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout()
        self.RecentFilesNoRecentFilesLayout.setObjectName(u"RecentFilesNoRecentFilesLayout")

        """ Fonts """

        # Font for sidebar buttons
        SidebarButtonsFont = QFont()
        SidebarButtonsFont.setWeight(QFont.Weight.Light)

        # Font for "Recent files" label
        RecentFilesLabelFont = QFont()
        RecentFilesLabelFont.setPointSize(12)
        RecentFilesLabelFont.setBold(True)

        # Font for labels in recent files bar
        RecentFilesBarLabelFont = QFont()
        RecentFilesBarLabelFont.setWeight(QFont.Weight.ExtraLight)

        # Font for version label
        BottomBarVersionLabelFont = QFont()
        BottomBarVersionLabelFont.setWeight(QFont.Weight.ExtraLight)
        BottomBarVersionLabelFont.setItalic(True)

        # Font for "No recent files" label
        NoRecentFilesLabelFont = QFont()
        NoRecentFilesLabelFont.setWeight(QFont.Weight.Light)
        NoRecentFilesLabelFont.setItalic(True)

        """ Size policies """

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        MaxMaxSizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        MaxMaxSizePolicy.setHorizontalStretch(0)
        MaxMaxSizePolicy.setVerticalStretch(0)

        sizePolicy2 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)

        sizePolicy3 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)

        sizePolicy4 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)

        """ Spacers """

        self.BottomBarSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.SidebarSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.RecentFilesBarTopSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.RecentFilesBarBottomSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)

        self.RecentFilesBarBottomSeparator = QtWidgets.QFrame(self)
        sizePolicy3.setHeightForWidth(self.RecentFilesBarBottomSeparator.sizePolicy().hasHeightForWidth())
        self.RecentFilesBarBottomSeparator.setSizePolicy(sizePolicy3)
        self.RecentFilesBarBottomSeparator.setMinimumSize(QSize(3, 24))
        self.RecentFilesBarBottomSeparator.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.RecentFilesBarBottomSeparator.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.RecentFilesBarBottomSeparator.setObjectName(u"RecentFilesBarBottomSeparator")

        """ Outputs """

        self.BottomBarVersionLabel = QtWidgets.QLabel(self)
        self.BottomBarVersionLabel.setObjectName(u"BottomBarVersionLabel")
        self.BottomBarVersionLabel.setFont(BottomBarVersionLabelFont)

        self.RecentFilesLabel = QtWidgets.QLabel(self)
        self.RecentFilesLabel.setObjectName(u"RecentFilesLabel")
        MaxMaxSizePolicy.setHeightForWidth(self.RecentFilesLabel.sizePolicy().hasHeightForWidth())
        self.RecentFilesLabel.setSizePolicy(MaxMaxSizePolicy)
        self.RecentFilesLabel.setFont(RecentFilesLabelFont)

        self.RecentFilesSortByLabel = QtWidgets.QLabel(self)
        self.RecentFilesSortByLabel.setObjectName(u"RecentFilesSortByLabel")
        MaxMaxSizePolicy.setHeightForWidth(self.RecentFilesSortByLabel.sizePolicy().hasHeightForWidth())
        self.RecentFilesSortByLabel.setSizePolicy(MaxMaxSizePolicy)
        self.RecentFilesSortByLabel.setFont(RecentFilesBarLabelFont)

        self.RecentFilesSearchLabel = QtWidgets.QLabel(self)
        self.RecentFilesSearchLabel.setObjectName(u"RecentFilesSearchLabel")
        MaxMaxSizePolicy.setHeightForWidth(self.RecentFilesSearchLabel.sizePolicy().hasHeightForWidth())
        self.RecentFilesSearchLabel.setSizePolicy(MaxMaxSizePolicy)
        self.RecentFilesSearchLabel.setFont(RecentFilesBarLabelFont)

        self.NoRecentFilesLabel = QtWidgets.QLabel(self.RecentFilesScrollAreaWidget)
        self.NoRecentFilesLabel.setObjectName(u"NoRecentFilesLabel")
        sizePolicy4.setHeightForWidth(self.NoRecentFilesLabel.sizePolicy().hasHeightForWidth())
        self.NoRecentFilesLabel.setSizePolicy(sizePolicy4)
        self.NoRecentFilesLabel.setFont(NoRecentFilesLabelFont)
        self.NoRecentFilesLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        """ Inputs """

        # Sidebar buttons
        self.CreateNewButton = QtWidgets.QPushButton(self)
        self.CreateNewButton.setObjectName(u"CreateNewButton")
        sizePolicy.setHeightForWidth(self.CreateNewButton.sizePolicy().hasHeightForWidth())
        self.CreateNewButton.setSizePolicy(sizePolicy)
        self.CreateNewButton.setMinimumSize(QSize(200, 0))
        self.CreateNewButton.setMaximumSize(QSize(300, 16777215))
        self.CreateNewButton.setFont(SidebarButtonsFont)

        self.OpenFileButton = QtWidgets.QPushButton(self)
        self.OpenFileButton.setObjectName(u"OpenFileButton")
        sizePolicy.setHeightForWidth(self.OpenFileButton.sizePolicy().hasHeightForWidth())
        self.OpenFileButton.setSizePolicy(sizePolicy)
        self.OpenFileButton.setMinimumSize(QSize(200, 0))
        self.OpenFileButton.setMaximumSize(QSize(300, 16777215))
        self.OpenFileButton.setFont(SidebarButtonsFont)

        # Radio buttons

        self.ShowRecentAsGridButton = QtWidgets.QRadioButton(self)
        self.ShowRecentAsGridButton.setObjectName(u"ShowRecentAsGridButton")
        MaxMaxSizePolicy.setHeightForWidth(self.ShowRecentAsGridButton.sizePolicy().hasHeightForWidth())
        self.ShowRecentAsGridButton.setSizePolicy(MaxMaxSizePolicy)

        self.ShowRecentAsListButton = QtWidgets.QRadioButton(self)
        self.ShowRecentAsListButton.setObjectName(u"ShowRecentAsListButton")
        MaxMaxSizePolicy.setHeightForWidth(self.ShowRecentAsListButton.sizePolicy().hasHeightForWidth())
        self.ShowRecentAsListButton.setSizePolicy(MaxMaxSizePolicy)

        # Icon buttons

        self.RecentFilesSortModeIncreaseButton = QtWidgets.QPushButton(self)
        self.RecentFilesSortModeIncreaseButton.setObjectName(u"RecentFilesSortModeIncreaseButton")
        MaxMaxSizePolicy.setHeightForWidth(self.RecentFilesSortModeIncreaseButton.sizePolicy().hasHeightForWidth())
        self.RecentFilesSortModeIncreaseButton.setSizePolicy(MaxMaxSizePolicy)
        self.RecentFilesSortModeIncreaseButton.setCheckable(True)
        self.RecentFilesSortModeIncreaseButton.setFlat(True)

        self.BottomBarSettingsButton = QtWidgets.QPushButton(self)
        self.BottomBarSettingsButton.setObjectName(u"BottomBarSettingsButton")
        MaxMaxSizePolicy.setHeightForWidth(self.BottomBarSettingsButton.sizePolicy().hasHeightForWidth())
        self.BottomBarSettingsButton.setSizePolicy(MaxMaxSizePolicy)
        self.BottomBarSettingsButton.setMinimumSize(QSize(40, 40))
        self.BottomBarSettingsButton.setMaximumSize(QSize(40, 40))
        self.BottomBarSettingsButton.setFlat(True)

        self.BottomBarAboutButton = QtWidgets.QPushButton(self)
        self.BottomBarAboutButton.setObjectName(u"BottomBarAboutButton")
        MaxMaxSizePolicy.setHeightForWidth(self.BottomBarAboutButton.sizePolicy().hasHeightForWidth())
        self.BottomBarAboutButton.setSizePolicy(MaxMaxSizePolicy)
        self.BottomBarAboutButton.setMinimumSize(QSize(40, 40))
        self.BottomBarAboutButton.setMaximumSize(QSize(40, 40))
        self.BottomBarAboutButton.setFlat(True)

        # Combo box
        self.RecentFilesSortModeCombo = QtWidgets.QComboBox(self)
        self.RecentFilesSortModeCombo.setObjectName(u"RecentFilesSortModeCombo")
        sizePolicy2.setHeightForWidth(self.RecentFilesSortModeCombo.sizePolicy().hasHeightForWidth())
        self.RecentFilesSortModeCombo.setSizePolicy(sizePolicy2)
        self.RecentFilesSortModeCombo.setMinimumSize(QSize(140, 0))

        # Line edit
        self.RecentFilesSearchInput = QtWidgets.QLineEdit(self)
        self.RecentFilesSearchInput.setObjectName(u"RecentFilesSearchInput")
        sizePolicy4.setHeightForWidth(self.RecentFilesSearchInput.sizePolicy().hasHeightForWidth())
        self.RecentFilesSearchInput.setSizePolicy(sizePolicy4)
        self.RecentFilesSearchInput.setMinimumSize(QSize(160, 0))

        """ Add objects to layouts """

        # Sidebar
        self.SidebarButtonsLayout.addWidget(self.CreateNewButton)
        self.SidebarButtonsLayout.addWidget(self.OpenFileButton)
        self.SidebarLayout.addLayout(self.SidebarButtonsLayout)
        self.SidebarLayout.addItem(self.SidebarSpacer)

        # Recent file bar top
        self.RecentFilesBarTopLayout.addWidget(self.RecentFilesLabel)
        self.RecentFilesBarTopLayout.addItem(self.RecentFilesBarTopSpacer)
        self.RecentFilesBarTopLayout.addWidget(self.ShowRecentAsGridButton)
        self.RecentFilesBarTopLayout.addWidget(self.ShowRecentAsListButton)

        # Recent file bar bottom
        self.RecentFilesBarBottomLayout.addWidget(self.RecentFilesSortByLabel)
        self.RecentFilesBarBottomLayout.addWidget(self.RecentFilesSortModeCombo)
        self.RecentFilesBarBottomLayout.addWidget(self.RecentFilesBarBottomSeparator)
        self.RecentFilesBarBottomLayout.addWidget(self.RecentFilesSortModeIncreaseButton)
        self.RecentFilesBarBottomLayout.addItem(self.RecentFilesBarBottomSpacer)
        self.RecentFilesBarBottomLayout.addWidget(self.RecentFilesSearchLabel)
        self.RecentFilesBarBottomLayout.addWidget(self.RecentFilesSearchInput)

        # Recent file bar
        self.RecentFilesBarLayout.addLayout(self.RecentFilesBarTopLayout)
        self.RecentFilesBarLayout.addLayout(self.RecentFilesBarBottomLayout)

        self.RecentFilesNoRecentFilesLayout.addWidget(self.NoRecentFilesLabel)
        self.RecentFilesScrollAreaWidgetLayout.addLayout(self.RecentFilesNoRecentFilesLayout)
        self.RecentFilesScrollAreaWidget.setLayout(self.RecentFilesScrollAreaWidgetLayout)
        self.RecentFilesScrollArea.setWidget(self.RecentFilesScrollAreaWidget)

        # Recent file
        self.RecentFilesLayout.addLayout(self.RecentFilesBarLayout)
        self.RecentFilesLayout.addWidget(self.RecentFilesScrollArea)

        # Central layout
        self.CentralLayout.addLayout(self.SidebarLayout)
        self.CentralLayout.addLayout(self.RecentFilesLayout)

        # Bottom layout
        self.BottomBarLayout.addWidget(self.BottomBarSettingsButton)
        self.BottomBarLayout.addWidget(self.BottomBarAboutButton)
        self.BottomBarLayout.addItem(self.BottomBarSpacer)
        self.BottomBarLayout.addWidget(self.BottomBarVersionLabel)

        # Widget layout
        self.WidgetLayout.addLayout(self.CentralLayout)
        self.WidgetLayout.addLayout(self.BottomBarLayout)

        self.setLayout(self.WidgetLayout)

    def translate_ui(self):
        self.CreateNewButton.setText(u"Create new")
        self.OpenFileButton.setText(u"Open...")
        self.RecentFilesLabel.setText(u"Recent files")
        self.ShowRecentAsGridButton.setText(u"G!")
        self.ShowRecentAsListButton.setText(u"L!")
        self.RecentFilesSortByLabel.setText(u"Sort by")
        self.RecentFilesSortModeIncreaseButton.setText(u"I!")
        self.RecentFilesSearchLabel.setText(u"Search")
        self.NoRecentFilesLabel.setText(u"No recent files :`(")
        self.BottomBarSettingsButton.setText(u"S!")
        self.BottomBarAboutButton.setText(u"H!")
        self.BottomBarVersionLabel.setText(u"Version: v1.0.0b")
