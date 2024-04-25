from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from SqlExecUI import Ui_sqlExec
from PyQt5.QtCore import pyqtSignal

class SqlExec(QWidget, Ui_sqlExec):
    goto_page = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.codeEditor.setPlainText('\n')

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    widget = SqlExec()
    widget.show()
    sys.exit(app.exec_())