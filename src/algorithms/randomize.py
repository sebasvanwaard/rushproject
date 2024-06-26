import random
import math
import time
import copy

def random_algorithm(start_board, max_moves=math.inf, max_time = math.inf):
	"""
	laat de board met auto's random stappen doen voor N keren of totdat het
	een oplossing heeft
	args:
		board: the starting board to be solved
		max_moves: the max 
	returns:
		board: the final board state
		valid_moves: number of moves before finding the final state
		total_moves: number of moves before finding the final state
		total_moves: number of moves before finding the final state
	"""
	board = copy.deepcopy(start_board)
	car_names = list(board.cars.keys())
	step_choices = [1, -1]
	moves = []

	valid_moves = 0
	total_moves = 0

	start_time = time.time()

	while valid_moves < max_moves and time.time() - start_time < max_time:
		car = board.cars[car_names[random.randint(0, len(car_names)-1)]]
		step = random.choice(step_choices)

		if car.move(step, board.grid):
			moves.append((car.name, step))
			board.update()
			valid_moves += 1

		total_moves += 1
		
		if board.cars['X'].x_pos == board.shape - 2:
			break

	return board, valid_moves, total_moves, total_moves
