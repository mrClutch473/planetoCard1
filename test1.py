from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt

from test import WindowA


class WindowB(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаем метку, на которую будем выводить сообщение о закрытии Окна А
        self.label = QLabel("Окно А не закрыто", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.windowA = WindowA()
        self.windowA.show()
        self.windowA.window_closed.connect(self.on_window_closed)

    def on_window_closed(self):
        print("close")


if __name__ == "__main__":
    app = QApplication([])
    window = WindowB()
    window.show()

    app.exec_()

