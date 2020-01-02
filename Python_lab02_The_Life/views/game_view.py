from prettytable import PrettyTable
from Python_lab02_The_Life.views.grid_view import GridView


class GameView:
    def __init__(self, size: int):
        """C'stor"""
        self.__grid = GridView(size)

    def plot_next_grid(self):
        self.__grid.next()
