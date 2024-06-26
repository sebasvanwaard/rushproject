import math

from src.algorithms import breadth_first_lukas, depth_first_lukas
from src.game.board import Board
from src.algorithms import a_star, iterative_deepening, a_star_nn, randomize
from src.algorithms import a_star_lukas as lukas

import argparse
import importlib

from src.plots import visualize
import time
import copy

# test = Experiment("gameboards/Rushhour12x12_7.csv")

# test.run_experiment(["randomize"], n=5, random_max_moves=10)

# run_experiment.random_experiment("gameboards/Rushhour12x12_1.csv", "experiments/random", n_experiment=1)

# run_experiment.run_all_boards("gameboards", "experiments/random", n_experiment=1000, max_moves=250000)

# parser = argparse.ArgumentParser(description = "filepath")
# parser.add_argument("board", help = "input file (csv)")
# args = parser.parse_args()
# filepath = args.board

# # test.compare_pos_start_end_board()
# run_random_n_times(filepath, 30)

# ----------------breadth_first -----------------------
# test_board = Board("gameboards/Rushhour6x6_1.csv")

# test_algorithm = breadth_first.Breadth_first(test_board)
# final_board, total_moves, total_states_used, total_states_generated = test_algorithm.run()

# print(f"total moves: {total_moves}, total states used: {total_states_used}, total states generated: {total_states_generated}")
# print(f"moves: {final_board.moves}")
# # final_board.plot()

# visualize.visualize_moves(test_board, final_board.moves)

# # ----------------random_start_depth_first -----------------------
# test_board = Board("gameboards/Rushhour6x6_1.csv")
#
# test_algorithm = depth_first.random_start_depth_first(test_board)
# # test_algorithm = depth_first.Depth_first(test_board)
# start = time.time()
# final_board, total_moves, total_states_used, total_states_generated = test_algorithm.run(2)
# end = time.time() - start
# print(end)
# print(f"total moves: {total_moves}, total states used: {total_states_used}, total states generated: {total_states_generated}")
# print(f"moves: {final_board.moves}")
# final_board.plot()
#
# # visualize.visualize_moves(test_board, final_board.moves)

# # ---------------- branch_n_bound_depth_first -----------------------
# test_board = Board("gameboards/Rushhour9x9_4.csv")

# test_algorithm = depth_first.branch_n_bound_depth_first(test_board)
# # test_algorithm = depth_first.Depth_first(test_board)
# final_board, total_moves, total_states_used, total_states_generated = test_algorithm.run(math.inf, n_goal_state=200)

# print(f"total moves: {total_moves}, total states used: {total_states_used}, total states generated: {total_states_generated}")
# print(f"moves: {final_board.moves}")
# # final_board.plot()

# # visualize.visualize_moves(test_board, final_board.moves)

# ----------------iterative_deepening_depth_first -----------------------
# test_board = Board("gameboards/Rushhour9x9_4.csv")

# test_algorithm = iterative_deepening.Iterative_deepening_with_archive(test_board)
# # test_algorithm = depth_first.Depth_first(test_board)
# final_board, total_moves, total_states_used, total_states_generated = test_algorithm.run(200)

# print(f"total moves: {total_moves}, total states used: {total_states_used}, total states generated: {total_states_generated}")
# print(f"moves: {final_board.moves}")
# final_board.plot()

# visualize.visualize_moves(test_board, final_board.moves)

# # ---------------- a_star -----------------------
# test_board = Board("gameboards/Rushhour6x6_1.csv")

# test_algorithm = a_star.A_star(test_board)
# start = time.time()

# final_board, total_moves, total_states_used, total_states_generated = test_algorithm.run()
# end = time.time() - start

# # cost = test_algorithm.calc_board_cost(test_board)
# # print(cost)
# print(end)
# print(f"total moves: {total_moves}, total states used: {total_states_used}, total states generated: {total_states_generated}")
# print(f"moves: {final_board.moves}")
# # final_board.plot()

# visualize.visualize_moves(test_board, final_board.moves)

# ------------A_star_lukas
# test_board = Board("gameboards/Rushhour6x6_2.csv")
# test_algorithm = lukas.A_star_lukas(test_board)
# start = time.time()

# final_board, total_moves, total_states_used, total_states_generated = test_algorithm.run()
# end = time.time() - start
# print(end)

# print(f"total moves: {total_moves}, total states used: {total_states_used}, total states generated: {total_states_generated}")
# print(f"moves: {final_board.moves}")

# # ---------------- a_star_NN -----------------------
# test_board = Board("gameboards/Rushhour6x6_1.csv")

# test_algorithm = a_star_NN.A_star_NN(test_board)
# start = time.time()

# # print(test_algorithm.calc_cost(test_board))

# final_board, total_moves, total_states_used, total_states_generated = test_algorithm.run()
# end = time.time() - start

# # cost = test_algorithm.calc_board_cost(test_board)
# # print(cost)
# print(end)
# print(f"total moves: {total_moves}, total states used: {total_states_used}, total states generated: {total_states_generated}")
# print(f"moves: {final_board.moves}")
# # final_board.plot()

# # visualize.visualize_moves(test_board, final_board.moves)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Main executable")
	parser.add_argument('boardfile', help='the filepath to the board csv to be solved')
	parser.add_argument('algorithm', help='the algorithm used to solve the board (Breadth_first, Depth_first, A_star, Iterative_deepening ; case sensitive)')
	parser.add_argument('-v', default=False, help='visualize the solution for the specified board')

	args = parser.parse_args()

	board = Board(args.boardfile)

	if args.algorithm == 'Randomize':
		start = time.time()
		final_board, total_moves, total_states_used, total_states_generated = randomize.random_algorithm(copy.deepcopy(board))
		end = time.time()
	else:
		module = importlib.import_module(f'src.algorithms.{args.algorithm.lower()}')
		algorithm_obj = getattr(module, args.algorithm)
		algorithm = algorithm_obj(copy.deepcopy(board))

		start = time.time()
		final_board, total_moves, total_states_used, total_states_generated = algorithm.run()
		end = time.time()


	runtime = end - start

	print(f"The solution to {args.boardfile} was found in {runtime} seconds, using the {args.algorithm} algorithm")
	print(f"The found solution: {final_board.moves}")
	print(f"This solution has {total_moves} moves")
	print(f"In total {total_states_generated} states have been generated, of which {total_states_generated-total_states_used} where duplicates (and thus unused)")
	print(f"A total of {total_states_used} states were visited")

	if args.v:
		visualize.visualize_moves(board, final_board.moves)
