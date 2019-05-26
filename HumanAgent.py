from Agent import Agent


class HumanAgent(Agent):

    def play(self, state, legalmoves):
        print(' '.join(legalmoves))
        i = input('>')
        while i not in legalmoves: i = input('>')
        return i
