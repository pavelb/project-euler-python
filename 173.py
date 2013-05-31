def main(tiles):
	return sum(tiles // 4 // k - k for k in range(1, int(tiles ** 0.5) // 2))

if __name__ == '__main__':
	print(main(10 ** 6)) # 1572729
