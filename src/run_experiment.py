import subprocess
import time
import csv
import os

from algorithms import breadth_first, depth_first, a_star, iterative_deepening, randomize
from game.board import Board
from experiment import Experiment

def run_algorithm(gameboards_dir, algorithm, output_dir):
    output_file = f"{output_dir}/{algorithm.__name__}"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    data = []

    for board_path in os.listdir(gameboards_dir):
        board = Board(f"{gameboards_dir}/{board_path}")

        if algorithm == 'baseline (random)':
            for iteration in range(1, 1000):
                final_board, valid_moves, total_moves = randomize.random_algorithm(board)
                iteration_data = {"iteration": iteration, "solved": final_board, "valid_moves": valid_moves, "total_moves": total_moves}
                data.append(iteration_data)
        
            with open(output_file, 'w') as file:
                writer = csv.writer(file)
                writer.writerow(['iteration', 'gameboard', 'valid_moves', 'total_moves'])
                for d in data:
                    writer.writerow(d)

        else:
            alg = algorithm(board)

            final_board, total_moves, total_states_used, total_states_generated = alg.run()
            data.append([board_path, total_moves, total_states_used, total_states_generated])

            with open(output_file, 'w') as file:
                writer = csv.writer(file)
                writer.writerow(['gameboard', 'total_moves', 'total_states_used', 'total_states_generated'])
                for d in data:
                    writer.writerow(d)


if __name__ == '__main__':
    algorithms = ['baseline (random)', depth_first.Depth_first, breadth_first.Breadth_first, a_star.A_star, iterative_deepening.Iterative_deepening_with_archive]

    for algorithm in algorithms:
        run_algorithm('gameboardscopy', algorithm, 'experiments/data2')