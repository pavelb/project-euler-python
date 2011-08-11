from math import sqrt
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

def sameDigit(n, pos):
	s = str(n)
	ref = s[pos[0]]
	return all(s[p] == ref for p in pos)

def main(lim):
	for digits in count(1):
		primes = primesOfLen(digits)
		cache = dict()
		for p in primes:
			for stars in range(1, digits):
				for starPos in combinations(range(digits), stars):
					if sameDigit(p, starPos):
						key = str(p)
						for s in starPos:
							key = key[:s] + '*' + key[s + 1:]
						if key not in cache:
							cache[key] = []
						cache[key].append(p)
		results = [t for t in cache.values() if len(t) >= lim]
		if len(results) > 0:
			return min(map(sorted, results))[0]

from time import clock
a = clock()
print(main(8))
print(clock() - a)
