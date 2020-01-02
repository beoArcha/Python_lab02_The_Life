from Python_lab02_The_Life.models.grid_model import GridModel


class GridController:
    def __init__(self, grid: GridModel):
        self.__grid = grid

    def change(self, changes: set) -> None:
        for c in changes:
            cell = self.__grid.get_cell_PM(c)
            cell.change()

    def affection(self) -> set:
        affected = set()
        for x in range(0, self.__grid.size):
            for y in range(0, self.__grid.size):
                if self.__grid.get_cell(x, y).alive:
                    affected.add(self.__grid.get_cell(x, y))
        return affected
