from Game import Game

N = 4
M = 5
G = 1

NHP = 2

ABDEPTH = 2


def main():
    game = Game(N, M, G, NHP, ABDEPTH)
    game.play()


if __name__ == '__main__':
    main()
