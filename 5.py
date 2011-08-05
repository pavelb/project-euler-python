from functools import reduce
from itertools import count

def primes(limit = float('inf')):
	prim = list()
	for n in count(2):
		if n > limit: return
		if all(n % k != 0 for k in prim):
			prim.append(n)
			yield n

def product(it):
	return reduce(lambda a, b: a * b, it)

def contribution(k, n): # return k^e for max e given k^e | n
	a, b = 1, k
	while n % b == 0:
		a, b = b, b * k
	return a

def main(n):
	# trick: consider the maximum individual contribution of each prime factor
	return product(max(contribution(p, n) for n in range(2, n + 1)) for p in primes(n))

print(main(20))