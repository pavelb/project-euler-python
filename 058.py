from lib import Primes
from itertools import count

primes = Primes()

def main(lim):
	diagonals = (
		lambda r: pow(2 * r - 1, 2) - 6 * (r - 1),
		lambda r: pow(2 * r - 1, 2) - 4 * (r - 1),
		lambda r: pow(2 * r - 1, 2) - 2 * (r - 1)
		#lambda r: pow(2 * r - 1, 2) # can't be prime
	)
	numPrimes = 0
	total = 1
	for r in count(2):
		numPrimes += sum(map(primes.isPrime, (d(r) for d in diagonals)))
		total += 4
		if numPrimes < lim * total:
			return 2 * r - 1

if __name__ == '__main__':
	print(main(0.1)) # 26241
