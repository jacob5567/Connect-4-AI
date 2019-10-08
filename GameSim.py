# Jacob Faulk

from GameState import GameState
from Connect4 import C4Game
import random
import math
import copy

MONTE_CARLO_SIMS = 10000
PLAYER_PIECE = 'X'
OTHER_PIECE = 'O'


def main():
    root = GameState()
    populate(root, 2)
    for _ in range(MONTE_CARLO_SIMS):
        monteCarlo(root)
    outputToFile(root)


def populate(node, depth):
    for move in node.game.available_moves():
        node.addMoveAsChild(move)
    if depth > 0:
        for child in node.children:
            populate(child, depth - 1)


def monteCarlo(node):
    if node.children:
        monteCarlo(max(node.children))
    else:
        backpropegate(node, simulateRestOfGame(node))


def simulateRestOfGame(node):
    while node.game.winner() == False:
        node.game.make_move(random.choice(node.game.available_moves()))
    return node.game.winner()


def backpropegate(node, winner):
    node.addSims(1)
    node.addWins(1 if winner == node.game.nextPlayer else 0)
    if node.parent is not None:
        backpropegate(node.parent, winner)


def minimax(node, depth, maximizingPlayer):
    if depth == 0 or node.game.winner():
        if depth != 0:
            if node.game.winner() == PLAYER_PIECE:
                return 1000000
            elif node.game.winner() == OTHER_PIECE:
                return -1000000
            else:
                return 0
        else:
            return node.heuristic()
    if maximizingPlayer:
        newScore = -math.inf
        column = random.choice(node.game.available_moves())
        for col in node.game.available_moves():
            node.addMoveAsChild(col)
            newScore = minimax(node.children.index(col), depth - 1, False)
    else:
        newScore = math.inf
        column = random.choice(node.game.available_moves())
        for col in node.game.available_moves():
            node.addMoveAsChild(col)
            newScore = minimax(node.children[0], depth - 1, False)


def outputToFile(move):
    f = open("outputFile.txt", 'a')
    f.write("Player: " + str('X' if move.game.nextPlayer == 'O' else 'O') +
            "; Column: " + str(move.col) + "; ")
    f.write(move.numWinsAndSimsStr())
    f.write('\n')
    f.close()
    for child in move.children:
        outputToFile(child)


if __name__ == "__main__":
    main()
