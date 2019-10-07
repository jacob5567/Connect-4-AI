# Jacob Faulk

from Move import Move
from Connect4 import C4Game
import random

FIRST_PLAYER = 'O'


def main():
    head = Move(None, 'O', None)
    populate(head, 2)
    for _ in range(500):
        monteCarlo(head)
    # print(head.numWinsAndSimsStr())
    outputToFile(head)
    # printGames(head)


def populate(move, depth):
    for i in range(7):
        move.add_child(Move(i, 'O' if move.player == 'X' else 'X', move))
    if depth > 0:
        for child in move.children:
            populate(child, depth - 1)


def monteCarlo(move, game=None):
    if move.children:
        monteCarlo(max(move.children))
    else:
        game = C4Game()
        parents = []
        parents.append(move)
        currentParent = move.parent
        while currentParent.col is not None:
            parents.append(currentParent)
            currentParent = currentParent.parent
        parents.reverse()
        for m in parents:
            if not game.make_move(m.col):
                return
        backpropegate(move, simulateRestOfGame(game))


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


def backpropegate(move, winner):
    move.addNumSimulations(1)
    move.addNumWins(1 if winner != move.player else 0)
    if move.parent is not None:
        backpropegate(move.parent, winner)


def simulateRestOfGame(game):
    while game.winner() == False:
        game.make_move(random.choice(game.available_moves()))
    return game.winner()


def outputToFile(move):
    if(move.col is not None):
        f = open("outputFile.txt", 'a')
        f.write("Player: " + str(move.player) +
                "; Column: " + str(move.col) + "; ")
        f.write(move.numWinsAndSimsStr())
        f.write('\n')
        f.close()
    for child in move.children:
        outputToFile(child)


if __name__ == "__main__":
    main()
