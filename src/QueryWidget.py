from PyQt5.QtWidgets import QWidget, QGridLayout
from CustomTableView import CustomTableView
from PyQt5.QtGui import QFont

class QueryWidget(QWidget):
    def __init__(self, header, data):
        super().__init__()
        self.header = header
        self.data = data
        self.initUI()

    def initUI(self):
        font = QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.setFont(font)
        self.table_view = CustomTableView()
        self.table_view.loadData(self.header, self.data)

        layout = QGridLayout()
        layout.addWidget(self.table_view)
        self.setLayout(layout)

