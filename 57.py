def cf2(lim):
	a, b = 1, 1
	for _ in range(lim):
		a, b = a + 2 * b, a + b
		yield a, b

def main(lim):
	return sum(len(str(n)) > len(str(d)) for n, d in cf2(lim))

print(main(1000))