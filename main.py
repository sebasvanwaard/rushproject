import pandas as pd
import argparse
import numpy as np
import board
from experiment import Experiment
import car

def run_random_n_times(filename, n, stepsize=1000000):
    """
    houdt bij hoeveel geldige stappen
    dit 10,30,50 keer doen en avg stappen bepalen maybe histogram
    """
    sum_valid_moves = 0
    sum_total_moves = 0
    runs_solved = {}
    
    for runs in range(n):
        test = Experiment(filepath)

        solved, valid_moves, total_moves = test.random_algorithm(stepsize)
        runs_solved[runs] = solved
        sum_valid_moves += valid_moves
        sum_total_moves += total_moves
        
    avg_valid_moves = sum_valid_moves / n
    avg_total_moves = sum_total_moves / n
    
    print(runs_solved)
    print(f"average valid moves: {avg_valid_moves}")
    print(f"average total moves: {avg_total_moves}")


parser = argparse.ArgumentParser(description = "filepath")
parser.add_argument("board", help = "input file (csv)")
args = parser.parse_args()
filepath = args.board

# test.compare_pos_start_end_board()
run_random_n_times(filepath, 30)
