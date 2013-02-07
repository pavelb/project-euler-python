from lib import Primes

def main(N, solns):
	primes = Primes(N)
	rv = 0

	for n in range(N):
		count = 0
		for A in primes.divisors(n):
			if A * A < 3 * n and (A + n // A) % 4 == 0:
				count += 1
				if count > solns:
					break

		if count == solns:
			rv += 1

	return rv

print(main(50000000, 1)) # 2544559
