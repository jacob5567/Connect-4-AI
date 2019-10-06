# Jacob Faulk

from GameInstance import GameInstance
from Move import Move
from Connect4 import C4Game
import random


def main():
    head = Move()
    populate(head, 5)


def populate(move, depth):
    for i in range(7):
        move.add_child(Move(i, 'O' if move.player == 'X' else 'X', move))
    if (depth > 0):
        for child in move.children:
            populate(child, depth - 1)


if __name__ == "__main__":
    main()
