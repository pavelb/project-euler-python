from itertools import count, product
from math import factorial
from lib import num

def main():
	rv = 0
	limit = next(n for n in count() if pow(10, n) - 1 > factorial(9) * n) - 1
	for r in range(2, limit):
		for d in product(range(10), repeat=r):
			if d[0] == 0:
				continue
			n = num(d)
			if n == sum(map(factorial, d)):
				rv += n
	return rv

if __name__ == '__main__':
	print(main()) # 40730
