# Jacob Faulk

from GameInstance import GameInstance
from Move import Move
from Connect4 import C4Game
import random


def main():
    head = Move()
    populate(head, 5)
    monteCarlo(head)
    head.printNumWinsAndSims()
    # printGames(head)


def populate(move, depth):
    for i in range(7):
        move.add_child(Move(i, 'O' if move.player == 'X' else 'X', move))
    if (depth > 0):
        for child in move.children:
            populate(child, depth - 1)


def monteCarlo(move, game=None):
    if move.children:
        for child in move.children:
            monteCarlo(child)
    else:
        game = C4Game()
        parents = []
        parents.append(move)
        currentParent = move.parent
        while (currentParent.col is not None):
            parents.append(currentParent)
            currentParent = currentParent.parent
        parents.reverse()
        for m in parents:
            if not game.make_move(m.col):
                return
        backpropegate(move, 1, 1 if simulateRestOfGame(game) == 'X' else 0)


def printGames(move):
    if move.children:
        for child in move.children:
            printGames(child)
    else:
        parents = []
        parents.append(move)
        currentParent = move.parent
        while (currentParent.col is not None):
            parents.append(currentParent)
            currentParent = currentParent.parent
        parents.reverse()
        game = C4Game()
        for m in parents:
            if not game.make_move(m.col):
                return
        print(game)


def backpropegate(move, numSimulations, numWins):
    move.addNumSimulations(numSimulations)
    move.addNumWins(numWins)
    if move.parent is not None:
        backpropegate(move.parent, numSimulations, numWins)


def simulateRestOfGame(game):
    while (game.winner() == False):
        game.make_move(random.choice(game.available_moves()))
    return game.winner()


if __name__ == "__main__":
    main()
