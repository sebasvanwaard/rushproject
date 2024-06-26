
from .algorithm import Algorithm

import math
import copy

class Depth_first_branch_n_bound(Algorithm):
    def __init__(self, board):
        super().__init__(board)

    def run(self, max_depth, n_goal_state = 200):
        start_state = copy.deepcopy(self.board)
        stack = [start_state]

        best_state_depth = math.inf
        best_state = None
        goal_states_visited = 0

        while len(stack) > 0:
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
