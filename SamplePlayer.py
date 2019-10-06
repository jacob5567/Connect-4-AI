"""
A sample implementation of PlayerX/PlayerO code to allow students who have not programmed in Python before to
participate in the tournament -- simply output your lookup table in the same format used as in Sample.txt
"""

def load_player(player):
    # open file containing stored lookup table
    file = open("Sample.txt")
    table = {}  # create a dictionary to store moves for the player whose character was passed in

    while True:
        who = file.readline()  # line formatted as "Player *\n" where * is either X or O
        if not who:  # if just read an empty string because reached end of file, then break
            break
        board_config = ""
        for row in range(6):  # read next 6 lines as layout of a board
            line = file.readline()
            board_config += line
        board_config = board_config[:-1]  # strip off final endline
        move = int(file.readline())  # read the recommended move

        if player in who:  #  if this recommendation is for the player we are loading, add it to the table
            table[board_config] = move

    return table

def next_move(board, player, lookup_table):
    # since we only stored moves for our player, will ignore player parameter
    key = str(board)  # convert table into a string to match key format used in lookup table
    if key in lookup_table:
        return lookup_table[key]
    else:
        return None
