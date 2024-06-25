from .algorithm import Algorithm

import copy
import math

class A_star(Algorithm):
    def __init__(self, board):
        super().__init__(board)

    def run(self):
        state = copy.deepcopy(self.board)
        goal_state = self.board.shape - 2

        total_states_used = 0
        total_states_generated = 0
        state_cost_dict = {state: 0}


        while state.cars['X'].x_pos != goal_state:
            total_states_used += 1

            unique_id = state.get_unique_id()
            self.state_archive.add(unique_id)

            for possible_state in self.get_actions(state):
                total_states_generated += 1

                possible_unique_id = possible_state.get_unique_id()
                if possible_unique_id not in self.state_archive:
                    state_cost_dict[possible_state] = possible_state.depth + self.red_car_cost(possible_state) + self.red_blocking_cost(possible_state) + self.calc_board_cost(possible_state)

            state_cost_dict = dict(sorted(state_cost_dict.items(), key=lambda item: item[1], reverse=True))
            # print(f"cost: {min(state_cost_dict.values())}")
            state = state_cost_dict.popitem()[0]


        print("joepie")
        return (state, state.depth, total_states_used, total_states_generated)

    def red_car_cost(self, state):
        goal_state = state.shape - 2

        cost = goal_state - state.cars["X"].x_pos

        return cost

    def red_blocking_cost(self, state):
        cost = 0

        for i in range(state.cars["X"].x_pos + state.cars["X"].length, state.shape):
            if state.grid[state.cars["X"].y_pos, i] != ".":
                cost += 1

        return cost

    def get_blocking_red(self, board):
        blocking_cars = []

        for i in range(board.cars["X"].x_pos + board.cars["X"].length, board.shape):
            if board.grid[board.cars["X"].y_pos, i] != ".":
                blocking_cars.append(board.grid[board.cars["X"].y_pos, i])

        return set(blocking_cars)

    def get_blocking_cars(self, board, car):
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


    def calc_cost(self, board, car, cost, calc_depth=0):
        if car == None or cost > len(board.cars):
            return math.inf

        blocking_cars = self.get_blocking_cars(board, board.cars[car])
        # print(blocking_cars)

        if '.' in blocking_cars:
            return cost

        for car in blocking_cars:
            # print(car)
            if car is None:
                cost = cost + 100
            elif board.cars[car].length == 2:
                cost = cost + 1
            else:
                cost = cost + 3
        # cost = cost + 1

        cost1 = self.calc_cost(board, blocking_cars[0], cost, calc_depth)
        cost2 = self.calc_cost(board, blocking_cars[1], cost, calc_depth)

        return min(cost1, cost2)

    def calc_board_cost(self, board):
        cars_blocking_red = self.get_blocking_red(board)
        total_cost = 0
        # print(cars_blocking_red)

        for car_blocking_red in cars_blocking_red:

            total_cost += self.calc_cost(board, car_blocking_red, 0)
            # print(total_cost)
            pass

        return total_cost
