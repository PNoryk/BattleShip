from Model.Entity.Board import Board
from Model.Entity.Ships.Ship import Ship


class Adder:
    @staticmethod
    def add_ship(board, ship, y, x):
        if isinstance(ship, Ship) and isinstance(board, Board) and \
                                ship.health + x < 10 and ship.health + y < 10:
            if ship.orientation == "horizontal":
                for item in range(ship.health):
                    board.pos[y][x + item].ship = ship
            else:  # ship.orientation == "vertical":
                for item in range(ship.health):
                    board.pos[y + item][x].ship = ship
            board.ships.append(ship)
            board.ships_count += 1
