from .algorithm import Algorithm

import copy
import math
import time

class Depth_first_lukas(Algorithm):
    """
	This is a subclass of the class Algorithm and
    entails the depth first algorithm.
    this is an algorithm without
    the use of deepcopy in the get_action function
	"""
    def __init__(self, board):
        """
		The subclass Depth first initializes everything from the parent class Algorithm.
		"""
        super().__init__(board)

    def get_actions(self, board):
        """
        gets all the possible moves for every car and checks if the new board(s)
        are in the archive and makes a tuple with the depth and moves list
        """
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
        """
        reverts the board to the original board given to the algorithm
        at the start
        """
        for move in self.board.moves[::-1]:
            car_name, step = move
            self.board.cars[car_name].simple_move(-step)
        self.board.update()
        self.board.depth = 0
        self.board.moves = []

        return self.board

    def modify_state(self, state, packaged_pop):
        """
        changes the board to the popped state from the stack
        by giving it the tuple with the new depth and moves list
        the moves list is then applied to the simple move function to create
        the new board which then can be used to get new actions
        """
        depth_, moves = packaged_pop

        self.board.depth = depth_
        self.board.moves = moves
        for move in self.board.moves:
            car_name, step = move
            self.board.cars[car_name].simple_move(step)
        self.board.update()

        return self.board

    def run(self, max_depth=math.inf, max_time = math.inf):
        """
        run a depth first search for a solution of the given board. Integrated stack.
		args:
			max_depth: the maximum depth the algorithm
            will search before giving up. Defaults to math.inf
		returns:
			state: the board of the final state
            state_depth: the depth of the board of the final state
			total_states_used: the total states visited before the solution was found
			total_states_generated: the total amount of states generated before the solution was found
        """
        start_state = copy.deepcopy(self.board)
        stack = [start_state]
        first_time_pop = False
        start_time = time.time()

        while len(stack) > 0 and time.time() - start_time < max_time:
            if first_time_pop == False:
                state = stack.pop()

            if self.is_goal_state(state):
                self.board = start_state
                return (state, state.depth, self.total_states_used, self.total_states_generated)

            if state.depth < max_depth:
                possible_states = self.get_actions(state)
                stack.extend(possible_states)
            if first_time_pop == True:
                state = self.undo_modify_state()
            state = self.modify_state(state, stack.pop())
            first_time_pop = True
            self.total_states_used += 1

        self.board = start_state

        return None, None, None, None
