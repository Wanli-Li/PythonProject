import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("MainWindow")
        self.layout = QVBoxLayout()
        label = QLabel()
        img = QImage("..//Images/10880.JPG")
        result = img.scaled(label.width(), label.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(QPixmap.fromImage(result))

        self.layout.addWidget(label)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
