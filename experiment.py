import pandas as pd
import argparse
import numpy as np
from board import Board
import copy

import random


class Experiment:
    def __init__(self, filename):
        self.board = Board(self.get_shape(filename), self.read_file(filename))
        self.starting_board = copy.deepcopy(self.board)
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

    def random_algorithm(self, n, print_states = False, print_end_output=False):
        """
        laat de board met auto's random stappen doen voor N keren of totdat het
        een oplossing heeft
        """
        car_names = list(self.board.cars.keys())
        step_choices = [1, -1]
        moves = []
        solved = False
        self.board.draw(print_in_terminal=print_states)

        valid_moves = 0
        total_moves = 0
        while valid_moves < n:
            car = self.board.cars[car_names[random.randint(0, len(car_names)-1)]]
            step = random.choice(step_choices)
            if car.move(step, self.board.board):
                moves.append((car.name, step))
                self.board.draw(print_in_terminal=False)

                valid_moves += 1

            if self.board.cars['X'].column == self.board.shape - 2:
                solved = True
                break

            total_moves += 1

        self.board.draw(print_in_terminal=print_states)
        if print_end_output:
            self.print_end_output()
            print(f"valid moves: {valid_moves}")
            print(f"total moves: {total_moves}")
        return solved, valid_moves, total_moves

    def reset_board(self):
        self.board = copy.deepcopy(self.starting_board)
