from Python_lab02_The_Life.models.position_model import PositionModel


class CellModel:
    """Cell representation"""
    def __init__(self, position: PositionModel):
        """C'stor"""
        self.__alive = False
        self.__position = position

    def change(self) -> None:
        """Change living state of cell"""
        self.__alive = not self.__alive

    @property
    def alive(self) -> bool:
        """Check, is cell is alive"""
        return self.__alive

    @alive.setter
    def alive(self, value):
        self.__alive = value

    @property
    def position(self) -> PositionModel:
        """Return position"""
        return self.__position
