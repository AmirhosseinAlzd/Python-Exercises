from math import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from functools import partial
from PySide6.QtGui import *


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("Advanced_calculator.ui")
        self.ui.show()
        self.ui.point.clicked.connect(partial(self.point))
        self.ui.zero.clicked.connect(partial(self.Number_dontcare, 0))
        self.ui.one.clicked.connect(partial(self.Number_dontcare, 1))
        self.ui.two.clicked.connect(partial(self.Number_dontcare, 2))
        self.ui.three.clicked.connect(partial(self.Number_dontcare, 3))
        self.ui.four.clicked.connect(partial(self.Number_dontcare, 4))
        self.ui.five.clicked.connect(partial(self.Number_dontcare, 5))
        self.ui.six.clicked.connect(partial(self.Number_dontcare, 6))
        self.ui.seven.clicked.connect(partial(self.Number_dontcare, 7))
        self.ui.eight.clicked.connect(partial(self.Number_dontcare, 8))
        self.ui.nine.clicked.connect(partial(self.Number_dontcare, 9))
        self.ui.Sum.clicked.connect(partial(self.two_operator, '+'))
        self.ui.Sub.clicked.connect(partial(self.two_operator, '-'))
        self.ui.Mul.clicked.connect(partial(self.two_operator, 'x'))
        self.ui.Div.clicked.connect(partial(self.two_operator, '/'))
        self.ui.Equ.clicked.connect(partial(self.equal))
        self.ui.sin.clicked.connect(partial(self.one_operator, 'sin'))
        self.ui.cos.clicked.connect(partial(self.one_operator, 'cos'))
        self.ui.tan.clicked.connect(partial(self.one_operator, 'tan'))
        self.ui.cot.clicked.connect(partial(self.one_operator, 'cot'))
        self.ui.log.clicked.connect(partial(self.one_operator, 'log'))
        self.ui.sqrt.clicked.connect(partial(self.one_operator, 'sqrt'))
        self.ui.c_btn.clicked.connect(self.reset_screen)

    def Number_dontcare(self, d):
        self.ui.Show_screen.setText(self.ui.Show_screen.text() + str(d))

    def two_operator(self, opr):
            if self.ui.Show_screen.text() != '':
                self.num1 = float(self.ui.Show_screen.text())
                self.ui.Show_screen.setText('')
                self.operator = opr

    def equal(self):
            if self.ui.Show_screen.text() != '':
                self.num2 = float(self.ui.Show_screen.text())

                if self.operator == '+':
                    result = self.num1 + self.num2
                elif self.operator == '-':
                    result = self.num1 - self.num2
                elif self.operator == 'x':
                    result = self.num1 * self.num2
                elif self.operator == '/':
                    result = self.num1 / self.num2

                self.ui.Show_screen.setText(str(result))

    def reset_screen(self):
        self.ui.Show_screen.setText('')

    def point(self):
        if '.' not in self.ui.Show_screen.text() and self.ui.Show_screen.text() != '':
            self.ui.Show_screen.setText(self.ui.Show_screen.text() + '.')

    def one_operator(self, sym):
            if self.ui.Show_screen.text() != '':
                text = radians(float(self.ui.Show_screen.text()))
                if sym == 'sin':
                    result = sin(text)
                elif sym == 'cos':
                    result = cos(text)
                elif sym == 'tan':
                    result = tan(text)
                elif sym == 'cot':
                    result = cos(text) / sin(text)
                elif sym == 'log':
                    result = log(float(self.ui.Show_screen.text()))
                elif sym == 'sqrt':
                    result = sqrt(float(self.ui.Show_screen.text()))

                result = round(result, 6)
                self.ui.Show_screen.setText(str(result))

my_app = QApplication()
Main_window_calculator = Calculator()                # JUST ONE MAIN WINDOW
my_app.exec()
