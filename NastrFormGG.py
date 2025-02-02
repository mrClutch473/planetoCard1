from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(728, 511)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 728, 511))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("nastrFon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(728, 511))
        self.pushButton.setObjectName("pushButton")


        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
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
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_2.addWidget(self.pushButton_13)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(560, 470, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("color: rgb(255, 171, 160);")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 10, 50, 50))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color: transparent;")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("NastrQuit1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_14 = QtWidgets.QPushButton(Form)
        self.pushButton_14.setEnabled(True)
        self.pushButton_14.setGeometry(QtCore.QRect(270, 70, 441, 391))
        self.pushButton_14.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(43, 46, 103);\n"
"    color: rgb(255, 56, 30);\n"
"\n"
"")
        self.pushButton_14.setObjectName("pushButton_14")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_9.setText(_translate("Form", "Звук"))
        self.pushButton_10.setText(_translate("Form", "Графика"))
        self.pushButton_11.setText(_translate("Form", "Видео"))
        self.pushButton_12.setText(_translate("Form", "Управление"))
        self.pushButton_13.setText(_translate("Form", "Учётная Запись"))
        self.label.setText(_translate("Form", "mrClutch473"))
        self.pushButton_14.setText(_translate("Form", "Тут Настройки"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
