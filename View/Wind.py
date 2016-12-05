import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QGridLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 640, 480)
        # label = QLabel("Hello", self).move(100, 100)

        q = QGridLayout()
        q.addWidget(QPushButton("Hello"), 0, 0)

        q.addWidget(QPushButton("its"), 0, 1, 1, 5)
        q.addWidget(QPushButton("me"), 1, 0)
        self.setLayout(q)

        self.resize(300, 300)

app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
sys.exit(app.exec_())
