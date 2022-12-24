# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMainWindow, QApplication
from lab3 import ui_MainWindow
from db import DatabaseConnection


class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = ui_MainWindow()
        self.ui.setupUi(self)

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.ui.onClose()
        super(AppWindow, self).closeEvent(a0)
        

if __name__ == "__main__":
    app = QApplication([])
    win = AppWindow()
    win.show()
    sys.exit(app.exec_())
