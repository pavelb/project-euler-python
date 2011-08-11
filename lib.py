from itertools import count
from math import sqrt

class Primes:
	computed = None
	computedLen = 0

	def __init__(self):
		self.compute(1024)

	def compute(self, n): # compute all primes <= n
		# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
		nroot = int(sqrt(n))
		sieve = [True] * (n + 1)
		sieve[0] = False
		sieve[1] = False
		for i in range(2, nroot + 1):
			if sieve[i]:
				sieve[i * i: n + 1:i] = [False] * (n // i - i + 1)
		self.computed = [i for i in range(n + 1) if sieve[i]]
		self.computedLen = len(self.computed)

	def get(self, i): # get the i-th prime, zero indexed
		lim = self.computedLen
		while i >= self.computedLen:
			lim *= 2
			self.compute(lim)
		return self.computed[i]

	def gen(self, limit = float('inf')): # return a generator of primes <= limit
		for i in count():
			p = self.get(i)
			if p > limit:
				break
			yield p
	
	def factors(self, n):
		rootn = sqrt(n)
		for p in self.gen():
			if p > rootn:
				break
			exp = 0
			while n % p == 0:
				exp += 1
				n //= p
			if exp > 0:
				rootn = sqrt(n)
				yield p, exp
		if n > 1:
			yield n, 1

def multiply(iterator):
	rv = 1
	for n in iterator:
		if n == 0:
			return 0
		rv *= n
	return rv