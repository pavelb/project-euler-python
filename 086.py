from lib import pythagoreanTriples
from itertools import count, takewhile
from math import sqrt

def countTriples(p, q, M):
	count = 0
	if q <= M:
		count += p // 2
	if p <= M:
		count += max(0, q // 2 - (q - p) + 1)
	return count

def countPaths(M):
	maxPerim = (3 + sqrt(5)) * M
	triples = takewhile(lambda t: sum(t) <= maxPerim, pythagoreanTriples())
	return sum(countTriples(p, q, M) for p, q, _ in triples)

def main(limit):
	# unwrap the box and draw straight lines from S to F
	# we see that the path is a hypotenuse
	# to get integer paths use pythagorean triples
	return next(M for M in count() if countPaths(M) > limit)

print(main(10 ** 6)) # 1818
