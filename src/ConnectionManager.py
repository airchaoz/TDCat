from NewConn import NewConn
from TDModel import TDConnect
from TDCommon import LocalConfig
from PyQt5.QtGui import QStandardItemModel
from ItemModel import ConnItem

class ConnectionManager():

    def __init__(self, parent=None):
        self.parent = parent
        self.connect_info = {}
        self._cfg = LocalConfig()

        self.parent.new_conn_action.triggered.connect(self.new_connect)
        self.parent.conn_action.triggered.connect(self.new_connect)
        self.exist_conn  = set()

        self.start()

    def load_setting(self):
        groups = self._cfg.get_groups()
        for group in groups:
            if group.startswith("DBConnect-"):
                self.connect_info[group[10:]] = TDConnect(**self._cfg.get_values(group))

    def dump_setting(self):
        for k, v in self.connect_info.items():
            cfg = v.config()
            self._cfg.set_values(f"DBConnect-{k}", cfg)

    def new_connect(self):
        new_connect_ui = NewConn(parent=self.parent)
        new_connect_ui.checkout_signal.connect(self.add_connect)
        new_connect_ui.show()

    def add_connect(self, params):
        conn_name = params[0]
        self.connect_info[conn_name] = TDConnect(*params)
        self.dump_setting()
        self.refresh_db_viewer()

    def edit_connect(self, conn_name):
        def del_connect():
            self.del_connect(conn_name)

        if conn_name not in self.connect_info.keys():
            return

        params = self.connect_info[conn_name]
        new_connect_ui = NewConn(*(params.get_params()), parent=self.parent)
        new_connect_ui.checkout_signal.connect(del_connect)
        new_connect_ui.checkout_signal.connect(self.add_connect)
        new_connect_ui.show()

    def del_connect(self, conn_name):
        if conn_name not in self.connect_info.keys():
            return
        del self.connect_info[conn_name]
        model = self.parent.tree_viewer.model()
        if model:
            for i in range(model.rowCount()):
                item = model.item(i)
                if item and item.name == conn_name:
                    model.removeRow(i)
        self.exist_conn.remove(conn_name)
        self._cfg.remove_group(f"DBConnect-{conn_name}")
        self.refresh_db_viewer()

    def start(self):
        self.load_setting()
        self.refresh_db_viewer()

    def refresh_db_viewer(self):
        if len(self.connect_info) == 0:
            return

        model = self.parent.tree_viewer.model()
        if not model:
            model = QStandardItemModel()
            self.parent.tree_viewer.setModel(model)

        for k, v in self.connect_info.items():
            item = ConnItem(k, v, parent=self.parent)
            if k not in self.exist_conn:
                self.exist_conn.add(k)
                model.appendRow(item)