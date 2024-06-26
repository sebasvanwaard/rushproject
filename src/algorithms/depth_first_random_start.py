from .algorithm import Algorithm

import copy
import math
import random

import time

class Depth_first_random_start(Algorithm):
    def __init__(self, board):
        super().__init__(board)

    def run(self, max_random_choice_depth=0, max_depth=math.inf, max_time=math.inf):
        """
        run a depth first search for a solution of the given board. It looks for the best solution by never looking deeper 
        than the best solution already found. Using an integrated stack. This variation on depth first search starts its search at a random
        start state, in contrast to regular depth first (which always starts at the same state).
		args:
			max_depth: the maximum depth the algorithm will search before giving up. Defaults to math.inf.
            max_time: the maximum time the algorithm will search before giving up. Defaults to math.inf. 
            n_goal_state: the maximum goal states one would visit. Defaults to 200. 
		returns:
			best_state: the board of the best final state
            best_state_depth: the depth of the board of the best final state
			total_states_used: the total states visited before the solution was found
			total_states_generated: the total amount of states generated before the solution was found
        """

        start_state = copy.deepcopy(self.board)
        stack = [start_state]

        start_time = time.time()

        random_choice = 0
        possible_states = []
        while len(stack) > 0 and time.time() - start_time < max_time:
            state = stack.pop()
            self.total_states_used += 1

            if self.is_goal_state(state):
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

        return False
