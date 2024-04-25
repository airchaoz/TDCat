from PyQt5.QtWidgets import QTableView
from PyQt5.QtCore import Qt, QAbstractTableModel


class CustomTableModel(QAbstractTableModel):
    def __init__(self, data, header):
        super().__init__()
        self._data = data
        self._header = header

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        if self.rowCount() > 0:
            return len(self._data[0])
        return 0

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            return str(self._data[index.row()][index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal and 0 <= section < len(self._header):
                return str(self._header[section])
            elif orientation == Qt.Vertical:
                return str(section + 1)
        return None


class CustomTableView(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = None

        # 设置每个单元格的大小
        self.verticalHeader().setDefaultSectionSize(5)  # 设置行高
        self.horizontalHeader().setDefaultSectionSize(100)  # 设置列宽
        self.verticalHeader().setVisible(False)

    def loadData(self, header, data):
        self.model = CustomTableModel(data, header)
        self.setModel(self.model)

    def clear(self):
        if self.model:
            self.model.removeRows(0, self.model.rowCount())
            self.model.removeColumns(0, self.model.columnCount())