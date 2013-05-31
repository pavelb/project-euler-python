from lib import Primes, digits, takeLen, same
from itertools import count, combinations

primes = Primes()

def sameDigit(n, pos):
	d = digits(n)
	return same(d[p] for p in pos)

def main(lim):
	for k in count(1):
		cache = dict()
		for p in takeLen(k, primes.gen()):
			for stars in range(1, k):
				for starPos in combinations(range(k), stars):
					if sameDigit(p, starPos):
						key = str(p)
						for s in starPos:
							key = key[:s] + '*' + key[s + 1:]
						cache.setdefault(key, []).append(p)
		results = [t for t in cache.values() if len(t) >= lim]
		if len(results) > 0:
			return min(map(sorted, results))[0]

if __name__ == '__main__':
	print(main(8)) # 121313
