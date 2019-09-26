import copy


class GameInstance:

    ROWS = 6
    COLS = 7

    board = ['.'] * ROWS

    def __init__(self, col=None, player=None, parent=None):
        if parent == None:
            self.board = [['.' for c in range(self.COLS)]
                          for r in range(self.ROWS)]
            self.parent = None
        else:
            self.parent = parent
            self.board = copy.deepcopy(parent.board)
            self.makeMove(col, player)

    def makeMove(self, col, player):
        if col < 0 or col >= self.COLS:  # if out of range, not a valid move
            return False
        if self.board[0][col] != '.':  # if column is full, not a valid move
            return False
        row = self.ROWS - 1  # loop from bottom row up, looking for first open row to place token
        while self.board[row][col] != '.':
            row -= 1
        self.board[row][col] = player
        return True

    def __str__(self):
        s = ""
        for row in range(self.ROWS):
            for col in range(self.COLS):
                s += self.board[row][col]
            s += "\n"
        return s[:-1]  # remove trailing newline and return
