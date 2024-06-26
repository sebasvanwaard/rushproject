
# ---------------------------------------- Randomize ------------------------------------------- #
"""
Run your very own breadth first algorithm!
Change the gameboard you want to solve by changing the board_path variable
but be careful this old chap will only solve 6x6 boards in at a reasonable pace

by: Lukas, Anouk en Sebas
"""
# ---------------------------------------------------------------------------------------------- #

from ..src.game.board import Board
from ..src.plots.visualize import visualize_moves
from ..src.algorithms.randomize import random_algorithm

import time

board_path = "../gameboards/Rushhour6x6_1.csv"

# Initialize the gameboard
test_board = Board(board_path)

# Run the algorithm
start = time.time()
final_board, total_moves, total_states_used, total_states_generated = random_algorithm.run()
end = time.time() - start

# Print the results
print(f"Solution found in {end} seconds")
print(f"Total moves: {total_moves}, total states used: {total_states_used}, total states generated: {total_states_generated}")
print(f"Toves: {final_board.moves}")

# Plot the final board
final_board.plot()
