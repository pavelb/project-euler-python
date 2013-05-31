import sys

# returns True if the board does not have repeated digits in any row/col/region
def valid(board):
	# returns True if no repeated digits in row i
	def validLineH(board, i):
		digits = [False] * 10
		for j in range(9):
			digit = board[i][j]
			if digit != 0 and digits[digit]:
				return False
			digits[digit] = True
		return True
	# returns True if no repeated digits in col j
	def validLineV(board, j):
		digits = [False] * 10
		for i in range(9):
			digit = board[i][j]
			if digit != 0 and digits[digit]:
				return False
			digits[digit] = True
		return True
	# returns True if no repeated digits in region starting at i0, j0
	def validBlock(board, i0, j0):
		digits = [False] * 10
		for i in range(i0, i0 + 3):
			for j in range(j0, j0 + 3):
				digit = board[i][j]
				if digit != 0 and digits[digit]:
					return False
				digits[digit] = True
		return True
	# ensure all rows are valid
	if any(not validLineH(board, j) for j in range(9)):
		return False
	# ensure all cols are valid
	if any(not validLineV(board, i) for i in range(9)):
		return False
	# ensure all regions are valid
	if any(not validBlock(board, 3 * i0, 3 * j0) for i0 in range(3) for j0 in range(3)):
		return False
	return True

# the basic solver
def solve_b(board):
	# create a list of the modifiable cells
	empties = []
	for i in range(9):
		for j in range(9):
			if board[i][j] == 0:
				empties.append([i, j])
	# this is the backtracking solution, on a valid solution increment the next modifiable cell
	# otherwise increment the current cell. on overflow set current cell to zero and backtrack
	e = 0
	while e < len(empties):
		i, j = empties[e]
		board[i][j] += 1
		if board[i][j] == 10:
			board[i][j] = 0
			e -= 1
		elif valid(board):
			e += 1

# set all modifiable cells to a bitmap B
# if B[i] is true the cell may contain the digit 1+i
def initEmpties(board):
	for i in range(9):
		for j in range(9):
			if board[i][j] == 0:
				board[i][j] = [True] * 9

# eliminate options from the bitmap of each modifiable cell based on the fixed cells
# then check if any bitmap only has a single value i s.t. B[i] is true and replace the bitmap with 1+i
# as it is the only option for that cell
def eliminateAndSimplify(board):
	# eliminate digit from call modifiable cells in row i
	def eliminateLineH(digit, board, i):
		for j in range(9):
			if type(board[i][j]) == list:
				board[i][j][digit - 1] = False
	# eliminate digit from call modifiable cells in col j
	def eliminateLineV(digit, board, j):
		for i in range(9):
			if type(board[i][j]) == list:
				board[i][j][digit - 1] = False
	# eliminate digit from call modifiable cells in region starting at i0, j0
	def eliminateBlock(digit, board, i0, j0):
		for i in range(i0, i0 + 3):
			for j in range(j0, j0 + 3):
				if type(board[i][j]) == list:
					board[i][j][digit - 1] = False

	rescan = True
	while rescan:
		rescan = False
		# elimination phase, iterate through all fixed cells and eliminate them from all modifiable cells
		for i in range(9):
			for j in range(9):
				cell = board[i][j]
				if type(cell) == int:
					eliminateLineH(cell, board, i)
					eliminateLineV(cell, board, j)
					eliminateBlock(cell, board, 3 * (i // 3), 3 * (j // 3))
		# simplification phase, find modifiable cells with only one possible value and fix that value to them
		for i in range(9):
			for j in range(9):
				cell = board[i][j]
				if type(cell) == list:
					if sum(cell) == 1:
						for index, valid in enumerate(cell):
							if valid:
								board[i][j] = 1 + index
								rescan = True
								break

# replace the bitmaps with zeroes
def zeroOutOptions(board):
	for i in range(9):
		for j in range(9):
			if type(board[i][j]) == list:
				board[i][j] = 0

# the extra solver
def solve(board):
	# iterate through all modifiable cell in the board. Let 1+i be a potential digit for the current cell C.
	# look at Cs row and see if any other cell can have the value 1+i, if not then C must have the value 1+i
	# similarly for Cs column and region
	def chooseOnlyCandidate(board):
		# return true if digit can be the value of only a single cell in row io
		def existsLineH(digit, board, io, jo):
			i = io
			for j in range(9):
				if j == jo:
					continue
				cell = board[i][j]
				if type(cell) == list and cell[digit - 1]:
					return True
			return False
		# return true if digit can be the value of only a single cell in col jo
		def existsLineV(digit, board, io, jo):
			j = jo
			for i in range(9):
				if i == io:
					continue
				cell = board[i][j]
				if type(cell) == list and cell[digit - 1]:
					return True
			return False
		# return true if digit can be the value of only a single cell in region of cell io, jo
		def existsBlock(digit, board, io, jo):
			i0 = 3 * (io // 3)
			j0 = 3 * (jo // 3)
			for i in range(i0, i0 + 3):
				for j in range(j0, j0 + 3):
					if i == io and j == jo:
						continue
					cell = board[i][j]
					if type(cell) == list and cell[digit - 1]:
						return True
			return False

		for i in range(9):
			for j in range(9):
				cell = board[i][j]
				if type(cell) == list:
					for index, valid in enumerate(cell):
						if valid:
							digit = index + 1
							if not existsLineH(digit, board, i, j) or not existsLineV(digit, board, i, j) or not existsBlock(digit, board, i, j):
								board[i][j] = digit
								return True
		return False

	# step 1
	initEmpties(board)
	eliminateAndSimplify(board)
	# step 2
	while chooseOnlyCandidate(board):
		eliminateAndSimplify(board)
	# step 3
	zeroOutOptions(board)
	solve_b(board)

# format a cell for printing
def fmt(r):
	return '%d\t\t' % r if type(r) == int else '%s\t' % ''.join(str(1 + i if b else '.') for i, b in enumerate(r))

def printBoard(board):
	sys.stdout.write('\n')
	for row in board:
		sys.stdout.write(' '.join(fmt(r) for r in row))
		sys.stdout.write('\n')
	sys.stdout.flush()

def main(file): # 24702
	rv = 0
	with open(file, 'r') as f:
		while f.readline():
			board = []
			for _ in range(9):
				row = list(str(f.readline()).strip())
				board.append([int(r) for r in row])
			solve(board)
			rv += board[0][0] * 100 + board[0][1] * 10 + board[0][2]
	return rv

if __name__ == '__main__':
	print(main('096.txt')) # 24702
