import argparse
from Game import Game


def main():
    parser = argparse.ArgumentParser(description='Game of Life')

    parser.add_argument('--width', type=int, default=640, help='provide width of the game field')
    parser.add_argument('--height', type=int, default=480, help='provide height of the game field')
    parser.add_argument('--cell', type=int, default=40, help='provide size of the cell')
    parser.add_argument('--speed', type=int, default=1, help='provide speed of the game')

    args = parser.parse_args()
    game = Game(args.width, args.height, args.cell, args.speed)
    game.run()


if __name__ == '__main__':
    main()


