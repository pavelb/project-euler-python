def fib3(limit): # generate every third fib < limit
	a, b = 0, 1
	while a < limit:
		yield a
		a, b = a + 2 * b, 2 * a + 3 * b

def main(limit):
	# trick: n % 3 == 0 <=> fib(n) is even
	return sum(fib3(limit))

print(main(4000000))