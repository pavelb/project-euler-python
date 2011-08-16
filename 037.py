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
