class Board:
    nodes = dict()
    goal_top = set()
    goal_bottom = set()
    active = None


    def __init__(self, n, m, g):
        self.generate(m * 2, n * 2, g)

    def generate(self, x, y):
        ...

