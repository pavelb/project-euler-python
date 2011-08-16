from lib import Primes

primes = Primes()

def main(lim):
	# trick: to minimize phi(n) and maximize n need n to not have duplicate factors
	prod = 1
	for p in primes.gen():
		prod *= p
		if prod * p > lim:
			return prod

print(main(1000000)) # 510510
