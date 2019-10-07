import random
import math


class Move:

    def __init__(self, col=None, player=None, parent=None):
        self.col = col
        self.player = player
        self.parent = parent
        self.children = []
        self.numSimulations = 0
        self.numWins = 0

    def add_child(self, child):
        self.children.append(child)

    def add_random_child(self):
        self.children.append(
            Move(random.randint(0, 6), 'O' if self.player == 'X' else 'X', self))

    def addRandomChildFromSelection(self, selection):
        self.children.append(
            Move(random.choice(selection), 'O' if self.player == 'X' else 'X', self))

    def addNumSimulations(self, num):
        self.numSimulations += num

    def addNumWins(self, num):
        self.numWins += num

    def numWinsAndSimsStr(self):
        return str(self.numWins) + "/" + str(self.numSimulations)

    def __str__(self):
        return str(self.col) + str(self.player)

    @classmethod
    def calculateUCB1(cls, samples, wins, parentSamples):
        if samples == 0:
            return math.inf
        return (wins / samples) + (math.sqrt(2) * math.sqrt(math.log(parentSamples) / samples))

    def __eq__(self, other):
        return Move.calculateUCB1(self.numSimulations, self.numWins, self.parent.numSimulations) == Move.calculateUCB1(other.numSimulations, other.numWins, other.parent.numSimulations)

    def __ne__(self, other):
        return Move.calculateUCB1(self.numSimulations, self.numWins, self.parent.numSimulations) != Move.calculateUCB1(other.numSimulations, other.numWins, other.parent.numSimulations)

    def __lt__(self, other):
        return Move.calculateUCB1(self.numSimulations, self.numWins, self.parent.numSimulations) < Move.calculateUCB1(other.numSimulations, other.numWins, other.parent.numSimulations)

    def __le__(self, other):
        return Move.calculateUCB1(self.numSimulations, self.numWins, self.parent.numSimulations) <= Move.calculateUCB1(other.numSimulations, other.numWins, other.parent.numSimulations)

    def __gt__(self, other):
        return Move.calculateUCB1(self.numSimulations, self.numWins, self.parent.numSimulations) > Move.calculateUCB1(other.numSimulations, other.numWins, other.parent.numSimulations)

    def __ge__(self, other):
        return Move.calculateUCB1(self.numSimulations, self.numWins, self.parent.numSimulations) >= Move.calculateUCB1(other.numSimulations, other.numWins, other.parent.numSimulations)
