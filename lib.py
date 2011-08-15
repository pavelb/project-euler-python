from itertools import count, combinations, product
from math import sqrt, floor, log10

class Primes:
	computed = None
	computedLen = 0
	refLen = 0

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
		self.refLen = n

	def get(self, i): # get the i-th prime, zero indexed
		while i >= self.computedLen:
			self.compute(2 * self.refLen)
		return self.computed[i]

	def gen(self):
		return map(self.get, count())

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

	def divisors(self, n, proper = False):
		if n > 0:
			parts = list([pow(b, i) for i in range(1, e + 1)] for b, e in self.factors(n))
			for k in range(len(parts) + 1):
				for tuples in combinations(parts, k):
					for tuple in product(*tuples):
						d = multiply(tuple)
						if proper and d == n:
							return
						yield d

	def isPrime(self, n):
		return n > 1 and all(b == 1 or b == n for b, _ in self.factors(n))

def multiply(iterator):
	rv = 1
	for n in iterator:
		if n == 0:
			return 0
		rv *= n
	return rv

def digits(n):
	rv = []
	while True:
		rv.append(n % 10)
		n //= 10
		if n == 0:
			return reversed(rv)

def num(digits):
	n = 0
	for d in digits:
		n = 10 * n + d
	return n

def numLen(n): # number if digits in n, equivalent to len(digits(n))
	return 1 + floor(log10(n)) if n > 0 else 1

def fibonacci():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a + b

def pythagoreanTriples(a = 3, b = 4, c = 5):
	# return a generator for the triplets in order of increasing perimiter
	# en.wikipedia.org/wiki/Pythagorean_triple#Parent.2Fchild_relationships
	yield a, b, c
	gens = [
		((k * a, k * b, k * c) for k in count(2)),
		pythagoreanTriples(a - 2 * b + 2 * c, 2 * a - b + 2 * c, 2 * a - 2 * b + 3 * c),
		pythagoreanTriples(a + 2 * b + 2 * c, 2 * a + b + 2 * c, 2 * a + 2 * b + 3 * c),
		pythagoreanTriples(-a + 2 * b + 2 * c, -2 * a + b + 2 * c, -2 * a + 2 * b + 3 * c)
	]
	opts = [(sum(v), v, i) for i, v in enumerate(map(next, gens))]
	while True:
		_, tuple, i = min(opts)
		yield tuple
		tuple = next(gens[i])
		opts[i] = (sum(tuple), tuple, i)

def pandigital(n, k = 9):
	saw = [False] * k
	for d in digits(n):
		if d == 0 or d > k or saw[d - 1]:
			return False
		saw[d - 1] = True
	return all(saw)

def charInd(char):
	return ord(char) - 64

def square(n):
	rootn = sqrt(n)
	return rootn == int(rootn)
