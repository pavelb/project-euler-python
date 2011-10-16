from itertools import count, takewhile
from lib import Primes

primes = Primes()

def main(limit):
	fun = lambda n: (n + 1) ** 3 - n ** 3
	seq = map(fun, count())
	seq = takewhile(lambda p: p < limit, seq)
	seq = map(primes.isPrime, seq)
	return sum(seq)

print(main(10 ** 6)) # 173
