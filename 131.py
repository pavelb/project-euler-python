import itertools

def primesUpTo(last):
	sieve = [True] * (last + 1)
	sieve[0] = False
	sieve[1] = False
	for i in range(2, int(last ** 0.5) + 1):
		if sieve[i]: sieve[i * i:last + 1:i] = [False] * (last // i - i + 1)
	return [i for i, prime in enumerate(sieve) if prime]

def isPrime(n):
	max = int(n ** 0.5)
	for p in primes:
		if p > max: break
		if n % p == 0: return False
	return True

def p131(limit):
	global primes
	primes = primesUpTo(int(limit ** 0.5))
	count = 0
	for i in itertools.count(1):
		p = (i + 1) ** 3 - i ** 3
		if p >= limit: break
		if isPrime(p): count += 1
	return count

print(p131(10 ** 6))
