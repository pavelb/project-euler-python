from itertools import combinations_with_replacement, takewhile
from lib import Primes

primes = Primes()

def main(limit=28123):
	abundant = [n for n in range(limit + 1) if n < primes.sumDivisors(n)]
	ab = set(abundant)

	def can(n):
		for a in abundant:
			if a > n / 2:
				break
			if n - a in ab:
				return True
		return False

	return sum(n for n in range(limit + 1) if not can(n))

if __name__ == '__main__':
	print(main()) # 4179871
