from lib import Primes

primes = Primes()

def main(lim):
	# trick: minimize phi(n)
	prod = 1
	for p in primes.gen():
		prod *= p
		if prod * p > lim:
			return prod

if __name__ == '__main__':
	print(main(1000000)) # 510510
