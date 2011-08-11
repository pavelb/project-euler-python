from math import sqrt

def countRec(n, m):
	return n * (n + 1) * m * (m + 1) // 4

def main(target):
	# trick: minimize f(n, m) = |countRec(n, m) - target| over the integers, easy since convex
	maxw = int(sqrt(0.25 + 2 * sqrt(target)) - 0.5)
	dims = ((w, round(sqrt(0.25 + 4 * target / (w * (w + 1))) - 0.5)) for w in range(1, maxw + 1))
	_, w, h = min((abs(target - countRec(w, h)), w, h) for w, h in dims)
	return w * h

print(main(2000000))