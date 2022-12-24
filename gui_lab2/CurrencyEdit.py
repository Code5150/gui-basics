import typing

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import *


class CurrencyEdit(QLineEdit):

    courseChanged = pyqtSignal(float, QLineEdit, float)

    def __init__(self, *__args):
        onlyNumberVal = QDoubleValidator()
        super().__init__(*__args)
        self.setValidator(onlyNumberVal)
        self.courseChanged.connect(self.change_currency)

    def change_currency(self, value, source, coef):
        source.setText(str(round(value*coef, 2)))
