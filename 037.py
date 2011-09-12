<<<<<<< HEAD
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

print(main(11)) # 748317
=======
from lib import Primes, digits, num
from itertools import islice, chain

primes = Primes()

def special(p):
	if p < 10:
		return False
	d = list(digits(p))
	return all(map(primes.isPrime, chain.from_iterable((num(d[i:]), num(d[:-i])) for i in range(1, len(d)))))

def main(limit):
	return sum(islice(filter(special, primes.gen()), limit))

print(main(11)) # 748317
>>>>>>> upstream/master
