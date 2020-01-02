import argparse
from datetime import datetime
from Python_lab02_The_Life.models.game_model import GameModel
from Python_lab02_The_Life.controllers.game_controller import GameController


def main() -> None:
    """Starting function"""
    args = parsing_args()
    game_model = GameModel(int(args.grid), int(args.turn), args.name, args.save)
    game_controller = GameController(game_model, int(args.living_cell))
    game_controller.play()
    input("Press any key to end...")


def parsing_args() -> argparse:
    """Prepare starting arguments"""
    parser = argparse.ArgumentParser(description="Play the life game.")
    parser.add_argument("--grid", "-g", help="Size of square grid between 5 and 24", type=int, default=10,
                        choices=range(5, 26))
    parser.add_argument("--living_cell", "-lc", help="Number of live cell between 2 and 24", type=int, default=12,
                        choices=range(3, 25))
    parser.add_argument("--turn", "-t", help="Number of turns between 5 and 25", type=int, default=10,
                        choices=range(5, 26))
    parser.add_argument("--name", "-n", help="Game's name", type=str,
                        default="the_game_of_life_{}".format(datetime.now()))
    parser.add_argument("--save", "-s", help="Save grid", action="store_true")
    return parser.parse_args()


if '__main__' == __name__:
    main()
