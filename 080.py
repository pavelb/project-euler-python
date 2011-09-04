from lib import square, digits, numLen
from decimal import Decimal, getcontext

getcontext().prec = 102

def dsum(n):
	n = pow(Decimal(n), Decimal('0.5'))
	n *= pow(10, 100 - numLen(int(n)))
	n = int(n)
	return sum(digits(n))

def main():
	return sum(dsum(n) for n in range(1, 101) if not square(n))

print(main()) # 40886
