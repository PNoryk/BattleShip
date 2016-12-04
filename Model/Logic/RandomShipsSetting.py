from Model.Entity.Ships.Battleship import Battleship
from Model.Entity.Ships.Cruiser import Cruiser
from Model.Entity.Ships.Destroyer import Destroyer
from Model.Entity.Ships.Submarine import Submarine
from Model.Entity.Board import Board
from random import randint


class RandomShipsSetting:
    __ships_start = [Battleship(randint(1, 2)), Cruiser(randint(1, 2)), Destroyer(randint(1, 2)),
                     Submarine(randint(1, 2))]
    __ships = []

    for i in range(len(__ships_start)):
        j = 0
        while j < i + 1:
            __ships.append(__ships_start[i])
            j += 1

    @staticmethod
    def set_ships(board):
        if isinstance(board, Board):
            for i in RandomShipsSetting.__ships:
                while board.add_ship(i, randint(0, 9), randint(0, 9)) == False:
                    pass

