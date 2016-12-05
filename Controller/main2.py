from Model.Entity.Board import Board
from Model.Entity.Ships.Cruiser import Cruiser
from Model.Entity.Ships.Destroyer import Destroyer
from Model.Entity.Ships.Battleship import Battleship
from Model.Logic.RandomShipsSetting import RandomShipsSetting


def min():
    board = Board()
    # board.add_ship(Destroyer(), 2, 2)
    # board.add_ship(Destroyer(), 4, 0)
    # board.add_ship(Submarine(), 0, 0)
    # board.add_ship(Submarine(), 7, 9)
    # board.add_ship(Submarine(), 9, 9)
    # board.add_ship(Submarine(), 4, 9)
    # board.add_ship(Submarine(), 0, 9)
    # board.add_ship(Battleship(2), 9, 0)
    # board.add_ship(Cruiser(2), 0, 0)
    # board.add_ship(Cruiser(2), 3, 3)

    RandomShipsSetting.set_ships(board)
    print(board.pos[2][2])

    # board.shot(0, 0)
    # board.shot(7, 9)
    # board.shot(2, 2)
    # board.shot(3, 2)
    # board.shot(5, 5)
    # board.shot(5, 6)
    # board.shot(0, 9)
    # board.shot(4, 9)
    # board.shot(9, 9)
    # print(board)

    return board

# if __name__ == '__main__':
#     main()
