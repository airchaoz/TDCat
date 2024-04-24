from PyQt5.QtWidgets import QWidget, QTabWidget, QPushButton, QTabBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import resources_rc


class CustomTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.close_buttons = {}
        self.titles = list()

    def addTab(self, widget, title):
        if title in self.titles:
            return self.titles.index(title)
        index = super().addTab(widget, title)
        self.setTabToolTip(index, title)
        self.titles.append(title)
        if index > 0:
            close_button = CloseButton(self.tabBar(), self, title)
            self.close_buttons[title] = close_button
            self.tabBar().setTabButton(index, QTabBar.RightSide, close_button)
        return index

    def delete_tab(self, title):
        if title in self.close_buttons:
            del self.close_buttons[title]  # 删除关闭按钮引用
        index = self.titles.index(title)
        del self.titles[index]
        super().removeTab(index)  # 删除选项卡


class CloseButton(QPushButton):
    def __init__(self, tab_bar, tab_widget, title):
        super().__init__()
        self.tab_bar = tab_bar  # 保存对 QTabBar 的引用
        self.tab_widget = tab_widget  # 保存对 CustomTabWidget 的引用
        self.title = title

        self.clicked.connect(self.close_tab)
        self.setIcon(QIcon(":tiny/cancel.png"))  # 设置关闭按钮图标
        self.setIconSize(QSize(12, 12))  # 设置图标大小
        self.setFixedSize(QSize(25, 25))

        self.setStyleSheet("""
            QPushButton {
                border: none;
            }
            QPushButton:hover {
                background-color: #F0F0F0;
            }
        """)

    def close_tab(self):
        self.tab_widget.delete_tab(self.title)
