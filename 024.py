from math import factorial

def main(n, items):
	n -= 1 # zero indexed
	rv = ''
	for i in reversed(range(len(items))):
		f = factorial(i)
		rv += str(items.pop(n // f))
		n %= f
	return rv

print(main(10 ** 6, list(range(10))))