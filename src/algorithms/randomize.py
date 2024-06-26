import random
import math
import time

def random_algorithm(board, max_moves=math.inf, max_time = math.inf):
	"""
	laat de board met auto's random stappen doen voor N keren of totdat het
	een oplossing heeft
	args:
		board: the starting board to be solved
		max_moves: the max 
	"""
	car_names = list(board.cars.keys())
	step_choices = [1, -1]
	moves = []
	solved = False

	valid_moves = 0
	total_moves = 0

	start_time = time.time()

	# probeer een n moves te maken
	while valid_moves < max_moves and start_time - time.time() < max_time:
		car = board.cars[car_names[random.randint(0, len(car_names)-1)]]
		step = random.choice(step_choices)
		# maak move, als dit succesvol append naar moves en update het board. Tel een valid move
		if car.move(step, board.grid):
			moves.append((car.name, step))
			board.update()
			valid_moves += 1

		total_moves += 1
		
		# als de rode auto op de uit positie is het spel is klaar
		if board.cars['X'].x_pos == board.shape - 2:
			solved = True
			break

	return board, valid_moves, total_moves
