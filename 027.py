from itertools import count, takewhile
from lib import Primes

primes = Primes()

def countPrimeSets(a, b):
	return next(n for n in count() if not primes.isPrime(n * n + a * n + b))

def main(alim, blim):
	# trick: f(0) = b so b must be prime
	# trick: f(1) = a + b >= 2 so a >= -(b-2)
	coeff = ((a, b) for b in takewhile(lambda n: n < blim, primes.gen()) for a in range(-min(b - 2, alim - 1), alim))
<<<<<<< HEAD
	a, b = max(coeff, key=lambda c: countPrimeSets(c[0], c[1]))
=======
	a, b = max(coeff, key = lambda c: countPrimes(c[0], c[1]))
>>>>>>> upstream/master
	return a * b

print(main(1000, 1000)) # -59231
