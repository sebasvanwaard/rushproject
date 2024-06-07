import pandas as pd
import argparse
import numpy as np
import board
from experiment import Experiment
import car

parser = argparse.ArgumentParser(description = "filepath")
parser.add_argument("board", help = "input file (csv)")
args = parser.parse_args()
filepath = args.board
test = Experiment(filepath)

# test.compare_pos_start_end_board()
test.random_algorithm(10000)
