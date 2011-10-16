from lib import Primes, multiply
from itertools import takewhile

primes = Primes()

def contribution(k, n): # return k^e for max e given k^e | n
	rv = 1
	while n % k == 0:
		n //= k
		rv *= k
	return rv

def main(n):
	# trick: consider the maximum individual contribution of each prime factor
	maxContribution = lambda p: max(contribution(p, n) for n in range(2, n + 1))
	factors = takewhile(lambda k: k <= n, primes.gen())
	return multiply(map(maxContribution, factors))

print(main(20)) # 232792560
