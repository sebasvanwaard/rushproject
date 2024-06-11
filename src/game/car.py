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

	def move(self, steps, board):

		# move vehicles with horizontal orientation
		if self.orientation == 'H':

			# dont move horizontal cars of the board
			if (self.x_pos + steps) > (board.shape[0] - self.length) or (self.x_pos + steps) < 0:
				return False

			# dont move horizontal cars if another car is in that place otherwise move the car
			if steps > 0:
				for i in range(1, steps + 1):
					if board[self.y_pos, (self.x_pos + self.length - 1 + i)] != '.':
						return False
				else:
					self.x_pos += steps

			else:
				for i in range(steps, 0):
					if board[self.y_pos, (self.x_pos + i)] != '.':
						return False
				else:
					self.x_pos += steps


		# move vehicles with vertical orientation
		if self.orientation == 'V':

			# dont move vertical cars of the board
			if (self.y_pos + steps) > (board.shape[0] - self.length) or (self.y_pos + steps) < 0:
				return False

			# dont move vertical cars if another vehicle is in that place otherwise move the car
			if steps > 0:
				for i in range(1, steps + 1):
					if board[(self.y_pos + self.length - 1 + i), self.x_pos] != '.':
						return False
				else:
					self.y_pos += steps


			else:
				for i in range(steps, 0):
					if board[(self.y_pos + i), self.x_pos] != '.':
						return False
				else:
					self.y_pos += steps
					
		return True
