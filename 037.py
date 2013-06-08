from lib import Primes, digits, num
from itertools import islice

primes = Primes()

def good(p):
	if p < 10:
		return False
	d = digits(p)
	for i in range(1, len(d)):
		if not primes.isPrime(num(d[:i])):
			return False
		if not primes.isPrime(num(d[i:])):
			return False
	return True

def main(limit):
	goodPrimes = filter(good, primes.gen())
	return sum(islice(goodPrimes, limit))

if __name__ == '__main__':
	print(main(11)) # 748317
