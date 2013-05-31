from lib import Primes, digits, num
from itertools import islice, chain

primes = Primes()

def good(p):
	if p < 10:
		return False
	d = digits(p)
	splitd = lambda i: (d[:i], d[i:])
	indices = range(1, len(d))
	splits = map(splitd, indices)
	parts = chain.from_iterable(splits)
	partNums = map(num, parts)
	return all(map(primes.isPrime, partNums))

def main(limit):
	goodPrimes = filter(good, primes.gen())
	return sum(islice(goodPrimes, limit))

if __name__ == '__main__':
	print(main(11)) # 748317
