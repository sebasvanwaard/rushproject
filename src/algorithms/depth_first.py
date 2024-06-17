from .algorithm import Algorithm

import copy
import math
import random
class Depth_first(Algorithm):
    def __init__(self, board):
        super().__init__(board)

    def run(self, max_depth=math.inf):
        goal_state = self.board.shape - 2

        start_state = copy.deepcopy(self.board)
        stack = [start_state]
        total_states_used = 0
        total_states_generated = 0

        while len(stack) > 0:
            state = stack.pop()
            total_states_used += 1
            print(f"depth =  {state.depth}")
            # print(len(stack))

            if state.cars['X'].x_pos == goal_state:
                print("joepie")
                return (state, state.depth, total_states_used, total_states_generated)

            if state.depth < max_depth:
                for possible_state in self.get_actions(state):
                    total_states_generated += 1
                    unique_id = possible_state.get_unique_id()
                    if unique_id not in self.state_archive:
                        self.state_archive.add(unique_id)
                        stack.append(possible_state)

        print(f"no solution found within {max_depth} depth")

        return False


class random_start_depth_first(Algorithm):
    def __init__(self, board):
        super().__init__(board)

    def run(self, max_random_choice_depth=0, max_depth=math.inf):
        goal_state = self.board.shape - 2

        start_state = copy.deepcopy(self.board)
        stack = [start_state]
        total_states_used = 0
        total_states_generated = 0
        random_choice = 0
        possible_states = []
        while len(stack) > 0:
            state = stack.pop()
            total_states_used += 1
            print(f"depth =  {state.depth}")
            # print(len(stack))

            if state.cars['X'].x_pos == goal_state:
                print("joepie")
                return (state, state.depth, total_states_used, total_states_generated)

            if state.depth < max_depth:
                for possible_state in self.get_actions(state):
                    total_states_generated += 1
                    unique_id = possible_state.get_unique_id()
                    if unique_id not in self.state_archive:
                        self.state_archive.add(unique_id)
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
