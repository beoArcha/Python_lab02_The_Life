from Python_lab02_The_Life.models.grid_model import GridModel
from Python_lab02_The_Life.views.grid_view import GridView


class GameView:
    """Main vie of game"""
    def __init__(self, size: int):
        """C'stor"""
        self.__size = size
        self.__plot_entry()

    def __plot_entry(self) -> None:
        """Plot first lines of game"""
        print(
            "Size of grid is {}.\nA - means alive.\nD - means dead.".format(self.__size)
        )

    def plot_next_grid(self, model: GridModel, turn: int) -> None:
        """Plot next grid"""
        print("\n{1}{0:02}{1}\n".format(turn, "+" * self.__size))
        view = GridView(self.__size)
        view.next(model)
