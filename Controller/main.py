from Model.Entity.Board import Board
from Model.Entity.Cell import Cell
from Model.Entity.Ships.Submarine import Submarine
from Model.Entity.Ships.Destroyer import Destroyer
from Model.Entity.Ships.Cruiser import Cruiser
from Model.Entity.Ships.Battleship import Battleship


def main():
    b = Board()

    # s = Ship(4)
    #
    # b.add_ship(s, 2, 2)
    # s2 = Ship(4)
    #
    # b.add_ship(s2, 1, 1)
    # print(b)

    s2 = Battleship()
    s3 = Cruiser()
    s1 = Submarine()
    s4 = Submarine(2)

    b.add_ship(s3, 7, 5)

    b.add_ship(s2, 5, 0)
    b.add_ship(s1, 5, 6)
    b.add_ship(s4, 7, 9)

    # c = Cell()
    # print("\n\n" + str(c.ship))

    # ship = Ship(3)
    # print(ship)

    # submarine = Submarine()
    # print(submarine)
if __name__ == '__main__':
    main()
