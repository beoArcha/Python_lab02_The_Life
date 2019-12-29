from .cell import Cell


class Grid:
    def __init__(self, size):
        row = [Cell for x in range(0, size)]
        self.__grid = [row for x in range(0, size)]

    def p(self):
        pass
