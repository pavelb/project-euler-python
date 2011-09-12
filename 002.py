<<<<<<< HEAD
from lib import fibonaccis
=======
from lib import fibonacci
>>>>>>> upstream/master
from itertools import takewhile, islice

def main(limit):
	# trick: n % 3 == 0 <=> fib(n) is even
<<<<<<< HEAD
	evenf = islice(fibonaccis(), 0, None, 3)
	return sum(takewhile(lambda n: n < limit, evenf))
=======
	return sum(takewhile(lambda n: n < limit, islice(fibonacci(), 0, None, 3)))
>>>>>>> upstream/master

print(main(4000000)) # 4613732
