from lib import Primes, runningSum
from itertools import takewhile

primes = Primes()

def main(lim):
	# trick: compute the running sum first so we can compute the sum of primes i to j in constant time

	sums = list(runningSum(takewhile(lambda p: p <= lim, primes.gen())))
	size = len(sums)

	# find max length
	length = 0
	while sums[length + 1] < lim:
		length += 1

	# return the first prime sum
	while length > 0:
		for start in range(size - length):
			total = sums[start + length] - sums[start]
			if total >= lim: # sums are in increasing order
				break
			if primes.isPrime(total):
				return total
		length -= 1

if __name__ == '__main__':
	print(main(1000000)) # 997651
