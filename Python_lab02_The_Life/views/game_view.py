from Python_lab02_The_Life.models.grid_model import GridModel
from Python_lab02_The_Life.views.grid_view import GridView


class GameView:
    def __init__(self, size: int):
        """C'stor"""
        self.__size = size
        self.__grid = GridView(size)

    def plot_next_grid(self, model: GridModel, turn: int):
        print("\n{1}{0}{1}\n".format(turn, "++++"))
        self.__grid.next(model)
