def main(n):
	h = n // 2
	return 1 + h * (16 * h * h + 30 * h + 26) // 3

if __name__ == '__main__':
	print(main(1001)) # 669171001
