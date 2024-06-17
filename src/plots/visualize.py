from ..game.board import *


def visualize_moves(board, moves):
	board.plot(show=True)

	plt.ion()
	
	for move_code in moves:
		car_name, step = move_code
		print(car_name, step)
		board.cars[car_name].move(step, board.grid)
		
		fig, _ = board.plot()
		board.update()
		fig.canvas.draw()
		plt.pause(0.5)
		fig.canvas.flush_events()
		plt.close()
	
	plt.ioff()
	
	board.plot(show=True)
