# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\sqlExec.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sqlExec(object):
    def setupUi(self, sqlExec):
        sqlExec.setObjectName("sqlExec")
        sqlExec.resize(965, 798)
        self.gridLayout = QtWidgets.QGridLayout(sqlExec)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.run_btn = QtWidgets.QPushButton(sqlExec)
        self.run_btn.setObjectName("run_btn")
        self.horizontalLayout.addWidget(self.run_btn)
        self.pretty_btn = QtWidgets.QPushButton(sqlExec)
        self.pretty_btn.setObjectName("pretty_btn")
        self.horizontalLayout.addWidget(self.pretty_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.codeEditor = QCodeEditor(sqlExec)
        self.codeEditor.setObjectName("codeEditor")
        self.verticalLayout.addWidget(self.codeEditor)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(sqlExec)
        QtCore.QMetaObject.connectSlotsByName(sqlExec)

    def retranslateUi(self, sqlExec):
        _translate = QtCore.QCoreApplication.translate
        sqlExec.setWindowTitle(_translate("sqlExec", "Form"))
        self.run_btn.setText(_translate("sqlExec", "运行"))
        self.pretty_btn.setText(_translate("sqlExec", "美化SQL"))
from QCodeEditor import QCodeEditor
