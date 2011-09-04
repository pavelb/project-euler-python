def primesUpTo(last):
	sieve = [True] * (last + 1)
	sieve[0] = False
	sieve[1] = False
	for i in range(2, int(last ** 0.5) + 1):
		if sieve[i]: sieve[i * i:last + 1:i] = [False] * (last // i - i + 1)
	return [i for i, prime in enumerate(sieve) if prime]

primes = primesUpTo(10 ** 8)

def p187(limit):
	count = 0
	i = 0
	p1 = primes[0]
	p1limit = limit / p1
	while p1 <= p1limit:
		j = i
		p2 = primes[i]
		p2limit = limit / p1
		while p2 <= p2limit:
			count += 1
			j += 1
			p2 = primes[j]
		i += 1
		p1 = primes[i]
	return count

print(p187(10 ** 8))
