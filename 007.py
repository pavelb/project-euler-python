from lib import Primes
from itertools import islice

primes = Primes()

def main(n):
	return next(islice(primes.gen(), n - 1, n))

print(main(10001)) # 104743
