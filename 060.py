from lib import Primes, numLen

primes = Primes()

def concat(a, b):
	return a * pow(10, numLen(b)) + b

def main(lim):
	prims = []
	tuples = [tuple()]
	for i, pi in enumerate(primes.gen()):
		prims.append(pi)
		commute = [primes.isPrime(concat(pi, pj)) and primes.isPrime(concat(pj, pi)) for pj in prims]
		for t in tuples:
			if all(commute[j] for j in t):
				nt = t + (i,)
				if len(nt) >= lim:
					return sum(prims[j] for j in nt)
				tuples.append(nt)

print(main(5)) # 26033
