from math import log10, floor

def primesUpTo(last):
	sieve = [True] * (last + 1)
	sieve[0] = False
	sieve[1] = False
	for i in range(2, int(last ** 0.5) + 1):
		if sieve[i]: sieve[i * i:last + 1:i] = [False] * (last // i - i + 1)
	return [i for i, prime in enumerate(sieve) if prime]

def digitCount(n): return 1 + floor(log10(n))

def S(p1, a):
	b = int(10 ** digitCount(p1))
	x, _ = extended_gcd(a, b)
	x *= p1
	# y *= p1
	t = x // b
	x -= t * b
	# y += t * a
	return a * x

def extended_gcd(a, b):
	x = 0
	lastx = 1
	y = 1
	lasty = 0
	while b != 0:
		quotient = a // b
		a, b = b, a % b
		lastx, x = x, lastx - quotient * x
		lasty, y = y, lasty - quotient * y
	return lastx, lasty

def p134():
	primes = primesUpTo(10 ** 6 + 3)
	return sum(S(p1, p2) for p1, p2 in zip(primes[2:], primes[3:]))

print(p134())

