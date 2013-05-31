from lib import multiply
from math import sqrt

def countRec(n, m):
	return n * (n + 1) * m * (m + 1) // 4

def main(target):
	# trick: minimize f(n, m) = |countRec(n, m) - target| over the integers, easy since convex
	maxw = int(sqrt(0.25 + 2 * sqrt(target)) - 0.5)
	dims = ((w, round(sqrt(0.25 + 4 * target / (w * (w + 1))) - 0.5)) for w in range(1, maxw + 1))
	distToTarget = lambda d: abs(target - countRec(d[0], d[1]))
	return multiply(min(dims, key=distToTarget))

if __name__ == '__main__':
	print(main(2000000)) # 2772
