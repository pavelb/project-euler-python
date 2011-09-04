from lib import Primes, num, multiply
from itertools import permutations, combinations

primes = Primes()

def part(arr, k, start=0): # like combinations(arr, k) but also returns the leftovers
	if k == 0:
		yield tuple(), arr
	else:
		for i in range(start, len(arr)):
			n = arr[i]
			for left, right in part(arr[:i] + arr[i + 1:], k - 1, i):
				yield (n,) + left, right

def subsetCombinations(arr, filter=None): # returns all sets of subsets of arr where each subset passes filter()
	if not arr:
		yield []
	else:
		arr = arr[:]
		X = arr.pop(0)
		for k in range(len(arr) + 1):
			for left, right in part(arr, k):
				s = (X,) + left
				if not filter or filter(s):
					L = [s]
					for R in subsetCombinations(right):
						yield L + R

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
			m = countPrimes((X,) + left)
			if m != 0:
				rv += m * countPrimeSets(right)
	return rv

def countPrimeSets2(digits):
	rv = 0
	for groups in subsetCombinations(digits, filter=countPrimes):
		rv += multiply(map(countPrimes, groups))
	return rv

def main(k):
	# generate all pandigital sets uniquely and count the ones containing only primes
	return countPrimeSets(k)

from time import clock
a = clock()
print(main([1, 2, 3, 4, 5, 6, 7, 8, 9])) # 44680
print(clock() - a)

from itertools import chain, combinations

def partition(s):
	n = len(s)
	b, mid, e = [0], list(range(1, n)), [n]
	splits = (d for i in range(n) for d in combinations(mid, i))
	return [[s[sl] for sl in map(slice, chain(b, d), chain(d, e))] for d in splits]

#for p in partition([1, 2, 3, 4]): print(p)
