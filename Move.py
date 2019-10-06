class Move:

    def __init__(self, col=None, player=None, parent=None):
        self.col = col
        self.player = player
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return str(self.col) + str(self.player)
