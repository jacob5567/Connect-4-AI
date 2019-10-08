import random
import math
from Connect4 import C4Game


class GameState:

    PLAYER_PIECE = 'X'
    OTHER_PIECE = 'O'

    def __init__(self, moveSequence=[], parent=None):
        self.moveSequence = moveSequence[:]
        if moveSequence:
            self.col = moveSequence[-1]
        else:
            self.col = None
        self.children = []
        self.parent = parent
        self.sims = 0
        self.wins = 0
        self.score = 0
        self.game = C4Game()
        for move in moveSequence:
            self.game.make_move(move)

    def add_child(self, child):
        self.children.append(child)

    def addMoveAsChild(self, col):
        self.children.append(GameState(self.moveSequence + [col], self))

    def addMoveFromSelection(self, selection):
        self.addMoveAsChild(random.choice(selection))

    def heuristic(self):
        gameBoard = self.game.board
        score = 0
        # horizontal check
        for row in range(6):
            currentRow = [i for i in gameBoard[row]]
            for col in range(3):
                selection = currentRow[col:col + 4]
                score += GameState.scoreSelection(selection)
        # vertical check
        for col in range(7):
            currentCol = [i for i in gameBoard[:, col]]
            for row in range(4):
                selection = currentCol[row:row + 4]
                score += GameState.scoreSelection(selection)
        # diagonals
        for row in range(3):
            for col in range(4):
                selection = [gameBoard[row + i][col + i] for i in range(4)]
                score += GameState.scoreSelection(selection)
        for row in range(3):
            for col in range(4):
                selection = [gameBoard[row + 3 - i][col + i] for i in range(4)]
                score += GameState.scoreSelection(selection)

        return score

    @classmethod
    def scoreSelection(cls, selection):
        score = 0
        if selection.count(GameState.PLAYER_PIECE) == 4:
            score += 1000
        if selection.count(GameState.PLAYER_PIECE) == 3 and selection.count(GameState.OTHER_PIECE) == 0:
            score += 100
        if selection.count(GameState.PLAYER_PIECE) == 2 and selection.count(GameState.OTHER_PIECE) == 0:
            score += 50
        if selection.count(GameState.OTHER_PIECE) == 4:
            score -= 1000
        if selection.count(GameState.OTHER_PIECE) == 3 and selection.count(GameState.PLAYER_PIECE) == 0:
            score -= 100
        if selection.count(GameState.OTHER_PIECE) == 2 and selection.count(GameState.PLAYER_PIECE) == 0:
            score -= 50
        return score

    # def addSims(self, num):
    #     self.sims += num
    #     if self.parent is not None:
    #         self.score = GameState.calculatescore(
    #             self.sims, self.wins, self.parent.sims)
    #     else:
    #         self.score = math.inf

    # def addWins(self, num):
    #     self.wins += num
    #     if self.parent is not None:
    #         self.score = GameState.calculatescore(
    #             self.sims, self.wins, self.parent.sims)
    #     else:
    #         self.score = math.inf

    # @classmethod
    # def calculatescore(cls, samples, wins, parentSamples):
    #     if samples == 0 or parentSamples == 0:
    #         return math.inf
    #     return (wins / samples) + (math.sqrt(2) * math.sqrt(math.log(parentSamples) / samples))

    def gameString(self):
        return str(self.game)

    def numWinsAndSimsStr(self):
        return str(self.wins) + "/" + str(self.sims)

    def __str__(self):
        return ''.join(self.moveSequence)

    def __eq__(self, other):
        return self.score == other.score

    def __ne__(self, other):
        return self.score != other.score

    def __lt__(self, other):
        return self.score < other.score

    def __le__(self, other):
        return self.score <= other.score

    def __gt__(self, other):
        return self.score > other.score

    def __ge__(self, other):
        return self.score >= other.score
