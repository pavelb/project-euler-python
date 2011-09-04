# not done

from lib import Primes
from itertools import count

primes = Primes()

def main(primeCount, powpow):
	# R(n+1) = 10 ** n + R(n), R(0) = 0

	mem = []
	for p in primes.gen():
		T = 1
		Rn = 0
		for n in range(10 ** powpow):
			T = (10 * T) % p
			Rn = (T + Rn) % p
		print(Rn)
		break

print(main(40, 9))
