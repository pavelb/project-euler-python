from lib import Primes, takeLen, digitCountMap
from itertools import combinations

primes = Primes()

def group(nums):
	record = dict()
	for n in nums:
		record.setdefault(digitCountMap(n), []).append(n)
	return record.values()

def sequence(a, b, c):
	return c - b == b - a

def main(k):
	groups = group(takeLen(k, primes.gen()))
	trips = (trip for g in groups for trip in combinations(g, 3))
	return [''.join(map(str, t)) for t in trips if sequence(*t)]

if __name__ == '__main__':
	print(main(4)) # 296962999629
