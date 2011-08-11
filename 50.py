from math import sqrt

def primes(n):
	nroot = int(sqrt(n))
	sieve = [True] * (n + 1)
	sieve[0] = False
	sieve[1] = False
	for i in range(2, nroot + 1):
		if sieve[i]:
			m = n // i - i
			sieve[i * i:n + 1:i] = [False] * (m + 1)
	return [i for i in range(n + 1) if sieve[i]]

def runningSum(it):
	n = 0
	yield n
	for i in it:
		n += i
		yield n

def main(lim):
	prime = primes(lim)
	sums = list(runningSum(prime))
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
			if total in prime:
				return total
		length -= 1

print(main(1000000))