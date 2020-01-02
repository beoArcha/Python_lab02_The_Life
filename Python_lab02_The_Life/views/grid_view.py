from prettytable import PrettyTable
from Python_lab02_The_Life.models.grid_model import GridModel


class GridView:
    def __init__(self, size: int):
        """C'stor"""
        self.__size = size
        self.__table = self.__generate()

    def next(self, current: GridModel) -> None:
        for x in range(0, self.__size):
            new_row = list()
            new_row.append(x)
            for y in range(0, self.__size):
                if current.get_cell(x, y).alive:
                    new_row.append("A")
                else:
                    new_row.append("D")
            self.__table.add_row(new_row)
        print(self.__table)

    def __generate(self) -> PrettyTable:
        pt = PrettyTable()
        pt.field_names = ["x\\y"] + [str(x) for x in range(0, self.__size)]
        return pt
