def primesUpTo(last):
	sieve = [True] * (last + 1)
	sieve[0] = False
	sieve[1] = False
	for i in range(2, int(last ** 0.5) + 1):
		if sieve[i]: sieve[i * i:last + 1:i] = [False] * (last // i - i + 1)
	return [i for i, prime in enumerate(sieve) if prime]

primes = primesUpTo(10 ** 4)

def factor(n):
	sq = n ** 0.5
	rv = []
	i = 0
	p = primes[0]
	while p <= sq:
		if n % p == 0:
			count = 0
			while n % p == 0:
				count += 1
				n /= p
			sq = n ** 0.5
			rv.append([p, count])
		i += 1
		p = primes[i]
	if n > 1: rv.append([n, 1]) # n is a prime
	return rv

def numDivisors(factors):
	return prod(e + 1 for _, e in factors)

def prod(iterable):
	p = 1
	for n in iterable: p *= n
	return p

def p179():
	rv = 0
	ldc = 0
	for n in xrange(2, int(10 ** 7) + 1):
		dc = numDivisors(factor(n))
		if dc == ldc: rv += 1
		ldc = dc
	return rv

print(p179())
