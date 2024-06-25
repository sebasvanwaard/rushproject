import subprocess
import time
import csv
import os

from algorithms import breadth_first
from algorithms import depth_first
from algorithms import a_star

def run_algorithm(algorithm, board, experiment_dir, csv_file):
    start = time.time()
    n_runs = 0
    
    if not os.path.exists(experiment_dir):
        os.makedirs(experiment_dir)
    
    csv_path = os.path.join(experiment_dir, csv_file)

    if not os.path.exists(csv_path):
        with open(csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Run', 'Execution Time (s)', 'Timestamp'])

    while time.time() - start < 3600:
        print(f"run: {n_runs}")
        run_start = time.time()
        subprocess.call(["gtimeout", "60", "python3", algorithm(board)])
        run_end = time.time()

        execution_time = run_end - run_start
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(run_end))

        with open(csv_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([n_runs, execution_time, timestamp])

        n_runs += 1

algorithms = [depth_first.Depth_first, breadth_first.Breadth_first, a_star.A_star]

for algorithm in algorithms:
    for board in 'gameboards':
        board_name = os.path.splitext(board)[0]
        algorithm_name = splitext(algorithm)[0]
        csv_filename = f'{algorithm_name}_{board_name}_results.csv'  
        experiment_directory = f'experiments/data/{algorithm_name}'  

        run_algorithm(algorithm, board_name, csv_filename, experiment_directory)