from itertools import combinations_with_replacement
from lib import Primes

primes = Primes()

def main(limit = 28123):
	# trick: sum up the numbers <= limit that _are_ a sum of two abundant numbers
	# then subtract that from the sum of all numbers <= limit
	abundant = [n for n in range(2, limit + 1) if n < sum(primes.divisors(n, proper = True))]
	return limit * (limit + 1) // 2 - sum(set(a + b for a, b in combinations_with_replacement(abundant, 2) if a + b <= limit))

print(main()) # 4179871
