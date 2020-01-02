from random import randrange
from Python_lab02_The_Life.models.game_model import GameModel
from Python_lab02_The_Life.views.game_view import GameView
from Python_lab02_The_Life.models.position_model import PositionModel
from .grid_controller import GridController
from ..models.cell_model import CellModel


class GameController:
    """Main controller for the game"""

    def __init__(self, game_model: GameModel, living_cell: int):
        """C'stor"""
        self.__game_model = game_model
        self.__number_of_starting_position = living_cell
        self.__view = GameView(self.__game_model.size)
        self.__number_of_changes = 0
        self.__current_changes = set()
        self.__set_starting_position()
        self.__grid_controller = GridController(self.__game_model.grid)

    def __set_starting_position(self):
        """Setting randomized starting position,
        where at least three are close"""
        if 3 <= self.__number_of_starting_position <= 10:
            x = randrange(1, self.__game_model.size - 1)
            y = randrange(1, self.__game_model.size - 1)
            self.__game_model.staring_position = PositionModel(x, y)
            self.__changes_inc(PositionModel(x, y))
            while self.__number_of_changes < 3:
                new_start_point = PositionModel(randrange(x - 1, x + 1),
                                                randrange(y - 1, y + 1))
                if new_start_point not in self.__current_changes:
                    self.__changes_inc(new_start_point)
                    self.__game_model.staring_position = new_start_point
            while self.__number_of_changes < self.__number_of_starting_position:
                new_start_point = PositionModel(randrange(0, self.__game_model.size),
                                                randrange(0, self.__game_model.size))
                if new_start_point not in self.__current_changes:
                    self.__changes_inc(new_start_point)
                    self.__game_model.staring_position = new_start_point
        else:
            raise Exception("Number of living cell must be between 3 and 10")

    def play(self) -> None:
        """Execute a game"""
        self.__grid_controller.change(self.__current_changes)
        self.__game_model.turn_inc()
        self.__view.plot_next_grid(self.__game_model.grid, self.__game_model.current_turn)
        self.__changes_zero()
        for i in range(1, self.__game_model.number_of_turns):
            self.__game_model.turn_inc()
            self.__next_turn()
            if self.__number_of_changes == 0:
                break
            self.__grid_controller.change(self.__current_changes)
            self.__view.plot_next_grid(self.__game_model.grid, self.__game_model.current_turn)
            self.__changes_zero()
        if self.__game_model.save:
            self.__save()

    def __next_turn(self) -> None:
        """Next turn of a game"""
        affected = self.__grid_controller.affection()
        neighbours = set()
        for a in affected:
            neighbours.update(self.__game_model.grid.get_cell_neighbours_PM(a.position))
        for neigh in neighbours:
            alive_count = 0
            for n in neighbours:
                if n.alive and self.__is_neighbour(neigh, n):
                    alive_count += 1
            if neigh.alive:
                if alive_count != 3:
                    self.__changes_inc(neigh.position)
            else:
                if alive_count == 3:
                    self.__changes_inc(neigh.position)

    @staticmethod
    def __is_neighbour(cell: CellModel, neighbour: CellModel) -> bool:
        """Check is neighbour, without itself"""
        x_c, y_c = cell.position.position
        x_n, y_n = neighbour.position.position
        if x_c == x_n and y_c == y_n:
            return False
        elif x_c - 1 <= x_n <= x_c +1 and y_c - 1 <= y_n <= y_c +1:
            return True
        else:
            return False

    def __save(self) -> None:
        pass

    def __changes_inc(self, position: PositionModel) -> None:
        """Increment changes by 1"""
        self.__number_of_changes = self.__number_of_changes + 1
        self.__current_changes.add(position)

    def __changes_zero(self) -> None:
        """Zeroing number of changes"""
        self.__number_of_changes = 0
        self.__current_changes = set()
