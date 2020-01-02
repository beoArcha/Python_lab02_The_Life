from Python_lab02_The_Life.models.grid_model import GridModel


class GridController:
    def __init__(self, grid: GridModel):
        self.__grid = grid

    def initialize(self, changes: set) -> None:
        for c in changes:
            x, y = c.position