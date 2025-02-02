from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.QtGui import QMovie
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QGraphicsOpacityEffect, QMainWindow


class ColForm(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(0, 0, 1920, 1080)
        self.label_pic = QtWidgets.QLabel(self)
        self.label_pic.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label_pic.setText("")
        self.label_pic.setObjectName("label_2")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(960, 80, 941, 211))
        self.label_2.setStyleSheet("background-color: rgb(90, 28, 138, 120);\n"
"border-radius: 10px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(969, 90, 921, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setMinimumSize(QtCore.QSize(200, 70))
        self.pushButton_13.setMaximumSize(QtCore.QSize(200, 70))
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 0, 3, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(200, 70))
        self.pushButton_7.setMaximumSize(QtCore.QSize(200, 70))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 0, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(200, 70))
        self.pushButton_8.setMaximumSize(QtCore.QSize(200, 70))
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 0, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(200, 70))
        self.pushButton_6.setMaximumSize(QtCore.QSize(200, 70))
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setMinimumSize(QtCore.QSize(200, 70))
        self.pushButton_11.setMaximumSize(QtCore.QSize(200, 70))
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 1, 2, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setMinimumSize(QtCore.QSize(200, 70))
        self.pushButton_10.setMaximumSize(QtCore.QSize(200, 70))
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 1, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setMinimumSize(QtCore.QSize(200, 70))
        self.pushButton_12.setMaximumSize(QtCore.QSize(200, 70))
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 1, 3, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setMinimumSize(QtCore.QSize(200, 70))
        self.pushButton_9.setMaximumSize(QtCore.QSize(200, 70))
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 0, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self)
        self.pushButton_14.setGeometry(QtCore.QRect(950, 10, 250, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("QPushButton\n"
"{\n"
"    color: rgb(253, 173, 255);\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(221, 221, 0);\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self)
        self.pushButton_15.setGeometry(QtCore.QRect(1640, 10, 261, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("QPushButton\n"
"{\n"
"    color: rgb(253, 173, 255);\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(221, 221, 0);\n"
"}")
        self.pushButton_15.setObjectName("pushButton_15")
        # self.pushButton = QtWidgets.QPushButton(self)
        # self.pushButton.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        # self.pushButton.setText("")
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("Punk_town.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.pushButton.setIcon(icon)
        # self.pushButton.setIconSize(QtCore.QSize(1920, 1080))
        # self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 320, 321, 711))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(218, 218, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 0, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;    \n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_16 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_16.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_16.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(218, 218, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 0, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;    \n"
"}")
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout.addWidget(self.pushButton_16)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(218, 218, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 0, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;    \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_17 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_17.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_17.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(218, 218, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 0, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;    \n"
"}")
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_18.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_18.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(218, 218, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 0, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;    \n"
"}")
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_19.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_19.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(218, 218, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 0, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;    \n"
"}")
        self.pushButton_19.setObjectName("pushButton_19")
        self.verticalLayout.addWidget(self.pushButton_19)
        self.pushButton_21 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_21.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_21.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(218, 218, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 0, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;    \n"
"}")
        self.pushButton_21.setObjectName("pushButton_21")
        self.verticalLayout.addWidget(self.pushButton_21)
        self.pushButton_23 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_23.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_23.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(218, 218, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 0, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;    \n"
"}")
        self.pushButton_23.setObjectName("pushButton_23")
        self.verticalLayout.addWidget(self.pushButton_23)
        self.pushButton_24 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_24.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_24.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(218, 218, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 0, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;    \n"
"}")
        self.pushButton_24.setObjectName("pushButton_24")
        self.verticalLayout.addWidget(self.pushButton_24)
        self.pushButton_25 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_25.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_25.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(218, 218, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 0, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;    \n"
"}")
        self.pushButton_25.setObjectName("pushButton_25")
        self.verticalLayout.addWidget(self.pushButton_25)
        self.pushButton_26 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_26.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_26.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(218, 218, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 0, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;    \n"
"}")
        self.pushButton_26.setObjectName("pushButton_26")
        self.verticalLayout.addWidget(self.pushButton_26)
        self.pushButton_31 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_31.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_31.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(218, 218, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 0, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;    \n"
"}")
        self.pushButton_31.setObjectName("pushButton_31")
        self.verticalLayout.addWidget(self.pushButton_31)
        self.pushButton_27 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_27.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_27.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(218, 218, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 0, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;    \n"
"}")
        self.pushButton_27.setObjectName("pushButton_27")
        self.verticalLayout.addWidget(self.pushButton_27)
        self.pushButton_30 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_30.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_30.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(218, 218, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 0, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;    \n"
"}")
        self.pushButton_30.setObjectName("pushButton_30")
        self.verticalLayout.addWidget(self.pushButton_30)
        self.pushButton_28 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_28.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_28.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(218, 218, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 0, 0);\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;    \n"
"}")
        self.pushButton_28.setObjectName("pushButton_28")
        self.verticalLayout.addWidget(self.pushButton_28)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(390, 320, 1511, 711))
        self.label.setStyleSheet("background-color: rgb(90, 28, 138, 120);\n"
"border-radius: 10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(400, 330, 1515, 700))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_35 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_35.setMinimumSize(QtCore.QSize(297, 228))
        self.pushButton_35.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(218, 218, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_35.setText("")
        self.pushButton_35.setObjectName("pushButton_35")
        self.gridLayout_2.addWidget(self.pushButton_35, 2, 2, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_22.setMinimumSize(QtCore.QSize(297, 228))
        self.pushButton_22.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(218, 218, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_22.setText("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_2.addWidget(self.pushButton_22, 0, 3, 1, 1)
        self.pushButton_38 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_38.setMinimumSize(QtCore.QSize(297, 228))
        self.pushButton_38.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(218, 218, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_38.setText("")
        self.pushButton_38.setObjectName("pushButton_38")
        self.gridLayout_2.addWidget(self.pushButton_38, 2, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(297, 228))
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(218, 218, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 0, 4, 1, 1)
        self.pushButton_37 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_37.setMinimumSize(QtCore.QSize(297, 228))
        self.pushButton_37.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(218, 218, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_37.setText("")
        self.pushButton_37.setObjectName("pushButton_37")
        self.gridLayout_2.addWidget(self.pushButton_37, 1, 1, 1, 1)
        self.pushButton_29 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_29.setMinimumSize(QtCore.QSize(297, 228))
        self.pushButton_29.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(218, 218, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_29.setText("")
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout_2.addWidget(self.pushButton_29, 1, 3, 1, 1)
        self.pushButton_36 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_36.setMinimumSize(QtCore.QSize(297, 228))
        self.pushButton_36.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(218, 218, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_36.setText("")
        self.pushButton_36.setObjectName("pushButton_36")
        self.gridLayout_2.addWidget(self.pushButton_36, 0, 1, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_20.setMinimumSize(QtCore.QSize(297, 228))
        self.pushButton_20.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(218, 218, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_20.setText("")
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_2.addWidget(self.pushButton_20, 1, 4, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(297, 228))
        self.pushButton_5.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(218, 218, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 2, 4, 1, 1)
        self.pushButton_33 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_33.setMinimumSize(QtCore.QSize(297, 228))
        self.pushButton_33.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(218, 218, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_33.setText("")
        self.pushButton_33.setObjectName("pushButton_33")
        self.gridLayout_2.addWidget(self.pushButton_33, 0, 2, 1, 1)
        self.pushButton_34 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_34.setMinimumSize(QtCore.QSize(297, 228))
        self.pushButton_34.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(218, 218, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_34.setText("")
        self.pushButton_34.setObjectName("pushButton_34")
        self.gridLayout_2.addWidget(self.pushButton_34, 1, 2, 1, 1)
        self.pushButton_32 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_32.setMinimumSize(QtCore.QSize(297, 228))
        self.pushButton_32.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(218, 218, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_32.setText("")
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout_2.addWidget(self.pushButton_32, 2, 3, 1, 1)
        self.pushButton_39 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_39.setMinimumSize(QtCore.QSize(297, 228))
        self.pushButton_39.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(218, 218, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_39.setText("")
        self.pushButton_39.setObjectName("pushButton_39")
        self.gridLayout_2.addWidget(self.pushButton_39, 0, 0, 1, 1)
        self.pushButton_40 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_40.setMinimumSize(QtCore.QSize(297, 228))
        self.pushButton_40.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(218, 218, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_40.setText("")
        self.pushButton_40.setObjectName("pushButton_40")
        self.gridLayout_2.addWidget(self.pushButton_40, 1, 0, 1, 1)
        self.pushButton_41 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_41.setMinimumSize(QtCore.QSize(297, 228))
        self.pushButton_41.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(253, 173, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(218, 218, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_41.setText("")
        self.pushButton_41.setObjectName("pushButton_41")
        self.gridLayout_2.addWidget(self.pushButton_41, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(0, 205, 241, 51))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(253, 173, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_43 = QtWidgets.QPushButton(self)
        self.pushButton_43.setGeometry(QtCore.QRect(1280, 10, 281, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setStyleSheet("QPushButton\n"
"{\n"
"    \n"
"    color: rgb(85, 255, 0);\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgb(221, 221, 0);\n"
"}")
        self.pushButton_43.setObjectName("pushButton_43")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(390, 240, 561, 71))
        self.label_3.setStyleSheet("background-color: rgb(90, 28, 138, 120);\n"
"border-radius: 10px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(390, 240, 561, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_44 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_44.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_44.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_44.setStyleSheet("background-color: transparent;")
        self.pushButton_44.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("btn1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_44.setIcon(icon1)
        self.pushButton_44.setIconSize(QtCore.QSize(70, 100))
        self.pushButton_44.setObjectName("pushButton_44")
        self.horizontalLayout.addWidget(self.pushButton_44)
        self.pushButton_45 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_45.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_45.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_45.setStyleSheet("background-color: transparent;")
        self.pushButton_45.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("btn2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_45.setIcon(icon2)
        self.pushButton_45.setIconSize(QtCore.QSize(70, 100))
        self.pushButton_45.setObjectName("pushButton_45")
        self.horizontalLayout.addWidget(self.pushButton_45)
        self.pushButton_46 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_46.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_46.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_46.setStyleSheet("background-color: transparent;")
        self.pushButton_46.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("btn3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_46.setIcon(icon3)
        self.pushButton_46.setIconSize(QtCore.QSize(70, 100))
        self.pushButton_46.setObjectName("pushButton_46")
        self.horizontalLayout.addWidget(self.pushButton_46)
        self.pushButton_47 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_47.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_47.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_47.setStyleSheet("background-color: transparent;")
        self.pushButton_47.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("btn4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_47.setIcon(icon4)
        self.pushButton_47.setIconSize(QtCore.QSize(70, 60))
        self.pushButton_47.setObjectName("pushButton_47")
        self.horizontalLayout.addWidget(self.pushButton_47)
        self.pushButton_48 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_48.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_48.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_48.setStyleSheet("background-color: transparent;")
        self.pushButton_48.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("btn5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_48.setIcon(icon5)
        self.pushButton_48.setIconSize(QtCore.QSize(70, 60))
        self.pushButton_48.setObjectName("pushButton_48")
        self.horizontalLayout.addWidget(self.pushButton_48)
        self.pushButton_49 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_49.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_49.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_49.setStyleSheet("background-color: transparent;")
        self.pushButton_49.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("btn6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_49.setIcon(icon6)
        self.pushButton_49.setIconSize(QtCore.QSize(70, 100))
        self.pushButton_49.setObjectName("pushButton_49")
        self.horizontalLayout.addWidget(self.pushButton_49)
        self.pushButton_50 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_50.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_50.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_50.setStyleSheet("background-color: transparent;")
        self.pushButton_50.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("btn7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_50.setIcon(icon7)
        self.pushButton_50.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_50.setObjectName("pushButton_50")
        self.horizontalLayout.addWidget(self.pushButton_50)
        self.pushButton_51 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_51.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_51.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_51.setStyleSheet("background-color: transparent;")
        self.pushButton_51.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("btn8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_51.setIcon(icon8)
        self.pushButton_51.setIconSize(QtCore.QSize(55, 55))
        self.pushButton_51.setObjectName("pushButton_51")
        self.horizontalLayout.addWidget(self.pushButton_51)
        self.pushButton_52 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_52.setMinimumSize(QtCore.QSize(40, 50))
        self.pushButton_52.setMaximumSize(QtCore.QSize(40, 50))
        self.pushButton_52.setStyleSheet("background-color: transparent;")
        self.pushButton_52.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("btn9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_52.setIcon(icon9)
        self.pushButton_52.setIconSize(QtCore.QSize(70, 100))
        self.pushButton_52.setObjectName("pushButton_52")
        self.horizontalLayout.addWidget(self.pushButton_52)
        self.pushButton_53 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_53.setMinimumSize(QtCore.QSize(50, 41))
        self.pushButton_53.setMaximumSize(QtCore.QSize(50, 41))
        self.pushButton_53.setStyleSheet("background-color: transparent;")
        self.pushButton_53.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("btn10.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_53.setIcon(icon10)
        self.pushButton_53.setIconSize(QtCore.QSize(70, 100))
        self.pushButton_53.setObjectName("pushButton_53")
        self.horizontalLayout.addWidget(self.pushButton_53)
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(550, 170, 241, 51))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(253, 173, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton_54 = QtWidgets.QPushButton(self)
        self.pushButton_54.setGeometry(QtCore.QRect(10, 10, 101, 91))
        self.pushButton_54.setStyleSheet("background-color: transparent;")
        self.pushButton_54.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("esc_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_54.setIcon(icon11)
        self.pushButton_54.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_54.setObjectName("pushButton_54")
        self.pushButton_42 = QtWidgets.QPushButton(self)
        self.pushButton_42.setGeometry(QtCore.QRect(0, 250, 321, 70))
        self.pushButton_42.setMinimumSize(QtCore.QSize(200, 70))
        self.pushButton_42.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_42.setObjectName("pushButton_42")
        #self.pushButton.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_2.raise_()
        self.gridLayoutWidget.raise_()
        self.pushButton_14.raise_()
        self.pushButton_15.raise_()
        self.verticalLayoutWidget.raise_()
        self.label.raise_()
        self.gridLayoutWidget_2.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_4.raise_()
        self.pushButton_43.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_3.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_5.raise_()
        self.pushButton_54.raise_()



        movie = QMovie("Punk_town.gif")
        self.label_pic.setMovie(movie)
        movie.start()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)



    def ColPerexod1(self):
        opacity_effect = QGraphicsOpacityEffect()
        self.pushButton1_2.setGraphicsEffect(opacity_effect)
        self.animation = QPropertyAnimation(opacity_effect, b"opacity")
        self.animation.setDuration(1000)  # Длительность анимации в миллисекундах
        self.animation.setStartValue(1.0)  # Начальное значение прозрачности (полностью непрозрачный)
        self.animation.setEndValue(0.0)  # Конечное значение прозрачности (полностью прозрачный)
        self.animation.start()
        QTest.qWait(2500)
        self.pushButton1_2.hide()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_14.setText(_translate("Form", "Ваши команды"))
        self.pushButton_15.setText(_translate("Form", "Другие команды"))
        self.pushButton_3.setText(_translate("Form", "Здесь будет "))
        self.pushButton_16.setText(_translate("Form", "Здесь будет "))
        self.pushButton_2.setText(_translate("Form", "Здесь будет "))
        self.pushButton_17.setText(_translate("Form", "Здесь будет "))
        self.pushButton_18.setText(_translate("Form", "Здесь будет "))
        self.pushButton_19.setText(_translate("Form", "Здесь будет "))
        self.pushButton_21.setText(_translate("Form", "Здесь будет "))
        self.pushButton_23.setText(_translate("Form", "Здесь будет "))
        self.pushButton_24.setText(_translate("Form", "Здесь будет "))
        self.pushButton_25.setText(_translate("Form", "Здесь будет "))
        self.pushButton_26.setText(_translate("Form", "Здесь будет "))
        self.pushButton_31.setText(_translate("Form", "Здесь будет "))
        self.pushButton_27.setText(_translate("Form", "Здесь будет "))
        self.pushButton_30.setText(_translate("Form", "Здесь будет "))
        self.pushButton_28.setText(_translate("Form", "Здесь будет "))
        self.label_4.setText(_translate("Form", "Текущая команда"))
        self.pushButton_43.setText(_translate("Form", "Собрать команду"))
        self.label_5.setText(_translate("Form", "Страницы"))
        self.pushButton_42.setText(_translate("Form", "Pic"))


if __name__ == "__main__":
        import sys

        App = QApplication(sys.argv)
        window = ColForm()
        window.show()
        App.exit(App.exec_())
