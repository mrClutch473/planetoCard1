
from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class WindowA(QMainWindow):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()

        # Создаем кнопку, которая будет закрывать окно
        self.button = QPushButton("Закрыть", self)
        self.button.clicked.connect(self.close)

    def closeEvent(self, event):
        self.window_closed.emit()  # отправляем сигнал о закрытии окна А
        event.accept()


if __name__ == "__main__":
    app = QApplication([])
    window = WindowA()
    window.show()
    app.exec_()

