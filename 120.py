def main(a, b):
	maxr = lambda n: 2 * n * ((n - 1) // 2)
	return sum(map(maxr, range(a, b + 1)))

if __name__ == '__main__':
	print(main(3, 1000)) # 333082500
