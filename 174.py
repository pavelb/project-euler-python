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

def count(t):
	if t % 4: return 0
	rt = t / 4
	roott = t ** 0.5
	rootrt = rt ** 0.5
	rv = 0
	for k in sorted(divisors(rt)):
		if k >= rootrt: break
		S = rt / k + k
		if S > roott: rv += 1
	return rv

def p174(): return sum(1 <= count(t) <= 10 for t in xrange(8, 10 ** 6 + 1, 4))

print(p174())
