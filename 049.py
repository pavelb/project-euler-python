from math import sqrt

def prime(n):
	return all(n % i != 0 for i in range(2, int(sqrt(n)) + 1))

def choose(items, n):
	if n == 0:
		yield []
	else:
		for i in range(len(items) - (n - 1)):
			for item in choose(items[i + 1:], n - 1):
				yield [items[i]] + item

def group(nums):
	record = dict()
	for n in nums:
		key = ''.join(sorted(list(str(n))))
		if key not in record:
			record[key] = []
		record[key].append(n)
	return record.values()

def sequence(triple):
	return triple[2] - triple[1] == triple[1] - triple[0]

def main(digits):
	primes = filter(prime, range(pow(10, digits - 1), pow(10, digits)))
	return [trip for g in group(primes) for trip in choose(g, 3) if sequence(trip)]

print(main(4))