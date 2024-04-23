from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QStandardItemModel, QIcon

import sys
import json

from TDCatUI import Ui_TDCat
from NewConn import NewConn
from TDModel import TDConnect
from ItemModel import ConnItem
from DataShow import DataWidget
import resources_rc


class MyApp(QMainWindow, Ui_TDCat):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.connect_info: dict = dict()
        self.db_viewer = None
        self.query_dict = dict()
        self.exist_conn = set()

        self.load_setting()
        self.init_db_viewer()

        self.new_conn_action.triggered.connect(self.new_connect)
        self.conn_action.triggered.connect(self.new_connect)
        self.tree_viewer.header().setVisible(False)

        self.setWindowIcon(QIcon(":icon/tdengine.png"))

    def load_setting(self):
        setting_obj = QSettings("./config.ini", QSettings.IniFormat)
        setting = setting_obj.value("DBSetting", defaultValue="{}")
        setting = json.loads(setting)
        for k, v in setting.items():
            params = json.loads(v)
            self.connect_info[k] = TDConnect(**params)

    def dump_setting(self):
        setting = dict()

        for k, v in self.connect_info.items():
            setting[k] = v.config_dump()

        setting = json.dumps(setting)
        setting_obj = QSettings("./config.ini", QSettings.IniFormat)
        setting_obj.setValue("DBSetting", setting)

    def new_connect(self):
        new_connect_ui = NewConn(parent=self)
        new_connect_ui.checkout_signal.connect(self.add_connect)
        new_connect_ui.show()

    def add_connect(self, params):
        conn_name = params[0]
        self.connect_info[conn_name] = TDConnect(*params)
        self.dump_setting()
        self.init_db_viewer()

    def edit_connect(self, conn_name):
        def del_connect():
            self.del_connect(conn_name)

        if conn_name not in self.connect_info.keys():
            return

        params = self.connect_info[conn_name]
        new_connect_ui = NewConn(*(params.get_params()), parent=self)
        new_connect_ui.checkout_signal.connect(del_connect)
        new_connect_ui.checkout_signal.connect(self.add_connect)
        new_connect_ui.show()

    def del_connect(self, conn_name):
        if conn_name not in self.connect_info.keys():
            return
        del self.connect_info[conn_name]
        model = self.tree_viewer.model()
        if model:
            for i in range(model.rowCount()):
                item = model.item(i)
                if item and item.name == conn_name:
                    model.removeRow(i)
        self.exist_conn.remove(conn_name)
        self.dump_setting()
        self.init_db_viewer()

    def init_db_viewer(self):
        if len(self.connect_info) == 0:
            return

        model = self.tree_viewer.model()
        if not model:
            model = QStandardItemModel()
            self.tree_viewer.setModel(model)

        for k, v in self.connect_info.items():
            item = ConnItem(k, v, parent=self)
            if k not in self.exist_conn:
                self.exist_conn.add(k)
                model.appendRow(item)

    def display_query_results(self, fields, data, obj):
        if obj in self.query_dict:
            return
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MyApp()
    ui.show()
    sys.exit(app.exec_())
