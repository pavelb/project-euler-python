def collatz(n):
	while n > 1:
		yield n
		n = n // 2 if n % 2 == 0 else 3 * n + 1
	yield 1

def main(lim):
	return max(range(lim), key = lambda n: len(list(collatz(n))))

print(main(1000000)) # 837799
