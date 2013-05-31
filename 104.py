from lib import fibonaccis, pandigital, numLen

def main():
	goodLast = lambda n: pandigital(n % 10 ** 9)
	goodFirst = lambda n: pandigital(n // 10 ** (numLen(n) - 9))
	good = lambda n: n > 123456789 and goodLast(n) and goodFirst(n)
	return next(k for k, n in enumerate(fibonaccis()) if good(n))

if __name__ == '__main__':
	print(main()) # 329468
