def collatz(n):
	while True:
		yield n
		if n <= 1: break
		n = n // 2 if n % 2 == 0 else 3 * n + 1

def main(lim):
	return max(range(lim), key = lambda n: len(list(collatz(n))))

print(main(1000000))