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
