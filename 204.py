def primesUpTo(last):
	sieve = [True] * (last + 1)
	sieve[0] = False
	sieve[1] = False
	for i in range(2, int(last ** 0.5) + 1):
		if sieve[i]: sieve[i * i:last + 1:i] = [False] * (last // i - i + 1)
	return [i for i, prime in enumerate(sieve) if prime]

def p204(limit, ubound):
	rv = [1]
	for p in primesUpTo(limit):
		rv2 = rv[:]
		m = p
		while m <= ubound:
			for r in rv:
				s = r * m
				if s > ubound: break
				rv2.append(s)
			m *= p
		rv = sorted(rv2)
	return len(rv)

print(p204(100, 10 ** 9))