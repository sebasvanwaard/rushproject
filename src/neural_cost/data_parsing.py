import pandas as pd
import numpy as np
import csv


# from ..algorithms import breadth_first as bf


def convert_board(board_string):
	"""
	Converts a board in Michael Fogleman's format to our format:
	args:
		board_string: the string in Michaels format
	returns:
		converted_string: the board string in our format
	"""
	converted_string = ""
	for char in board_string:
		if char == 'A':
			converted_string += 'X'
		elif char == 'o':
			converted_string += '.'
		else:
			converted_string += chr(ord(char) - 1)

	return converted_string

def board_string_to_df(board_string, shape):
	"""
	Function that converts the converted_board string to a dataframe that can be writen to the board csv
	args:
		board_string: the converted board_string
		shape: the shape of the board
	returns:
		pandas dataframe with the board
	"""
	board_dict = {}

	for i in range(len(board_string)):		
		if board_string[i] != '.':
			if board_string[i] not in board_dict:
				row = i // shape + 1
				column = i % shape + 1
				orientation = 'V'
				if column < shape:
					if board_string[i+1] == board_string[i]: # double if statement to prevent index out of bounds
						orientation = 'H'
				board_dict[board_string[i]] = [orientation, column, row, 1]
			else:
				board_dict[board_string[i]][3] += 1
	
	df = pd.DataFrame.from_dict(board_dict, orient='index', columns=['orientation', 'col', 'row', 'length'])
	df.index.name = 'car'
	return df


# code to convert the list of board by Michael Fogleman to a format we could train our model on

data_dicts = []
with open('src/neural_cost/rush.txt') as file:
	for line in file:
		split_line = line.split(sep=' ')
		if 'x' not in split_line[1]:
			data_dicts.append({'moves': split_line[0], 'board': convert_board(split_line[1])})
	
with open('src/neural_cost/board_data.csv', 'w') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=['moves', 'board'])
	writer.writeheader()
	writer.writerows(data_dicts)








# def get_training_data():
# 	starting_board
# 	solution = get_solution(starting_board)

# 	for move in solution:
# 		x_data_array.append(previous_state + possible_next_state)
# 		y_data_array.append( 1 if good move 0 if bad)

