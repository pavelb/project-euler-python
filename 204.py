from lib import Primes
from itertools import takewhile

primes = Primes()

def main(limit, ubound):
	rv = [1]
	for p in takewhile(lambda p: p < limit, primes.gen()):
		rv2 = rv[:]
		m = p
		while m <= ubound:
			for r in rv:
				s = r * m
				if s > ubound: break
				rv2.append(s)
			m *= p
		rv = sorted(rv2)
	return len(rv)

print(main(100, 10 ** 9)) # 2944730
