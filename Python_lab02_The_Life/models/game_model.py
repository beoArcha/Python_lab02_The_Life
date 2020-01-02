from .grid_model import GridModel


class GameModel:
    """Game models"""
    def __init__(self, size: int, turn: int, interval: int):
        """C'stor"""
        self.__grid = GridModel(size)
        self.__current_turn = 0
        self.__number_of_turns = turn
        self.__interval_time = interval
        self.__staring_position = []

    @property
    def current_turn(self) -> int:
        """"Return current turn number"""
        return self.__current_turn
