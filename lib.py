from itertools import count, islice, takewhile, dropwhile
from math import sqrt, floor, log10, factorial
from heapq import heappush, heappop

class Primes:
	computed = None
	computedLen = 0
	refLen = 0

	def __init__(self):
		self.compute(2 ** 16)

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

	def gen(self, initLen=None):
		if initLen != None and initLen > self.computedLen:
			self.compute(initLen)
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

	#def divisors(self, n, proper=False):
	#	if n > 0:
	#		parts = list([pow(b, i) for i in range(1, e + 1)] for b, e in self.factors(n))
	#		for k in range(len(parts) + 1):
	#			for tuples in combinations(parts, k):
	#				for tuple in product(*tuples):
	#					d = multiply(tuple)
	#					if proper and d == n:
	#						return
	#						yield d

	def sumDivisors(self, n, proper=True):
		# http://en.wikipedia.org/wiki/Divisor_function
		if n < 1: return 0
		rv = multiply((pow(pi, ai + 1) - 1) // (pi - 1) for pi, ai in self.factors(n))
		return rv - n if proper else rv

	def isPrime(self, n):
		return n > 1 and all(b == 1 or b == n for b, _ in self.factors(n))

	def phi(self, n):
		return multiply(pow(b, e - 1) * (b - 1) for b, e in self.factors(n))

def takeLen(k, iter):
	lbound = pow(10, k - 1)
	ubound = 10 * lbound - 1
	rv = iter
	rv = dropwhile(lambda p: p < lbound, rv)
	rv = takewhile(lambda p: p < ubound, rv)
	return rv

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
			return list(reversed(rv))

def digitCountMap(n):
	rv = [0] * 10
	for d in digits(n):
		rv[d] += 1
	return tuple(rv)

def num(digits):
	n = 0
	for d in digits:
		n = 10 * n + d
	return n

def numLen(n): # number if digits in n, equivalent to len(digits(n))
	return 1 + floor(log10(n)) if n > 0 else 1

def fibonaccis():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a + b

#def pythagoreanTriplesGens(a=3, b=4, c=5):
#	# generate all triplets in order of increasing perimeter
#	# en.wikipedia.org/wiki/Pythagorean_triple#Parent.2Fchild_relationships
#	yield a, b, c
#	gens = [
#		((k * a, k * b, k * c) for k in count(2)),
#		pythagoreanTriples(a - 2 * b + 2 * c, 2 * a - b + 2 * c, 2 * a - 2 * b + 3 * c),
#		pythagoreanTriples(a + 2 * b + 2 * c, 2 * a + b + 2 * c, 2 * a + 2 * b + 3 * c),
#		pythagoreanTriples(-a + 2 * b + 2 * c, -2 * a + b + 2 * c, -2 * a + 2 * b + 3 * c)
#	]
#	opts = [(sum(v), v, i) for i, v in enumerate(map(next, gens))]
#	while True:
#		_, tuple, i = min(opts)
#		yield tuple
#		tuple = next(gens[i])
#		opts[i] = (sum(tuple), tuple, i)

def pythagoreanTriples():
	# generate all triplets, sorted and in order of increasing perimeter
	# en.wikipedia.org/wiki/Pythagorean_triple#Parent.2Fchild_relationships
	T = (
		lambda a, b, c: (+a - 2 * b + 2 * c, +2 * a - b + 2 * c, +2 * a - 2 * b + 3 * c),
		lambda a, b, c: (+a + 2 * b + 2 * c, +2 * a + b + 2 * c, +2 * a + 2 * b + 3 * c),
		lambda a, b, c: (-a + 2 * b + 2 * c, -2 * a + b + 2 * c, -2 * a + 2 * b + 3 * c)
	)
	mem = []
	push = lambda a, b, c, m = 1: heappush(mem, ((a + b + c) * m, (a, b, c), m))
	push(3, 4, 5)
	while True:
		_, (a, b, c), m = heappop(mem)
		yield a * m, b * m, c * m
		push(a, b, c, m + 1)
		if m == 1: # only expand primitives
			for t in T:
				push(*sorted(t(a, b, c)))

def pandigital(n, k=9):
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

def ngonalNums(n):
	n -= 2
	rv = 0
	for k in count():
		rv += n * k + 1
		yield rv

def triangular(n):
	return square(8 * n + 1)

def pentagonal(n):
	ds = 1 + 24 * n
	return square(ds) and (1 + sqrt(ds)) % 6 == 0

def hexagonal(n):
	ds = 1 + 8 * n
	return square(ds) and (1 + sqrt(ds)) % 4 == 0

def same(iterator):
	arr = list(iterator)
	return len(arr) < 2 or all(n == arr[0] for n in arr)

def choose(n, k):
	return factorial(n) // (factorial(n - k) * factorial(k))

def palindrome(n):
	d = digits(n)
	return all(d[i] == d[-1 - i] for i in range(len(d) // 2 + 1))

def CFRparts(n):
	if not square(n):
		m, d, a, S = 0, 1, int(sqrt(n)), n
		while True:
			yield m, d, a, S
			mn = d * a - m
			dn = (S - mn * mn) / d
			an = int((sqrt(S) + mn) / dn)
			m, d, a, S = mn, dn, an, S

def CFR(n): # continued fraction representation
	for _, _, a, _ in CFRparts(n):
		yield a

def reduce(a, d):
	c, b = d
	return a * c + b, c

def convergents(n):
	def sumProperDivisors(gen):
		an = next(gen)
		yield an, 1
		for c in sumProperDivisors(gen):
			yield reduce(an, c)
	return sumProperDivisors(CFR(n))

def extendedGCD(a, b):
	lastx, x = 1, 0
	lasty, y = 0, 1
	while b != 0:
		q = a // b
		a, b = b, a % b
		lastx, x = x, lastx - q * x
		lasty, y = y, lasty - q * y
	return lastx, lasty

def gcd(x, y):
	while y != 0:
		x, y = y, x % y
	return x

def reduceFrac(n, d):
	fac = gcd(n, d)
	return n // fac, d // fac

def prevFarey(f, n):
	# http://en.wikipedia.org/wiki/Farey_sequence
	a, b = f
	x, y = extendedGCD(a, b)
	k = (n - x) // b
	return -(y - k * a), x + k * b

def partitionFnGen():
	# http://mathworld.wolfram.com/PartitionFunctionP.html
	# Euler recurrence equation solved with dynamic programming

	mem = [1]
	get = lambda n: mem[n] if n >= 0 else 0

	for n in count(1):
		pn = 0
		for k in range(1, int(sqrt(n)) + 1):
			sgn = 2 * (k % 2) - 1
			t1 = get(n - k * (3 * k - 1) // 2)
			t2 = get(n - k * (3 * k + 1) // 2)
			pn += sgn * (t1 + t2)
		yield pn
		mem.append(pn)

def partitionFn(n):
	return next(islice(partitionFnGen(), n - 1, None))

def runningSum(it):
	n = 0
	yield n
	for i in it:
		n += i
		yield n

def Dijkstra(vertices, neighbours, distance, start):
	dist = dict()
	prev = dict()
	Q = []
	for v in vertices:
		Q.append(v)
		dist[v] = float('inf')
		prev[v] = None
	dist[start] = distance(start, start)
	while len(Q) > 0:
		u = min(Q, key=lambda c: dist[c])
		if dist[u] == float('inf'): break
		Q.remove(u)
		for v in neighbours(u):
			alt = dist[u] + distance(u, v)
			if alt < dist[v]:
				dist[v] = alt
				prev[v] = u
	return dist
