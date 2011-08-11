from itertools import count

def sumDigits(n, exp):
	rv = 0
	while n > 0:
		rv += pow(n % 10, exp)
		n //= 10
	return rv

def main(exp):
	limit = next(n for n in count(1) if pow(10, n) > pow(9, exp) * n)
	return sum(n for n in range(2, pow(10, limit)) if n == sumDigits(n, exp))

print(main(5))