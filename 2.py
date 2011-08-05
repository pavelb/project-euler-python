def main(limit):
	# trick: n % 3 == 0 <=> fib(n) is even
	rv = 0
	a, b = 0, 1
	while a < limit:
		rv += a
		a, b = a + 2 * b, 2 * a + 3 * b # step by three
	return rv

print(main(4000000))