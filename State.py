from Board import Board


class State:
    moves = []

    def __init__(self, n, m, g):
        self.n, self.m, self.g = n, m, g
        self.board = Board(n, m, g)

    def add(self, move):
        self.moves.append(move)
        self.board.move(move)

    def state_string(self):
        return ''.join(self.moves)

    def get_legal_moves(self):
        return self.board.get_legal_moves()
