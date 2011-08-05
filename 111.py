def primesUpTo(last):
	sieve = [True] * (last + 1)
	sieve[0] = False
	sieve[1] = False
	for i in range(2, int(last ** 0.5) + 1):
		if sieve[i]: sieve[i * i:last + 1:i] = [False] * (last // i - i + 1)
	return [i for i, prime in enumerate(sieve) if prime]

primes = primesUpTo(10 ** 5)

def is_prime(n):
	sq = n ** 0.5
	for p in primes:
		if p >= sq: break
		if n % p == 0: return False
	return True

def dcm(n):
	rv = [0] * 10
	while n > 0:
		rv[n % 10] += 1
		n //= 10
	return rv

def p111(e):
	hist = [[0, 0]] * 10
	for n in range(10 ** (e - 1) + 1, 10 ** e + 1, 2):
		if is_prime(n):
			for digit, count in enumerate(dcm(n)):
				M, S = hist[digit]
				if count == M: hist[digit] = M, S + n
				elif count > M: hist[digit] = count, n
	return sum(s for _, s in hist)

print(p111(10))