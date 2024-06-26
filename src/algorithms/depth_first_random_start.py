
from .algorithm import Algorithm

import copy
import math
import random

import time

class Depth_first_random_start(Algorithm):
    """
	This is a subclass of the class Algorithm and entails the depth first algorithm with a random start. 
	"""

    def __init__(self, board):
        """
		The subclass Depth first with a random start initializes everything from the parent class Algorithm.
		"""

        super().__init__(board)

    def run(self, max_random_choice_depth=0, max_depth=math.inf, max_time=math.inf):
        """
        run a depth first search for a solution of the given board. Integrated stack.
		args:
			max_random_choice_depth: the maximum random choice is the maximum of how many times a random choice is made. Defaults to 0. 
            max_depth: the maximum depth the algorithm will search before giving up. Defaults to math.inf.
            max_time: the maximum time the algorithm will search before giving up. Defaults to math.inf.
        returns:
			state: the board of the final state
            state_depth: the depth of the board of the final state
			total_states_used: the total states visited before the solution was found
			total_states_generated: the total amount of states generated before the solution was found
        """

        start_state = copy.deepcopy(self.board)
        stack = [start_state]

        start_time = time.time()

        random_choice = 0
        possible_states = []
        while len(stack) > 0 and start_time - time.time() < max_time:
            state = stack.pop()
            self.total_states_used += 1

            if self.is_goal_state(state):
                print("joepie")
                return (state, state.depth, self.total_states_used, self.total_states_generated)

            if state.depth < max_depth:
                for possible_state in self.get_actions(state):
                    self.total_states_generated += 1
                    if not self.is_in_archive(possible_state):
                        possible_states.append(possible_state)

                if random_choice < max_random_choice_depth:
                    random.shuffle(possible_states)
                    stack.extend(possible_states)
                    random_choice += 1
                    possible_states.clear()
                else:
                    stack.extend(possible_states)
                    possible_states.clear()

        print(f"no solution found within {max_depth} depth")

        return False
