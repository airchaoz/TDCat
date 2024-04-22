from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from NewConnectionUI import Ui_NewConUI
from TDModel import TDConnect
from PyQt5.QtCore import pyqtSignal


class NewConn(QMainWindow, Ui_NewConUI):
    checkout_signal = pyqtSignal(list)

    def __init__(
        self,
        conn_ip="",
        conn_port="",
        conn_user="",
        conn_pwd="",
        conn_name="",
        parent=None,
    ):
        super().__init__(parent)
        self.setupUi(self)

        # 禁止其他窗口响应
        QMainWindow.setWindowModality(self, Qt.ApplicationModal)
        self.check_pbutton.clicked.connect(self.checkout)
        self.conn_ip_lineedit.setText(conn_ip)
        self.conn_port_lineedit.setText(conn_port)
        self.conn_user_lineedit.setText(conn_user)
        self.conn_pwd_lineedit.setText(conn_pwd)
        self.conn_name_lineedit.setText(conn_name)

    def checkout(self):
        conn_ip = self.conn_ip_lineedit.text()
        if len(conn_ip) == 0:
            QMessageBox.warning(self, "提示", "IP地址不能为空!")
            return
        conn_port = self.conn_port_lineedit.text()
        if len(conn_port) == 0:
            QMessageBox.warning(self, "提示", "端口号不能为空!")
            return
        conn_user = self.conn_user_lineedit.text()
        if len(conn_user) == 0:
            QMessageBox.warning(self, "提示", "用户名不能为空!")
            return
        conn_pwd = self.conn_pwd_lineedit.text()
        if len(conn_pwd) == 0:
            QMessageBox.warning(self, "提示", "密码不能为空!")
            return
        conn_name = self.conn_name_lineedit.text()
        if len(conn_name) == 0:
            conn_name = conn_ip

        sign = [conn_name, conn_ip, conn_port, conn_user, conn_pwd]
        self.checkout_signal.emit(sign)

        self.close()
