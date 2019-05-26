from Agent import Agent

from evaluation import evaluate


class ArtificialAgent(Agent):

    def play(self, state):
        print('thinking ...')
        goal = max if self.is_top else min
        options = {evaluate(state.add_tonew(move), not self.is_top): move for move in state.get_legal_moves()}
        return options[goal(options)]

