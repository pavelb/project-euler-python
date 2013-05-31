from lib import reduceFrac
from itertools import product

def countRT(p, limit): # counts right triangles OPQ where Q is to the left of OP
	# for a right angle, Q must lie on line perpendicular to OP
	# get the shortest integer vector on that line in the counter-clockwise direction
	# count how many times we can add it to P before going out of bounds
	if p[1] == 0: return limit
	dx, dy = reduceFrac(*p)
	return min(p[0] // dy, (limit - p[1]) // dx)

def main(limit):
	# count right triangles at P, double them for Q by symmetry, then add triangles at O
	nonxpoints = product(range(1, limit + 1), range(limit + 1))
	rv = sum(countRT(P, limit) for P in nonxpoints)
	rv *= 2 # same for Q
	rv += limit * limit # triangles where the right angle is at O
	return rv

if __name__ == '__main__':
	print(main(50)) # 14234
