from itertools import count
from math import sqrt

def prime(n):
	return all(n % i != 0 for i in range(2, int(sqrt(n)) + 1))

def goldbach(n):
	for s in count(1):
		n2 = n - 2 * s * s
		if n2 < 2:
			return False
		if prime(n2):
			return True

def main():
	n = 1
	while prime(n) or goldbach(n):
		n += 2
	return n

print(main())