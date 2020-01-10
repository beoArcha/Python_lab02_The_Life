from enum import Enum


class CellRepresentation(Enum):
    """Cell representation"""
    Alive = 'O'
    Dead = ' '

    def __str__(self):
        return self.value
