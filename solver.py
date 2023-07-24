import math
from generator import generate_board
import random
import copy

def print_board(bo):
	for i in range(len(bo)):
		if i!=0 and i%3==0:
			print("- - - - - - - - - - - - ")
		for j in range(len(bo[0])):
			if j%3 == 0 and j!=0:
				print(" | ",end="")

			if j==8:
				print(bo[i][j])
			else:
				print(str(bo[i][j]) + " ",end="")

	# return bo


def canPlace(bo,number,row,col,n):
	# check row and col
	for i in range(n):
		if(bo[row][i]==number or bo[i][col]==number):
			return False

	# check subgrid
	rn = int(math.sqrt(n))
	sx = (row // rn) * rn
	sy = (col // rn) * rn

	for x in range(int(sx), int(sx+rn)):
		for y in range(int(sy), int(sy+rn)):
			if(bo[x][y] == number):
				return False

	return True


def solveSudoku(bo,row,col,n):
	# base case
	if row == n:
		# print_board(bo)
		# return True
		solved = [row[:] for row in bo]
		return solved

	if(col == n):
		return solveSudoku(bo,row+1,0,n)
	if bo[row][col] != 0:
		return solveSudoku(bo,row,col+1,n)

	for number in range(1,n+1):
		if(canPlace(bo,number,row,col,n)):
			bo[row][col] = number
			check = solveSudoku(bo,row,col+1,n)

			if(check):
				return check

	# Backtrack
	bo[row][col] = 0
	return False


# def generate_board(new_board):
# 	# Generate the number of cells to delete
# 	delete_cells = random.randint(30,60)
# 	for i in range(delete_cells):
# 		x = random.randint(0,8)
# 		y = random.randint(0,8)
# 		new_board[x][y] = 0
# 	return new_board

board = [
	[7,8,0,4,0,0,1,2,0],
	[6,0,0,0,7,5,0,0,9],
	[0,0,0,6,0,1,0,7,8],
	[0,0,7,0,4,0,2,6,0],
	[0,0,1,0,5,0,9,3,0],
	[9,0,4,0,6,0,0,0,5],
	[0,7,0,3,0,0,0,1,2],
	[1,2,0,0,0,7,4,0,0],
	[0,4,9,2,0,6,0,0,7]
]

new_board = [
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0]
]


# solved = solveSudoku(board,0,0,9)
# unsolved = generate_board(solved)
# print_board(unsolved)

# print_board(solveSudoku(unsolved,0,0,9))



