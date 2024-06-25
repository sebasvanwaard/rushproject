import pandas as pd
import copy
import os
import csv

from .game.board import *
from .algorithms.randomize import *
from src.algorithms import breadth_first, depth_first, iterative_deepening, randomize, a_star_lukas, a_star_nn, a_star

import random


class Experiment:
    def __init__(self, filename):
        self.board = Board(filename)
        self.starting_board = copy.deepcopy(self.board)
        self.gameboard_filename = filename

    def run_experiment(self, algorithms, n, random_max_moves=None):
        if random_max_moves == None:
            random_max_moves = self.random_max_moves
        
        for algorithm in algorithms:

            if algorithm == "randomize":
                random_data = []
                for iteration in range(1, n + 1):
                    print(iteration)
                    solved, valid_moves, total_moves, _ = self.run_random(random_max_moves)
                    iteration_data = {"iteration": iteration, "solved": solved, "valid_moves": valid_moves, "total_moves": total_moves}
                    random_data.append(iteration_data)

                self.data_to_csv(random_data, self.gameboard_filename, f"experiments/data/{algorithm}")

    def run_random(self, max_moves=100000):
        return random_algorithm(copy.deepcopy(self.board), max_moves)

    def run_astar(self):
        pass

    def run_breadth(self):
        pass

    def run_depth(self):
        pass

    def data_to_csv(self, data, gameboard_file, experiment_dir):
        fields = list(data[0].keys())

        if not os.path.isdir(experiment_dir):
            os.mkdir(experiment_dir)

        if os.path.isfile(f"{experiment_dir}/solved_{gameboard_file.split('/')[-1]}"):
            overwrite = input(f"{experiment_dir}/solved_{gameboard_file.split('/')[-1]} already exists. Overwrite current file? (y/n)")
            if overwrite != 'y':
                print("Cancelled")
                return

        with open(f"{experiment_dir}/solved_{gameboard_file.split('/')[-1]}", 'w') as output:
            writer = csv.DictWriter(output, fieldnames=fields)
            writer.writeheader()

            for dict in data:
                writer.writerow(dict)

    def reset_board(self):
        self.board = copy.deepcopy(self.starting_board)
