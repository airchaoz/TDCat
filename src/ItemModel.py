from PyQt5.QtGui import QStandardItem, QIcon
from PyQt5.QtWidgets import QMessageBox, QMenu, QAction
from TDModel import TCConnectException, TDConnect, TDDBModel, TDTableModel
import resources_rc
from PyQt5.QtCore import pyqtSignal


class CustomItem(QStandardItem):
    def __init__(self, text="", parent=None):
        super().__init__(text)
        self.parent = parent

    def mouseDoubleClickEvent(self):
        if not self.parent:
            return

        model = self.parent.tree_viewer.model()
        index = model.indexFromItem(self)
        if self.parent.tree_viewer.isExpanded(index):
            self.parent.tree_viewer.collapse(index)
        else:
            self.parent.tree_viewer.expand(index)


class TableItem(CustomItem):
    def __init__(self, text="", table: TDTableModel = None, parent=None):
        super().__init__(text)
        self.table_name = text
        self.table = table
        self.parent = parent
        self.setIcon(QIcon(":icon/table.png"))

    def mouseDoubleClickEvent(self):
        fields, data = self.table.query()
        self.parent.display_query_results(fields, data, self.table)


class StableItem(CustomItem):
    def __init__(self, text="", table: TDTableModel = None, parent=None):
        super().__init__(text)
        self.table_name = text
        self.table = table
        self.setIcon(QIcon(":icon/table.png"))

    def mouseDoubleClickEvent(self):
        pass


class CategoryItem(CustomItem):
    def __init__(self, text="", objs: list = None, parent=None):
        super().__init__(text)
        self.table_name = text
        self.objs = objs

        self.appendRows(objs)
        self.setIcon(QIcon(":icon/table.png"))

    def mouseDoubleClickEvent(self):
        super().mouseDoubleClickEvent()


class DBItem(CustomItem):
    def __init__(self, text="", db: TDDBModel = None, parent=None):
        super().__init__(text, parent)
        self.db_name = text
        self.db = db
        self.parent = parent

        self.table = None
        self.stable = None

        self.init_flat = False
        self.setIcon(QIcon(":icon/database_un.png"))

    def mouseDoubleClickEvent(self):
        super().mouseDoubleClickEvent()

        if self.init_flat:
            return

        self.db.init()
        table = []
        stable = []
        for k in sorted(self.db.table_dict.keys()):
            v = self.db.table_dict[k]
            table.append(TableItem(k, v, self.parent))
        for k in sorted(self.db.stable_dict.keys()):
            v = self.db.stable_dict[k]
            stable.append(StableItem(k, v, self.parent))
        self.table = CategoryItem("表", table, self.parent)
        self.stable = CategoryItem("超表", stable, self.parent)
        self.appendRows([self.table, self.stable])

        self.init_flat = True
        self.setIcon(QIcon(":icon/database.png"))


class ConnItem(CustomItem):
    del_signal = pyqtSignal(str)

    def __init__(self, text="", conn: TDConnect = None, parent=None):
        super().__init__(text, parent)
        self.name = text
        self.conn = conn
        self.parent = parent

        self.init_flat = False
        self.setIcon(QIcon(":icon/tdengine_un.png"))

    def mouseDoubleClickEvent(self):
        super().mouseDoubleClickEvent()

        if self.init_flat:
            return

        try:
            self.conn.connect_init()
        except TCConnectException as e:
            QMessageBox.warning(None, "连接错误", str(e))
            return

        self.conn.db_init()

        for k in sorted(self.conn.db_dict.keys()):
            v = self.conn.db_dict[k]
            item = DBItem(k, v, self)
            self.appendRow(item)

        self.init_flat = True
        self.setIcon(QIcon(":icon/tdengine.png"))

    def contextMenuEvent(self, event, host):
        # 创建上下文菜单
        menu = QMenu(host)
        edit_action = QAction("修改配置", host)
        refresh_action = QAction("刷新连接", host)
        del_action = QAction("删除配置", host)
        menu.addAction(edit_action)
        menu.addAction(refresh_action)
        menu.addAction(del_action)

        # 点击事件
        # edit_action.triggered.connect(lambda: self.edit_connect())

        del_action.triggered.connect(lambda: self.parent.del_connect(self.name))

        # 显示上下文菜单
        menu.exec_(host.mapToGlobal(event.pos()))

