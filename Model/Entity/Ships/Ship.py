class Ship:
    __orient = {1: "vertical", 2: "horizontal"}

    def __init__(self, orientation=1):
        self.__health = 0
        if 1 <= orientation <= 2:
            self.__orientation = self.__orient[orientation]
        else:
            self.__orientation = self.__orient[1]
        self.__shots = 0

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        self.__health = health

    def shot(self):
        self.__shots += 1

    @property
    def orientation(self):
        return self.__orientation

    def is_dead(self):
        if self.__health == self.__shots:
            return True
        return False

    def __str__(self):
        return "\nOrientation: \t" + self.__orientation + "\nHealth: " + str(self.__health)
