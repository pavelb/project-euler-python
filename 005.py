from lib import Primes, multiply

primes = Primes()

def contribution(k, n): # return k^e for max e given k^e | n
	rv = 1
	while n % k == 0:
		n //= k
		rv *= k
	return rv

def main(n):
	# trick: consider the maximum individual contribution of each prime factor
	return multiply(max(contribution(p, n) for n in range(2, n + 1)) for p in primes.gen(n))

print(main(20))