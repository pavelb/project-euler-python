from itertools import count
from math import sqrt

def primes(limit = float('inf')):
	prim = list()
	for n in count(2):
		rootn = sqrt(n)
		if n > limit:
			return
		good = True
		for p in prim:
			if p > rootn:
				break
			if n % p == 0:
				good = False
				break
		if good:
			prim.append(n)
			yield n

def main(n):
	return next(p for i, p in enumerate(primes()) if i + 1 == n)

print(main(10001))