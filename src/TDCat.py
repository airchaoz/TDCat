from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

import sys

from TDCatUI import Ui_TDCat
from DataShow import DataWidget
from UIHelper import WindowResizeHelper
from SqlExec import SqlExec
from ConnectionManager import ConnectionManager
import resources_rc


class MyApp(QMainWindow, Ui_TDCat):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.connect_info: dict = dict()
        self.db_viewer = None
        self.query_dict = dict()
        self.exist_conn = set()
        self.conn_mgr = ConnectionManager(self)

        self.new_query_action.triggered.connect(self.new_query)

        self.setWindowIcon(QIcon(":icon/tdengine.png"))
        self.resize_monitor = WindowResizeHelper(self)

    def display_query_results(self, fields, data, obj):
        page_size = obj.query_pages()
        widget = DataWidget(obj, fields, data, page_size)
        widget.goto_page.connect(self.query_page)
        index = self.table_tab.addTab(widget, obj.table_name)
        self.table_tab.setCurrentIndex(index)
        self.query_dict[obj] = widget

    def query_page(self, event):
        obj, page = event
        fields, data = obj.query(page - 1)
        self.query_dict[obj].load_data(fields, data)

    def new_query(self):
        widget = SqlExec()
        widget.goto_page.connect(self.query_page)
        index = self.table_tab.addTab(widget, "新建查询")
        self.table_tab.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MyApp()
    ui.show()
    sys.exit(app.exec_())
