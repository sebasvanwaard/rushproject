import pandas as pd
import argparse
import numpy as np
import car


class Board:
    def __init__(self, shape, car_info):
        self.shape = shape
        self.board = np.full((shape, shape), 'o')
        self.car_info = car_info
        print(self.board)
        print(self.car_info)
