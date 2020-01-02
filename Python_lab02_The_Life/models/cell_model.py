class CellModel:
    """Cell representation"""
    def __init__(self):
        """C'stor"""
        self.__alive = False

    def change(self) -> None:
        """Change living state of cell"""
        self.__alive = not self.__alive

    @property
    def alive(self) -> bool:
        """Check if cell is alive"""
        return self.__alive
