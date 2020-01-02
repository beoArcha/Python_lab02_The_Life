from Python_lab02_The_Life.views.grid_view import GridView


class GameView:
    def __init__(self, size: int):
        """C'stor"""
        self.__size = size
        self.__grid = GridView(size)

    def plot_next_grid(self, current: set, turn: int):
        print("\n{1}{0}{1}\n".format(turn, "++++"))
        self.__grid.next(current)
