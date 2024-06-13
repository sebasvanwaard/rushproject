from .algorithm import Algorithm

import copy
import math

class Depth_first(Algorithm):
    def __init__(self, board):
        super().__init__(board)

    def run(self, max_depth=math.inf):
        goal_state = self.board.shape - 2

        start_state = copy.deepcopy(self.board)
        stack = [start_state]
        depth = 0
        total_states_used = 0
        total_states_generated = 0

        while len(stack) > 0:
            state = stack.pop()
            total_states_used += 1
            print(len(stack))

            if state.cars['X'].x_pos == goal_state:
                print("joepie")
                return (state, depth, total_states_used, total_states_generated)
            
            if depth <= max_depth:
                for possible_state in self.get_actions(state):
                    total_states_generated += 1
                    unique_id = possible_state.get_unique_id()
                    if unique_id not in self.state_archive:
                        self.state_archive.add(unique_id)
                        stack.append(possible_state)

                depth += 1

        print(f"no solution found within {max_depth} moves")

        return False
