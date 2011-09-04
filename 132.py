# not done

from lib import Primes
from itertools import count

primes = Primes()

def isFactor(p, e):
	return pow(10, e + 1, 9 * p) == 1

def main(primeCount, e):
	rv = 0
	for p in count(1, 2):
		if not primes.isPrime(p):
			continue
		if primeCount == 0:
			break
		i = 1
		while isFactor(pow(p, i), e):
			print(40 - primeCount + 1, p)
			rv += p
			primeCount -= 1
			i += 1
	return rv

print(main(40, 10 ** 9))
