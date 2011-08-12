from math import factorial

def main(iterator, n):
	items = list(iterator)
	n -= 1 # zero indexed
	rv = ''
	for i in reversed(range(len(items))):
		f = factorial(i)
		rv += str(items.pop(n // f))
		n %= f
	return rv

print(main(range(10), 10 ** 6)) # 2783915460
