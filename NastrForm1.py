from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from PyQt5.QtCore import Qt

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 728, 511))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("nastrFon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(728, 511))
        self.pushButton.setObjectName("pushButton")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()

    Form.show()
    sys.exit(app.exec_())
