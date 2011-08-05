def primesUpTo(last):
	sieve = [True] * (last + 1)
	sieve[0] = False
	sieve[1] = False
	for i in range(2, int(last ** 0.5) + 1):
		if sieve[i]: sieve[i * i:last + 1:i] = [False] * (last // i - i + 1)
	return [i for i, prime in enumerate(sieve) if prime]

primes = primesUpTo(100000)

def factor(n):
	rv = []
	i = 0
	while n > 1:
		p = primes[i]
		if n % p == 0:
			count = 0
			while n % p == 0:
				count += 1
				n /= p
			rv.append([p, count])
		i += 1
	return rv

def countSolutions(factors):
	return (prod(2 * e + 1 for _, e in factors) + 1) / 2

def prod(iterable):
	p = 1
	for n in iterable: p *= n
	return p

def stitch(factors, ifactors):
	rv = factors[:]
	for fb, fe in ifactors:
		added = False
		for i, [b, e] in enumerate(rv):
			if b == fb:
				rv[i] = [b, e + fe]
				added = True
				break
		if not added:
			rv.append([fb, fe])
	return rv

def getNumber(factors):
	return prod(b ** e for b, e in factors)

def p110():
	primes = primesUpTo(37)
	size = len(primes)
	exp = [1] * size
	factors = list(zip(primes, exp))
	base = getNumber(factors)
	i = 1
	while True:
		ifactors = factor(i)
		tfactors = stitch(factors, ifactors)
		t = countSolutions(tfactors)
		if t > 4000000: return base * i
		i += 1

print(p110())
