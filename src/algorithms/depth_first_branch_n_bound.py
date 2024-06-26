
from .algorithm import Algorithm

import math
import copy
import time

class Depth_first_branch_n_bound(Algorithm):
    """
	This is a subclass of the class Algorithm and entails the depth first algorithm with a branch and bound. 
	"""

    def __init__(self, board):
        """
		The subclass Depth first with brach and bound initializes everything from the parent class Algorithm.
		"""
        
        super().__init__(board)

    def run(self, max_depth=math.inf, max_time=math.inf, n_goal_state = 200):
        """
        run a depth first search for a solution of the given board. It looks for the best solution by never looking deeper 
        than the best solution already found. Using an integrated stack. 
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

        best_state_depth = math.inf
        best_state = None
        goal_states_visited = 0

        start_time = time.time()

        while len(stack) > 0 and time.time() - start_time < max_time:
            state = stack.pop()
            self.total_states_used += 1

            if self.is_goal_state(state):
                goal_states_visited += 1

                if state.depth < best_state_depth:
                    best_state_depth = state.depth
                    best_state = state
                    max_depth = state.depth

                if goal_states_visited == n_goal_state:
                    return (best_state, best_state.depth, self.total_states_used, self.total_states_generated)

            if state.depth < max_depth:
                for possible_state in self.get_actions(state):
                    self.total_states_generated += 1
                    if not self.is_in_archive(possible_state):
                        stack.append(possible_state)

        if best_state is not None:
            return (best_state, best_state.depth, self.total_states_used, self.total_states_generated)
        else:
            print(f"no solution found within {max_depth} depth")

            return False
