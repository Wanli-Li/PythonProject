import sys
from PyQt5.QtWidgets import *


class MainWindow(QWidget):

    # noinspection PyArgumentList
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("MainWindow")
        self.setWindowOpacity(0.2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
