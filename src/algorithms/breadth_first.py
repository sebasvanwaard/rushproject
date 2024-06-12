from .algorithm import Algorithm

import copy
import math

class Breadth_first(Algorithm):
	def __init__(self, board):
		super().__init__(board)

	def run(self, max_depth=math.inf):
		"""
		run a breadth first search for a solution of the given board.
		args:
			max_depth: the maximum depth the algorithm will search before giving up. Defaults to math.inf
		returns:
			state: the board of the final state
			moves: the total moves needed to solve the board
			total_states: the total amount of states visited before the solution was found
		"""
		possible_states = [copy.deepcopy(self.board)]
		temp_states = []
		moves = 0
		total_states = 0

		while moves < max_depth:	
			print(len(possible_states))
			for state in possible_states:
				unique_id = state.get_unique_id()
				if unique_id not in self.state_archive:
					self.state_archive.add(unique_id)
					total_states += 1
					if state.cars["X"].x_pos == self.board.shape - 2:
						print("joepie")
						return (state, moves, total_states)
					
					for possible_state in self.get_actions(state):
						temp_states.append(possible_state)
	
			possible_states.clear()
			possible_states = copy.deepcopy(temp_states)
			temp_states.clear()
			moves += 1
		
		print(f"no solution found within {max_depth} moves")

		return False

		

