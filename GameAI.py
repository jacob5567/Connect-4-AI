# Jacob Faulk

from Move import Move
from Connect4 import C4Game
import random
import math
import copy

FIRST_PLAYER = 'O'


def main():
    head = Move(None, 'O', None)
    print("populating...")
    populate(head, 5)
    print("monte carlo")
    for _ in range(10000):
        monteCarlo(head)
    # print(head.numWinsAndSimsStr())
    print("outputting...")
    outputToFile(head)
    print("alphabeta")
    print(alphabeta(head, 2, -math.inf, math.inf, 'X'))
    # printGames(head)
    print("generating lookup table..")
    makeLookupTable(head, C4Game())


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


def alphabeta(move, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or not move.children:
        return Move.calculateUCB1(move.numSimulations, move.numWins, move.parent.numSimulations)
    if move.player == maximizingPlayer:
        value = -math.inf
        for child in move.children:
            value = max(value, alphabeta(child, depth - 1, alpha,
                                         beta, 'O' if maximizingPlayer == 'X' else 'X'))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = math.inf
        for child in move.children:
            value = min(value, alphabeta(child, depth -
                                         1, alpha, beta, maximizingPlayer))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value


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


def makeLookupTable(move, game):
    f = open("JacobFaulkLookupTable.txt", 'a')
    f.write("Player: " + str(move.player) + '\n')
    if move.col is not None:
        game.make_move(move.col)
    f.write(str(game))
    if move.children:
        f.write('\n' + str(max(move.children).col) + '\n')
    else:
        f.write("\nrandom choice\n")
    f.close()
    for child in move.children:
        makeLookupTable(child, copy.deepcopy(game))


if __name__ == "__main__":
    main()
