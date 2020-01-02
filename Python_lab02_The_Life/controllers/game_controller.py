from Python_lab02_The_Life.models.game_model import GameModel
from Python_lab02_The_Life.views.game_view import GameView


class GameController:
    """Main controller for the game"""
    def __init__(self, game: GameModel, living_cell: int):
        """C'stor"""
        self.__game = game
        self.__number_of_starting_position = living_cell
        self.__set_starting_position()
        self.__view = GameView(self.__game.size)

    def __set_starting_position(self):
        """Setting randomized starting position,
        where at least three are close"""
        pass

    def play(self) -> None:
        """Execute game"""
        for i in range(0, self.__game.number_of_turns):
            self.__game.turn_inc()
