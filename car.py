import pandas as pd
import argparse
import numpy as np
import board


class Car:
	def __init__(self, name, column, row, length, orientation):
		self.name = name
		self.column = column
		self.row = row
		self.length = length
		self.orientation = orientation

	def move(self, steps):
		
		# move vehicles with horizontal orientation
		if self.orientation == 'H':

			# moving of the horizontal cars
			if self.length == 2:

				# dont move horizontal cars of the board
				if (self.column + steps) > 4 or (self.column + steps) < 0:
					pass
				
				# dont move horizontal cars if another car is in that place
				elif board((self.column + steps + 1), self.row) != '.':
					pass
				
				# move the horizontal car
				else:
					self.column += steps
			
			# moving of the horizontal trucks
			if self.length == 3:

				# dont move horizontal trucks of the board
				if (self.column + steps) > 3 or (self.column + steps) < 0:
					pass

				# dont move horizontal trucks if another car is in that place
				elif board((self.column + steps + 2), self.row) != '.':
					pass

				# move the horizontal truck
				else:
					self.column += steps
		
		# move vehicles with vertical orientation
		if self.orientation == 'V':

			# moving of the vertical cars
			if self.length == 2:

				# dont move vertical cars of the board
				if (self.row + steps) > 4 or (self.row + steps) < 0:
					pass

				# dont move vertical cars if another car is in that place
				elif board((self.column + steps + 1), self.row) != '.':
					pass
				
				# moving vertical cars
				else:
					self.row += steps
			
			# moving of the vertical trucks
			if self.length == 3:

				# dont move vertical trucks of the board
				if (self.row + steps) > 3 or (self.row + steps) < 0:
					pass
				
				# dont move vertical trucks if another car is in that place
				elif board((self.column + steps + 2), self.row) != '.':
					pass
				
				# move vertical trucks
				else:
					self.row += steps
		


