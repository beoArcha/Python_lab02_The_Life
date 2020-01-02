from Python_lab02_The_Life.models.game_model import GameModel


class GameController:
    """Main controller for the game"""
    def __init__(self, game: GameModel):
        self.__game = game

    def play(self) -> None:
        pass
