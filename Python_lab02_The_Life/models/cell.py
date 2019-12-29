class Cell:
    def __init__(self):
        self.__alive = False

    def change(self):
        self.__alive = not self.__alive

    @property
    def Alive(self):
        return self.__alive
