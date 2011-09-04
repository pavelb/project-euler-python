from lib import choose

def main(n, k):
	return sum(choose(n - c * (s - 1), c) for s in range(2, k + 1) for c in range(1, n // s + 1))

print(main(50, 4)) # 20492570929
