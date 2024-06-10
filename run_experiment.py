import csv
from experiment import Experiment
import os
import copy

def run_random_algorithm(experiment, n=50, max_moves=100000):
	data = []

	for iteration in range(1, n + 1):
		new_experiment = copy.deepcopy(experiment)
		solved, valid_moves, total_moves = new_experiment.random_algorithm(max_moves)
		iteration_data = {"iteration": iteration, "solved": solved, "valid_moves": valid_moves, "total_moves": total_moves}
		data.append(iteration_data)

	return data

def write_data_dict(data, experiment_dir, gameboard_file):
	fields = list(data[0].keys())

	if not os.path.isdir(experiment_dir):
		os.mkdir(experiment_dir)

	with open(f"{experiment_dir}/{gameboard_file.split('/')[-1]}", 'w') as output:
		writer = csv.DictWriter(output, fieldnames=fields)
		writer.writeheader()

		for dict in data:
			writer.writerow(dict)

def random_experiment(filepath, output_file, n_experiment = 50, max_moves = 100000):
	rand_experiment = Experiment(filepath)

	data = run_random_algorithm(rand_experiment, n = n_experiment, max_moves=max_moves)
	write_data_dict(data, output_file, filepath)

