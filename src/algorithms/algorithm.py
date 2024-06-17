import pandas as pd
import numpy as np
import copy

class Algorithm:
    def __init__(self, board):
        self.board = board
        self.state_archive = set([self.board])

    def get_actions(self, board):
        """
        Get the possible next game states for 'board'.
        args:
            board: the board you want to find the possible game states for
        return:
            possible_gamestates: a list of boards that are direct possible next gamestates for the initial board
        """
        possible_gamestates = []

        for car in board.cars.values():
            if car.orientation == "H" and car.x_pos - 1 >= 0:
                if board.grid[car.y_pos, car.x_pos - 1] == ".":
                    board_copy = copy.deepcopy(board)
                    board_copy.depth += 1
                    board_copy.cars[car.name].x_pos -= 1
                    board_copy.moves.append((car.name, -1))
                    board_copy.update()
                    possible_gamestates.append(board_copy)

            if car.orientation == "H" and car.x_pos + car.length < board.shape:
                if board.grid[car.y_pos, car.x_pos + car.length] == ".":
                    board_copy = copy.deepcopy(board)
                    board_copy.depth += 1
                    board_copy.cars[car.name].x_pos += 1
                    board_copy.moves.append((car.name, 1))
                    board_copy.update()
                    possible_gamestates.append(board_copy)

            if car.orientation == "V" and car.y_pos - 1 >= 0:
                if board.grid[car.y_pos - 1, car.x_pos] == ".":
                    board_copy = copy.deepcopy(board)
                    board_copy.depth += 1
                    board_copy.cars[car.name].y_pos -= 1
                    board_copy.moves.append((car.name, -1))
                    board_copy.update()
                    possible_gamestates.append(board_copy)

            if car.orientation == "V" and car.y_pos + car.length < board.shape:
                if board.grid[car.y_pos + car.length, car.x_pos] == ".":
                    board_copy = copy.deepcopy(board)
                    board_copy.depth += 1
                    board_copy.cars[car.name].y_pos += 1
                    board_copy.moves.append((car.name, 1))
                    board_copy.update()
                    possible_gamestates.append(board_copy)

        return possible_gamestates

    def run(self):
        pass

    def prune():
        pass

    def reset():
        pass
