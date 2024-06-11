import pandas as pd
import copy
from .game.board import *

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

    def print_end_output(self):
        """
        Print the differences between the initial and final car positions on the board
        args:
            None
        returns:
            None
        """
        output = {}
        for car in self.board.cars.values():
            output[car.name] = car.moves
        output_df = pd.DataFrame.from_dict(output, orient='index', columns=['move'])
        print(output_df)

    def random_algorithm(self, n, print_states = False, print_end_output=False):
        """
        laat de board met auto's random stappen doen voor N keren of totdat het
        een oplossing heeft
        args:
            n: max amount of valid moves that can be made
            print_states: print the initial an final state of the board
            print_end_output: print the difference between starting and ending positions of cars, as well as the total valid and total attempted moves
        """
        car_names = list(self.board.cars.keys())
        step_choices = [1, -1]
        moves = []
        solved = False
        self.board.draw(print_in_terminal=print_states)

        valid_moves = 0
        total_moves = 0

        # probeer een n moves te maken
        while valid_moves < n:
            car = self.board.cars[car_names[random.randint(0, len(car_names)-1)]]
            step = random.choice(step_choices)
            # maak move, als dit succesvol append naar moves en update het board. Tel een valid move
            if car.move(step, self.board.board):
                moves.append((car.name, step))
                self.board.draw(print_in_terminal=False)
                valid_moves += 1

            # als de rode auto op de uit positie is het spel is klaar
            if self.board.cars['X'].column == self.board.shape - 2:
                solved = True
                break

            total_moves += 1

        # print de final output (als dit aangegeven is als arg)
        self.board.draw(print_in_terminal=print_states)
        if print_end_output:
            self.print_end_output()
            print(f"valid moves: {valid_moves}")
            print(f"total moves: {total_moves}")
        
        return solved, valid_moves, total_moves

    def reset_board(self):
        self.board = copy.deepcopy(self.starting_board)
