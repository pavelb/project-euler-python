from lib import Primes, num
from itertools import combinations, product

primes = Primes()

def fillMask(mask, skip, vars):
	digi = (n for n in range(10) if n != skip)
	for k in product(digi, repeat=vars):
		for indices in combinations(range(len(mask)), vars):
			m = mask[:]
			for i, d in enumerate(k):
				m[indices[i]] = d
			if m[0] != 0:
				yield num(m)

def S(size, d):
	mask = [d] * size
	for k in range(1, size):
		nums = fillMask(mask, d, k)
		nums = filter(primes.isPrime, nums)
		rv = sum(nums)
		if rv > 0:
			return rv

def main(k):
	return sum(S(k, d) for d in range(10))

if __name__ == '__main__':
	print(main(10)) # 612407567715
