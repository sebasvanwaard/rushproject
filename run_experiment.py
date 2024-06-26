import csv
import math
import os

import argparse

from src.algorithms import breadth_first, breadth_first_lukas, \
                        depth_first, depth_first_lukas, depth_first_branch_n_bound, depth_first_random_start,\
                        a_star, a_star_lukas, a_star_nn, \
                        iterative_deepening, randomize
from src.game.board import Board


def run_algorithm(gameboards_dir, algorithm, output_dir, max_time = math.inf, random_iterations = 1000):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    data = []

    for board_path in os.listdir(gameboards_dir):
        board = Board(f"{gameboards_dir}/{board_path}")

        if algorithm == 'baseline (random)':
            print(f"Running Randomize for {board_path}")
            output_file = f"{output_dir}/{'randomize'}"

            for iteration in range(1, random_iterations):
                final_board, valid_moves, total_moves, total_states_generated = randomize.random_algorithm(board, max_time = max_time)
                data.append([iteration, board_path, valid_moves, total_moves])
                
        
            with open(output_file, 'w') as file:
                writer = csv.writer(file)
                writer.writerow(['iteration', 'gameboard', 'valid_moves', 'total_moves'])
                for d in data:
                    writer.writerow(d)

        else:
            print(f"Running {algorithm.__name__} for {board_path}")
            output_file = f"{output_dir}/{algorithm.__name__}"
            alg = algorithm(board)

            output = alg.run(max_time = max_time)
            final_board, total_moves, total_states_used, total_states_generated = None, None, None, None
            if output is not False:
                final_board, total_moves, total_states_used, total_states_generated = output
            data.append([board_path, total_moves, total_states_used, total_states_generated])

            with open(output_file, 'w') as file:
                writer = csv.writer(file)
                writer.writerow(['gameboard', 'total_moves', 'total_states_used', 'total_states_generated'])
                for d in data:
                    writer.writerow(d)


if __name__ == '__main__':
    algorithms = ['baseline (random)',
                    depth_first.Depth_first, depth_first_lukas.Depth_first_lukas, depth_first_branch_n_bound.Depth_first_branch_n_bound, depth_first_random_start.Depth_first_random_start,
                    breadth_first.Breadth_first, breadth_first_lukas.Breadth_first_lukas,
                    a_star.A_star, a_star_nn.A_star_nn, a_star_lukas.A_star_lukas,
                    iterative_deepening.Iterative_deepening]

    parser = argparse.ArgumentParser(description="Run all algorithms")
    parser.add_argument('gamefile_path', help='The path to the directory containing the gamefile.csv you want to test on')
    parser.add_argument('output_path', help='path to directory you want to output the data to')
    parser.add_argument('-max_time', default = 300, help='the maximum time an iteration can take fan any algorithm (in seconds)')
    parser.add_argument('-random_iterations', default=1000, help='the maximum amount of iterations the random algorithm will do')

    args = parser.parse_args()

    for algorithm in algorithms:
        run_algorithm(args.gamefile_path, algorithm, args.output_path, max_time = int(args.max_time), random_iterations=int(args.random_iterations))