import sys

from View.Button import Button
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QWidgetAction, QButtonGroup
from PyQt5.uic import loadUiType

from Model.Entity.Board import Board
from Model.Logic.RandomShipsSetting import RandomShipsSetting


app = QApplication(sys.argv)
app.setApplicationName('course_work')
form_class, base_class = loadUiType('WindForm.ui')


class MainWindow(QDialog, form_class):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)

        self.setupUi(self)

        self.computer_board = Board()
        RandomShipsSetting.set_ships(self.computer_board)
        self.gamer_board = Board()

        self.gridLayout.columnCount = 11
        self.gridLayout.rowCount = 11
        self.gridLayout_2.columnCount = 11
        self.gridLayout_2.rowCount = 11

        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K']
        for i in range(1, 11):
            label = QLabel(letters[i - 1])
            label.setAlignment(QtCore.Qt.AlignHCenter)
            self.gridLayout.addWidget(label, 0, i)
            label_2 = QLabel(letters[i - 1])
            label_2.setAlignment(QtCore.Qt.AlignHCenter)
            self.gridLayout_2.addWidget(label_2, 0, i)
        for j in range(1, 11):
            self.gridLayout.addWidget(QLabel(str(j)), j, 0)
            self.gridLayout_2.addWidget(QLabel(str(j)), j, 0)

        for i in range(1, 11):
            for j in range(1, 11):
                button = Button(i - 1, j - 1)
                button.setStyleSheet('background-color: rgb(133,133,150)')
                button2 = Button(i - 1, j - 1)
                button2.setStyleSheet('background-color: grey')
                button2.clicked.connect(self.player_shot)
                self.gridLayout.addWidget(button, i, j)
                self.gridLayout_2.addWidget(button2, i, j)

    def player_shot(self):
        sender = self.sender()
        if sender.get_count() == 0:
            sender.inc_count()
            self.computer_board.shot(sender.get_x(), sender.get_y())
            print("\n\n" + str(self.computer_board))
            self.re_print()

    def random_set(self):
        RandomShipsSetting.set_ships(self.gamer_board)
        print("\n\n\n")
        print(self.gamer_board)
        self.re_print()

    def re_print(self):
        for i in range(1, 11):
            for j in range(1, 11):
                if self.computer_board.pos[i - 1][j - 1].ship and self.computer_board.pos[i - 1][j - 1].state:
                    self.gridLayout_2.itemAtPosition(i, j).widget().setText("X")
                elif self.computer_board.pos[i - 1][j - 1].state == False:
                    self.gridLayout_2.itemAtPosition(i, j).widget().setStyleSheet("")
                    self.gridLayout_2.itemAtPosition(i, j).widget().setEnabled(0)

form = MainWindow()
form.setWindowTitle('BattleShips')
form.show()
sys.exit(app.exec_())
