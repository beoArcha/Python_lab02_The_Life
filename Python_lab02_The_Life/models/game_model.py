from .grid_model import GridModel
from .position_model import PositionModel


class GameModel:
    """Game models"""
    def __init__(self, size: int, turn: int, name: str, save: bool):
        """C'stor"""
        self.__grid = GridModel(size)
        self.__current_turn = 0
        self.__number_of_turns = turn
        self.__name = name
        self.__save = save
        self.__staring_position = []

    @property
    def grid(self) -> GridModel:
        """"Return grid"""
        return self.__grid

    @property
    def size(self) -> int:
        """Return grid size"""
        return self.__grid.size

    @property
    def current_turn(self) -> int:
        """Return current turn number"""
        return self.__current_turn

    @property
    def number_of_turns(self) -> int:
        """Return number of turns"""
        return self.__number_of_turns

    @property
    def save(self) -> bool:
        """Return saved"""
        return self.__save

    @property
    def name(self) -> str:
        """Return game name"""
        return self.__name

    @property
    def staring_position(self) -> list:
        """Return starting positions"""
        return self.__staring_position

    @staring_position.setter
    def staring_position(self, val: PositionModel) -> None:
        """Setting new starting position"""
        if val not in self.staring_position:
            self.staring_position.append(val)
        else:
            raise Exception("The same starting position already added")

    def turn_inc(self) -> None:
        """Increment turn number by 1"""
        self.__current_turn += 1
