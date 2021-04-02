from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import sys
from calc import Ui_MainWindow


class MyCalc(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.zero.clicked.connect(self.btn_press)
        self.one.clicked.connect(self.btn_press)
        self.two.clicked.connect(self.btn_press)
        self.three.clicked.connect(self.btn_press)
        self.four.clicked.connect(self.btn_press)
        self.five.clicked.connect(self.btn_press)
        self.six.clicked.connect(self.btn_press)
        self.Seven.clicked.connect(self.btn_press)
        self.eight.clicked.connect(self.btn_press)
        self.nine.clicked.connect(self.btn_press)
        self.minus.clicked.connect(self.btn_press)
        self.plus.clicked.connect(self.btn_press)
        self.mult.clicked.connect(self.btn_press)
        self.divide.clicked.connect(self.btn_press)
        self.equ.clicked.connect(self.equ_press)
        self.percent.clicked.connect(self.perc)
        self.point.clicked.connect(self.point_press)
        self.clear.clicked.connect(self.clearone_press)
        self.AllCrear.clicked.connect(self.clear_press)

    def btn_press(self):
        button = self.sender()
        k = self.TextWindow.text()
        if k == '0':
            k = ''
        New_TextWindow = k + button.text()
        self.TextWindow.setText(New_TextWindow)

    def point_press(self):
        self.TextWindow.setText(self.TextWindow.text() + '.')

    def perc(self):
        self.TextWindow.setText('Buy access ')

    def equ_press(self):
        bnt = self.TextWindow.text()
        try:
            res = str(eval(bnt))
        except:
            res = 'err'
        self.TextWindow.setText(res)

    def clear_press(self):
        self.TextWindow.setText('')

    def clearone_press(self):
        self.TextWindow.setText('Buy access ')


app = QtWidgets.QApplication(sys.argv)
calc = MyCalc()
sys.exit(app.exec_())
