from lib import Primes

primes = Primes()

def main(lim):
	d = [sum(primes.divisors(i, proper = True)) for i in range(lim)]
	return sum(i for i in range(lim) if d[i] < lim and i == d[d[i]] and i != d[i])

print(main(10000)) # 31626
