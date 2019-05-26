from Agent import Agent


class HumanAgent(Agent):

    def __init__(self, is_top):
        super().__init__(is_top)
        print('You are trying to score in the ' + ('top' if is_top else 'bottom') + ' goal.')

    def play(self, state):
        legalmoves = state.get_legal_moves()
        print(' '.join(legalmoves))
        i = input('> ')
        while i not in legalmoves: i = input('>')
        return i
