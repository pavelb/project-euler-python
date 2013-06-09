from lib import Primes, takeLen
from itertools import count, combinations
from collections import defaultdict

primes = Primes()

def keys(p, stars):
	p = list(str(p))

	mem = defaultdict(list)
	for i, digit in enumerate(p):
		mem[digit].append(i)

	for digit, indices in mem.items():
		for ind in combinations(indices, stars):
			pp = list(p)
			for i in ind:
				pp[i] = '*'
			yield ''.join(pp)

def main(lim):
	for k in count(1):
		for stars in range(1, k):
			mem = defaultdict(list)
			for p in takeLen(k, primes.gen()):
				for key in keys(p, stars):
					mem[key].append(p)
			results = [t for t in mem.values() if len(t) >= lim]
			if len(results) > 0:
				return min(map(sorted, results))[0]

if __name__ == '__main__':
	print(main(8)) # 121313
