from math import factorial

def main(n, items):
	n -= 1 # zero indexed
	rv = ''
	for f in reversed([factorial(k) for k in range(len(items))]):
		rv += str(items.pop(n // f))
		n %= f
	return rv

print(main(10 ** 6, list(range(10))))