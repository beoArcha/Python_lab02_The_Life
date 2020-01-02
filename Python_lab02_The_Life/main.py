import argparse
from Python_lab02_The_Life.models.game_model import GameModel
from Python_lab02_The_Life.controllers.game_controller import GameController


def main() -> None:
    """Starting function"""
    args = parsing_args()
    game_model = GameModel(args.grid, args.turn, args.interval)
    game_controller = GameController(game_model)
    game_controller.play()
    input("Press any key to end...")


def parsing_args() -> argparse:
    """Prepare starting arguments"""
    parser = argparse.ArgumentParser(description="Play the life game.")
    parser.add_argument("--grid", "-g", help="Size of square grid between 5 and 24", type=int, default=10,
                        choices=range(5, 25))
    parser.add_argument("--turn", "-t", help="Number of turns between 5 and 24", type=int, default=10,
                        choices=range(5, 25))
    parser.add_argument("--interval", "-i", help="Interval time", type=int, default=500,
                        choices=range(50, 2500))
    parser.add_argument("--debug", "-de", help="Debug mode", action="store_true")
    return parser.parse_args()


if '__main__' == __name__:
    main()
