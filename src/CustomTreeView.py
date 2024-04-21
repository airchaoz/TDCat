from PyQt5.QtWidgets import QTreeView


class CustomTreeView(QTreeView):

    def __init__(self, parent=None):
        super(CustomTreeView, self).__init__(parent)

    def mouseDoubleClickEvent(self, event):
        index = self.indexAt(event.pos())  # 获取双击位置的索引
        if index.isValid():
            item = self.model().itemFromIndex(index)  # 获取对应的 QStandardItem 对象
            if item is not None:
                item.mouseDoubleClickEvent()