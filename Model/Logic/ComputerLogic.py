from Model.Entity.Board import Board


class Computer:
    def __init__(self):
        self.__y = 1
        self.__x = 0

    def shot(self, board, state=False):
        if isinstance(board, Board):
            if state:
                if self.__y - 2 >= board.rows:
                    tempy = self.__y - 2
            else:
                if board.shot_check(self.__y, self.__x):
                    board.shot(self.__y, self.__x)
                self.__first(board)

    def __first(self, board):
        if self.__y + 2 >= board.rows and self.__x < board.columns:
            self.__x += 1
            self.__y -= 3
            while self.__y - 2 >= 0:
                self.__y -= 2
        else:
            self.__y += 2
        if self.__y >= board.rows - 1 and self.__x >= board.columns - 1:
            self.__null()

    def __null(self):
        self.__y = 0
        self.__x = 0





