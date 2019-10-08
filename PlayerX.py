# Jacob Faulk

from Connect4 import C4Game
import copy
import math
import random
SCORE_BONUS_4 = 10000
SCORE_DETRACTION_4 = 10000
SCORE_BONUS_3 = 500
SCORE_BONUS_2 = 200
SCORE_DETRACTION_3 = 400
SCORE_DETRACTION_2 = 5
PREFER_HIGHER_ROWS_MULTIPLIER = 10
PREFER_CENTRAL_COLUMN_MULTIPLIER = 3
PREFER_NEARBY_COLUMNS_MULTIPLIER = 1
ALPHA_BETA_DEPTH_LEVEL = 7

def load_player(player):
    # My AI is calculating the play it should make live, and is thus not using a lookup table
    return None


def next_move(board, player, lookup_table):
    col = alphabeta(board, ALPHA_BETA_DEPTH_LEVEL, -math.inf, math.inf, True, player)[1]
    return col


def getBestMove(board, player):
    maxScore = -math.inf
    colChoice = random.choice(board.available_moves())
    for col in board.available_moves():
        newBoard = copy.deepcopy(board)
        newBoard.make_move(col)
        score = scoreBoard(newBoard, player)
        if score > maxScore:
            maxScore = score
            colChoice = col
    return colChoice

def alphabeta(board, depth, alpha, beta, maximizingPlayer, player):
    if depth == 0 or board.winner():
        if depth != 0:
            if board.winner() == player:
                return (999999999, None)
            elif board.winner() == 'O' if player == 'X' else 'X':
                return (-999999999, None)
            else:
                return (scoreBoard(board, player), None)
        else:
            return (scoreBoard(board, player), None)
    else:
        if maximizingPlayer:
            value = -math.inf
            bestColumn = random.choice(board.available_moves())
            for col in board.available_moves():
                boardCopy = copy.deepcopy(board)
                boardCopy.make_move(col)
                score = alphabeta(boardCopy, depth - 1, alpha, beta, False, player)[0]
                if score > value:
                    value = score
                    bestColumn = col
                alpha = max(value, alpha)
                if alpha >= beta:
                    break
            return (value, bestColumn)
        else:
            value = math.inf
            bestColumn = random.choice(board.available_moves())
            for col in board.available_moves():
                boardCopy = copy.deepcopy(board)
                boardCopy.make_move(col)
                score = alphabeta(boardCopy, depth - 1, alpha, beta, True, player)[0]
                if score < value:
                    value = score
                    bestColumn = col
                beta = min(value, beta)
                if alpha >= beta:
                    break
            return (value, bestColumn)



def scoreBoard(game, player):
    score = 0
    gameBoard = game.board

    # prefer central column
    score += [r[3] for r in gameBoard].count(player) * PREFER_CENTRAL_COLUMN_MULTIPLIER

    # prefer closer to center columns
    score += [r[2] for r in gameBoard].count(player) * PREFER_NEARBY_COLUMNS_MULTIPLIER
    score += [r[4] for r in gameBoard].count(player) * PREFER_NEARBY_COLUMNS_MULTIPLIER

    # horizontal check
    for row in range(6):
        currentRow = gameBoard[row]
        for col in range(4):
            selection = currentRow[col:col + 4]
            score += scoreSelection(selection, player) * (row / PREFER_HIGHER_ROWS_MULTIPLIER) # weights higher sets better
    # vertical check
    for col in range(7):
        currentCol = [r[col] for r in gameBoard]
        for row in range(3):
            selection = currentCol[row:row + 4]
            score += scoreSelection(selection, player)
    # diagonals
    for row in range(3):
        for col in range(4):
            selection = [gameBoard[row + i][col + i] for i in range(4)]
            score += scoreSelection(selection, player)
    for row in range(3):
        for col in range(4):
            selection = [gameBoard[row + 3 - i][col + i] for i in range(4)]
            score += scoreSelection(selection, player)

    return score


def scoreSelection(selection, player):
    score = 0
    if selection.count(player) == 4:
        score += SCORE_BONUS_4
    elif selection.count(player) == 3 and selection.count('O' if player == 'X' else 'X') == 0:
        score += SCORE_BONUS_3
    elif selection.count(player) == 2 and selection.count('O' if player == 'X' else 'X') == 0:
        score += SCORE_BONUS_2
    if selection.count('O' if player == 'X' else 'X') == 4:
        score -= SCORE_DETRACTION_4
    elif selection.count('O' if player == 'X' else 'X') == 3 and selection.count(player) == 0:
        score -= SCORE_DETRACTION_3
    elif selection.count('O' if player == 'X' else 'X') == 2 and selection.count(player) == 0:
        score -= SCORE_DETRACTION_2
    return score
