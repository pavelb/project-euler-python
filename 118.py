from lib import Primes, num
from itertools import permutations

primes = Primes()

def part(arr, k, start=0): # like combinations(arr, k) but also returns the leftovers
	if k == 0:
		yield [], arr
	else:
		for i in range(start, len(arr)):
			n = arr[i]
			for left, right in part(arr[:i] + arr[i + 1:], k - 1, i):
				yield [n] + left, right

def countPrimes(digits):
	perms = map(num, permutations(digits))
	return sum(map(primes.isPrime, perms))

def countPrimeSets(digits):
	# trick: to get a unique set ensure subsets are sorted left to right by smallest element
	if not digits:
		return 1

	rv = 0
	digits = digits[:]
	X = digits.pop(0) # smallest digit
	for k in range(len(digits) + 1):
		for left, right in part(digits, k):
			m = countPrimes([X] + left)
			if m != 0:
				rv += m * countPrimeSets(right)
	return rv

def main(k):
	# generate all pandigital sets uniquely and count the ones containing only primes
	return countPrimeSets(k)

print(main([1, 2, 3, 4, 5, 6, 7, 8, 9])) # 44680
