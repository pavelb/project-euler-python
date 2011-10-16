#not finished

def primesUpTo(last):
	sieve = [True] * (last + 1)
	sieve[0] = False
	sieve[1] = False
	for i in range(2, int(last ** 0.5) + 1):
		if sieve[i]: sieve[i * i:last + 1:i] = [False] * (last // i - i + 1)
	return [i for i, prime in enumerate(sieve) if prime]

primes = primesUpTo(10 ** 6)

def factor(n):
	sq = n ** 0.5
	i = 0
	p = primes[0]
	while p <= sq:
		if n % p == 0:
			count = 0
			while n % p == 0:
				count += 1
				n /= p
			sq = n ** 0.5
			yield [p, count]
		i += 1
		p = primes[i]
	if n > 1: yield [n, 1] # n is a prime

def divisors(n):
	rv = [1]
	for f, e in factor(n):
		rv.extend([r * f ** i for i in range(1, e + 1) for r in rv])
	return rv

def isInt(n): return n == int(n)

def at(s):
	rootn = s ** 0.5
	for p in sorted(divisors(s)):
		if p >= rootn: break
		y = float(s / p - p) / 2
		if isInt(y):
			x = y + p
			yield x, y

def p135():
	n = 27
	for s in range(3, n * n):
		for x, y in at(s):
			zs = x * x - y * y - n
			if zs <= 0: continue
			z = zs ** 0.5
			if not isInt(z): continue
			print(x, y, z);

p135()
