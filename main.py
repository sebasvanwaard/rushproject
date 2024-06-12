
from src.experiment import *

test = Experiment("gameboards/Rushhour12x12_7.csv")

test.run_experiment(["randomize"], n=5, random_max_moves=10)

# run_experiment.random_experiment("gameboards/Rushhour12x12_1.csv", "experiments/random", n_experiment=1)

# run_experiment.run_all_boards("gameboards", "experiments/random", n_experiment=1000, max_moves=250000)

# parser = argparse.ArgumentParser(description = "filepath")
# parser.add_argument("board", help = "input file (csv)")
# args = parser.parse_args()
# filepath = args.board

# # test.compare_pos_start_end_board()
# run_random_n_times(filepath, 30)
