import random

def generate_board(new_board):
	# Generate the number of cells to delete
	delete_cells = random.randint(30,40)
	for i in range(0,delete_cells):
		x = random.randint(0,8)
		y = random.randint(0,8)
		new_board[x][y] = 0
	return new_board

