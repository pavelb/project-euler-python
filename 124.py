from lib import Primes, multiply

primes = Primes()

def main(limit, k):
	rad = lambda n: multiply(f for f, _ in primes.factors(n))
	return sorted(range(1, limit + 1), key=rad)[k - 1]

print(main(100000, 10000)) # 21417
