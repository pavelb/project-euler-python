from lib import Primes, digits, num

primes = Primes()

def circular(p):
	d = list(digits(p))
	return all(primes.isPrime(num(d[i:] + d[:i])) for i in range(1, len(d)))

def main(limit):
	return sum(circular(p) for p in primes.gen(limit))

print(main(1000000))