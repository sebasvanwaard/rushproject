from .algorithm import Algorithm

import copy
import math

import time

class Breadth_first_lukas(Algorithm):
    def __init__(self, board):
        super().__init__(board)

    def get_actions(self, board):
        moves = []
        possible_gamestates = []

        for car in board.cars.values():
            original_position = (car.x_pos, car.y_pos)

            for possible_move in car.get_possible_moves(board.grid):
                car.simple_move(possible_move)
                board.update()
                new_depth = board.depth + 1

                if not self.is_in_archive(board, new_depth):
                    board_info = {}
                    moves = board.moves[:] + [(car.name, possible_move)]
                    board_info = (new_depth, moves)
                    possible_gamestates.append(board_info)

                car.x_pos, car.y_pos = original_position
                board.update()

        return possible_gamestates

    def is_in_archive(self, possible_state, depth):
        """
        Check the archive of visited states to see if the possible state is present, and if its depth is less than the depth
        of the visited state. Adds the state to be checked to the archive.

        Args:
            possible_state: The state to be checked.
            depth: The depth of the state to be checked.

        Returns:
            bool: True if the state is present in the archive and the visited state has a smaller depth.
                  Returns False if the state to be checked is not present in the archive or if its depth is lower than the
                  archived depth.
        """
        unique_id = possible_state.get_unique_id()
        existing_depth = self.state_dict.get(unique_id)

        if existing_depth is None or depth < existing_depth:
            self.state_dict[unique_id] = depth
            return False

        return True

    def undo_modify_state(self):
        # print(self.board.moves.reverse())

        for move in self.board.moves[::-1]:
            car_name, step = move
            self.board.cars[car_name].simple_move(-step)
        self.board.update()
        # print(self.board.grid)
        self.board.depth = 0
        self.board.moves = []

        return self.board

    def modify_state(self, state, packaged_pop):
        # moet naar tuple
        depth_, moves = packaged_pop

        self.board.depth = depth_
        self.board.moves = moves
        for move in self.board.moves:
            # print(move)
            car_name, step = move
            self.board.cars[car_name].simple_move(step)
        self.board.update()

        return self.board

    def run(self, max_depth=100, max_time = math.inf):
        start_state = copy.deepcopy(self.board)
        start_board = copy.deepcopy(self.board)
        stack = [start_state]
        first_time_pop = False

        start_time = time.time()

        while len(stack) > 0 and time.time() - start_time < max_time:
            if first_time_pop == False:
                state = stack.pop(0)

            if self.is_goal_state(state):
                print("joepie")
                return (state, state.depth, self.total_states_used, self.total_states_generated)

            if state.depth < max_depth:
                possible_states = self.get_actions(state)
                stack.extend(possible_states)
            if first_time_pop == True:
                state = self.undo_modify_state()
            state = self.modify_state(state, stack.pop(0))
            first_time_pop = True
            self.total_states_used += 1

        print(f"no solution found within {max_depth} depth")
        self.board = start_board
        return False
