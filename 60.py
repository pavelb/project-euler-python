from math import sqrt, log10

def primeGenUpTo(n):
	nroot = int(sqrt(n))
	sieve = [True] * (n + 1)
	sieve[0] = False
	sieve[1] = False
	for i in range(2, nroot + 1):
		if sieve[i]:
			m = n // i - i
			sieve[i * i: n + 1:i] = [False] * (m + 1)
	return [i for i in range(n + 1) if sieve[i]]

def primeGen():
	lim = 2
	i = 0
	while True:
		prime = primeGenUpTo(lim)
		l = len(prime)
		while i < l:
			yield prime[i]
			i += 1
		lim *= lim

def prime(n):
	return all(n % i != 0 for i in range(2, int(sqrt(n)) + 1))

def concat(a, b):
	return int(a * pow(10, 1 + int(log10(b))) + b)

def main(lim):
	primes = []
	tuples = [[]]
	for i, pi in enumerate(primeGen()):
		primes.append(pi)
		commute = [prime(concat(pi, pj)) and prime(concat(pj, pi)) for pj in primes]
		for tuple in tuples:
			if all(commute[j] for j in tuple):
				t = tuple + [i]
				if len(t) >= lim:
					return sum(primes[j] for j in t)
				tuples.append(t)

print(main(5))
