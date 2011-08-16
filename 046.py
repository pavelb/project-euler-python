from itertools import takewhile, count
from lib import Primes, square

primes = Primes()

def goldbach(n):
	return any(square((n - p) / 2) for p in takewhile(lambda p: p < n, primes.gen()))

def main():
	return next(n for n in count(3, 2) if not primes.isPrime(n) and not goldbach(n))

print(main()) # 5777
