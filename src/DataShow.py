from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from DataShowUI import Ui_DataShow
from PyQt5.QtCore import pyqtSignal

class DataWidget(QWidget, Ui_DataShow):
    goto_page = pyqtSignal(list)

    def __init__(self, table_obj, header, data, max_page=1):
        super().__init__()
        self.table_obj = table_obj
        self.header = header
        self.data = data
        self.setupUi(self)
        self.tableView.loadData(self.header, self.data)

        self.page = 1
        self.max_page = max_page
        self.page_entry.setText(str(self.page))
        self.init_events()

    def init_events(self):
        self.first_page_btn.clicked.connect(self.first_page)
        self.pre_page_btn.clicked.connect(self.prev_page)
        self.next_page_btn.clicked.connect(self.next_page)
        self.last_page_btn.clicked.connect(self.last_page)

    def first_page(self):
        self.page = 1
        self.goto_page.emit([self.table_obj, self.page])

    def last_page(self):
        self.page = self.max_page
        self.goto_page.emit([self.table_obj, self.page])

    def next_page(self):
        if self.page < self.max_page:
            self.page += 1
            self.goto_page.emit([self.table_obj, self.page])

    def prev_page(self):
        if self.page > 1:
            self.page -= 1
            self.goto_page.emit([self.table_obj, self.page])

    def load_data(self, header, data):
        self.tableView.loadData(header, data)
        self.page_entry.setText(str(self.page))


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    header = ["列1", "列2", "列3"]
    data = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    app = QApplication(sys.argv)
    widget = DataWidget(header, data)
    widget.show()
    sys.exit(app.exec_())