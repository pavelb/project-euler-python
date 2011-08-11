from functools import reduce
from itertools import count

def primes(limit = float('inf')):
	prim = list()
	for n in count(2):
		if n > limit: return
		good = True
		for p in prim:
			if p * p > n: break
			if n % p == 0:
				good = False
				break
		if good:
			prim.append(n)
			yield n

def factor(n):
	prims = primes()
	sq = n ** 0.5
	rv = []
	i = 0
	p = next(prims)
	while p <= sq:
		if n % p == 0:
			count = 0
			while n % p == 0:
				count += 1
				n /= p
			sq = n ** 0.5
			rv.append([p, count])
		i += 1
		p = next(prims)
	if n > 1: rv.append([n, 1])
	return rv

def product(it):
	return reduce(lambda a, b: a * b, it)

def numDivisors(n):
	return product(e + 1 for _, e in factor(n))

def main(n):
	for i in count(2):
		t = i * (i + 1) // 2
		if numDivisors(t) > n:
			return t

print(main(500))