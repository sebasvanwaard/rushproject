
from .algorithm import Algorithm

import copy
import math
import random

import time

class Depth_first_random_start(Algorithm):
    def __init__(self, board):
        super().__init__(board)

    def run(self, max_random_choice_depth=0, max_depth=math.inf, max_time=math.inf):
        goal_state = self.board.shape - 2

        start_state = copy.deepcopy(self.board)
        stack = [start_state]

        start_time = time.time()

        random_choice = 0
        possible_states = []
        while len(stack) > 0 and time.time() - start_time < max_time:
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
