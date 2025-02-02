import os

from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QDialog
from PyQt5.QtCore import Qt

from formMenu2 import MainWindow

class Ui_Dialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.setObjectName("Dialog")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 1200, 750))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("LaumchMen.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(1200, 750))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(340, 130, 521, 511))
        self.label.setStyleSheet("background-color: rgb(43, 17, 18, 120);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(380, 300, 441, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(142, 186, 198);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(142, 186, 198);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(97, 37, 26, 165);\n"
"color: rgb(142, 186, 198);\n"
"border: none;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(97, 37, 26, 165);\n"
"color: rgb(142, 186, 198);\n"
"border: none;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(450, 150, 311, 71))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(184, 224, 249);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(410, 230, 401, 71))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(238, 187, 96);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 510, 161, 23))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777214, 16777215))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(11)
        font.setUnderline(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: transparent;\n"
"color: rgb(247, 214, 137);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 570, 121, 61))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(13)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(42, 14, 13, 200);\n"
"color: rgb(247, 214, 137);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(5, 680, 64, 64))
        self.pushButton_4.setStyleSheet("background-color: transparent;")
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("VyklRegistr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(64, 64))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(340, 690, 521, 20))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 255, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_6.hide()

        self.addFunctons()
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def addFunctons(self):
        self.pushButton_4.clicked.connect(self.QuitPK)
        self.pushButton_2.clicked.connect(self.RegUser)
        self.pushButton_3.clicked.connect(self.VxodUser)
        self.pushButton_3.setAutoDefault(True)  # click on <Enter>
        self.lineEdit_2.returnPressed.connect(self.pushButton_3.click)  # click on <Enter>
        self.lineEdit_3.returnPressed.connect(self.pushButton_3.click)  # click on <Enter>

    def RegUser(self):
        login = self.lineEdit_3.text()
        password = self.lineEdit_2.text()
        if login == "" or password == "":
            print("ошибка")
        else:
            if f'{login}.txt' in os.listdir():
                self.label_6.setStyleSheet("color: rgb(255, 0, 0);")
                self.label_6.setText("Пользователь с таким логином уже существует, попробуйте ещё раз")
                self.label_6.show()
            else:
                files = open(f'{login}.txt', 'w', encoding='utf-8')
                files.write(password)
                files.close()
                self.lineEdit_3.setText("")
                self.lineEdit_2.setText("")
                self.label_6.setStyleSheet("color: rgb(0, 255, 0);")
                self.label_6.setText("Вы успешно зарегистрировались")
                self.label_6.show()


    def VxodUser(self):
        login = self.lineEdit_3.text()
        if f'{login}.txt' in os.listdir():
            password = self.lineEdit_2.text()
            files = open(f'{login}.txt', 'r', encoding='utf-8')
            pasUs = files.readline()
            pasUs = pasUs.replace("\n", "")
            if password == pasUs:
                filesL = open("baza.txt", 'a', encoding='utf-8')
                filesL.write(login+"\n")
                files.close()
                filesL.close()
                self.animation = QPropertyAnimation(self, b"windowOpacity")
                self.animation.setDuration(500)  # Длительность анимации в миллисекундах
                self.animation.setEndValue(0)  # Конечное значение прозрачности (0 - полностью прозрачное окно)
                self.animation.start()
                self.animation.finished.connect(self.MenGo)

            else:
                self.label_6.setStyleSheet("color: rgb(255, 0, 0);")
                self.label_6.setText("Неправильный логин или пароль, попробуйте ещё раз")
                self.label_6.show()
        else:
            self.label_6.setStyleSheet("color: rgb(255, 0, 0);")
            self.label_6.setText("Такого пользователя нет в базе")
            self.label_6.show()

    def MenGo(self):
        self.close()
        self.mainW = MainWindow()
        self.mainW.show()

    def QuitPK(self):
        os.kill()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Password:"))
        self.label_3.setText(_translate("Dialog", "Login:"))
        self.label_4.setText(_translate("Dialog", "PlanetoKard"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p>Добро пожаловать в PlanetoKard!?</p><p>Вводите свои даннные:</p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "Зарегистрироваться"))
        self.pushButton_3.setText(_translate("Dialog", "Вход"))
        self.label_6.setText(_translate("Dialog", "Вы успешно зарегистрировались"))


if __name__ == "__main__":
    app = QApplication([])

    w = Ui_Dialog()
    w.resize(1200, 750)
    w.show()

    app.exec()