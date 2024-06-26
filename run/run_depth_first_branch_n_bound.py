
# --------------------------------------- Depth First ------------------------------------------ #
"""
Run your very own Depth First algorithm!
Change the gameboard you want to solve by changing the board_path variable
Change the depth (max amount of moves) the board has to be solved by changing max_depth
Change the maximum amount of solutions are visited before settling for the best one by changing max_solutions

Gameboards up to dimensions of 9x9 can be solved by this guy

by: Lukas, Anouk en Sebas
"""
# ---------------------------------------------------------------------------------------------- #

from ..src.game.board import Board
from ..src.plots.visualize import visualize_moves
from ..src.algorithms.depth_first_branch_n_bound import Depth_first_branch_n_bound

import time

board_path = "../gameboards/Rushhour6x6_1.csv"
max_depth = 50
max_solutions = 200

# Initialize the gameboard
test_board = Board(board_path)

# Initialize the algorithm
test_algorithm = Depth_first_branch_n_bound(test_board)

# Run the algorithm
start = time.time()
final_board, total_moves, total_states_used, total_states_generated = test_algorithm.run(max_depth, n_goal_state=max_solutions)
end = time.time() - start

# Print the results
print(f"Solution found in {end} seconds")
print(f"Total moves: {total_moves}, total states used: {total_states_used}, total states generated: {total_states_generated}")
print(f"Toves: {final_board.moves}")

# Plot the final board
final_board.plot()

# Play the visualization of the found solution (start by closing the first window)
visualize_moves(test_board, final_board.moves)
