def primes(n):
	# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
	nroot = int(n ** 0.5)
	sieve = [True] * (n + 1)
	sieve[0] = False
	sieve[1] = False
	for i in range(2, nroot + 1):
		if sieve[i]:
			m = n // i - i
			sieve[i * i:n + 1:i] = [False] * (m + 1)
	return [i for i in range(n + 1) if sieve[i]]

def main(n):
	return sum(primes(n))

print(main(2000000))