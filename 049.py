from lib import Primes, digitCountMap
from itertools import combinations

primes = Primes()

def group(nums):
	record = dict()
	for n in nums:
		key = tuple(digitCountMap(n))
		if key not in record:
			record[key] = []
		record[key].append(n)
	return record.values()

def sequence(triple):
	return triple[2] - triple[1] == triple[1] - triple[0]

def main(digits):
	primeSrc = filter(primes.isPrime, range(pow(10, digits - 1), pow(10, digits)))
	return [trip for g in group(primeSrc) for trip in combinations(g, 3) if sequence(trip)]

print(main(4)) # 296962999629
