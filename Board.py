from BoardNode import BoardNode


class Board:
    nodes = dict()
    goal_top = set()
    goal_bottom = set()
    active = None

    def __init__(self, n, m, g):
        self.generate(n * 2 + 3, m * 2 + 1, g)

    def generate(self, i, j, g):
        for y in range(i):
            for x in range(j):
                if 0 < y < i - 1 or (j - g) / 2 <= x <= (j + g) / 2:
                    node = BoardNode(x, y)
                    if (x, y - 1) in self.nodes: node.add_neighbor(0, self.nodes[(x, y - 1)])
                    if (x - 1, y - 1) in self.nodes: node.add_neighbor(7, self.nodes[(x - 1, y - 1)])
                    if (x - 1, y) in self.nodes: node.add_neighbor(6, self.nodes[(x - 1, y)])
                    self.nodes[(x, y)] = node
                    if y == 0:
                        self.goal_top.add(node)
                    elif y == i - 1:
                        self.goal_bottom.add(node)
                    if y == i//2 and x == j//2:
                        self.active = node

    def get_legal_moves(self):
        return self.active.get_legal_moves()

    def move(self,direction):
        self.active = self.active.add_link(direction)
