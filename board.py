import pandas as pd
import argparse
import numpy as np
from car import Car


class Board:
    def __init__(self, shape, car_info):
        self.shape = shape
        self.car_info = car_info
        self.cars = {}

    def load_cars(self, car_info):
        for car in car_info:
            self.cars[car_info['car']] = Car(car_info['car'], car_info['col'], car_info['row'], car_info['length'],car_info['orientation'])
    
    def draw(self, print_in_terminal = False):
        """
        Draw a numpy representation of the board
        args:
            print_in_terminal = print the board in the terminal
        returns:
            the numpy array of the board
        """
        board = np.full((self.shape, self.shape), '.')

        for car in self.cars:
            if car.orientation == 'H':
                for i in range(car.length):
                    board[car.row, car.column + i] = car.name
            else:
                for i in range(car.length):
                    board[car.row + i, car.column] = car.name

        if print_in_terminal:
            print(board)
        
        return board
        