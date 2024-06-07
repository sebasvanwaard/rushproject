import pandas as pd
import argparse
import numpy as np
from board import Board
import copy
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

    def print_end_output(self):
        output = {}
        for car in self.board.cars.values():
            output[car.name] = car.moves
        output_df = pd.DataFrame.from_dict(output, orient='index', columns=['move'])
        print(output_df)
    def random_algorithm(self):
        """
        laat de board met auto's random stappen doen voor N keren of totdat het
        een oplossing heeft, houdt bij hoeveel geldige stappen
        dit 10,30,50 keer doen en avg stappen bepalen maybe histogram
        """
        pass
