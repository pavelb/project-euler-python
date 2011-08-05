def P(n):
	# using the method of Lagrange multipliers, must have x_i = i*x_1
	rv = (2 / (n + 1)) ** (n * (n + 1) / 2)
	for i in range(1, n + 1):
		rv *= i ** i
	return int(rv)

def main(a, b):
	return sum(P(m) for m in range(a, b + 1))

print(main(2, 15))
