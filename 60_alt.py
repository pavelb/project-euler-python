from math import sqrt, log10

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

def primes():
	lim = 2
	i = 0
	while True:
		prime = primesUpTo(lim)
		l = len(prime)
		while i < l:
			yield prime[i]
			i += 1
		lim *= 2

def prime(n):
	return all(n % i != 0 for i in range(2, int(sqrt(n)) + 1))

def concat(a, b):
	return int(a * pow(10, 1 + int(log10(b))) + b)

def cached(fn):
	cache = dict()
	def new(a, b):
		key = a * b
		if key in cache:
			rv = cache[key]
		else:
			rv = fn(a, b)
			cache[key] = rv
		return rv
	return new

@cached
def pcommute(a, b):
	return prime(concat(a, b)) and prime(concat(b, a))

def main(lim):
	tuples = [[]]
	for p in primes():
		for tuple in tuples:
			if all(pcommute(p, n) for n in tuple):
				t = tuple + [p]
				if len(t) >= lim:
					return sum(t)
				tuples.append(t)

print(main(5))