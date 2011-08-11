from math import sqrt

def primesUpTo(last):
	sieve = [True] * (last + 1)
	sieve[0] = False
	sieve[1] = False
	for i in range(2, int(sqrt(last)) + 1):
		if sieve[i]:
			sieve[i * i:last + 1:i] = [False] * (last // i - i + 1)
	return [i for i, prime in enumerate(sieve) if prime]

def digitCountMap(n):
	dcm = [0] * 10
	while n > 0:
		dcm[n % 10] += 1
		n //= 10
	return dcm

def p70(limit):
	# trick: to maximuze phi(n) need n to be a product of two primes, as it cant be prime itself
	primes = primesUpTo(limit)
	minn, minr = 0, limit
	for i, p1 in enumerate(primes):
		for j in range(i, len(primes)):
			p2 = primes[j]
			n = p1 * p2
			if n > limit:
				break
			t = (p1 - 1) * (p2 - 1)
			if float(n) < t * minr and digitCountMap(n) == digitCountMap(t):
				minn, minr = n, float(n) / t
	return minn

print(p70(pow(10, 7)))