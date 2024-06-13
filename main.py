
from src.experiment import *
from src.game import *
from src.algorithms import breadth_first
# from src.algorithms import depth_first

# test = Experiment("gameboards/Rushhour12x12_7.csv")

# test.run_experiment(["randomize"], n=5, random_max_moves=10)

# run_experiment.random_experiment("gameboards/Rushhour12x12_1.csv", "experiments/random", n_experiment=1)

# run_experiment.run_all_boards("gameboards", "experiments/random", n_experiment=1000, max_moves=250000)

# parser = argparse.ArgumentParser(description = "filepath")
# parser.add_argument("board", help = "input file (csv)")
# args = parser.parse_args()
# filepath = args.board

# # test.compare_pos_start_end_board()
# run_random_n_times(filepath, 30)


test_board = Board("gameboards/Rushhour6x6_1.csv")

# test_algorithm = breadth_first.Breadth_first(test_board)
test_algorithm = depth_first.Depth_first(test_board)
final_board, total_moves, total_states = test_algorithm.run(max_depth=100)

print(f"total moves: {total_moves}, total states used: {total_states_used}, total states generated: {total_states_generated}")
final_board.plot()
