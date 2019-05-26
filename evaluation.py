# top player is maximizer
# (top as in trying to score in the top goal)

# should this be 12? (if so make it 11-y and y+1
# also make these come from main
H = 10
N = 4
DEPTH = 3  # float('inf') might work on a really small board


def evaluate(state, is_top):
    return alphabeta(state, is_top, float('-inf'), float('inf'), DEPTH, trackmove=True)


def alphabeta(state, is_max, alpha, beta, depth, trackmove=False):
    if state.active[1] < 0: return float('inf')
    if state.active[1] > H or not state.get_legal_moves(): return float('-inf')
    if depth <= 0:
        return heuristic(state.active)
    else:
        goal = max if is_max else min
        moves = state.get_legal_moves()
        value = float('-inf') if is_max else float('inf')
        bestmove = None
        for move in moves:
            value = goal(value, alphabeta(state.add_tonew(move), not is_max, alpha, beta, depth - 1))
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
                bestmove = alphabeta(state, is_max, float('-inf'), float('inf'), 1, trackmove=True)
            return bestmove
        return value


cache = dict()


def heuristic(pos):
    if pos in cache:
        return cache[pos]
    else:
        xx = (N - pos[0]) ** 2
        y = pos[1]
        h = (xx + (H - y) ** 2) ** .5 - (xx + y ** 2) ** .5
        cache[pos] = h
        return h
