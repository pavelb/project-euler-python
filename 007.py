from lib import Primes

primes = Primes()

def main(n):
	return next(p for i, p in enumerate(primes.gen()) if i + 1 == n)

print(main(10001))