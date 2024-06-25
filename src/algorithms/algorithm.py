import pandas as pd
import numpy as np
import copy

class Algorithm:
    def __init__(self, board):
        self.board = board

        self.state_archive = set([self.board])
        self.state_dict = {}

        self.total_states_used = 0
        self.total_states_generated = 0

    def get_actions(self, board):
        """
        Get the possible next game states for 'board'.
        args:
            board: the board you want to find the possible game states for
        return:
            possible_gamestates: a list of boards that are direct possible next gamestates for the initial board
        """
        possible_gamestates = []

        for car in board.cars.values():
            for possible_move in car.get_possible_moves(board.grid):
                board_copy = copy.deepcopy(board)
                board_copy.depth += 1
                board_copy.cars[car.name].simple_move(possible_move)
                board_copy.moves.append((car.name, possible_move))
                board_copy.update()

                possible_gamestates.append(board_copy)

        return possible_gamestates

    def is_in_archive(self, possible_state):
        """
        Check the archive of visited states to see if possible state is present, and if its depth is less than the depth of the visited state. Adds the state to be checked to the archive.
        args:
            state: the state to be checked
        returns: True if the state is present in the archive and the visited state has a smaller depth. Returns False if the state to be checked is not present in the archive or if its depth is lower than the archived depth.
        """
        unique_id = possible_state.get_unique_id()

        if unique_id not in self.state_dict:
            self.state_dict[unique_id] = possible_state.depth
            return False
        elif possible_state.depth < self.state_dict[unique_id]:
            self.state_dict[unique_id] = possible_state.depth
            return False

        return True

    def is_goal_state(self, state):
        """
        Check if state is a possible goal state.
        args:
            state: the board to be checked
        returns:
            True is state is a possible goal state, False if not
        """
        return state.cars['X'].x_pos == self.board.shape - 2

    def run(self):
        pass

    def reset():
        pass
