import csv
import math
import os

from algorithms import breadth_first, breadth_first_lukas, \
                        depth_first, depth_first_lukas, depth_first_branch_n_bound, depth_first_random_start,\
                        a_star, a_star_lukas, a_star_nn, \
                        iterative_deepening, randomize
from game.board import Board


def run_algorithm(gameboards_dir, algorithm, output_dir, max_time = math.inf):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    data = []

    for board_path in os.listdir(gameboards_dir):
        board = Board(f"{gameboards_dir}/{board_path}")

        if algorithm == 'baseline (random)':
            output_file = f"{output_dir}/{'randomize'}"

            for iteration in range(1, 10):
                print(iteration)
                final_board, valid_moves, total_moves, total_states_generated = randomize.random_algorithm(board, max_time = max_time)
                data.append([iteration, board_path, valid_moves, total_moves])
                
        
            with open(output_file, 'w') as file:
                writer = csv.writer(file)
                writer.writerow(['iteration', 'gameboard', 'valid_moves', 'total_moves'])
                for d in data:
                    writer.writerow(d)

        else:
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
                   depth_first.Depth_first, depth_first_lukas.Depth_first_lukas, 
                   breadth_first.Breadth_first, a_star.A_star, iterative_deepening.Iterative_deepening]

    for algorithm in algorithms:
        run_algorithm('gameboardscopy', algorithm, 'experiments/data2', 0)