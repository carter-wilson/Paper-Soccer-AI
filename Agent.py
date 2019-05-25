class Agent:
    def __init__(self, side):
        self.invert = side

    # Converts global move to relative move and vice versa
    def relative_move(self, move):
        return (move + 4) % 8 if self.invert else move
