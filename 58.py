from itertools import count
from math import sqrt

def prime(n):
	return all(n % i != 0 for i in range(2, int(sqrt(n)) + 1))

def A(r):
	return pow(2 * r - 1, 2) - 6 * (r - 1)

def B(r):
	return pow(2 * r - 1, 2) - 4 * (r - 1)

def C(r):
	return pow(2 * r - 1, 2) - 2 * (r - 1)

#def D(r):
#	return pow(2 * r - 1, 2)

def main(lim):
	primes = 0
	nums = 1
	for r in count(2):
		primes += prime(A(r)) + prime(B(r)) + prime(C(r))
		nums += 4
		if primes < lim * nums:
			return 2 * r - 1

print(main(0.1))