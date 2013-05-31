from lib import Primes, reduceFrac

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
	n, d = 1, 1
	for a, b in seq():
		n, d = a * n, b * d
	n, d = reduceFrac(n, d)
	return d

if __name__ == '__main__':
	print(main()) # 100
