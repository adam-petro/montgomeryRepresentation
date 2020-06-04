# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys


def convertToMontgomery(x, n):

    result = str(int(x) * int(n))
    returnString = (
        f"<span style=\"font-size:20px\">x: {x}<br>n: {n}<br>result: {result}</span>"
    )
    return returnString


def convertFromMontgomery(x, n):
    result = str(int(x) + int(n))
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())