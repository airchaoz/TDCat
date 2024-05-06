from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from SqlExecUI import Ui_sqlExec
from PyQt5.QtCore import pyqtSignal
from SQLFormat import sql_format


class SqlExec(QWidget, Ui_sqlExec):
    goto_page = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pretty_btn.clicked.connect(self.pretty_sql)
        self.codeEditor.setPlainText("\n")

    def pretty_sql(self):
        sql = self.codeEditor.toPlainText()
        if len(sql.strip()) == 0:
            return

        formatted_sql = sql_format(sql)
        self.codeEditor.setPlainText(formatted_sql)
        self.codeEditor.appendPlainText("")  # feature


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    widget = SqlExec()
    widget.show()
    sys.exit(app.exec_())