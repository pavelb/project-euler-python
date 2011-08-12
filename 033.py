from lib import Primes

primes = Primes()

def main():
	# this is a terrible question
	def seq():
		for d in range(11, 100):
			da, db = d // 10, d % 10
			if db > 0 and da != db:
				for n in range(10, d):
					na, nb = n // 10, n % 10
					if nb > 0 and na != nb and (da == na and n * db == nb * d or da == nb and n * db == na * d or db == na and n * da == nb * d or db == nb and n * da == na * d):
						yield n, d
	n = 1
	d = 1
	for a, b in seq():
		n *= a
		d *= b
	for b, e in primes.factors(n):
		for _ in range(e):
			if d % b == 0:
				d //= b
			else:
				break
	return d

print(main())