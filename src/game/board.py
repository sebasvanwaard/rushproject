import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

from .car import *


class Board:
    def __init__(self, filename):
        self.shape = self.get_shape(filename)
        self.car_info = self.read_file(filename)
        self.cars = self.load_cars()
        self.grid = self.update()

    def read_file(self, filename):
        """
        Read a file containing car information for the starting position of a game of rush hour
        args:
            filename: the path to the file containing the info
        returns:
            a df/list/dict containing the car information
        """
        df = pd.read_csv(filename)
        return df

    def get_shape(self, filename):
        """
        Parse the shape of the board from the filename (has to be present in the name seperated by x)
        args:
            filename: the name of the board file
        return:
            the dimension (int)
        """
        name = filename.split('/')[-1].split('x')[0]
        numbers_lst = [s for s in name if s.isdigit()]
        shape = int(''.join(numbers_lst))

        return shape

    def load_cars(self):

        cars = {}

        for _, car in self.car_info.iterrows():
            cars[car['car']] = Car(car['car'], car['col'] - 1, car['row'] - 1, car['length'], car['orientation'])

        return cars

    def update(self):
        """
        Draw a numpy representation of the board
        args:
            print_in_terminal = print the board in the terminal
        returns:
            the numpy array of the board
        """
        self.grid = np.full((self.shape, self.shape), '.')

        for car in self.cars.values():
            if car.orientation == 'H':
                for i in range(car.length):
                    self.grid[car.y_pos, car.x_pos + i] = car.name
            else:
                for i in range(car.length):
                    self.grid[car.y_pos + i, car.x_pos] = car.name

        return self.grid

    def draw(self):
        print(self.grid)

    def plot(self):
        
        fig, ax = plt.subplots()
        ax.plot()

        ax.set_xlim(right=self.shape)
        ax.set_ylim(bottom=self.shape)

        for car in self.cars.values():
            rectangle = None
            color = "#00" + f"{format(random.randrange(0, 16**8), '08x')}"[2:]
            if car.name == 'X':
                color = "#FF0000"
            if car.orientation == "H":
                rectangle = patches.Rectangle((car.x_pos, car.y_pos), car.length, 1, edgecolor = 'black', facecolor = color)
            else:
                rectangle = patches.Rectangle((car.x_pos, car.y_pos), 1, car.length, edgecolor = 'black', facecolor = color)

            ax.add_patch(rectangle)

        plt.show()
        
    def get_unique_id(self):
        return np.array2string(self.grid)
        return np.array2string(self.grid)
