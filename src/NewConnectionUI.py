# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\NewConnection.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewConUI(object):
    def setupUi(self, NewConUI):
        NewConUI.setObjectName("NewConUI")
        NewConUI.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(NewConUI)
        self.centralwidget.setObjectName("centralwidget")
        self.conn_name_label = QtWidgets.QLabel(self.centralwidget)
        self.conn_name_label.setGeometry(QtCore.QRect(70, 70, 81, 18))
        self.conn_name_label.setObjectName("conn_name_label")
        self.conn_ip_label = QtWidgets.QLabel(self.centralwidget)
        self.conn_ip_label.setGeometry(QtCore.QRect(70, 110, 81, 18))
        self.conn_ip_label.setObjectName("conn_ip_label")
        self.conn_port_label = QtWidgets.QLabel(self.centralwidget)
        self.conn_port_label.setGeometry(QtCore.QRect(70, 160, 81, 18))
        self.conn_port_label.setObjectName("conn_port_label")
        self.conn_user_label = QtWidgets.QLabel(self.centralwidget)
        self.conn_user_label.setGeometry(QtCore.QRect(70, 220, 81, 18))
        self.conn_user_label.setObjectName("conn_user_label")
        self.conn_pwd_label = QtWidgets.QLabel(self.centralwidget)
        self.conn_pwd_label.setGeometry(QtCore.QRect(70, 270, 81, 18))
        self.conn_pwd_label.setObjectName("conn_pwd_label")
        self.conn_name_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.conn_name_lineedit.setGeometry(QtCore.QRect(170, 70, 321, 25))
        self.conn_name_lineedit.setObjectName("conn_name_lineedit")
        self.conn_ip_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.conn_ip_lineedit.setGeometry(QtCore.QRect(170, 110, 321, 25))
        self.conn_ip_lineedit.setObjectName("conn_ip_lineedit")
        self.conn_port_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.conn_port_lineedit.setGeometry(QtCore.QRect(170, 150, 321, 25))
        self.conn_port_lineedit.setObjectName("conn_port_lineedit")
        self.conn_user_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.conn_user_lineedit.setGeometry(QtCore.QRect(170, 220, 321, 25))
        self.conn_user_lineedit.setObjectName("conn_user_lineedit")
        self.conn_pwd_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.conn_pwd_lineedit.setGeometry(QtCore.QRect(170, 270, 321, 25))
        self.conn_pwd_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.conn_pwd_lineedit.setObjectName("conn_pwd_lineedit")
        self.check_pbutton = QtWidgets.QPushButton(self.centralwidget)
        self.check_pbutton.setGeometry(QtCore.QRect(530, 550, 112, 34))
        self.check_pbutton.setObjectName("check_pbutton")
        self.cancel_pbutton = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_pbutton.setGeometry(QtCore.QRect(670, 550, 112, 34))
        self.cancel_pbutton.setObjectName("cancel_pbutton")
        NewConUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(NewConUI)
        QtCore.QMetaObject.connectSlotsByName(NewConUI)

    def retranslateUi(self, NewConUI):
        _translate = QtCore.QCoreApplication.translate
        NewConUI.setWindowTitle(_translate("NewConUI", "新建连接"))
        self.conn_name_label.setText(_translate("NewConUI", "连接名:"))
        self.conn_ip_label.setText(_translate("NewConUI", "主机"))
        self.conn_port_label.setText(_translate("NewConUI", "端口"))
        self.conn_user_label.setText(_translate("NewConUI", "用户名"))
        self.conn_pwd_label.setText(_translate("NewConUI", "密码"))
        self.check_pbutton.setText(_translate("NewConUI", "确定"))
        self.cancel_pbutton.setText(_translate("NewConUI", "取消"))
