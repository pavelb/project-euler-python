from itertools import count, takewhile
from lib import Primes

primes = Primes()

def countPrimeSets(a, b):
	return next(n for n in count() if not primes.isPrime(n * n + a * n + b))

def coefficients(alim, blim):
	# trick: f(0) = b so b must be prime
	# trick: f(n) = n^2 + na + b >= 2 so a >= (2 - b) // n - n
	# trick: from the question we know that n >= 41
	n = 41
	for b in primes.gen():
		if b >= blim:
			break
		for a in range(max((2 - b) // n - n, -alim), alim):
			yield a, b

def main(alim, blim):
	a, b = max(coefficients(alim, blim), key=lambda c: countPrimeSets(*c))
	return a * b

if __name__ == '__main__':
	print(main(1000, 1000)) # -59231
