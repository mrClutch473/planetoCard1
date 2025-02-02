from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from PyQt5.QtCore import Qt, QUrl, pyqtSignal, QPropertyAnimation
from PyQt5.QtMultimedia import QSoundEffect, QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QDialog, QSlider, QGraphicsOpacityEffect
from PyQt5.QtCore import Qt


class Widget(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)


        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 728, 511))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("nastrFon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(728, 511))
        self.pushButton.setObjectName("pushButton")


        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 231, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(16, 24, 37);\n"
                                        "    color: rgb(239, 92, 74);\n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(239, 92, 74);\n"
                                        "    color: rgb(16, 24, 37);\n"
                                        "    border-radius: 10px;\n"
                                        "}")
        self.pushButton_9.setText("Звук")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_10.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(16, 24, 37);\n"
                                         "    color: rgb(239, 92, 74);\n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(239, 92, 74);\n"
                                         "    color: rgb(16, 24, 37);\n"
                                         "    border-radius: 10px;\n"
                                         "}")
        self.pushButton_10.setText("Графика")
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_11.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(16, 24, 37);\n"
                                         "    color: rgb(239, 92, 74);\n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(239, 92, 74);\n"
                                         "    color: rgb(16, 24, 37);\n"
                                         "    border-radius: 10px;\n"
                                         "}")
        self.pushButton_11.setText("Видео")
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_2.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_12.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(16, 24, 37);\n"
                                         "    color: rgb(239, 92, 74);\n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(239, 92, 74);\n"
                                         "    color: rgb(16, 24, 37);\n"
                                         "    border-radius: 10px;\n"
                                         "}")
        self.pushButton_12.setText("Управление")
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_2.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_13.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(16, 24, 37);\n"
                                         "    color: rgb(239, 92, 74);\n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(239, 92, 74);\n"
                                         "    color: rgb(16, 24, 37);\n"
                                         "    border-radius: 10px;\n"
                                         "}")
        self.pushButton_13.setText("Учётная Запись")
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_2.addWidget(self.pushButton_13)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(560, 470, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("color: rgb(255, 171, 160);")
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setText("mrClutch473")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 10, 50, 50))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color: transparent;")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("NastrQuit1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_14 = QtWidgets.QPushButton(self)
        self.pushButton_14.setEnabled(True)
        self.pushButton_14.setGeometry(QtCore.QRect(270, 70, 441, 391))
        self.pushButton_14.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(43, 46, 103);\n"
                                         "border-radius: 10px;\n"
                                         "")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(360, 180, 261, 91))
        self.label_4.setStyleSheet("background-color: rgb(29, 31, 71);\n"
                                   "border-radius: 10px;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(360, 80, 261, 91))
        self.label_5.setStyleSheet("background-color: rgb(29, 31, 71);\n"
                                   "border-radius: 10px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(380, 280, 221, 51))
        self.label_6.setStyleSheet("background-color: rgb(29, 31, 71);\n"
                                   "border-radius: 10px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.radioButton = QtWidgets.QCheckBox(self)
        self.radioButton.setGeometry(QtCore.QRect(400, 290, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: rgb(252, 226, 105);")
        self.radioButton.setObjectName("radioButton")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(380, 340, 221, 51))
        self.label_7.setStyleSheet("background-color: rgb(29, 31, 71);\n"
                                   "border-radius: 10px;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(396, 95, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(252, 226, 105);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalSlider = QtWidgets.QSlider(self)
        self.horizontalSlider.setGeometry(QtCore.QRect(370, 130, 241, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(396, 195, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(252, 226, 105);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalSlider_2 = QtWidgets.QSlider(self)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(370, 230, 241, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.radioButton_2 = QtWidgets.QCheckBox(self)
        self.radioButton_2.setGeometry(QtCore.QRect(400, 350, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: rgb(252, 226, 105);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 400, 101, 51))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "    \n"
                                        "    background-color: rgb(179, 68, 55);\n"
                                        "    color: rgb(29, 31, 71);\n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(29, 31, 71);\n"
                                        "    color: rgb(239, 92, 74);\n"
                                        "    border-radius: 10px;\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(500, 400, 101, 51))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
                                        "    \n"
                                        "    \n"
                                        "    background-color: rgb(29, 31, 71);\n"
                                        "    color: rgb(239, 92, 74);\n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(239, 92, 74);\n"
                                        "    color: rgb(16, 24, 37);\n"
                                        "    border-radius: 10px;\n"
                                        "}")
        self.pushButton_5.setObjectName("pushButton_5")

        self.radioButton.setText("Отключить звук")
        self.label_2.setText("Громкость Звука")
        self.label_3.setText("Громкость Музыки")
        self.radioButton_2.setText("Отключить музыку")
        self.pushButton_4.setText("Отменить")
        self.pushButton_5.setText("Принять")


        self.volume = self.horizontalSlider_2.value()
        self.volume1 = self.horizontalSlider.value()
        self.volumeChk = False
        self.volumeChk1 = False


        self.horizontalSlider_2.valueChanged.connect(self.changeSlide)
        self.horizontalSlider.valueChanged.connect(self.changeSlide1)
        self.radioButton.stateChanged.connect(self.changeBox)
        self.radioButton_2.stateChanged.connect(self.changeBox1)


        self.ZvykPok = False

        self.vool1 = self.horizontalSlider.value()
        self.vool2 = self.horizontalSlider_2.value()
        self.chekBut1 = False
        self.chekBut2 = False

        self.pushButton_14.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.radioButton.hide()
        self.radioButton_2.hide()
        self.label_7.hide()
        self.horizontalSlider.hide()
        self.horizontalSlider_2.hide()
        self.pushButton_4.hide()
        self.pushButton_5.hide()



        self.addFunctons()

    def addFunctons(self):
        self.pushButton_2.clicked.connect(self.ButExit)
        self.pushButton_9.clicked.connect(self.showNastrZvyk)
        self.pushButton_4.clicked.connect(self.otmnFunc)
        self.pushButton_5.clicked.connect(self.prinFunc)

    def prinFunc(self):
        self.close()

    def otmnFunc(self):
        self.horizontalSlider.setValue(self.vool1)
        self.horizontalSlider_2.setValue(self.vool2)
        if self.chekBut1 == True:
            self.radioButton.setChecked(True)
        else:
            self.radioButton.setChecked(False)

        if self.chekBut2 == True:
            self.radioButton_2.setChecked(True)
        else:
            self.radioButton_2.setChecked(False)


    def changeSlide(self):
        self.volume = self.horizontalSlider_2.value()

    def changeSlide1(self):
        self.volume1 = self.horizontalSlider.value()

    def changeBox(self):
        if self.radioButton.isChecked():
            self.volumeChk = True
        else:
            self.volumeChk = False

    def changeBox1(self):
        if self.radioButton_2.isChecked():
            self.volumeChk1 = True
        else:
            self.volumeChk1 = False

    def ButExit(self):
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(500)  # Длительность анимации в миллисекундах
        self.animation.setEndValue(0)  # Конечное значение прозрачности (0 - полностью прозрачное окно)
        self.animation.start()
        if self.ZvykPok == True:
            self.otmnFunc()
        self.animation.finished.connect(self.close)


    def showNastrZvyk(self):

        if self.pushButton_14.isHidden():
            self.ZvykPok = True
            self.vool1 = self.horizontalSlider.value()
            self.vool2 = self.horizontalSlider_2.value()

            if self.radioButton.isChecked():
                self.chekBut1 = True
            if self.radioButton_2.isChecked():
                self.chekBut2 = True
            self.pushButton_9.setStyleSheet("border-radius: 10px;\n"
                                            "background-color: rgb(239, 92, 74);\n"
                                            "color: rgb(16, 24, 37);\n")
            self.pushButton_10.setStyleSheet("background-color: rgb(16, 24, 37);\n"
                                            "color: rgb(239, 92, 74);\n"
                                            "border-radius: 10px;\n")
            self.pushButton_11.setStyleSheet("background-color: rgb(16, 24, 37);\n"
                                            "color: rgb(239, 92, 74);\n"
                                            "border-radius: 10px;\n")
            self.pushButton_12.setStyleSheet("background-color: rgb(16, 24, 37);\n"
                                            "color: rgb(239, 92, 74);\n"
                                            "border-radius: 10px;\n")
            self.pushButton_13.setStyleSheet("background-color: rgb(16, 24, 37);\n"
                                            "color: rgb(239, 92, 74);\n"
                                            "border-radius: 10px;\n")
            self.pushButton_14.show()
            self.radioButton.show()
            self.radioButton_2.show()
            self.horizontalSlider.show()
            self.horizontalSlider_2.show()
            self.label_2.show()
            self.label_3.show()
            self.label_4.show()
            self.label_5.show()
            self.label_6.show()
            self.label_7.show()
            self.pushButton_4.show()
            self.pushButton_5.show()
        else:
            self.ZvykPok = False
            print(self.ZvykPok)
            self.otmnFunc()
            self.pushButton_14.hide()
            self.label_2.hide()
            self.label_3.hide()
            self.label_4.hide()
            self.label_5.hide()
            self.label_6.hide()
            self.radioButton.hide()
            self.radioButton_2.hide()
            self.label_7.hide()
            self.horizontalSlider.hide()
            self.horizontalSlider_2.hide()
            self.pushButton_4.hide()
            self.pushButton_5.hide()
            self.pushButton_9.setStyleSheet("QPushButton {\n"
                                            "    background-color: rgb(16, 24, 37);\n"
                                            "    color: rgb(239, 92, 74);\n"
                                            "    border-radius: 10px;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(239, 92, 74);\n"
                                            "    color: rgb(16, 24, 37);\n"
                                            "    border-radius: 10px;\n"
                                            "}")
            self.pushButton_10.setStyleSheet("QPushButton {\n"
                                            "    background-color: rgb(16, 24, 37);\n"
                                            "    color: rgb(239, 92, 74);\n"
                                            "    border-radius: 10px;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(239, 92, 74);\n"
                                            "    color: rgb(16, 24, 37);\n"
                                            "    border-radius: 10px;\n"
                                            "}")
            self.pushButton_11.setStyleSheet("QPushButton {\n"
                                            "    background-color: rgb(16, 24, 37);\n"
                                            "    color: rgb(239, 92, 74);\n"
                                            "    border-radius: 10px;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(239, 92, 74);\n"
                                            "    color: rgb(16, 24, 37);\n"
                                            "    border-radius: 10px;\n"
                                            "}")
            self.pushButton_12.setStyleSheet("QPushButton {\n"
                                            "    background-color: rgb(16, 24, 37);\n"
                                            "    color: rgb(239, 92, 74);\n"
                                            "    border-radius: 10px;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(239, 92, 74);\n"
                                            "    color: rgb(16, 24, 37);\n"
                                            "    border-radius: 10px;\n"
                                            "}")
            self.pushButton_13.setStyleSheet("QPushButton {\n"
                                            "    background-color: rgb(16, 24, 37);\n"
                                            "    color: rgb(239, 92, 74);\n"
                                            "    border-radius: 10px;\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(239, 92, 74);\n"
                                            "    color: rgb(16, 24, 37);\n"
                                            "    border-radius: 10px;\n"
                                            "}")








if __name__ == '__main__':
    app = QApplication([])

    w = Widget()
    w.resize(728, 511)
    w.show()

    app.exec()