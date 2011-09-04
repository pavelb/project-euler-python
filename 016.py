from lib import digits

def main(n):
	return sum(digits(pow(2, n)))

print(main(1000)) # 1366
