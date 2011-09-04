from lib import Dijkstra
from itertools import product, chain

def main(file):
	with open(file, 'r') as f:
		matrix = [[int(n) for n in line.rstrip().split(',')] for line in f]

	size = len(matrix)
	START = (0, size)
	FINISH = (size, 0)
	vertices = chain([START, FINISH], product(range(size), repeat=2))

	def neighbours(v):
		if v == START:
			for y in range(size):
				yield 0, y
		elif v == FINISH:
			pass
		else:
			x, y = v
			if y > 0: yield x, y - 1
			if y + 1 < size: yield x, y + 1
			if x + 1 < size: yield x + 1, y
			if x + 1 == size: yield FINISH

	def distance(_, v):
		if v == START or v == FINISH: return 0
		x, y = v
		return matrix[y][x]

	return Dijkstra(vertices, neighbours, distance, START)[FINISH]

print(main('082.txt')) # 260324
