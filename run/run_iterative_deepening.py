
# ------------------------------------- Iterative Deepening ------------------------------------- #
"""
Run your very own A-start algorithm!
Change the gameboard you want to solve by changing the board_path variable
Change the maximum depth it searches by changing max depth value

by: Lukas, Anouk en Sebas
"""
# ----------------------------------------------------------------------------------------------- #

from ..src.game.board import Board
from ..src.plots.visualize import visualize_moves
from ..src.algorithms.iterative_deepening import Iterative_deepening

import time
import math

board_path = "../gameboards/Rushhour6x6_1.csv"
max_depth = math.inf

# Initialize the gameboard
test_board = Board(board_path)

# Initialize the algorithm
test_algorithm = Iterative_deepening(test_board, max_depth)

# Run the algorithm
start = time.time()
final_board, total_moves, total_states_used, total_states_generated = test_algorithm.run()
end = time.time() - start

# Print the results
print(f"Solution found in {end} seconds")
print(f"Total moves: {total_moves}, total states used: {total_states_used}, total states generated: {total_states_generated}")
print(f"Toves: {final_board.moves}")

# Plot the final board
final_board.plot()

# Play the visualization of the found solution (start by closing the first window)
visualize_moves(test_board, final_board.moves)
