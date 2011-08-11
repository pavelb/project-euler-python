from functools import reduce
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

def product(it):
	return reduce(lambda a, b: a * b, it)

def contribution(k, n): # return k^e for max e given k^e | n
	rv = 1
	while n % k == 0:
		n //= k
		rv *= k
	return rv

def main(n):
	# trick: consider the maximum individual contribution of each prime factor
	return product(max(contribution(p, n) for n in range(2, n + 1)) for p in primes(n))

print(main(20))