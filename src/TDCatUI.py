# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\TDCat.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TDCat(object):
    def setupUi(self, TDCat):
        TDCat.setObjectName("TDCat")
        TDCat.resize(1726, 1295)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TDCat.sizePolicy().hasHeightForWidth())
        TDCat.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        TDCat.setFont(font)
        self.centralwidget = QtWidgets.QWidget(TDCat)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(2)
        self.splitter.setObjectName("splitter")
        self.tree_viewer = CustomTreeView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_viewer.sizePolicy().hasHeightForWidth())
        self.tree_viewer.setSizePolicy(sizePolicy)
        self.tree_viewer.setMinimumSize(QtCore.QSize(400, 0))
        self.tree_viewer.setMaximumSize(QtCore.QSize(2000, 16777215))
        self.tree_viewer.setObjectName("tree_viewer")
        self.widget_2 = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.table_tab = QtWidgets.QTabWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.table_tab.sizePolicy().hasHeightForWidth())
        self.table_tab.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(10)
        self.table_tab.setFont(font)
        self.table_tab.setStyleSheet("QTabBar::tab { min-width: 120px; min-height: 35px; }")
        self.table_tab.setTabsClosable(True)
        self.table_tab.setObjectName("table_tab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.table_tab.addTab(self.tab, "")
        self.gridLayout.addWidget(self.table_tab, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout.addLayout(self.verticalLayout)
        TDCat.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(TDCat)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1726, 33))
        self.menuBar.setObjectName("menuBar")
        self.file_menu = QtWidgets.QMenu(self.menuBar)
        self.file_menu.setObjectName("file_menu")
        self.help_menu = QtWidgets.QMenu(self.menuBar)
        self.help_menu.setObjectName("help_menu")
        TDCat.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(TDCat)
        self.statusBar.setObjectName("statusBar")
        TDCat.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(TDCat)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolBar.setFont(font)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(100, 60))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        TDCat.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.new_conn_action = QtWidgets.QAction(TDCat)
        self.new_conn_action.setObjectName("new_conn_action")
        self.conn_action = QtWidgets.QAction(TDCat)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/connection.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.conn_action.setIcon(icon)
        self.conn_action.setObjectName("conn_action")
        self.new_query_action = QtWidgets.QAction(TDCat)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/query.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_query_action.setIcon(icon1)
        self.new_query_action.setObjectName("new_query_action")
        self.file_menu.addAction(self.new_conn_action)
        self.menuBar.addAction(self.file_menu.menuAction())
        self.menuBar.addAction(self.help_menu.menuAction())
        self.toolBar.addAction(self.conn_action)
        self.toolBar.addAction(self.new_query_action)

        self.retranslateUi(TDCat)
        self.table_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TDCat)

    def retranslateUi(self, TDCat):
        _translate = QtCore.QCoreApplication.translate
        TDCat.setWindowTitle(_translate("TDCat", "TDCat"))
        self.table_tab.setTabText(self.table_tab.indexOf(self.tab), _translate("TDCat", "对象"))
        self.file_menu.setTitle(_translate("TDCat", "文件"))
        self.help_menu.setTitle(_translate("TDCat", "帮助"))
        self.toolBar.setWindowTitle(_translate("TDCat", "toolBar"))
        self.new_conn_action.setText(_translate("TDCat", "新建连接"))
        self.conn_action.setText(_translate("TDCat", "连接"))
        self.new_query_action.setText(_translate("TDCat", "新建查询"))
from CustomTreeView import CustomTreeView
import resources_rc
