from .algorithm import Algorithm

import copy
import math

class Iterative_deepening_with_archive(Algorithm):
    def __init__(self, board):
        super().__init__(board)

    def run(self, max_depth=math.inf):
        goal_state = self.board.shape - 2



        for _iterative_depth in range(1, max_depth):
            start_state = copy.deepcopy(self.board)
            stack = [start_state]
            total_states_used = 0
            total_states_generated = 0

            while len(stack) > 0:
                state = stack.pop()
                total_states_used += 1
                # print(f"depth =  {state.depth}")

                if state.cars['X'].x_pos == goal_state:
                    print("joepie")
                    return (state, state.depth, total_states_used, total_states_generated)

                if state.depth < _iterative_depth:
                    for possible_state in self.get_actions(state):
                        total_states_generated += 1
                        stack.append(possible_state)

        print(f"no solution found within {max_depth} depth")

        return False
