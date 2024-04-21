from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QStandardItemModel, QIcon

import sys
import json

from TDCatUI import Ui_TDCat
from NewConn import NewConn
from TDModel import TDConnect
from ItemModel import ConnItem
from QueryWidget import QueryWidget
import resources_rc


class MyApp(QMainWindow, Ui_TDCat):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.connect_info: dict = dict()
        self.new_conn_ui = None
        self.db_viewer = None
        self.query_dict = dict()

        self.load_setting()
        self.init_db_viewer()

        self.new_conn_action.triggered.connect(self.new_connect)
        self.tree_viewer.header().setVisible(False)

        self.setWindowIcon(QIcon(':icon/tdengine.png'))

    def load_setting(self):
        setting_obj = QSettings('./config.ini', QSettings.IniFormat)
        setting = setting_obj.value('DBSetting', defaultValue='{}')
        setting = json.loads(setting)
        for k, v in setting.items():
            params = json.loads(v)
            self.connect_info[k] = TDConnect(**params)

    def dump_setting(self):
        setting = dict()

        for k, v in self.connect_info.items():
            setting[k] = v.config_dump()

        setting = json.dumps(setting)
        setting_obj = QSettings('./config.ini', QSettings.IniFormat)
        setting_obj.setValue('DBSetting', setting)

    def new_connect(self):
        if not self.new_conn_ui:
            self.new_connect_ui = NewConn(self)
            self.new_connect_ui.show()

        self.init_db_viewer()

    def init_db_viewer(self):
        if len(self.connect_info) == 0:
            return

        model = QStandardItemModel()
        self.tree_viewer.setModel(model)
        for k, v in self.connect_info.items():
            item = ConnItem(k, v, self)
            model.appendRow(item)

    def display_query_results(self, fields, data, obj):

        if obj in self.query_dict:
            return

        widget = QueryWidget(fields, data)
        index = self.table_tab.addTab(widget, obj.table_name)
        self.table_tab.setCurrentIndex(index)
        self.query_dict[obj] = widget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MyApp()
    ui.show()
    sys.exit(app.exec_())
