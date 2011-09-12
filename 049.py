<<<<<<< HEAD
from lib import Primes, takeLen, digitCountMap
=======
from lib import Primes, digitCountMap
>>>>>>> upstream/master
from itertools import combinations

primes = Primes()

def group(nums):
	record = dict()
	for n in nums:
<<<<<<< HEAD
		record.setdefault(digitCountMap(n), []).append(n)
=======
		key = tuple(digitCountMap(n))
		if key not in record:
			record[key] = []
		record[key].append(n)
>>>>>>> upstream/master
	return record.values()

def sequence(a, b, c):
	return c - b == b - a

<<<<<<< HEAD
def main(k):
	groups = group(takeLen(k, primes.gen()))
	trips = (trip for g in groups for trip in combinations(g, 3))
	return [''.join(map(str, t)) for t in trips if sequence(*t)]
=======
def main(digits):
	primeSrc = filter(primes.isPrime, range(pow(10, digits - 1), pow(10, digits)))
	return [trip for g in group(primeSrc) for trip in combinations(g, 3) if sequence(trip)]
>>>>>>> upstream/master

print(main(4)) # 296962999629
