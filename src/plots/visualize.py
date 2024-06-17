from ..game.board import *


def visualize_moves(board, moves):
	board.plot(show=True)

	plt.ion()
	
	for move_code in moves:
		car_name, step = move_code
		print(car_name, step)
		board.cars[car_name].move(step, board.grid)
		
		fig = board.plot()
		board.update()
		fig.canvas.draw()
		fig.canvas.flush_events()
		plt.close()
	
	plt.ioff()
	
	board.plot(show=True)
