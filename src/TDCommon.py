from PyQt5.QtCore import QSettings

PAGE_SIZE = 1000


class Singleton:
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]

@Singleton
class LocalConfig:

    def __init__(self):
        self._setting = QSettings("./config.ini", QSettings.IniFormat)

    def set_value(self, key, value):
        self._setting.setValue(key, value)

    def set_values(self, key, values):
        self._setting.beginGroup(key)
        for k, v in values.items():
            self._setting.setValue(k, v)
        self._setting.endGroup()

    def get_value(self, key):
        return self._setting.value(key)

    def get_values(self, group):
        group_settings = {}
        self._setting.beginGroup(group)
        keys = self._setting.childKeys()
        for key in keys:
            value = self._setting.value(key)
            group_settings[key] = value

        self._setting.endGroup()
        return group_settings

    def get_groups(self):
        return self._setting.childGroups()

    def remove_group(self, group):
        self._setting.beginGroup(group)
        self._setting.remove('')
        self._setting.endGroup()