import pandas as pd
import argparse
import numpy as np


class Car:
	def __init__(self, name, x_pos, y_pos, length, orientation):
		self.name = name
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.length = length
		self.orientation = orientation

	def move(self, steps):
		pass
