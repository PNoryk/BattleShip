from Model.Entity.Ships.Ship import Ship


class Battleship(Ship):
    def __init__(self, orientation=1):
        super().__init__(orientation)
        self.health = 4
