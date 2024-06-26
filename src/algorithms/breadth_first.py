# importing
from .algorithm import Algorithm

import copy
import math
import queue

# Breadth first subclass from the Algorithm parent class
class Breadth_first(Algorithm):
	"""
	This is a subclass of the class Algorithm and entails the breadth first algorithm. 
	"""

	def __init__(self, board):
		"""
		The subclass Breadth first initializes everything from the parent class Algorithm.
		"""

		super().__init__(board)

	def run(self, max_depth=math.inf):
		"""
		run a breadth first search for a solution of the given board. Integrated queue.
		args:
			max_depth: the maximum depth the algorithm will search before giving up. Defaults to math.inf
		returns:
			state: the board of the final state
            state_depth: the depth of the board of the final state
			total_states_used: the total states visited before the solution was found
			total_states_generated: the total amount of states generated before the solution was found
		"""

		# queue the possible states
		possible_states = queue.Queue()
		possible_states.put(copy.deepcopy(self.board))

		# as long as there are possible states
		while not possible_states.empty():

			# get the first possible state from the queue
			state = possible_states.get()

			# update the states used
			self.total_states_used += 1

			# check whether the puzzle is solved, if so use return the relevant information
			if self.is_goal_state(state):
				print("joepie")					
				return (state, state.depth, self.total_states_used, self.total_states_generated)

			# create the new possible states
			for possible_state in self.get_actions(state):
				self.total_states_generated += 1

				# check whether the new possible states are already in the archive, if not add them to the queue
				if not self.is_in_archive(possible_state):
					possible_states.put(possible_state)

		# print when no solution is found within max_depth and return false
		print(f"no solution found within {max_depth} moves")
		return False
