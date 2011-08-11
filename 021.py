from lib import Primes

primes = Primes()

def main(lim):
	divisorSum = [sum(primes.divisors(i, proper = True)) for i in range(lim)]
	amicable = []
	for i in range(lim):
		j = divisorSum[i]
		if j < lim and i == divisorSum[j] and i != j:
			amicable.append(i)
	return sum(amicable)

print(main(10000))