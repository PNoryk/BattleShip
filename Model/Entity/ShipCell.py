class ShipCell:
    def __init__(self, count=1, ship=None):
        self.__cell_count = count
        self.__ship = ship

    @property
    def cell_count(self):
        return self.__cell_count

    @property
    def ship(self):
        return self.__ship

    def __str__(self):
        return "Номер ячейки корабля: " + self.__cell_count + "\nАдресс корабля: " + self.__ship
