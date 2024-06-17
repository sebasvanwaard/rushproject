from .algorithm import Algorithm

import copy

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
                    state_cost_dict[possible_state] = possible_state.depth + self.red_car_cost(possible_state) + self.red_blocking_cost(possible_state)+ self.blocking_blocking_cost(possible_state)
                
            state_cost_dict = dict(sorted(state_cost_dict.items(), key=lambda item: item[1], reverse=True))
            print(f"cost: {min(state_cost_dict.values())}")
            state = state_cost_dict.popitem()[0]


        print("joepie")
        return (state, state.depth, total_states_used, total_states_generated)

    def red_car_cost(self, state):
        goal_state = state.shape - 2

        cost = goal_state - state.cars["X"].x_pos

        return 100 * cost

    def red_blocking_cost(self, state):
        cost = 0

        for i in range(state.cars["X"].x_pos + state.cars["X"].length, state.shape):
            if state.grid[state.cars["X"].y_pos, i] != ".":
                cost += 1
        
        return 50 * cost

    def blocking_blocking_cost(self, state):
        blocking_cars = []
        cost = 0

        for i in range(state.cars["X"].x_pos + state.cars["X"].length, state.shape):
            if state.grid[state.cars["X"].y_pos, i] != ".":
                blocking_cars.append(state.grid[state.cars["X"].y_pos, i])

        if len(blocking_cars) == 0:
            return -500
        
        else:
            for car in blocking_cars:
                found_blocking_cars = []
                while self.find_blocking_car(state, car):
                    temp_list = set()
                    for i in self.find_blocking_car(state, car):
                        temp_list.add(i)
                   
                    if len(found_blocking_cars) == 0:
                        found_blocking_cars = temp_list
                        cost += 1

                    car = found_blocking_cars.pop()

        return cost
                    
    def find_blocking_car(self, state, car):
        blocking_cars_ = []
        if state.cars[car].orientation == 'H':
            try:
                blocking_car1 = state.grid[state.cars[car].y_pos, (state.cars[car].x_pos + state.cars[car].length)]
                blocking_cars_.append(blocking_car1)
            except IndexError:
                pass

            try:
                blocking_car2 = state.grid[state.cars[car].y_pos, (state.cars[car].x_pos - 1)]
                blocking_cars_.append(blocking_car2)
            except IndexError:
                pass

        if state.cars[car].orientation == 'V':
            try:
                blocking_car1 = state.grid[(state.cars[car].y_pos + state.cars[car].length), state.cars[car].x_pos]
                blocking_cars_.append(blocking_car1)
            except IndexError:
                pass

            try:
                blocking_car2 = state.grid[(state.cars[car].y_pos - 1), state.cars[car].x_pos]
                blocking_cars_.append(blocking_car2)
            except IndexError:
                pass

        if "." in blocking_cars_:
            return False
        else:                
            return blocking_cars_