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
		self.moves = 0

	def move(self, steps, board):

		# move vehicles with horizontal orientation
		if self.orientation == 'H':

			# dont move horizontal cars of the board
			if (self.column + steps) > (board.shape[0] - self.length) or (self.column + steps) < 0:
				return False

			# dont move horizontal cars if another car is in that place otherwise move the car
			if steps > 0:
				for i in range(1, steps + 1):
					if board[self.row, (self.column + self.length - 1 + i)] != '.':
						return False
				else:
					self.column += steps
					self.moves += steps

			else:
				for i in range(steps, 0):
					if board[self.row, (self.column + i)] != '.':
						return False
				else:
					self.column += steps
					self.moves += steps


		# move vehicles with vertical orientation
		if self.orientation == 'V':

			# dont move vertical cars of the board
			if (self.row + steps) > (board.shape[0] - self.length) or (self.row + steps) < 0:
				return False

			# dont move vertical cars if another vehicle is in that place otherwise move the car
			if steps > 0:
				for i in range(1, steps + 1):
					if board[(self.row + self.length - 1 + i), self.column] != '.':
						return False
				else:
					self.row += steps
					self.moves += steps

			else:
				for i in range(steps, 0):
					if board[(self.row + i), self.column] != '.':
						return False
				else:
					self.row += steps
					self.moves += steps
					
		return True
