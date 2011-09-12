from lib import Primes

primes = Primes()

def main(lim):
<<<<<<< HEAD
	d = [primes.sumDivisors(n) for n in range(lim)]
	amicable = lambda n: d[n] < lim and n == d[d[n]] and n != d[n]
	return sum(filter(amicable, range(lim)))

print(main(10000)) # 31626
=======
	d = [sum(primes.divisors(i, proper = True)) for i in range(lim)]
	return sum(i for i in range(lim) if d[i] < lim and i == d[d[i]] and i != d[i])

print(main(10000)) # 31626
>>>>>>> upstream/master
