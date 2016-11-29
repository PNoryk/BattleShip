from Model.Entity.Ships.Ship import Ship


class Submarine(Ship):
    def __init__(self, orientation=1):
        super().__init__(orientation)
        self.health = 1
