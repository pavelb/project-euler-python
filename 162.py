def main(limit):
	count = 0
	for n in range(3, limit + 1):
		c = 15 * (16 ** (n - 1))

		no0 = (16 - 1) ** n
		no1 = (16 - 2) * ((16 - 1) ** (n - 1))
		noA = (16 - 2) * ((16 - 1) ** (n - 1))

		no0no1 = (16 - 2) ** n
		no0noA = (16 - 2) ** n
		no1noA = (16 - 3) * ((16 - 2) ** (n - 1))

		no0no1noA = (16 - 3) ** n

		count += c - (no0 + no1 + noA) + (no0no1 + no0noA + no1noA) - no0no1noA
	return hex(count).replace('0x', '').upper()


if __name__ == '__main__':
	print(main(16))  # 3D58725572C62302
