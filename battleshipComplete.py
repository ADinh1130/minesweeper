import random
"""
#1
def initialize_b(row,col):
	a_boar=[['-' for i in range(col)] for j in range(col)]
	return a_boar

#2
def initialize_d(row,col):
	a_boar2=[['?' for i in range(col)] for j in range(col)]
	return a_boar2

#3
def print_board(board):
	row = len(board)
	col = len(board[0])
	print("  ", end="")
	for j in range(col):
		print(j, end=" ")
	print()
	for i in range(row):
		print(i, end=" ")
		for j in range(col):
			print(board[i][j], end=" ")
		print()
#4
def valid_guess(board, row, col):
	return board[row][col] == "?"
"""
#5
print("Hello World!")
def valid_placement(board, row, col, direction, ship_size):
	valid = True
	check_row = row
	check_col = col
	if(direction == 1):
		if(row + ship_size - 1 < len(board) and row >= 0):
			i = 0
			while(i < ship_size and valid == True):
				if(board[check_row][col] != "-"):
					valid = False
				else:
					check_row += 1
					i += 1
		else:
			valid = False

	elif(direction == -1):
		if(row - ship_size + 1 >= 0 and row < len(board)):
			i = 0
			while(i < ship_size and valid == True):
				if(board[check_row][col] != "-"):
					valid = False
				else:
					check_row -= 1
					i += 1
		else:
			valid = False

	elif(direction == 2):
		if(col >= 0 and col + ship_size - 1 < len(board[row])):
			i = 0
			while(i < ship_size and valid == True):
				if(board[row][check_col] != "-"):
					valid = False
				else:
					check_col += 1
					i += 1
		else:
			valid = False

	elif(direction == -2):
		if(col - ship_size + 1 >= 0 and col < len(board[row])):
			i = 0
			while(i < ship_size and valid == True):
				if(board[row][check_col] != "-"):
					valid = False
				else:
					check_col -= 1
					i += 1
		else:
			valid = False
	return valid

#6.5
def placer(board, row, col, direction, ship_size, letter):
	if(direction == 1):
		i = 0
		while(i < ship_size):
			board[row][col] = letter
			row += 1
			i += 1
	elif(direction == -1):
		i = 0
		while(i < ship_size):
			board[row][col] = letter
			row -= 1
			i += 1
	elif(direction == 2):
		i = 0
		while(i < ship_size):
			board[row][col] = letter
			col += 1
			i += 1
	elif(direction == -2):
		i = 0
		while(i < ship_size):
			board[row][col] = letter
			col -= 1
			i += 1
	return board
"""
#6
def place_ships(board):
	ships = [
	["Carrier",5,"C"],
	["Battleship",4,"B"],
	["Destroyer",3,"D"],
	["Submarine",3,"S"],
	["Patrol Boat",2,"P"]
	]
	for i in range(5):
		row = int(input(f"Enter {ships[i][0]} row: "))
		col = int(input(f"Enter {ships[i][0]} column: "))
		direction = int(input(f"Enter {ships[i][0]} direction: "))
		while(direction != -2 and direction != -1 and direction != 1 and direction != 2):
			direction = int(input(f"Enter {ships[i][0]} direction: "))
		valid = valid_placement(board, row, col, direction, ships[i][1])
		while(valid == False):
			row = int(input(f"Enter {ships[i][0]} row: "))
			col = int(input(f"Enter {ships[i][0]} column: "))
			direction = int(input(f"Enter {ships[i][0]} dicrection: "))
			while(direction != -2 and direction != -1 and direction != 1 and direction != 2):
				direction = int(input(f"Enter {ships[i][0]} direction: "))
			valid = valid_placement(board, row, col, direction, ships[i][1])
		board = placer(board, row, col, direction, ships[i][1],ships[i][2])
"""
#7

def ran_place(board):
	ships = [
	["Carrier",5,"C"],
	["Battleship",4,"B"],
	["Destroyer",3,"D"],
	["Submarine",3,"S"],
	["Patrol Boat",2,"P"]
	]
	for i in range(5):
		row = random.randint(0,len(board) - 1)
		col = random.randint(0,len(board[row]) - 1)
		direction = random.randint(-2,2)
		while(direction==0):
			direction = random.randint(-2,2)
		valid = valid_placement(board, row, col, direction, ships[i][1])
		while(valid == False):
			row = random.randint(0,len(board) - 1)
			col = random.randint(0,len(board[row]) - 1)
			direction = random.randint(-2,2)
			while(direction==0):
				direction = random.randint(-2,2)
			valid = valid_placement(board, row, col, direction, ships[i][1])
		board = placer(board, row, col, direction, ships[i][1],ships[i][2])
		#test
		for row  in board:
			print(row)
#8

"""
def board_update(hidden_board, display_board, row, col):
	if(hidden_board[row][col])
"""
#test

board = [
['-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-', '-']]
ran_place(board)

