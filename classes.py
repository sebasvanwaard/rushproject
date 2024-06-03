import pandas as pd
import argparse
import numpy as np


class Experiment:
    def __init__(self, filename):
        self.board = Board(self.get_shape(filename), self.read_file(filename))
        # self.read_file(filename)
        # self.get_shape(filename)

    def read_file(self, filename):
        """
		Read a file containing car information for the starting position of a game of rush hour
		args:
			filename: the path to the file containing the info
		returns:
			a df/list/dict containing the car information
		"""
        df = pd.read_csv(filename)
        # print(df)
        return df

    def get_shape(self, filename):
        name = filename.split('/')[-1].split('x')[0]
        numbers_lst = [s for s in name if s.isdigit()]
        shape = int(''.join(numbers_lst))
        return shape

class Board:
	def __init__(self, shape, car_info):
		self.shape = shape
		self.board = np.full((shape, shape), 'o')
		print(self.board)
		self.cars = {'a': Car('a')}

		self.cars['a'].x_pos

	def draw(self):
		pass

	def add_cars(self, car_info):
		pass

	def read_board_csv(self):
		pass

	def check_finish(self):
		pass

class Car:
	def __init__(self, name, x_pos, y_pos, length, orientation):
		self.name = name
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.length = length
		self.orientation = orientation

	def move(self, steps):
		pass


parser = argparse.ArgumentParser(description = "filepath")
parser.add_argument("board", help = "input file (csv)")
args = parser.parse_args()
filepath = args.board
test = Experiment(filepath)
