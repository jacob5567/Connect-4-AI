# Jacob Faulk

from GameInstance import GameInstance
from Move import Move
from Connect4 import C4Game
import random


def main():
    head = Move()
    populate(head, 7)
    printGames(head)


def populate(move, depth):
    for i in range(7):
        move.add_child(Move(i, 'O' if move.player == 'X' else 'X', move))
    if (depth > 0):
        for child in move.children:
            populate(child, depth - 1)


def monteCarlo(move):
    if move.children:
        for child in move.children:
            monteCarlo(child)
    else:
        # TODO add until game complete
        # TODO backpropegate results
        move.add_random_child()
        monteCarlo(move.children[0])


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


if __name__ == "__main__":
    main()
