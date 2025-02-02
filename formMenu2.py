import os

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
import sys
from PyQt5.QtTest import QTest
from PyQt5.QtCore import QTimer, QTime, pyqtSignal, QUrl, QPropertyAnimation, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsOpacityEffect


from NastrForm import Widget
from KompForm import KompWindow
from ColectionForm import ColForm

class HoverButton(QPushButton):
    mouseHover = pyqtSignal(bool)

    def __init__(self, parent=None):
        QPushButton.__init__(self, parent)
        self.setMouseTracking(True)

    def enterEvent(self, event):
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("NastrIc3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mouseHover.emit(True)
        self.setIcon(icon2)

    def leaveEvent(self, event):
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("nastrIc1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mouseHover.emit(False)
        self.setIcon(icon1)




class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.setGeometry(0, 0, 1920, 1080)
        self.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        self.pushButton.setFont(font)
        self.pushButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PoKmenu1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(1920, 1080))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(640, 260, 631, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(25)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(205, 115, 39);\n"
"    color: rgb(18, 46, 93);\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(18, 46, 93);\n"
"    color: rgb(205, 115, 39);\n"
"    border-radius: 6px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(25)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb(205, 115, 39);\n"
"    color: rgb(18, 46, 93);\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(18, 46, 93);\n"
"    color: rgb(205, 115, 39);\n"
"    border-radius: 6px;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(25)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(205, 115, 39);\n"
"    color: rgb(18, 46, 93);\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(18, 46, 93);\n"
"    color: rgb(205, 115, 39);\n"
"    border-radius: 6px;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(25)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(205, 115, 39);\n"
"    color: rgb(18, 46, 93);\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(18, 46, 93);\n"
"    color: rgb(205, 115, 39);\n"
"    border-radius: 6px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 1020, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
                                        "    background-color: transparent;\n"
                                        "    color: rgb(134, 97, 36);\n"
                                        "    border-radius: 6px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: transparent;\n"
                                        "    color: rgb(120, 133, 170);\n"
                                        "    border-radius: 6px;\n"
                                        "}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1840, 0, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(175, 94, 101);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_7 = HoverButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1780, 960, 101, 91))
        self.pushButton_7.setStyleSheet("background-color: transparent;")
        self.pushButton_7.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("nastrIc1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.mouseHover.connect(self.NastrButChngd)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Base 05")
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(139, 70, 41);")
        self.label_2.setObjectName("label_2")
        self.setCentralWidget(self.centralwidget)

        self.pushButton1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1_1.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.pushButton1_1.setText("")
        self.pushButton1_1.setObjectName("pushButton")
        self.pushButton1_1.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton1_1.hide()

        self.addFunctons()
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.timer1 = QTimer(self)

        self.player = QMediaPlayer()

        self.player.setMedia(QMediaContent(QUrl(
            "menSound.mp3"
        )))

        self.player.setVolume(20)

        self.V1 = self.player.volume()
        self.V2 = 0
        self.Vc1 = False
        self.Vc2 = False

        self.RegFormOpen()



    def addFunctons(self):
        self.pushButton_6.clicked.connect(self.ButExit)
        self.pushButton_7.clicked.connect(self.NastrFormOpen)
        self.pushButton_2.clicked.connect(self.KompFormOpen)
        self.pushButton_3.clicked.connect(self.ColPerexod)

    def ColPerexod(self):
        self.colForm = ColForm()
        self.hide()
        self.colForm.show()

    def volumeGlob(self, valuT):
        pass

    def KompPerexod(self):
        self.pushButton1_1.show()
        opacity_effect = QGraphicsOpacityEffect()
        self.pushButton1_1.setGraphicsEffect(opacity_effect)
        self.animation = QPropertyAnimation(opacity_effect, b"opacity")
        self.animation.setDuration(2500)  # Длительность анимации в миллисекундах
        self.animation.setStartValue(0.0)  # Начальное значение прозрачности (полностью непрозрачный)
        self.animation.setEndValue(1.0)  # Конечное значение прозрачности (полностью прозрачный)
        self.animation.start()

    def KompFormOpen(self):
        self.KompPerexod()
        self.timer1.timeout.connect(self.fadeout)
        self.timer1.start(100)
        QTest.qWait(2500)
        self.kompForm = KompWindow()
        self.kompForm.show()
        self.close()
        self.kompForm.window_closed.connect(self.on_window_closed)
        self.kompForm.V = self.V2
        self.kompForm.Vm = self.V1
        print("nnnnnnnnnnnnnnnnnnnnnn")

    def on_window_closed(self):
        self.show()

    def fadeout(self):
        current_volume = self.player.volume()
        # Уменьшаем громкость на небольшое значение
        self.player.setVolume(current_volume - 3)
        if current_volume <= 0:
            # Если громкость достигла нуля, останавливаем воспроизведение
            self.player.stop()
            # Останавливаем таймер
            self.timer1.stop()

    def NastrFormOpen(self):
        self.widget = Widget()
        self.widget.horizontalSlider_2.setValue(self.V1)
        self.widget.horizontalSlider.setValue(self.V2)
        if self.Vc2 == True:
            self.widget.radioButton.setChecked(True)
        else:
            self.widget.radioButton.setChecked(False)

        if self.Vc1 == True:
            self.widget.radioButton_2.setChecked(True)
        else:
            self.widget.radioButton_2.setChecked(False)

        opacity_effect = QGraphicsOpacityEffect()
        self.widget.setGraphicsEffect(opacity_effect)
        self.animation = QPropertyAnimation(opacity_effect, b"opacity")
        self.animation.setDuration(1000)  # Длительность анимации в миллисекундах
        self.animation.setStartValue(0.0)  # Начальное значение прозрачности (полностью непрозрачный)
        self.animation.setEndValue(1.0)  # Конечное значение прозрачности (полностью прозрачный)
        self.animation.start()
        self.widget.exec()
        self.V1 = self.widget.volume
        self.V2 = self.widget.volume1
        self.Vc1 = self.widget.volumeChk1
        self.Vc2 = self.widget.volumeChk
        self.player.setVolume(self.V1)
        self.volumeGlob(self.V2)
        if self.Vc1 == True:
            self.player.setVolume(0)
        if self.Vc2 == True:
            self.volumeGlob(0)
        print(self.widget.volume1)
        print(self.widget.volumeChk)
        print(self.widget.volumeChk1)

    def NastrButChngd(self):
        pass

    def RegFormOpen(self):
        fileeLL = open("baza.txt", 'r', encoding='utf-8')
        self.logUs = fileeLL.readlines()[-1]
        self.logUs = self.logUs.replace("\n", "")
        self.label_2.setText(self.logUs)
        fileeLL.close()
        self.player.play()



    def showTime(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm')
        self.label.setText(label_time)

    def ButExit(self):
        os.kill()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Кампания"))
        self.pushButton_5.setText(_translate("MainWindow", "Арена"))
        self.pushButton_4.setText(_translate("MainWindow", "Лаборатория"))
        self.pushButton_3.setText(_translate("MainWindow", "Коллекция"))
        self.pushButton_6.setText(_translate("MainWindow", "Выход"))
        self.label.setText(_translate("MainWindow", "00:00"))



if __name__ == "__main__":
    import sys

    App = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    App.exit(App.exec_())
