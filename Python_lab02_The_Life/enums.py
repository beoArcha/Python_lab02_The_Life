from enum import Enum


class CellRepresentation(Enum):
    """Cell representation"""
    Alive = 'O'
    Dead = 'X'

    def __str__(self):
        return self.value
