from lib import fibonaccis
from itertools import takewhile, islice

def main(limit):
	# trick: n % 3 == 0 <=> fib(n) is even
	evenf = islice(fibonaccis(), 0, None, 3)
	return sum(takewhile(lambda n: n < limit, evenf))

print(main(4000000)) # 4613732
