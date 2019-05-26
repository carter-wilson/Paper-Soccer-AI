from copy import deepcopy


class State:
    moves = []
    board = dict()
    legal_moves = None

    def __init__(self, n, m, g):
        self.n, self.m, self.g = n, m, g
        self.active = (n, m)

    def get_neighbors(self, node):
        return {direction: neighbor for (direction, neighbor) in enumerate(border(node)) if self.islegal(neighbor)}

    def islegal(self, node):
        x, y = node
        return 0 <= x <= self.n * 2 and 0 <= y <= self.m * 2 or \
               y in (-1, self.m * 2 + 1) and self.n - self.g < x < self.n + self.g

    def get_links(self, node):
        return self.board.get(node, set())

    def add_link(self, node, direction):
        s = shift[direction]
        node2 = (node[0] + s[0], node[1] + s[1])
        self.add_directional_link(node, direction)
        self.add_directional_link(node2, (direction + 4) % 8)
        return node2

    def add_directional_link(self, node1, direction):
        if node1 in self.board:
            self.board[node1].add(direction)
        else:
            self.board[node1] = {direction}

    def add(self, move):
        self.legal_moves = None
        self.moves.append(move)
        for d in move:
            self.active = self.add_link(self.active, int(d))

    def add_tonew(self, move):
        n = self.clone()
        n.add(move)
        return n

    def state_string(self):
        return self.moves

    def get_legal_moves(self):
        if not self.legal_moves:
            self.legal_moves = self.bounce(self.active, self.get_legal_moves_detached(self.active))
        return self.legal_moves

    def bounce(self, start, moves, newlinks=None):
        if newlinks is None:
            newlinks = dict()
        fullmoves = dict()
        for direction, node in moves.items():
            backwards = (direction + 4) % 8
            if self.get_links(node) - {backwards}:
                newnewlinks = deepcopy(newlinks)
                if newlinks.get(start, False):
                    newnewlinks[start].add(direction)
                else:
                    newnewlinks.update({start: {direction}})
                if newlinks.get(node, False):
                    newnewlinks[node].add(backwards)
                else:
                    newnewlinks.update({node: {backwards}})
                fullmoves.update(pre_dict(str(direction),
                                          self.bounce(node,
                                                      self.get_legal_moves_detached(node, newlinks=newnewlinks[node]),
                                                      newlinks=newnewlinks)))
            else:
                fullmoves[str(direction)] = node
        return fullmoves

    def get_legal_moves_detached(self, node, newlinks=None):
        links = self.get_links(node) | (newlinks if newlinks else set())
        return {k: v for (k, v) in self.get_neighbors(node).items() if k not in links}

    def clone(self):
        new = State(self.n, self.m, self.g)
        new.active = self.active
        new.moves = deepcopy(self.moves)
        new.board = deepcopy(self.board)
        return new

    def finished(self):
        return not 0 <= self.active[1] <= self.m*2 or not self.get_legal_moves()


xshift = (0, 1, 1, 1, 0, -1, -1, -1)
shift = [(xshift[i], xshift[(i - 2) % 8]) for i in range(len(xshift))]


def border(xy):
    x, y = xy
    return [(x + s[0], y + s[1]) for s in shift]


def pre_dict(s, d):
    return {s + k: v for (k, v) in d.items()}
