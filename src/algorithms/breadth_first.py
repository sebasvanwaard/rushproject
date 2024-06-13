from .algorithm import Algorithm

import copy
import math
import queue

class Breadth_first(Algorithm):
	def __init__(self, board):
		super().__init__(board)

	def run(self, max_depth=math.inf):
		"""
		run a breadth first search for a solution of the given board. Integrated queue.
		args:
			max_depth: the maximum depth the algorithm will search before giving up. Defaults to math.inf
		returns:
			state: the board of the final state
			moves: the total moves needed to solve the board
			total_states: the total amount of states visited before the solution was found
		"""
		possible_states = queue.Queue()
		possible_states.put(copy.deepcopy(self.board))

		moves = 0
		total_states_used = 0
		total_states_generated = 0
		goal_state = self.board.shape - 2

		while not possible_states.empty():
				state = possible_states.get()
				total_states_used += 1
				if state.cars["X"].x_pos == goal_state:
					print("joepie")
					return (state, state.depth, total_states_used, total_states_generated)

				for possible_state in self.get_actions(state):
					unique_id = possible_state.get_unique_id()
					total_states_generated += 1
					if unique_id not in self.state_archive:
						self.state_archive.add(unique_id)
						possible_states.put(possible_state)

		print(f"no solution found within {max_depth} moves")

		return False
	