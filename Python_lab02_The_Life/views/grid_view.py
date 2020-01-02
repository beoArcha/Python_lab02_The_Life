from prettytable import PrettyTable


class GridView:
    def __init__(self, size: int):
        """C'stor"""
        self.__size = size
        self.__table = self.__generate()

    def next(self, current: set) -> None:
        pass

    def __generate(self) -> PrettyTable:
        pt = PrettyTable()
        pt.add_column = ["x\\y", [str(x) for x in range(0, self.__size)]]
        return pt
