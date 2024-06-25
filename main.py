import math

from src.experiment import *
from src.game import *
from src.algorithms import breadth_first
from src.algorithms import depth_first
from src.algorithms import a_star
from src.algorithms import iterative_deepening
from src.algorithms import a_star_lukas as lukas

from src.plots import visualize
import time
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

# ----------------breadth_first -----------------------
# test_board = Board("gameboards/Rushhour9x9_4.csv")

# test_algorithm = breadth_first.Breadth_first(test_board)
# # test_algorithm = depth_first.Depth_first(test_board)
# final_board, total_moves, total_states_used, total_states_generated = test_algorithm.run()

# print(f"total moves: {total_moves}, total states used: {total_states_used}, total states generated: {total_states_generated}")
# print(f"moves: {final_board.moves}")
# # final_board.plot()

# visualize.visualize_moves(test_board, final_board.moves)

# # ----------------random_start_depth_first -----------------------
# test_board = Board("gameboards/Rushhour6x6_1.csv")
#
# test_algorithm = depth_first.random_start_depth_first(test_board)
# # test_algorithm = depth_first.Depth_first(test_board)
# start = time.time()
# final_board, total_moves, total_states_used, total_states_generated = test_algorithm.run(2)
# end = time.time() - start
# print(end)
# print(f"total moves: {total_moves}, total states used: {total_states_used}, total states generated: {total_states_generated}")
# print(f"moves: {final_board.moves}")
# final_board.plot()
#
# # visualize.visualize_moves(test_board, final_board.moves)

# # ---------------- branch_n_bound_depth_first -----------------------
# test_board = Board("gameboards/Rushhour9x9_4.csv")

# test_algorithm = depth_first.branch_n_bound_depth_first(test_board)
# # test_algorithm = depth_first.Depth_first(test_board)
# final_board, total_moves, total_states_used, total_states_generated = test_algorithm.run(math.inf, n_goal_state=200)

# print(f"total moves: {total_moves}, total states used: {total_states_used}, total states generated: {total_states_generated}")
# print(f"moves: {final_board.moves}")
# # final_board.plot()

# # visualize.visualize_moves(test_board, final_board.moves)

# ----------------iterative_deepening_depth_first -----------------------
# test_board = Board("gameboards/Rushhour9x9_4.csv")

# test_algorithm = iterative_deepening.Iterative_deepening_with_archive(test_board)
# # test_algorithm = depth_first.Depth_first(test_board)
# final_board, total_moves, total_states_used, total_states_generated = test_algorithm.run(200)

# print(f"total moves: {total_moves}, total states used: {total_states_used}, total states generated: {total_states_generated}")
# print(f"moves: {final_board.moves}")
# final_board.plot()

# visualize.visualize_moves(test_board, final_board.moves)

# # ---------------- a_star -----------------------
# test_board = Board("gameboards/Rushhour6x6_2.csv")
#
# test_algorithm = a_star.A_star(test_board)
# start = time.time()
#
# final_board, total_moves, total_states_used, total_states_generated = test_algorithm.run()
# end = time.time() - start
#
# # cost = test_algorithm.calc_board_cost(test_board)
# # print(cost)
# print(end)
# print(f"total moves: {total_moves}, total states used: {total_states_used}, total states generated: {total_states_generated}")
# print(f"moves: {final_board.moves}")
# final_board.plot()
# #
# # visualize.visualize_moves(test_board, final_board.moves)

# ------------A_star_lukas
test_board = Board("gameboards/Rushhour6x6_2.csv")
test_algorithm = lukas.A_star_lukas(test_board)
start = time.time()

final_board, total_moves, total_states_used, total_states_generated = test_algorithm.run()
end = time.time() - start
print(end)

print(f"total moves: {total_moves}, total states used: {total_states_used}, total states generated: {total_states_generated}")
# print(f"moves: {final_board.moves}")
