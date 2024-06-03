
class Experiment:
	def __init__(self, filename):
		self.board = Board(self.get_shape(filename), self.read_file(filename))

	def read_file(self, filename):
		"""
		Read a file containing car information for the starting position of a game of rush hour
		args:
			filename: the path to the file containing the info
		returns:
			a df/list/dict containing the car information
		"""
		pass

	def get_shape(self, filename):
		pass

class Board:
	def __init__(self, shape, car_info):
		self.shape = shape
		self.board = np.zeros(shape)
		self.cars = {'a': Car('a')}

		self.cars['a'].x_pos

	def draw(self):
		pass

	def add_cars(self, car_info):
		pass

	def read_board_csv(self):
		pass

	def check_finish(self):
		pass

class Car:
	def __init__(self, name, x_pos, y_pos, length, orientation):
		self.name = name
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.length = length
		self.orientation = orientation
	
	def move(self, steps):
		pass