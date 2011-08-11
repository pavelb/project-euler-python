from math import sqrt
from functools import reduce
from itertools import count, combinations

def primes(last):
	sieve = [True] * (last + 1)
	sieve[0] = False
	sieve[1] = False
	for i in range(2, int(sqrt(last)) + 1):
		if sieve[i]:
			sieve[i * i:last + 1:i] = [False] * (last // i - i + 1)
	return [i for i, prime in enumerate(sieve) if prime]

def primesOfLen(digits):
	lbound = pow(10, digits - 1)
	ubound = 10 * lbound - 1
	rv = primes(ubound)
	i = next(i for i, p in enumerate(rv) if p > lbound)
	return rv[i:]

def digit(n, i):
	return int(str(n)[i])

def sameDigit(n, pos):
	s = str(n)
	ref = s[pos[0]]
	return all(s[p] == ref for p in pos)

def main(lim):
	rv = []
	for digits in count(1):
		primes = primesOfLen(digits)
		table = [[set() for _ in range(10)] for _ in range(digits)]
		for p in primes:
			for d in range(digits):
				table[d][digit(p, d)].add(p)
		for matches in range(1, digits):
			for matchPos in combinations(range(digits), matches):
				starPos = [i for i in range(digits) if i not in matchPos]
				results = reduce(lambda t1, t2: [r1 & r2 for r1 in t1 for r2 in t2], (table[m] for m in matchPos))
				results = ([n for n in tuple if sameDigit(n, starPos)] for tuple in results)
				rv.extend(r for r in results if len(r) >= lim)
		if len(rv) > 0:
			return min(map(sorted, rv))[0]

from time import clock
a = clock()
print(main(8))
print(clock() - a)
