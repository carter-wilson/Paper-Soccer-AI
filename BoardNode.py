class BoardNode:
    neighbors = dict()
    links = dict()

    def __init__(self, x, y):
        self.x, self.y = x, y

    def add_neighbor(self, direction, neighbor, fromneighbor=False):
        self.neighbors[direction] = neighbor
        if not fromneighbor:
            neighbor.add_neigbor((direction + 4) % 8, self, fromneighbor=True)

    def add_link(self, direction):
        self.links[direction] = self.neighbors[direction]
        return self.links[direction]

    def get_legal_moves(self):
        return self.neighbors.keys() - self.links.keys()

    def visited(self):
        return bool(self.links)
