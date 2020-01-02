from copy import deepcopy
from .cell_model import CellModel
from .position_model import PositionModel


class GridModel:
    """Cell's grid"""
    def __init__(self, size: int):
        """C'stor"""
        self.__size = size
        self.__grid = self.__make_grid()

    @property
    def size(self) -> int:
        """"Return grid size"""
        return self.__size

    def __make_grid(self) -> tuple:
        """Make grid of tuple of tuple of Cell object"""
        row = tuple(CellModel() for x in range(0, self.__size))
        return tuple(deepcopy(row) for x in range(0, self.__size))

    def get_cell(self, x: int, y: int) -> CellModel:
        """Return cell from grid"""
        if 0 <= x < self.__size and 0 <= y < self.__size:
            return self.__grid[x][y]
        else:
            raise Exception('X and Y should be between 0 and {}'.format(self.__size))

    def get_cell_PM(self, position: PositionModel) -> CellModel:
        """Return cell from grid"""
        t = position.position
        return self.get_cell(t[0], t[1])

    def get_cell_neighbours(self, x: int, y: int) -> set:
        """Return neighbours of cell"""
        neighbours = set()
        if 1 <= x < self.size - 1:
            for i in range(x - 1, x + 2):
                neighbours.update(self.__get_cell_neighbours_y(i, y))
        elif x == 0:
            for i in range(x, x + 2):
                neighbours.update(self.__get_cell_neighbours_y(i, y))
        else:
            for i in range(x, x + 1):
                neighbours.update(self.__get_cell_neighbours_y(i, y))
        return neighbours

    def __get_cell_neighbours_y(self, x: int, y: int) -> set:
        """Return neighbours of cell, y part"""
        neighbours = set()
        if 1 <= y < self.size - 1:
            for j in range(y - 1, y + 2):
                neighbours.add(self.get_cell(x, j))
        elif y == 0:
            for j in range(y, y + 2):
                neighbours.add(self.get_cell(x, j))
        else:
            for j in range(y, y + 1):
                neighbours.add(self.get_cell(x, j))
        return neighbours
