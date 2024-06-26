from .algorithm import Algorithm

import copy
import math
import time

class Iterative_deepening(Algorithm):
    """
	This is a subclass of the class Algorithm and entails the breadth first algorithm. 
	"""
    
    def __init__(self, board):
        """
		The subclass Depth first initializes everything from the parent class Algorithm.
		"""

        super().__init__(board)

    def run(self, max_depth=200, max_time=math.inf):
        """
        run a iterative deepening search, combining depth first and breadth first techniques, for a solution of the given board. 
        Intergrated stack.
		args:
			max_depth: the maximum depth the algorithm will search before giving up. Defaults to math.inf.
		returns:
			state: the board of the final state
            state_depth: the depth of the board of the final state
			total_states_used: the total states visited before the solution was found
			total_states_generated: the total amount of states generated before the solution was found
        """

        goal_state = self.board.shape - 2
        start_time = time.time()

        _iterative_depth = 1

        while _iterative_depth in range(1, max_depth) and (time.time() - start_time) < max_time:
            state_dict = {}
            start_state = copy.deepcopy(self.board)
            stack = [start_state]
            total_states_used = 0
            total_states_generated = 0

            while len(stack) > 0:
                state = stack.pop()
                total_states_used += 1

                if state.cars['X'].x_pos == goal_state:
                    return (state, state.depth, total_states_used, total_states_generated)

                if state.depth < _iterative_depth:
                    for possible_state in self.get_actions(state):
                        total_states_generated += 1
                        unique_id = possible_state.get_unique_id()
                        
                        if unique_id not in state_dict:
                            state_dict[unique_id] = state.depth
                            stack.append(possible_state)
                        elif state.depth < state_dict[unique_id]:
                            stack.append(possible_state)
                            state_dict[unique_id] = state.depth
            _iterative_depth += 1

        return False
