from lib import digits

def main(n):
	return sum(digits(pow(2, n)))

if __name__ == '__main__':
	print(main(1000)) # 1366
