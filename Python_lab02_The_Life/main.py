import argparse


def main() -> None:
    args = parsing_args()
    grid = args.grid
    input("Press any key to end...")


def parsing_args() -> argparse:
    parser = argparse.ArgumentParser(description="Play the life game.")
    parser.add_argument("--grid", "-g", help="Size of square grid", type=int, default=10, choices=range(5, 25))
    parser.add_argument("--debug", "-de", help="Debug mode", action="store_true")
    return parser.parse_args()


if '__main__' == __name__:
    main()
