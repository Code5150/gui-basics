from PyQt5.QtWidgets import *
import sys


class MainWindow(QMainWindow): # главное окно
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.edit = None
        self.button = None
        self.lbl = None
        self.setupUi()
        
    def setupUi(self):
        self.setWindowTitle("Hello, world") # заголовок окна
        self.move(300, 300) # положение окна
        self.resize(200, 200) # размер окна
        self.lbl = QLabel('Hello, world!!!', self)
        self.lbl.move(30, 30)
        self.edit = QLineEdit('Hello, world!!!', self)
        self.edit.move(30, 60)
        self.button = QPushButton('Изменить текст', self)
        self.button.move(30, 90)
        self.button.clicked.connect(self._changeLabel)

    def _changeLabel(self):
        self.lbl.setText(self.edit.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
