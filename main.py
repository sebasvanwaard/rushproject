import pandas as pd
import argparse
import numpy as np
import board
import experiment
import car



parser = argparse.ArgumentParser(description = "filepath")
parser.add_argument("board", help = "input file (csv)")
args = parser.parse_args()
filepath = args.board
test = experiment.Experiment(filepath)
