from itertools import count
from lib import Primes, multiply

primes = Primes()

def divisorCount(n):
	return multiply(e + 1 for _, e in primes.factors(n))

def triangleNums():
	for i in count(1):
		yield i * (i + 1) // 2

def main(n):
	return next(t for t in triangleNums() if divisorCount(t) > n)

print(main(500))