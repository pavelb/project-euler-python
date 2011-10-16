# not finished

from math import floor, log, factorial

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

def addFactors(factors, ifactors):
	rv = factors[:]
	for fb, fe in ifactors:
		found = False
		for i, [b, e] in enumerate(rv):
			if b == fb:
				rv[i] = [b, e + fe]
				found = True
				break
		if not found:
			rv.append([fb, fe])
	return rv

def subtractFactors(factors, ifactors):
	rv = factors[:]
	for fb, fe in ifactors:
		found = False
		for i, [b, e] in enumerate(rv):
			if b == fb:
				if e == fe:
					del rv[i]
				else:
					rv[i] = [b, e - fe]
				found = True
				break
		if not found:
			rv.append([fb, -fe])
	return rv

def factorOfFactorial(n):
	rv = []
	for i in range(2, n + 1):
		rv = addFactors(rv, factor(i))
	return rv

def factorsOfChoose(n, k):
	return subtractFactors(subtractFactors(factorOfFactorial(n), factorOfFactorial(n - k)), factorOfFactorial(k))

def countFactors(n, k):
	if n >= 98: return 16
	return n // k + floor(log(n / k, k)) if n >= k else 0

def countFactors2(n, k):
	for f, c in factorOfFactorial(n):
		if f == k: return c
	return 0

count = 0
for n in range(0, 100):
	for k in range(0, n + 1):
		if countFactors(n, 7) != countFactors2(n, 7): print(n, countFactors(n, 7), countFactors2(n, 7))
		if countFactors(n - k, 7) != countFactors2(n - k, 7): print(n - k, countFactors(n - k, 7), countFactors2(n - k, 7))
		if countFactors(k, 7) != countFactors2(k, 7): print(k, countFactors(n, 7), countFactors2(k, 7))
		if countFactors(n, 7) - countFactors(n - k, 7) - countFactors(k, 7) == 0:
			# print(n, k)
			count += 1
print(count)
