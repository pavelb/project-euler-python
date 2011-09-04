from lib import Primes, multiply, ngonalNums

primes = Primes()

def divisorCount(n):
	return multiply(e + 1 for _, e in primes.factors(n))

def main(n):
	return next(t for t in ngonalNums(3) if divisorCount(t) > n)

print(main(500)) # 76576500
