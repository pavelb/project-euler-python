from lib import convergents

def minX(D):
	for x, y in convergents(D):
		if x * x - D * y * y == 1:
			return x
	return float('-inf')

def main(limit):
	# trick: Pell equation, solutions are convergents of sqrt(D)
	return max(range(2, limit + 1), key = lambda D: minX(D))

print(main(1000)) # 661
