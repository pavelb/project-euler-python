from lib import Primes, num
from itertools import permutations

primes = Primes()

def main():
	# trick: all 9-digit pandigital numbers are divisible by 9
	# trick: all 8-digit pandigital numbers are divisible by 9
	# return the max prime 7 digit pandigital number
	pandigitals = map(num, permutations((7, 6, 5, 4, 3, 2, 1)))
	return next(filter(primes.isPrime, pandigitals))

if __name__ == '__main__':
	print(main()) # 7652413
