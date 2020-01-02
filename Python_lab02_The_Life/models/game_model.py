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

    @property
    def number_of_turns(self) -> int:
        """"Return number of turns"""
        return self.__number_of_turns

    def interval_time(self) -> int:
        """"Return interval time"""
        return self.__interval_time

    @property
    def staring_position(self) -> list:
        """"Return starting positions"""
        return self.__staring_position
