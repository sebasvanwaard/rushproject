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

test.board.draw(print_in_terminal=True)
test.board.cars['J'].move(-1, test.board.board)
test.board.draw(print_in_terminal=True)
test.board.cars['I'].move(2, test.board.board)
test.board.draw(print_in_terminal=True)