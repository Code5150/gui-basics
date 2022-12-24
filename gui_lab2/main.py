import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import *

from CurrencyEdit import CurrencyEdit

CURRENCY_COEF = 65


class MainWindow(QMainWindow):  # главное окно

    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = None
        self.roubleEdit = None
        self.dollarEdit = None
        self.oilEdit = None
        self.roubleLabel = None
        self.dollarLabel = None
        self.oilLabel = None
        self.roubleChange = pyqtSignal()
        self.dollarChange = pyqtSignal()
        self.setupUi()
        self.prevOilPrice = 80

    def setupUi(self):
        onlyNumberVal = QDoubleValidator()
        self.setWindowTitle("Курсы и котировки")  # заголовок окна
        self.move(300, 300)  # положение окна
        self.resize(300, 200)  # размер окна
        self.oilLabel = QLabel('Нефть', self)
        self.oilLabel.move(30, 30)
        self.dollarLabel = QLabel('Доллар', self)
        self.dollarLabel.move(30, 60)
        self.roubleLabel = QLabel('Рубль', self)
        self.roubleLabel.move(30, 90)
        self.oilEdit = QLineEdit('80', self)
        self.oilEdit.move(150, 30)
        self.oilEdit.setValidator(onlyNumberVal)
        self.dollarEdit = CurrencyEdit('1', self)
        self.dollarEdit.move(150, 60)
        self.roubleEdit = CurrencyEdit('65', self)
        self.roubleEdit.move(150, 90)
        self.button = QPushButton('Анализ', self)
        self.button.move(60, 130)
        self.button.clicked.connect(self._analyze)

    def _analyze(self):
        newOilPrice = float(self.oilEdit.text())
        oilPriceRatio = newOilPrice - self.prevOilPrice

        if oilPriceRatio < 0:
            dollarPrice = float(self.dollarEdit.text())
            dollarPrice = dollarPrice - oilPriceRatio * 2
            self.dollarEdit.courseChanged.emit(dollarPrice, self.roubleEdit, CURRENCY_COEF)
        if oilPriceRatio > 0:
            roublePrice = float(self.roubleEdit.text())
            roublePrice = roublePrice + oilPriceRatio * 2
            self.roubleEdit.courseChanged.emit(roublePrice, self.dollarEdit, 1/CURRENCY_COEF)

        self.prevOilPrice = newOilPrice


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
