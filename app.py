# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import random
import math
#import unittest
r = 64  #2^6

def inverznyEuklid(a, m):
    a = int(a)
    m = int(m)
    m0 = m
    y = 0
    x = 1

    if int(m) == 1:
        return 0

    while int(a) > 1:
        q = a // int(m)
        t = m
        m = a % int(m)
        a = t
        t = y

        y = x-q*y
        x = t

    if x < 0:
        x = x+m0

    return x

def convertToMontgomery(x, n):
    #r = 64  # 2^6
    res = (int(x)*int(r)) % int(n)
    result = str(res)
    returnString = (
        f"<span style=\"font-size:20px\">x: {x}<br>n: {n}<br>result: {result}</span>"
    )
    return returnString


def convertFromMontgomery(x, n):
    invR = inverznyEuklid(r, n)
    res = (int(x)*int(invR)) % int(n)
    result = str(res)
    returnString = (
        f"<span style=\"font-size:20px\">x: {x}<br>n: {n}<br>result: {result}</span>"
    )
    return returnString


def openUnfilledPrompt():
    msg = QMessageBox()
    msg.setWindowTitle("Unfilled fields")
    msg.setIcon(QMessageBox.Warning)
    msg.setText('''
    <span style=\"font-size:25px\">Please, fill both fields <i><b>x</i></b> and <i><b>N</i></b><span>
    ''')
    msg.exec_()


def executeConversion():
    x = ui.xInput.text()
    n = ui.nInput.text()
    if (len(n).__eq__(0) or len(x).__eq__(0)):
        openUnfilledPrompt()
        return
    if (ui.radioDecToMon.isChecked()):
        result = convertToMontgomery(x, n)
    else:
        result = convertFromMontgomery(x, n)
    ui.output.setText(result)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(844, 552)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.xInput = QtWidgets.QLineEdit(self.centralwidget)
        self.xInput.setObjectName("xInput")
        self.horizontalLayout_2.addWidget(self.xInput)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.nInput = QtWidgets.QLineEdit(self.centralwidget)
        self.nInput.setObjectName("nInput")
        self.horizontalLayout.addWidget(self.nInput)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioMonToDec = QtWidgets.QRadioButton(self.centralwidget)
        self.radioMonToDec.setObjectName("radioMonToDec")
        self.radioMonToDec.setChecked(True)
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioMonToDec)
        self.horizontalLayout_4.addWidget(self.radioMonToDec)
        self.radioDecToMon = QtWidgets.QRadioButton(self.centralwidget)
        self.radioDecToMon.setObjectName("radioDecToMon")
        self.buttonGroup.addButton(self.radioDecToMon)
        self.horizontalLayout_4.addWidget(self.radioDecToMon)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.execButton = QtWidgets.QPushButton(self.centralwidget)
        self.execButton.setObjectName("execButton")
        self.execButton.clicked.connect(executeConversion)
        self.gridLayout.addWidget(self.execButton, 2, 0, 1, 1)
        self.output = QtWidgets.QTextBrowser(self.centralwidget)
        self.output.setObjectName("output")
        self.gridLayout.addWidget(self.output, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionl = QtWidgets.QAction(MainWindow)
        self.actionl.setObjectName("actionl")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Montgomery Representation Converter"))
        self.label.setText(_translate("MainWindow", "x:"))
        self.label_2.setText(_translate("MainWindow", "N:"))
        self.radioMonToDec.setText(
            _translate("MainWindow", "Montgomery to Decimal"))
        self.radioDecToMon.setText(
            _translate("MainWindow", "Decimal to Montgomery"))
        self.execButton.setText(_translate("MainWindow", "Execute conversion"))
        self.actionl.setText(_translate("MainWindow", "l;"))


# class MontgomeryReducerTest(unittest.TestCase):
#
#     def test_basic(self):
#         for _ in range(3000):
#             bitlen = random.randint(2, 100)
#             mod = random.randrange(1 << bitlen, 2 << bitlen) | 1  # Force it to be odd
#             mr = MontgomeryReducer(mod)
#
#             for _ in range(100):
#                 x = random.randrange(0, mod)
#                 y = random.randrange(0, mod)
#                 u = mr.convert_in(x)
#                 v = mr.convert_in(y)
#                 w = mr.multiply(u, v)
#                 if mr.convert_out(w) != x * y % mod:
#                     raise AssertionError()
#
#             for _ in range(10):
#                 x = random.randrange(0, mod)
#                 y = random.randrange(0, mod)
#                 u = mr.convert_in(x)
#                 v = mr.pow(u, y)
#                 if mr.convert_out(v) != pow(x, y, mod):
#                     raise AssertionError()


# class MontgomeryReducer:
#
#     def __init__(self, mod):
#         # Modulus
#         if mod < 3 or mod % 2 == 0:
#             raise ValueError("Modulus must be an odd number at least 3")
#         self.modulus = mod
#
#         # Reducer
#         self.reducerbits = (mod.bit_length() // 8 + 1) * 8  # This is a multiple of 8
#         self.reducer = 1 << self.reducerbits  # This is a power of 256
#         self.mask = self.reducer - 1
#         assert self.reducer > mod and math.gcd(self.reducer, mod) == 1
#
#         # Other computed numbers
#         self.reciprocal = MontgomeryReducer.reciprocal_mod(self.reducer % mod, mod)
#         self.factor = (self.reducer * self.reciprocal - 1) // mod
#         self.convertedone = self.reducer % mod
#
#     # The range of x is unlimited
#     def convert_in(self, x):
#         return (x << self.reducerbits) % self.modulus
#
#     # The range of x is unlimited
#     def convert_out(self, x):
#         return (x * self.reciprocal) % self.modulus
#
#     # Inputs and output are in Montgomery form and in the range [0, modulus)
#     def multiply(self, x, y):
#         mod = self.modulus
#         assert 0 <= x < mod and 0 <= y < mod
#         product = x * y
#         temp = ((product & self.mask) * self.factor) & self.mask
#         reduced = (product + temp * mod) >> self.reducerbits
#         result = reduced if (reduced < mod) else (reduced - mod)
#         assert 0 <= result < mod
#         return result
#
#     # Input x (base) and output (power) are in Montgomery form and in the range [0, modulus); input y (exponent) is in standard form
#     def pow(self, x, y):
#         assert 0 <= x < self.modulus
#         if y < 0:
#             raise ValueError("Negative exponent")
#         z = self.convertedone
#         while y != 0:
#             if y & 1 != 0:
#                 z = self.multiply(z, x)
#             x = self.multiply(x, x)
#             y >>= 1
#         return z
#
#     @staticmethod
#     def reciprocal_mod(x, mod):
#         # Based on a simplification of the extended Euclidean algorithm
#         assert mod > 0 and 0 <= x < mod
#         y = x
#         x = mod
#         a = 0
#         b = 1
#         while y != 0:
#             a, b = b, a - x // y * b
#             x, y = y, x % y
#         if x == 1:
#             return a % mod
#         else:
#             raise ValueError("Reciprocal does not exist")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #unittest.main()
    #print(pow(200, 18, 37))
    sys.exit(app.exec_())