# Connect 4 AI
There is no lookup table for this project; all the work is done in the PlayerX and PlayerO files. This allows for less work to be done overall. The parameters for the algorithm can be changed by changing the constants on the top of each file.

`SCORE_BONUS_4` is the bonus given to the score if the AI player has a 4-in-a-row on a given board.

`SCORE_DETRACTION_4` is the amount of points taken away from the score score if the other player has a 4-in-a-row on a given board.

`SCORE_BONUS_3` is the bonus given to the score if the AI player has a 3-in-a-row on a given board.

`SCORE_BONUS_2` is the bonus given to the score if the AI player has a 3-in-a-row on a given board.

`SCORE_DETRACTION_3` is the amount of points taken away from the score score if the other player has a 3-in-a-row on a given board.

`SCORE_DETRACTION_2` is the amount of points taken away from the score score if the other player has a 2-in-a-row on a given board.

`PREFER_HIGHER_ROWS_MULTIPLIER` is *inverse to* the amount by which the bonus points for a 3-in-a-row is multiplied for successively higher.

`PREFER_CENTRAL_COLUMN_MULTIPLIER` is the amount by which the AI prefers a central move to an edge move.

`PREFER_NEARBY_COLUMNS_MULTIPLIER` is the amount by which the AI prefers a move in a column adjacent to the center column.

`ALPHA_BETA_DEPTH_LEVEL` is the number of levels deeps the alpha-beta pruning tree goes. I found that 6 terminates in less than 3 seconds at the most, and 7 terminates in less than 8 seconds at the most.

The most optimal parameters are the ones that are preset in the files.

The "Connect4.py" file that has been provided must be in the folder with the PlayerX and PlayerO files for them to work.
