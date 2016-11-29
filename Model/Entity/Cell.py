from Model.Entity.Ships.Ship import Ship


class Cell:
    def __init__(self):
        self.__ship = None  # Ссылка на корабль
        self.__state = None  # None - не стоеляли / True - Попал / False - Мимо

    @property
    def ship(self):
        return self.__ship

    @ship.setter
    def ship(self, ship):
        if isinstance(ship, Ship):
            self.__ship = ship

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

    def __str__(self):
        if self.__ship and self.__state:
            return "X "
        elif self.__ship:
            return "S "
        elif self.__state == False:
            return "• "
        else:
            return "- "
