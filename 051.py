from lib import Primes, digits
from itertools import count, combinations, dropwhile, takewhile

primes = Primes()

def primesOfLen(digits):
	lbound = pow(10, digits - 1)
	ubound = 10 * lbound - 1
	gen = dropwhile(lambda p: p < lbound, primes.gen())
	return takewhile(lambda p: p < ubound, gen)

def sameDigit(n, pos):
	d = list(digits(n))
	ref = d[pos[0]]
	return all(d[p] == ref for p in pos)

def main(lim):
	for digits in count(1):
		cache = dict()
		for p in primesOfLen(digits):
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

print(main(8)) # 121313
