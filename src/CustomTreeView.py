from PyQt5.QtWidgets import QTreeView


class CustomTreeView(QTreeView):

    def __init__(self, parent=None):
        super(CustomTreeView, self).__init__(parent)

    def mouseDoubleClickEvent(self, event):
        index = self.indexAt(event.pos())
        if index.isValid():
            item = self.model().itemFromIndex(index)
            if item is not None:
                item.mouseDoubleClickEvent()

    def contextMenuEvent(self, event):
        index = self.indexAt(event.pos())
        if index.isValid():
            item = self.model().itemFromIndex(index)
            if item is not None:
                item.contextMenuEvent(event, self)