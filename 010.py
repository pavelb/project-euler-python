from lib import Primes

primes = Primes()

def main(limit):
	return sum(primes.gen(limit))

print(main(2000000))