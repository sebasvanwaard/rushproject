import pandas as pd
import argparse
import numpy as np


class Car:
	def __init__(self, name, x_pos, y_pos, length, orientation, color):

		self.name = name
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.length = length
		self.orientation = orientation
		self.color = color
	
	def move(self, step, board):
		"""
		Function to move the car on the board.
		args:
			steps: the amount of steps to move the car
			board: the Board object the car belongs to
		returns True if move was made, False if the move could not be made (because cars/walls were in the way)
		"""
		moves = self.get_possible_moves(board.gird)

		if step in moves:
			if self.orientation == 'H':
				self.x_pos += step
			elif self.orientation == 'V':
				self.y_pos += step
			return True
		else:
			return False

	def simple_move(self, step):
		"""
		Equivalent to the normal move function, but does not check if the move is possible or not. This has to be done before calling the function!
		args:
			step: the step to be taken
		returns: -
		"""
		if self.orientation == 'H':
			self.x_pos += step
		if self.orientation == 'V':
			self.y_pos += step

	def get_possible_moves(self, board_grid):
		"""
		Funtion to check and return the moves that are possible for the car. Check 1 space in front and behind the car
		args:
			board_grid: the grid of to the board to which the car belongs
		returns:
			a list of the possible moves (can be either 1 or -1)
		"""

		moves = set()

		if self.orientation == "H":
			if not self.x_pos - 1 < 0:
				if board_grid[self.y_pos, self.x_pos - 1] == '.':
					moves.add(-1)

			if not self.x_pos + self.length >= board_grid.shape[0]:
				if board_grid[self.y_pos, self.x_pos + self.length] == '.':
					moves.add(1)
		
		if self.orientation == 'V':
			if not self.y_pos - 1 < 0:
				if board_grid[self.y_pos - 1, self.x_pos] == '.':
					moves.add(-1)
					
			if not self.y_pos + self.length >= board_grid.shape[0]:
				if board_grid[self.y_pos + self.length, self.x_pos] == '.':
					moves.add(1)
			
		return moves