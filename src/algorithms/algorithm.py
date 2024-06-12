import pandas as pd
import numpy as np
import copy

class Algorithm:
    def __init__(self, board, cars):
        self.board = board
        self.cars = cars
    
    def get_actions(self):

        # for car_check in self.cars:
        #     for car_other in self.cars:
        #         if car_check.orientation == 'H':
        #             if (car_check.y_pos, car_check.x_pos - 1) == (car_other.y_pos, car_other.x_pos):
                        
        #             if car_check.x_pos + car_check.length:
                

            
        #         if car_check.orientation == 'V':
        #             if car_check.y_pos - 1: 
                
        #             if car_check.y_pos + car_check.length:


        # positions = np.where(self.board == '.')
        # positions = list(zip(positions[0], positions[1]))
        
        # neighbouring_cars = {}

        # for position in positions:
        #     if self.board[(position[0] - 1), position[1]] != '.':
        #         neighbouring_cars[self.board[(position[0] - 1), position[1]]] = ['V', 1]
            
        #     if self.board[(position[0] + 1), position[1]] != '.':
        #         neighbouring_cars[self.board[(position[0] + 1), position[1]]] = ['V', -1]
            
        #     if self.board[position[0], (position[1] - 1)] != '.':
        #         neighbouring_cars[self.board[position[0], (position[1] - 1)]] = ['H', 1]
            
        #     if self.board[position[0], (position[1] + 1)] != '.':
        #         neighbouring_cars[self.board[position[0], (position[1] - 1)]] = ['H', -1]
        
        # possible_cars = {}

        # for neighbouring_car in neighbouring_cars:
        #     if self.cars[neighbouring_car].orientation == 'H' and neighbouring_cars[neighbouring_car][0] == 'H':
        #         possible_cars[neighbouring_car] = neighbouring_cars[neighbouring_car][1]
        #     if self.cars[neighbouring_car].orientation == 'V' and neighbouring_cars[neighbouring_car][0] == 'V':
        #         possible_cars[neighbouring_car] = neighbouring_cars[neighbouring_car][1]
        
        # copies = len(possible_cars)
        
        # for copie in range(copies):
        #     copy.deepcopy(self.board)

        def get_actions(self, board):
            possible_gamestates = []

            for car in board.cars:
                if car.orientation == "H":
                    if board.grid[car.x_pos - 1, car.y_pos] == ".":
                        board_copy = copy.deepcopy(board)
                        board_copy.cars[car.name].move(-1)
                        possible_gamestates.append(board_copy)
                    if board.grid(car.x_pos + car.length, car.y_pos) == ".":
                        board_copy = copy.deepcopy(board)
                        board_copy.cars[car.name].move(1)
                        possible_gamestates.append(board_copy)
                
                if car.orientation == "V":
                    if board.grid[car.x_pos, car.y_pos - 1] == ".":
                        board_copy = copy.deepcopy(board)
                        board_copy.cars[car.name].move(-1)
                        possible_gamestates.append(board_copy)
                    if board.grid(car.x_pos, car.y_pos + car.length) == ".":
                        board_copy = copy.deepcopy(board)
                        board_copy.cars[car.name].move(1)
                        possible_gamestates.append(board_copy)
                

            return possible_gamestates

    def get_unique_id(self):
        self.unique_id = self.board.tostring()

    def run():
        pass

    def prune():
        pass

    def reset():
        pass

