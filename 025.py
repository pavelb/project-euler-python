<<<<<<< HEAD
from lib import fibonaccis, numLen

def main(limit):
	return next(n for n, f in enumerate(fibonaccis()) if numLen(f) >= limit)
=======
from lib import fibonacci, numLen

def main(limit):
	return next(n for n, f in enumerate(fibonacci()) if numLen(f) >= limit)
>>>>>>> upstream/master

print(main(1000)) # 4782
