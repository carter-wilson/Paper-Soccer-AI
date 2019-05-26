from ArtificialAgent import ArtificialAgent
from Display import Display
from HumanAgent import HumanAgent
from State import State


class Game:
    display = None

    def __init__(self, n, m, g, nhp, display=True):
        self.n, self.m, self.g = n, m, g
        self.agents = [HumanAgent(not i) if 2 - nhp - i > 0 else ArtificialAgent(not i) for i in range(2)]
        if display:
            self.display = Display(n, m, g)
            self.display.startupdateloop()
        self.state = State(n, m, g)

    def play(self):
        done = False
        while not done:
            for agent in self.agents:
                move = agent.play(self.state)
                self.state.add(move)
                self.display.addmove(move)
                if self.state.finished():
                    print('done')
                    done = True
                    break
