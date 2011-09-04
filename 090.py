from itertools import combinations, product

def checkIfIn(d1, d2, c1, c2):
	return (d1 in c1 and d2 in c2) or (d2 in c1 and d1 in c2)

def canMakeSquares(cubes):
	c1, c2 = cubes
	return \
		checkIfIn(0, 1, c1, c2) and \
		checkIfIn(0, 4, c1, c2) and \
		(checkIfIn(0, 9, c1, c2) or checkIfIn(0, 6, c1, c2)) and \
		(checkIfIn(1, 6, c1, c2) or checkIfIn(1, 9, c1, c2)) and \
		checkIfIn(2, 5, c1, c2) and \
		(checkIfIn(3, 6, c1, c2) or checkIfIn(3, 9, c1, c2)) and \
		(checkIfIn(4, 9, c1, c2) or checkIfIn(4, 6, c1, c2)) and \
		(checkIfIn(6, 4, c1, c2) or checkIfIn(9, 4, c1, c2)) and \
		checkIfIn(8, 1, c1, c2)

def main():
	# One of the worst problems on PE
	# There is less code here than it took to describe the problem
	return sum(map(canMakeSquares, product(combinations(range(10), 6), repeat=2))) // 2

print(main()) # 1217
