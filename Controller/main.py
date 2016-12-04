from Model.Entity.Board import Board
from Model.Logic.ComputerLogic import Computer
from Model.Entity.Cell import Cell
from Model.Entity.Ships.Submarine import Submarine
from Model.Entity.Ships.Destroyer import Destroyer
from Model.Entity.Ships.Cruiser import Cruiser
from Model.Entity.Ships.Battleship import Battleship

from Model.Logic.RandomShipsSetting import RandomShipsSetting


def main():
    b = Board()
    RandomShipsSetting.set_ships(b)
    c = Computer()
    i = 0
    while i < 49:
        i += 1
        c.shot(b)

    #
    # s2 = Battleship()
    # s3 = Cruiser()
    # s1 = Submarine()
    # s4 = Submarine(2)
    #
    # b.add_ship(s3, 7, 5)
    #
    # b.add_ship(s2, 5, 0)
    # b.add_ship(s1, 5, 6)
    # b.add_ship(s4, 7, 9)
    # print(b)
    # b.shot(7, 9)
    # b.shot(5, 6)
    # b.shot(0, 0)
    # for i in range(5, 9):
    #     b.shot(i, 0)
    # for j in range(7, 10):
    #     b.shot(j, 5)
    # print(b)


    print(b)



if __name__ == '__main__':
    main()
