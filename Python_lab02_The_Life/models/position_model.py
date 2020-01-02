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
