from lib import fibonaccis, numLen

def main(limit):
	return next(n for n, f in enumerate(fibonaccis()) if numLen(f) >= limit)

if __name__ == '__main__':
	print(main(1000)) # 4782
