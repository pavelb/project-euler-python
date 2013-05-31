def collatz(n):
	while n > 1:
		yield n
		n = n // 2 if n % 2 == 0 else 3 * n + 1
	yield 1

def main(lim):
	chainlen = lambda n: sum(1 for _ in collatz(n))
	return max(range(lim), key=chainlen)

if __name__ == '__main__':
	print(main(1000000)) # 837799
