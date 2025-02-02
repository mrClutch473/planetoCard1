import os
import signal
import subprocess

import psutil as psutil
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QDialog
from PyQt5.QtCore import Qt


class Ui_NastrKompForm(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.setObjectName("SettingsKomp1")
        self.resize(361, 271)
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 361, 271))
        self.label_10.setStyleSheet("background-color: rgb(22, 14, 53);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(4, 80, 352, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_25 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_25.setMinimumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(119, 59, 205);\n"
"    color: rgb(255, 142, 163);\n"
"    border: 1px solid rgb(119, 59, 205);    \n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton {\n"
"    color: rgb(255, 142, 163);\n"
"    background-color: transparent;\n"
"    border: 1px solid rgb(119, 59, 205);    \n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_25.setObjectName("pushButton_25")
        self.verticalLayout.addWidget(self.pushButton_25)
        self.pushButton_24 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_24.setMinimumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(119, 59, 205);\n"
"    color: rgb(255, 142, 163);\n"
"    border: 1px solid rgb(119, 59, 205);    \n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton {\n"
"    color: rgb(255, 142, 163);\n"
"    background-color: transparent;\n"
"    border: 1px solid rgb(119, 59, 205);    \n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_24.setObjectName("pushButton_24")
        self.verticalLayout.addWidget(self.pushButton_24)
        self.pushButton_26 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_26.setMinimumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(119, 59, 205);\n"
"    color: rgb(255, 142, 163);\n"
"    border: 1px solid rgb(119, 59, 205);    \n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton {\n"
"    color: rgb(255, 142, 163);\n"
"    background-color: transparent;\n"
"    border: 1px solid rgb(119, 59, 205);    \n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_26.setObjectName("pushButton_26")
        self.verticalLayout.addWidget(self.pushButton_26)
        self.pushButton_27 = QtWidgets.QPushButton(self)
        self.pushButton_27.setGeometry(QtCore.QRect(4, 10, 350, 41))
        self.pushButton_27.setMinimumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(175, 0, 2);\n"
"    color: rgb(206, 161, 70);\n"
"    border: 1px solid rgb(119, 59, 205);    \n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton {\n"
"    background-color: rgb(107, 0, 1);\n"
"    color: rgb(255, 200, 87);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_27.setObjectName("pushButton_27")

        self.ConcidVal = False

        self.addFunction()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def addFunction(self):
        self.pushButton_26.clicked.connect(self.VixodClose)
        self.pushButton_27.clicked.connect(self.ConcidBut)
        self.pushButton_24.clicked.connect(self.ZakrBut)

    def ConcidBut(self):
        self.ConcidVal = True
        self.close()

    def ZakrBut(self):
        self.close()

    def VixodClose(self):
        os.kill()

    def retranslateUi(self, NastrKompForm):
        _translate = QtCore.QCoreApplication.translate
        NastrKompForm.setWindowTitle(_translate("SettingsKomp1", "SettingsKomp1"))
        self.pushButton_25.setText(_translate("NastrKompForm", "Настройки"))
        self.pushButton_24.setText(_translate("NastrKompForm", "Закрыть"))
        self.pushButton_26.setText(_translate("NastrKompForm", "Выход"))
        self.pushButton_27.setText(_translate("NastrKompForm", "Сдаться"))


if __name__ == '__main__':
    app = QApplication([])

    w = Ui_NastrKompForm()
    w.resize(361, 271)
    w.show()

    app.exec()
