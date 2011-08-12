from lib import digits

def main(n):
	return sum(digits(n))

print(main(pow(2, 1000))) # 1366
