from lib import numLen
from itertools import islice

def convergents2():
	a, b = 1, 1
	while True:
		yield a, b
		a, b = a + 2 * b, a + b

def main(lim):
	return sum(numLen(n) > numLen(d) for n, d in islice(convergents2(), lim))

print(main(1000)) # 153