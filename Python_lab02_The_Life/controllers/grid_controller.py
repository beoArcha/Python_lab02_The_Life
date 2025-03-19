from Python_lab02_The_Life.models.grid_model import GridModel


class GridController:
    """"Controller for gird"""
    def __init__(self, grid: GridModel):
        """C'stor"""
        self.__grid = grid

    def change(self, changes: set) -> None:
        """Change cell life status"""
        for c in changes:
            cell = self.__grid.get_cell_pm(c)
            cell.change()

    def affection(self) -> set:
        """Return set of alive cell position in grid"""
        affected = set()
        for x in range(0, self.__grid.size):
            for y in range(0, self.__grid.size):
                if self.__grid.get_cell(x, y).alive:
                    affected.add(self.__grid.get_cell(x, y))
        return affected
