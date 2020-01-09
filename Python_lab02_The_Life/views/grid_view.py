from prettytable import PrettyTable
from Python_lab02_The_Life.enums import CellRepresentation
from Python_lab02_The_Life.models.grid_model import GridModel


class GridView:
    """Create view of grid"""
    def __init__(self, size: int):
        """C'stor"""
        self.__size = size
        self.__table = self.__generate()

    def next(self, current: GridModel) -> None:
        """Plot next table from current status of grid model"""
        for x in range(0, self.__size):
            new_row = list()
            new_row.append(x)
            for y in range(0, self.__size):
                if current.get_cell(x, y).alive:
                    new_row.append(CellRepresentation.Alive)
                else:
                    new_row.append(CellRepresentation.Dead)
            self.__table.add_row(new_row)
        print(self.__table)

    def __generate(self) -> PrettyTable:
        """Generate Pretty Table field names"""
        pt = PrettyTable()
        pt.field_names = ["x\\y"] + [str(x) for x in range(0, self.__size)]
        return pt
