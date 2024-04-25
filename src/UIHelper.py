from PyQt5.QtCore import QTimer
from TDCommon import LocalConfig


class WindowResizeHelper:
    def __init__(self, parent_widget):
        self.parent_widget = parent_widget
        self.resize_timer = QTimer(parent_widget)
        self._cfg = LocalConfig()
        self.resize()
        self.start_monitoring()

    def resize(self):
        sizes = self._cfg.get_values('window_size')
        if sizes:
            self.parent_widget.resize(int(sizes['width']), int(sizes['height']))

    def start_monitoring(self):
        self.resize_timer.setSingleShot(True)
        self.resize_timer.timeout.connect(self.handle_resize)
        self.parent_widget.resizeEvent = self.on_resize

    def on_resize(self, event):
        self.resize_timer.stop()
        self.resize_timer.start(500)

    def handle_resize(self):
        new_size = self.parent_widget.size()
        self._cfg.set_values(
            "window_size", {"width": new_size.width(), "height": new_size.height()}
        )