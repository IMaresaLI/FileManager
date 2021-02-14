# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileManagerDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 704)
        MainWindow.setStyleSheet("#MainWindow{background-color: rgb(99, 99, 99);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_4.setStyleSheet("#frame_4{\n"
"background-color: rgb(48, 48, 48);}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LogoLbl = QtWidgets.QLabel(self.frame_4)
        self.LogoLbl.setMinimumSize(QtCore.QSize(120, 30))
        self.LogoLbl.setMaximumSize(QtCore.QSize(100, 100))
        self.LogoLbl.setText("")
        self.LogoLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.LogoLbl.setObjectName("LogoLbl")
        self.horizontalLayout_2.addWidget(self.LogoLbl)
        spacerItem = QtWidgets.QSpacerItem(420, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.minimizeBtn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimizeBtn.sizePolicy().hasHeightForWidth())
        self.minimizeBtn.setSizePolicy(sizePolicy)
        self.minimizeBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.minimizeBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.minimizeBtn.setText("")
        self.minimizeBtn.setIconSize(QtCore.QSize(50, 50))
        self.minimizeBtn.setObjectName("minimizeBtn")
        self.horizontalLayout_2.addWidget(self.minimizeBtn)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.fullScreenBtn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.fullScreenBtn.sizePolicy().hasHeightForWidth())
        self.fullScreenBtn.setSizePolicy(sizePolicy)
        self.fullScreenBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.fullScreenBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.fullScreenBtn.setText("")
        self.fullScreenBtn.setObjectName("fullScreenBtn")
        self.horizontalLayout_2.addWidget(self.fullScreenBtn)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.exitBtn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.exitBtn.sizePolicy().hasHeightForWidth())
        self.exitBtn.setSizePolicy(sizePolicy)
        self.exitBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.exitBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.exitBtn.setStatusTip("")
        self.exitBtn.setWhatsThis("")
        self.exitBtn.setText("")
        self.exitBtn.setObjectName("exitBtn")
        self.horizontalLayout_2.addWidget(self.exitBtn)
        spacerItem4 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("#frame{\n"
"background-color: rgb(94, 94, 94);\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(120, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_2.setStyleSheet("#frame_2{background-color: rgb(71, 71, 71);}\n"
"\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.HomeBtn = QtWidgets.QPushButton(self.frame_2)
        self.HomeBtn.setMinimumSize(QtCore.QSize(0, 100))
        self.HomeBtn.setMaximumSize(QtCore.QSize(150, 100))
        self.HomeBtn.setText("")
        self.HomeBtn.setObjectName("HomeBtn")
        self.verticalLayout_4.addWidget(self.HomeBtn)
        self.fileManagerBtn = QtWidgets.QPushButton(self.frame_2)
        self.fileManagerBtn.setMinimumSize(QtCore.QSize(0, 100))
        self.fileManagerBtn.setMaximumSize(QtCore.QSize(150, 250))
        self.fileManagerBtn.setText("")
        self.fileManagerBtn.setObjectName("fileManagerBtn")
        self.verticalLayout_4.addWidget(self.fileManagerBtn)
        self.AdvancedSearchBtn = QtWidgets.QPushButton(self.frame_2)
        self.AdvancedSearchBtn.setMinimumSize(QtCore.QSize(0, 100))
        self.AdvancedSearchBtn.setMaximumSize(QtCore.QSize(150, 250))
        self.AdvancedSearchBtn.setText("")
        self.AdvancedSearchBtn.setObjectName("AdvancedSearchBtn")
        self.verticalLayout_4.addWidget(self.AdvancedSearchBtn)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_3)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Home)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(self.Home)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.stackedWidget.addWidget(self.Home)
        self.FileManager = QtWidgets.QWidget()
        self.FileManager.setObjectName("FileManager")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.FileManager)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.FileManager)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.createFile = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createFile.sizePolicy().hasHeightForWidth())
        self.createFile.setSizePolicy(sizePolicy)
        self.createFile.setMinimumSize(QtCore.QSize(32, 32))
        self.createFile.setMaximumSize(QtCore.QSize(32, 32))
        self.createFile.setSizeIncrement(QtCore.QSize(4, 0))
        self.createFile.setObjectName("createFile")
        self.horizontalLayout_4.addWidget(self.createFile)
        self.deleteFile = QtWidgets.QPushButton(self.frame_6)
        self.deleteFile.setMinimumSize(QtCore.QSize(32, 32))
        self.deleteFile.setMaximumSize(QtCore.QSize(32, 32))
        self.deleteFile.setObjectName("deleteFile")
        self.horizontalLayout_4.addWidget(self.deleteFile)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.treeView = QtWidgets.QTreeView(self.FileManager)
        self.treeView.setDragDropOverwriteMode(True)
        self.treeView.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.treeView.setAllColumnsShowFocus(True)
        self.treeView.setWordWrap(True)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_2.addWidget(self.treeView)
        self.stackedWidget.addWidget(self.FileManager)
        self.NetworkPage = QtWidgets.QWidget()
        self.NetworkPage.setObjectName("NetworkPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.NetworkPage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.NetworkPage)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.fileCountTbx = QtWidgets.QLineEdit(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileCountTbx.sizePolicy().hasHeightForWidth())
        self.fileCountTbx.setSizePolicy(sizePolicy)
        self.fileCountTbx.setMinimumSize(QtCore.QSize(10, 0))
        self.fileCountTbx.setMaximumSize(QtCore.QSize(60, 16777215))
        self.fileCountTbx.setText("")
        self.fileCountTbx.setAlignment(QtCore.Qt.AlignCenter)
        self.fileCountTbx.setReadOnly(True)
        self.fileCountTbx.setObjectName("fileCountTbx")
        self.horizontalLayout_5.addWidget(self.fileCountTbx)
        self.searchtbx = QtWidgets.QLineEdit(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchtbx.sizePolicy().hasHeightForWidth())
        self.searchtbx.setSizePolicy(sizePolicy)
        self.searchtbx.setToolTip("")
        self.searchtbx.setObjectName("searchtbx")
        self.horizontalLayout_5.addWidget(self.searchtbx)
        self.searchBtn = QtWidgets.QPushButton(self.frame_7)
        self.searchBtn.setObjectName("searchBtn")
        self.horizontalLayout_5.addWidget(self.searchBtn)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.NetworkPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.FileListWidget = QtWidgets.QListWidget(self.frame_8)
        self.FileListWidget.setObjectName("FileListWidget")
        self.verticalLayout_6.addWidget(self.FileListWidget)
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem8 = QtWidgets.QSpacerItem(66, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.FileDescription = QtWidgets.QTextBrowser(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FileDescription.sizePolicy().hasHeightForWidth())
        self.FileDescription.setSizePolicy(sizePolicy)
        self.FileDescription.setMinimumSize(QtCore.QSize(500, 0))
        self.FileDescription.setMaximumSize(QtCore.QSize(500, 16777215))
        self.FileDescription.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FileDescription.setObjectName("FileDescription")
        self.horizontalLayout_6.addWidget(self.FileDescription)
        spacerItem9 = QtWidgets.QSpacerItem(66, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout_6.addWidget(self.frame_9)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.stackedWidget.addWidget(self.NetworkPage)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(100, 30))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setContentsMargins(0, 6, 0, 6)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cpuPercent = QtWidgets.QProgressBar(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cpuPercent.sizePolicy().hasHeightForWidth())
        self.cpuPercent.setSizePolicy(sizePolicy)
        self.cpuPercent.setStyleSheet("")
        self.cpuPercent.setProperty("value", 24)
        self.cpuPercent.setAlignment(QtCore.Qt.AlignCenter)
        self.cpuPercent.setTextVisible(True)
        self.cpuPercent.setOrientation(QtCore.Qt.Horizontal)
        self.cpuPercent.setInvertedAppearance(False)
        self.cpuPercent.setObjectName("cpuPercent")
        self.horizontalLayout_3.addWidget(self.cpuPercent)
        self.ramPercent = QtWidgets.QProgressBar(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ramPercent.sizePolicy().hasHeightForWidth())
        self.ramPercent.setSizePolicy(sizePolicy)
        self.ramPercent.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ramPercent.setStyleSheet("")
        self.ramPercent.setProperty("value", 24)
        self.ramPercent.setAlignment(QtCore.Qt.AlignCenter)
        self.ramPercent.setTextVisible(True)
        self.ramPercent.setOrientation(QtCore.Qt.Horizontal)
        self.ramPercent.setInvertedAppearance(False)
        self.ramPercent.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.ramPercent.setObjectName("ramPercent")
        self.horizontalLayout_3.addWidget(self.ramPercent)
        self.gpuPercent = QtWidgets.QProgressBar(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gpuPercent.sizePolicy().hasHeightForWidth())
        self.gpuPercent.setSizePolicy(sizePolicy)
        self.gpuPercent.setStyleSheet("")
        self.gpuPercent.setProperty("value", 24)
        self.gpuPercent.setAlignment(QtCore.Qt.AlignCenter)
        self.gpuPercent.setTextVisible(True)
        self.gpuPercent.setOrientation(QtCore.Qt.Horizontal)
        self.gpuPercent.setInvertedAppearance(False)
        self.gpuPercent.setObjectName("gpuPercent")
        self.horizontalLayout_3.addWidget(self.gpuPercent)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 842, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.minimizeBtn.setToolTip(_translate("MainWindow", "Simge Küçültme"))
        self.fullScreenBtn.setToolTip(_translate("MainWindow", "Minimize"))
        self.exitBtn.setToolTip(_translate("MainWindow", "Exit"))
        self.createFile.setText(_translate("MainWindow", "+"))
        self.deleteFile.setText(_translate("MainWindow", "X"))
        self.fileCountTbx.setPlaceholderText(_translate("MainWindow", "Sayı"))
        self.searchtbx.setPlaceholderText(_translate("MainWindow", "Aranacak Dosya Adı"))
        self.searchBtn.setText(_translate("MainWindow", "Search"))
        self.cpuPercent.setToolTip(_translate("MainWindow", "CPU"))
        self.cpuPercent.setFormat(_translate("MainWindow", "%p%"))
        self.ramPercent.setToolTip(_translate("MainWindow", "RAM"))
        self.ramPercent.setFormat(_translate("MainWindow", "%p%"))
        self.gpuPercent.setToolTip(_translate("MainWindow", "GPU"))
        self.gpuPercent.setFormat(_translate("MainWindow", "%p%"))
