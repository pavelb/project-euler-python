from lib import Primes

def main(limit=28123):
	primes = Primes(limit)
	abundant = [n for n in range(limit + 1) if n < primes.sumDivisors(n)]
	abundantSet = set(abundant)

	def can(n):
		for a in abundant:
			if 2 * a > n:
				break
			if n - a in abundantSet:
				return True
		return False

	return sum(n for n in range(limit + 1) if not can(n))

if __name__ == '__main__':
	print(main()) # 4179871
