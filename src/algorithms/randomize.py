import random

def random_algorithm(board, n):
	"""
	laat de board met auto's random stappen doen voor N keren of totdat het
	een oplossing heeft
	args:
		n: max amount of valid moves that can be made
		print_states: print the initial an final state of the board
		print_end_output: print the difference between starting and ending positions of cars, as well as the total valid and total attempted moves
	"""
	car_names = list(board.cars.keys())
	step_choices = [1, -1]
	moves = []
	solved = False

	valid_moves = 0
	total_moves = 0

	# probeer een n moves te maken
	while valid_moves < n:
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

	return solved, valid_moves, total_moves, board.grid
