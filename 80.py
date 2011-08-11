from decimal import Decimal, getcontext
from math import sqrt

getcontext().prec = 102

def square(n):
	rootn = sqrt(n)
	return rootn == int(rootn)

def sumDigits(n):
	return sum(map(int, str(n)))

def dsum(n):
	n = pow(Decimal(n), Decimal('0.5'))
	n *= pow(10, 100 - len(str(int(n))))
	n = int(n)
	return sumDigits(n)

def p80():
	return sum(dsum(n) for n in range(1, 101) if not square(n))

print(p80())
