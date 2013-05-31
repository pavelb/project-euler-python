def main(a, b):
	return len(set(pow(i, j) for i in range(2, a + 1) for j in range(2, b + 1)))

if __name__ == '__main__':
	print(main(100, 100)) # 9183
