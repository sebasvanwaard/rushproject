import pandas as pd
import argparse
import numpy as np


class Car:
	def __init__(self, name, column, row, length, orientation):
		super().__init__()

		self.name = name
		self.column = column
		self.row = row
		self.length = length
		self.orientation = orientation

	def move(self, steps, board):

		# move vehicles with horizontal orientation
		if self.orientation == 'H':

			# moving of the horizontal cars
			if self.length == 2:

				# dont move horizontal cars of the board
				if (self.column + steps) > 4 or (self.column + steps) < 0:
					return
				
				# dont move horizontal cars if another car is in that place
				if steps > 0:
					for i in range(1, steps + 1):
						if board[self.row, (self.column + 1 + i)] != '.': 
							return
					else:
						self.column += steps

				else:
					for i in range(steps, 0):
						if board[self.row, (self.column + i)] != '.':
							return 
					else:
						self.column += steps
			
			# moving of the horizontal trucks
			if self.length == 3:

				# dont move horizontal trucks of the board
				if (self.column + steps) > 3 or (self.column + steps) < 0:
					return

				# dont move horizontal trucks if another car is in that place
				if steps > 0:
					for i in range(1, steps + 1):
						if board[self.row, (self.column + 2 + i)] != '.': 
							return
					else:
						self.column += steps

				else:
					for i in range(steps, 0):
						if board[self.row, (self.column + i)] != '.':
							return
					else:
						self.column += steps
		
		# move vehicles with vertical orientation
		if self.orientation == 'V':

			# moving of the vertical cars
			if self.length == 2:

				# dont move vertical cars of the board
				if (self.row + steps) > 4 or (self.row + steps) < 0:
					return

				# dont move vertical cars if another vehicle is in that place
				if steps > 0:
					for i in range(1, steps + 1):
						if board[(self.row + 1 + i), self.column] != '.':
							return
					else:
						self.row += steps

				else: 
					for i in range(steps, 0):
						if board[(self.row + i), self.column] != '.':
							return
					else:
						self.row += steps
			
			# moving of the vertical trucks
			if self.length == 3:

				# dont move vertical trucks of the board
				if (self.row + steps) > 3 or (self.row + steps) < 0:
					return
				
				# dont move vertical trucks if another vehicle is in that place
				if steps > 0:
					for i in range(i, steps + 1):
						if board[(self.row + 2 + i), self.column] != '.':
							return
					else:
						self.row += steps

				else: 
					for i in range(steps, 0):
						if board[(self.row + i), self.column] != '.':
							return
					else:
						self.row += steps
		


