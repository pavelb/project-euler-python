from itertools import count
from lib import Primes

primes = Primes()

def countPrimes(a, b):
	return next(n for n in count() if not primes.isPrime(n * n + a * n + b))

def main(alim, blim):
	# trick: f(0) = b so b must be prime
	# trick: f(1) = a + b >= 2 so a >= -(b-2)
	coeff = ((a, b) for b in primes.gen(blim) for a in range(-min(b - 2, alim - 1), alim))
	_, a, b = max((countPrimes(a, b), a, b) for a, b in coeff)
	return a * b

print(main(1000, 1000))