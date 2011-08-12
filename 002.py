from lib import fibonacci
from itertools import takewhile, islice

def main(limit):
	# trick: n % 3 == 0 <=> fib(n) is even
	return sum(takewhile(lambda n: n < limit, islice(fibonacci(), 0, None, 3)))

print(main(4000000)) # 4613732
