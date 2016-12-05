from PyQt5.QtWidgets import QPushButton
from Model.Entity.Board import Board


class Button(QPushButton):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.__x = x
        self.__y = y
        self.__count = 0

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def push(self, board):
        if isinstance(board, Board):
            board.shot(self.__x, self.__y)

    def get_count(self):
        return self.__count

    def inc_count(self):
        self.__count += 1

    def get_state(self):
        return self.__x, self.__y
