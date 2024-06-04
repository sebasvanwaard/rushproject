import pandas as pd
import argparse
import numpy as np
import board

class Experiment:
    def __init__(self, filename):
        self.board = board.Board(self.get_shape(filename), self.read_file(filename))
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
