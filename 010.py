from lib import Primes
from itertools import takewhile

primes = Primes()

def main(limit):
	return sum(takewhile(lambda n: n < limit, primes.gen()))

print(main(2000000)) # 142913828922
