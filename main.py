from Display import Display
from Game import Game

N = 5
M = 4
G = 2

NHP = 1


def main():
    game = Game(N, M, G, NHP)
    game.play()

if __name__ == '__main__':
    main()
