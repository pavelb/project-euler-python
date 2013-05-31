def squareOfSum(n):
	return pow(n * (n + 1) // 2, 2)

def sumOfSquare(n):
	return n * (n + 1) * (2 * n + 1) // 6

def main(n):
	return squareOfSum(n) - sumOfSquare(n)

if __name__ == '__main__':
	print(main(100)) # 25164150
