from Model.Entity.Cell import Cell
from Model.Entity.Ships.Ship import Ship


class Board:
    __rows = 10
    __columns = 10

    def __init__(self):
        self.__pos = []

        for i in range(self.__rows):
            line = []
            for _ in range(self.__columns):
                line.append(Cell())
            self.__pos.append(line)

        self.__ships = []
        self.__ships_count = 0

    def __check(self, y, x, health, orient):  # False - есть рядом корабли или выход за пределы поля / True - нет
        while health != 0:
            y1, y2, x1, x2 = y - 1, y + 2, x - 1, x + 2
            if y == 0:
                y1 = y
            if x == 0:
                x1 = x
            if y == self.__rows - 1:
                y2 = y + 1
            if x == self.__columns - 1:
                x2 = x + 1
            if x + health > self.__rows and orient == "horizontal":
                return False
            if y + health > self.__columns and orient == "vertical":
                return False

            for i in range(y1, y2):
                for j in range(x1, x2):
                    if self.__pos[i][j].ship:
                        return False

            if orient == "horizontal":
                x += 1
            else:
                y += 1
            health -= 1
        return True

    def __close_cells(self, y, x):
        if self.__pos[y][x].ship:
            if self.__pos[y][x].ship.orientation == "vertical":  # Находим начало корабля (Х, У)
                while self.__pos[y - 1][x].ship and y - 1 >= 0:
                    y -= 1
            else:
                while self.__pos[y][x - 1].ship and x - 1 >= 0:
                    x -= 1

            y1, x1 = y - 1, x - 1
            if y == 0:
                y1 = y

            if x == 0:
                x1 = x

            if self.__pos[y][x].ship.orientation == "vertical":
                if y + self.__pos[y][x].ship.health == self.__rows:
                    y2 = self.__rows
                else:
                    y2 = y + self.__pos[y][x].ship.health + 1
                if x + 1 == self.__columns:
                    x2 = x + 1
                else:
                    x2 = x + 2
            else:
                if x + self.__pos[y][x].ship.health == self.__columns:
                    x2 = self.__columns
                else:
                    x2 = x + self.__pos[y][x].ship.health + 1
                if y + 1 == self.__rows:
                    y2 = y + 1
                else:
                    y2 = y + 2

            for i in range(y1, y2):
                for j in range(x1, x2):
                    if not self.__pos[i][j].ship:
                        self.__pos[i][j].state = False
            print("x =" + str(x) + " y =" + str(y))

    def add_ship(self, ship, y, x):
        if isinstance(ship, Ship) and self.__check(y, x, ship.health, ship.orientation):
            for item in range(ship.health):
                if ship.orientation == "horizontal" and ship.health + x <= self.__columns:
                    self.__pos[y][x + item].ship = ship
                elif ship.orientation == "vertical" and ship.health + y <= self.__rows:
                    self.__pos[y + item][x].ship = ship
            self.__ships_count += 1

    def win(self):
        if self.__ships_count == 0:
            return True
        return False

    def shot(self, y, x):
        if self.__pos[y][x].state == None:
            if self.__pos[y][x].ship:
                self.__pos[y][x].state = True
                self.__pos[y][x].ship.shot()
                if self.__pos[y][x].ship.is_dead():
                    self.__close_cells(y, x)
                    self.__ships_count -= 1
            else:
                self.__pos[y][x].state = False

    @property
    def pos(self):
        return self.__pos

    @property
    def ships(self):
        return self.__ships

    @property
    def ships_count(self):
        return self.__ships_count

    def __str__(self):
        string = ""
        for i in range(len(self.__pos)):
            for j in range(len(self.__pos[0])):
                string += str(self.__pos[i][j])
            if i < self.__rows - 1:
                string += "\n"
        return string
