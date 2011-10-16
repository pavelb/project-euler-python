from lib import Primes

primes = Primes()

def main(lim):
	return max(range(1, lim), key=lambda n: n / primes.phi(n))

print(main(1000000)) # 510510
