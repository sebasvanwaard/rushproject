from .algorithm import Algorithm

import copy
import math

class A_star_lukas(Algorithm):
    def __init__(self, board):
        super().__init__(board)

    def on_or_off_goalline(self, board):
        """
        checkt de kost van alles wat anders dan de rode auto op de goal lijn
        staat. afhankelijk van het type auto is de kosten hoger of lager
        """
        cost = 0
        v_trucks, v_cars = self.get_orientation_cars_trucks(board, 'V')

        for truck in v_trucks:
            if board.cars[truck].y_pos == 3:
                cost += 0.1
            elif board.cars[truck].y_pos + 1 == 3:
                cost += 0.3
            elif board.cars[truck].y_pos + 2 == 3:
                cost += 0.5
            else:
                cost += 5

        for car in v_cars:
            if board.cars[car].y_pos == 3:
                cost += 0.1
            elif board.cars[car].y_pos + 1 == 3:
                cost += 1
            else:
                cost += 5

        return cost

    def cost_h_cars(self, board):
        """
        checkt welke horizontale auto's links of rechts van de
        rode auto staan. hoe meer links hoe duurder de cost
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
        maakt een lijst met alle verticale auto's
        en een lijst van alle verticale trucks
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
        van een gegeven orientatie, kijkt hoeveel voertuigen een auto blokkeren
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
        
    def run(self):
        state = copy.deepcopy(self.board)
        goal_state = self.board.shape - 2

        total_states_used = 0
        total_states_generated = 0
        state_cost_dict = {state: 0}


        while state.cars['X'].x_pos != goal_state:
            total_states_used += 1
            current_cost = self.on_or_off_goalline(state)
            unique_id = state.get_unique_id()
            self.state_archive.add(unique_id)

            for possible_state in self.get_actions(state):
                total_states_generated += 1

                possible_unique_id = possible_state.get_unique_id()
                if possible_unique_id not in self.state_archive:
                    state_cost_dict[possible_state] = self.on_or_off_goalline(possible_state) + self.cost_h_cars(possible_state) + self.get_blocking_vehicles(possible_state, 'V') + self.get_blocking_vehicles(possible_state, 'H')

            state_cost_dict = dict(sorted(state_cost_dict.items(), key=lambda item: item[1], reverse=True))
            state = state_cost_dict.popitem()[0]


        print("joepie")
        return (state, state.depth, total_states_used, total_states_generated)
