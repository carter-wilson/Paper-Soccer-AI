from Agent import Agent

from evaluation import evaluate


class ArtificialAgent(Agent):

    def play(self, state):
        print('thinking ...')
        return evaluate(state, self.is_top)

