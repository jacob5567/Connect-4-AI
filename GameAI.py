# Jacob Faulk

from GameInstance import GameInstance


def main():
    firstMove = GameInstance()
    print(firstMove)
    secondMove = GameInstance(2, 'X', firstMove)
    print(secondMove)
    thirdMove = GameInstance(4, 'O', secondMove)
    print(thirdMove)
    print(thirdMove.parent)
    print(firstMove)


if __name__ == "__main__":
    main()
