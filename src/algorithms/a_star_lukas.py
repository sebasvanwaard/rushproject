from .algorithm import Algorithm

import copy
import math
import time

class A_star_lukas(Algorithm):
    """
	This is a subclass of the class Algorithm and entails the A* algorithm.
    this one is an algorithm without
    the use of deepcopy in the get_action function
	"""
    def __init__(self, board):
        """
		The subclass A* initializes everything from the parent class Algorithm.
		"""
        super().__init__(board)

    def on_or_off_goalline(self, board):
        """
        checks the cost of every car except the red car
        that is vertical and on or above the goal line, resulting in a different
        cost depending on the position of the cars
        """
        cost = 0
        v_trucks, v_cars = self.get_orientation_cars_trucks(board, 'V')

        for truck in v_trucks:
            if board.cars[truck].y_pos == board.cars["X"].y_pos:
                cost += 1
            elif board.cars[truck].y_pos + 1 == board.cars["X"].y_pos:
                cost += 3
            elif board.cars[truck].y_pos + 2 == board.cars["X"].y_pos:
                cost += 5
            else:
                cost += 0.1

        for car in v_cars:
            if board.cars[car].y_pos == board.cars["X"].y_pos:
                cost += 0.1
            elif board.cars[car].y_pos + 1 == board.cars["X"].y_pos:
                cost += 1
            else:
                cost += 5

        return cost

    def cost_h_cars(self, board):
        """
        checks for every horizontal car if it is to the left or right of the
        red car and that is represented in the difference in costs depending on
        how far from the red car
        """
        cost = 0
        h_trucks, h_cars = self.get_orientation_cars_trucks(board, 'H')
        red_car_x_pos = board.cars["X"].x_pos

        for truck in h_trucks:
            if board.cars[truck].x_pos <  red_car_x_pos:
                cost += 1
            elif board.cars[truck].x_pos + 1 < red_car_x_pos:
                cost += 1
            elif board.cars[truck].x_pos + 2 < red_car_x_pos:
                cost += 1
            else:
                cost += 5

        for car in h_cars:
            if board.cars[car].x_pos < red_car_x_pos:
                cost += 1
            elif board.cars[car].x_pos + 1 < red_car_x_pos:
                cost += 1
            else:
                cost += 5

        return cost

    def get_orientation_cars_trucks(self, board, orientation):
        """
        makes two lists for cars and trucks for a given orientation
        """

        cost = 0
        orientation_trucks = []
        orientation_cars= []
        for car in board.cars:
            if board.cars[car].orientation == orientation:

                if board.cars[car].length == 3:
                    orientation_trucks.append(car)
                elif car != "X":
                    orientation_cars.append(car)
        return orientation_trucks, orientation_cars

    def get_blocking_vehicles(self, board, orientation):
        """
        from a given orientation of cars and trucks, checks if there are cars
        and/or trucks blocking it, represented in a difference in cost.
        """
        cost = 0
        orientation_trucks, orientation_cars = self.get_orientation_cars_trucks(board, orientation)

        for truck in orientation_trucks:
            for thing in self.get_blocking_cars(board, board.cars[truck]):
                if thing == None:
                    cost += 1
                elif thing == '.':
                    cost += 1
                else:
                    cost += 1

        for car in orientation_cars:
            for thing in self.get_blocking_cars(board, board.cars[car]):
                if thing == None:
                    cost += 1
                elif thing == '.':
                    cost += 1
                else:
                    cost += 1

        return cost



    def get_blocking_cars(self, board, car):
        """
        gives a list of two cars that blocks the given car
        """
        blocking_car1 = None
        blocking_car2 = None

        if car.orientation == 'H':
            if car.x_pos + car.length < 6 and board.grid[car.y_pos, car.x_pos + car.length] != car:
                blocking_car1 = board.grid[car.y_pos, car.x_pos + car.length]
            if car.x_pos - 1 >= 0 and board.grid[car.y_pos, car.x_pos - 1] != car:
                blocking_car2 = board.grid[car.y_pos, car.x_pos - 1]
        if car.orientation == 'V':
            if car.y_pos + car.length < 6 and board.grid[car.y_pos + car.length, car.x_pos] != car:
                blocking_car1 = board.grid[car.y_pos + car.length, car.x_pos]
            if car.y_pos - 1 >= 0 and board.grid[car.y_pos - 1, car.x_pos] != car:
                blocking_car2 = board.grid[car.y_pos - 1, car.x_pos]

        return [blocking_car1, blocking_car2]

    def get_actions(self, board):
        """
        gets all the possible moves for every car and checks if the new board(s)
        are in the archive and makes a tuple with the cost in it and the new depth
        and moves list to. the new board is created by making a move and then
        giving the old x and y positions to the cars and reverting the board
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
                    cost = self.on_or_off_goalline(board) + self.cost_h_cars(board)
                    board_info = (cost, (new_depth, moves))
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
        """
        cost, (depth_, moves) = packaged_pop

        self.board.depth = depth_
        self.board.moves = moves
        for move in self.board.moves:
            car_name, step = move
            self.board.cars[car_name].simple_move(step)
        self.board.update()

        return self.board

    def run(self, max_depth=math.inf, max_time = math.inf):
        """
        run an A* search for a solution of the given board, with several
        heuristics. Using a sorted list.
		returns:
			state: the board of the final state
            state_depth: the depth of the board of the final state
			total_states_used: the total states visited before the solution was found
			total_states_generated: the total amount of states generated before the solution was found
        """
        start_state = copy.deepcopy(self.board)
        start_board = copy.deepcopy(self.board)
        stack = [start_state]

        # this variable is a one time use to make sure the first pop works
        # properly
        first_time_pop = False

        start_time = time.time()

        while len(stack) > 0 and time.time() - start_time < max_time:
            if first_time_pop == False:
                state = stack.pop()

            if self.is_goal_state(state):
                self.board = start_board
                return (state, state.depth, self.total_states_used, self.total_states_generated)

            if state.depth < max_depth:
                possible_states = self.get_actions(state)
                stack.extend(possible_states)
                stack = sorted(stack, key=lambda x: x[0], reverse=True)

            if first_time_pop == True:
                state = self.undo_modify_state()

            state = self.modify_state(state, stack.pop())
            first_time_pop = True
            self.total_states_used += 1

        self.board = start_board
        return False
