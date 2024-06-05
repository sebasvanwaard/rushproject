import pandas as pd
import argparse
import numpy as np


class Car:
	def __init__(self, name, column, row, length, orientation):
		self.name = name
		self.column = column
		self.row = row
		self.length = length
		self.orientation = orientation

	def move(self, steps):
		
		# move vehicles with horizontal orientation
		if self.orientation == H:

			# dont move cars of the board
			if self.length == 2:
				if (self.column + steps) > 5 or (self.column + steps) < 1:
					pass
			
			# dont move trucks of the board
			if self.length == 3:
				if (self.column + steps) > 4 or (self.column + steps) < 1:
					pass
			
			# move the horizontal vehicle
			else:
				self.column += steps
		
		# move vehicles with vertical orientation
		if orientation == V:

			# dont move cars of the board
			if self.length == 2:
				if (self.row + steps) > 5 or (self.row + steps) < 1:
					pass
			
			# dont move trucks of the board
			if self.length == 3:
				if (self.row + steps) > 4 or (self.row + steps) < 1:
					pass
			
			# move the vertical vehicle
			else:
				self.row += steps
		


