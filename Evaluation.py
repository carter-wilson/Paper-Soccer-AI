class Evaluation:
    ...

# minimax renamed as top-bottom
# eval_top(state) := min([eval_bottom(state+i) for i in legal_move]) + 1
# eval_x(winning state) := 0
# eval_x(loosing state) := inf
# eval_x(reached depth limit) := sqrt(2)*squarelength + remainder
# don't forget to alpha-beta prune

# should probably do symmetry: eval_bottom := eval_top(state.shifted)

# cache with dict saved to pickle
# maps state to evaluation
