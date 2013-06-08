from lib import num

def gen(nums, primes, pos=0, prefix=0):
	if pos >= 4 and prefix % 10 ** 3 % primes[pos - 4] != 0:
		return

	if not nums:
		yield prefix
		return

	for n in nums:
		nums.remove(n)
		for g in gen(nums, primes, pos + 1, 10 * prefix + n):
			yield g
		nums.add(n)


def main():
	# trick: generate all permutations of 0..9 by extending valid prefixes
	primes = (2, 3, 5, 7, 11, 13, 17)
	return sum(gen(set(range(10)), primes))

if __name__ == '__main__':
	print(main()) # 16695334890
