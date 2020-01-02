class PositionModel:
    """Position of first living cells"""
    def __init__(self, x: int, y: int):
        """C'stor"""
        self.__x = x
        self.__y = y

    @property
    def position(self) -> tuple:
        """Return (x,y) position"""
        return self.__x, self.__y

    def __hash__(self):
        return hash((self.__x, self.__y))

    def __eq__(self, other):
        try:
            return self.position == other.position
        except AttributeError:
            return NotImplemented
