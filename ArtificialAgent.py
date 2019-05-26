class ArtificialAgent:
    cache = dict()

    def __init__(self, is_top, n, m, abdepth):
        self.is_top = is_top
        self.h = m * 2
        self.w = n
        self.depth = abdepth

    def play(self, state):
        print('thinking ...')
        m = self.evaluate(state, self.is_top)
        print()
        return m

    def evaluate(self, state, is_top):
        return self.alphabeta(state, is_top, float('-inf'), float('inf'), self.depth, trackmove=True)

    def alphabeta(self, state, is_max, alpha, beta, depth, trackmove=False):
        if state.active[1] < 0: return float('inf')
        if state.active[1] > self.h or not state.get_legal_moves(): return float('-inf')
        if depth <= 0:
            return self.heuristic(state.active)
        else:
            goal = max if is_max else min
            moves = state.get_legal_moves()
            if depth == self.depth:
                print(len(moves))
            elif depth == self.depth - 1:
                print('x', end='')
            value = float('-inf') if is_max else float('inf')
            bestmove = None
            for move in moves:
                value = goal(value, self.alphabeta(state.add_tonew(move), not is_max, alpha, beta, depth - 1))
                if is_max:
                    f = trackmove and alpha < value
                    alpha = max(alpha, value)
                else:
                    f = trackmove and beta > value
                    beta = min(beta, value)
                if f:
                    bestmove = move
                if alpha >= beta:
                    break
            if trackmove:
                if not bestmove:
                    # Lost the game, but lets not look stupid
                    bestmove = self.alphabeta(state, is_max, float('-inf'), float('inf'), 1, trackmove=True)
                return bestmove
            return value

    def heuristic(self, pos):
        if pos in self.cache:
            return self.cache[pos]
        else:
            xx = (self.w - pos[0]) ** 2
            y = pos[1]
            h = (xx + (self.h - y) ** 2) ** .5 - (xx + y ** 2) ** .5
            self.cache[pos] = h
            return h
