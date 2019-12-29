import argparse
from Python_lab02_The_Life.models.grid import Grid


def main() -> None:
    """Starting function"""
    args = parsing_args()
    grid = Grid(args.grid)
    input("Press any key to end...")


def parsing_args() -> argparse:
    """Prepare starting arguments"""
    parser = argparse.ArgumentParser(description="Play the life game.")
    parser.add_argument("--grid", "-g", help="Size of square grid between 5 and 24", type=int, default=10,
                        choices=range(5, 25))
    parser.add_argument("--debug", "-de", help="Debug mode", action="store_true")
    return parser.parse_args()


if '__main__' == __name__:
    main()
