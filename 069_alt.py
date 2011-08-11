from math import sqrt

def primesUpTo(n):
	nroot = int(sqrt(n))
	sieve = [True] * (n + 1)
	sieve[0] = False
	sieve[1] = False
	for i in range(2, nroot + 1):
		if sieve[i]:
			m = n // i - i
			sieve[i * i: n + 1:i] = [False] * (m + 1)
	return [i for i in range(n + 1) if sieve[i]]

def primeGen():
	lim = 2
	i = 0
	while True:
		prime = primesUpTo(lim)
		l = len(prime)
		while i < l:
			yield prime[i]
			i += 1
		lim *= 2

def main(lim):
	# trick: to minimize phi(n) and maximize n need n to not have duplicate factors
	prod = 1
	for p in primeGen():
		prod *= p
		if lim < prod * p:
			return prod

print(main(1000000))
