from math import sqrt

def primesUpTo(last):
	sieve = [True] * (last + 1)
	sieve[0] = False
	sieve[1] = False
	for i in range(2, int(sqrt(last)) + 1):
		if sieve[i]:
			sieve[i * i:last + 1:i] = [False] * (last // i - i + 1)
	return [i for i, prime in enumerate(sieve) if prime]

def factors(n, primes):
	rootn = sqrt(n)
	for p in primes:
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

def product(iterator):
	rv = 1
	for n in iterator:
		rv *= n
	return rv

def phi(n, primes):
	return product(pow(b, e - 1) * (b - 1) for b, e in factors(n, primes))

def main(lim):
	primes = primesUpTo(lim)
	return max((n / phi(n, primes), n) for n in range(1, lim))[1]

print(main(1000000))
