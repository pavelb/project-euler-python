from lib import Primes

primes = Primes()

def main(lim):
	d = [primes.sumDivisors(n) for n in range(lim)]
	amicable = lambda n: d[n] < lim and n == d[d[n]] and n != d[n]
	return sum(filter(amicable, range(lim)))

print(main(10000)) # 31626