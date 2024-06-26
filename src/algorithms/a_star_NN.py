from .algorithm import Algorithm

import copy
import math
import numpy as np
from tensorflow.keras import models

import time

class A_star_nn(Algorithm):
    """
	This is a subclass of the class Algorithm and entails the A* algorithm. 
	"""

    def __init__(self, board, model="src/neural_cost/models/board_cost_model_36x72x144x1.h5"):
        """
		The subclass A* with the neural network initializes everything from the parent class Algorithm and loads the neural network model used. 
		"""

        super().__init__(board)
        self.cost_model = models.load_model(model)

    def run(self, max_time = math.inf):
        """
        run an A* search for a solution of the given board, with a neural network model to predict the moves necessary to solve the puzzle. 
        Using a priority dictionary.
        args:
            max_time: maximum time to solve the puzzle before giving up. Default set to math.inf.
		returns:
			state: the board of the final state
            state_depth: the depth of the board of the final state
			total_states_used: the total states visited before the solution was found
			total_states_generated: the total amount of states generated before the solution was found
        """

        state = copy.deepcopy(self.board)
        goal_state = self.board.shape - 2

        total_states_used = 0
        total_states_generated = 0
        state_cost_dict = {state: 0}

        start_time = time.time()


        while state.cars['X'].x_pos != goal_state and time.time() - start_time < max_time:
            total_states_used += 1

            unique_id = state.get_unique_id()
            self.state_archive.add(unique_id)

            for possible_state in self.get_actions(state):
                total_states_generated += 1

                possible_unique_id = possible_state.get_unique_id()
                if possible_unique_id not in self.state_archive:
                    state_cost_dict[possible_state] = self.calc_cost(possible_state)

            state_cost_dict = dict(sorted(state_cost_dict.items(), key=lambda item: item[1], reverse=True))
            state = state_cost_dict.popitem()[0]

        return (state, state.depth, total_states_used, total_states_generated)

    
    
    def calc_cost(self, board):
        x_data = board.grid.flatten()

        to_ascii = np.vectorize(ord)
        x_data = to_ascii(x_data)
        x_data = x_data.reshape(1,36)

        return self.cost_model.predict(x_data, verbose=0)
