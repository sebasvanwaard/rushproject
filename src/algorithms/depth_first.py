from .algorithm import Algorithm

import copy
import math

class Depth_first(Algorithm):
    def __init__(self, board):
        super().__init__(board)

    def run(self, max_depth=math.inf):
        start_state = copy.deepcopy(self.board)
        stack = [start_state]
        while len(stack) > 0:
            state = stack.pop()
            self.total_states_used += 1

            if self.is_goal_state(state):
                return (state, state.depth, self.total_states_used, self.total_states_generated)

            if state.depth < max_depth:
                for possible_state in self.get_actions(state):
                    self.total_states_generated += 1
                    if not self.is_in_archive(possible_state):
                        stack.append(possible_state)

        print(f"no solution found within {max_depth} depth")

        return False