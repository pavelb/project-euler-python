from lib import Dijkstra
from itertools import product

def main(file):
	with open(file, 'r') as f:
		matrix = [[int(n) for n in line.rstrip().split(',')] for line in f]

	size = len(matrix)
	START = (0, 0)
	FINISH = (size - 1, size - 1)
	vertices = product(range(size), repeat=2)

	def neighbours(v):
		x, y = v
		if x > 0: yield x - 1, y
		if y > 0: yield x, y - 1
		if y + 1 < size: yield x, y + 1
		if x + 1 < size: yield x + 1, y

	def distance(u, v):
		x, y = v
		return matrix[y][x]

	return Dijkstra(vertices, neighbours, distance, START)[FINISH]

if __name__ == '__main__':
	print(main('083.txt')) # 425185
