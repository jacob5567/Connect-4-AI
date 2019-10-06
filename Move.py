import random


class Move:

    def __init__(self, col=None, player=None, parent=None):
        self.col = col
        self.player = player
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_random_child(self):
        self.children.append(
            Move(random.randint(0, 6), 'O' if self.player == 'X' else 'X', self))

    def __str__(self):
        return str(self.col) + str(self.player)
