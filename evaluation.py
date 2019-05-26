# top player is maximizer
# (top as in trying to score in the top goal)

# should this be 12? (if so make it 11-y and y+1
# also make these come from main
H = 10
N = 4
DEPTH = 2  # float('inf') might work on a really small board


# is_max refers to the player who will be taking these moves, which is not the player calling it
def evaluate(state, is_max, depth=DEPTH):
    goal = max if is_max else min
    moves = state.get_legal_moves()
    if depth <= 1:
        def subevalfunc(p):
            return heuristic(moves[p])
    else:
        def subevalfunc(p):
            return evaluate(state.add_tonew(p), not is_max, depth=depth - 1)
    return goal(map(subevalfunc, moves))


def heuristic(pos):
    xx = (N - pos[0]) ** 2
    y = pos[1]
    if y > H: return float('inf')
    if y < 0: return float('-inf')
    return (xx + (H - y) ** 2) ** .5 - (xx + y ** 2) ** .5
