import csv
from rushproject.code.algorithms.experiment import Experiment
import os
import copy

def run_random_algorithm(experiment, n=50, max_moves=100000):
	data = []

	for iteration in range(1, n + 1):
		print(f"Solving iteration #{iteration}")
		experiment.reset_board()
		solved, valid_moves, total_moves = experiment.random_algorithm(max_moves)
		iteration_data = {"iteration": iteration, "solved": solved, "valid_moves": valid_moves, "total_moves": total_moves}
		data.append(iteration_data)

	return data

def write_data_dict(data, experiment_dir, gameboard_file):
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

def random_experiment(board_filepath, output_dir, n_experiment = 50, max_moves = 100000):
	rand_experiment = Experiment(board_filepath)

	data = run_random_algorithm(rand_experiment, n = n_experiment, max_moves=max_moves)
	write_data_dict(data, output_dir, board_filepath)


def run_all_boards(board_dir, experiment_dir, n_experiment=50, max_moves=100000):
	boards = os.listdir(board_dir)

	for board in boards:
		random_experiment(f"{board_dir}/{board}", experiment_dir, n_experiment=n_experiment, max_moves=max_moves)