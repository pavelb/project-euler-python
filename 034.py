from itertools import count
from math import factorial
from lib import digits

def main():
	fac9 = factorial(9)
	limit = next(n for n in count() if pow(10, n) - 1 > fac9 * n) - 1
	return sum(n for n in range(10, pow(10, limit)) if n == sum(map(factorial, digits(n))))

print(main())