# Jacob Faulk

from GameInstance import GameInstance
from Move import Move
from Connect4 import C4Game
import random


def main():
    firstMove = Move()
    for i in range(7):
        firstMove.add_child(Move(i, 'X', firstMove))

    for i in range(7):
        for j in range(7):
            firstMove.children[i].add_child(
                Move(j, 'O', firstMove.children[i]))

    game = C4Game()
    currentMove = firstMove
    while len(currentMove.children) > 0:
        print(currentMove)
        # print(game)
        nextMove = random.choice(currentMove.children)
        game.make_move(nextMove.col)
        currentMove = nextMove
    print(game)


if __name__ == "__main__":
    main()
