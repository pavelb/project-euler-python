from lib import Primes, multiply
from itertools import count

primes = Primes()

def main(limit):
	solns = lambda n: (multiply(2 * e + 1 for _, e in primes.factors(n)) + 1) // 2

	n = 1
	bases = []
	for p in primes.gen():
		n *= p
		bases.append(n)
		if solns(n) > limit:
			break

	rv = bases.pop()
	for base in reversed(bases):
		candidates = (base * n for n in count(1))
		n = next(n for n in candidates if solns(n) > limit)
		if rv <= n:
			return rv
		rv = n

print(main(1000)) # 180180
